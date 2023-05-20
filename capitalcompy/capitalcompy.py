# -*- coding: utf-8 -*-
"""Capital.com API wrapper for capitals REST-V10 API."""

import json
import requests
import logging
from .exceptions import V10Error

ITER_LINES_CHUNKSIZE = 60

TRADING_ENVIRONMENTS = {
    "demo": {
        "stream": 'wss://api-streaming-capital.backend-capital.com/connect',
        "api": 'https://demo-api-capital.backend-capital.com/'
    },
    "live": {
        "stream": 'wss://api-streaming-capital.backend-capital.com/connect',
        "api": 'https://api-capital.backend-capital.com'
    }
}

DEFAULT_HEADERS = {
    "Accept-Encoding": "gzip, deflate"
}

logger = logging.getLogger(__name__)


class API(object):
    r"""API - class to handle APIRequests objects to access API endpoints.
    """

    def __init__(self, apikey, environment="demo",
                 headers=None, request_params=None):
        """Instantiate an instance of CapitalcomPy's API wrapper.

        Parameters
        ----------

        environment : string
            Provide the environment for capital.com's REST api. Valid values:
            'demo' or 'live'. Default: 'demo'.

        headers : dict (optional)
            Provide request headers to be set for a request.
            For all requests this should be:

            X-SECURITY-TOKEN : string
            Provide a valid account token

            CST : string
            Provide a valid session authorization token

            Note X-SECURITY-TOKEN and CST are provided by the Capital.com API based on the
            call to the session endpoint. These fields are added to the headers of the API object
            after successfull call to the getEncryptionKey and session calls.

        """
        logger.info("setting up API-client for environment %s", environment)
        try:
            TRADING_ENVIRONMENTS[environment]

        except KeyError as err:  # noqa F841
            logger.error("unkown environment %s", environment)
            raise KeyError("Unknown environment: {}".format(environment))

        else:
            self.environment = environment

        self.apikey = apikey
        self.client = requests.Session()
        self.client.stream = False
        self._request_params = request_params if request_params else {}

        # personal token authentication
        if self.apikey:
            self.client.headers['X-CAP-API-KEY'] = self.apikey
            self.client.headers['Content-Type'] = 'application/json'

        self.client.headers.update(DEFAULT_HEADERS)

        if headers:
            self.client.headers.update(headers)
            logger.info("applying headers %s", ",".join(headers.keys()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """close.

        explicit close of the session.
        """
        self.client.close()

    @property
    def request_params(self):
        """request_params property."""
        return self._request_params

    def __request(self, method, url, request_args, headers=None, stream=False):
        """__request.

        make the actual request. This method is called by the
        request method in case of 'regular' API-calls. Or indirectly by
        the__stream_request method if it concerns a 'streaming' call.
        """
        func = getattr(self.client, method)
        headers = headers if headers else {}
        response = None
        try:
            logger.info("performing request %s", url)
            response = func(url, stream=stream, headers=headers,
                            **request_args)
        except requests.RequestException as err:
            logger.error("request %s failed [%s]", url, err)
            raise err

        # Handle error responses
        if response.status_code >= 400:
            """ Prices are retrieved using a generator that retrieves the candles.
            Sometimes individual calls yield a response code of 400 with and errorcode.
            We don't want the calls to stop and just continue to get the next prices. 
            This is achieved by setting the status code to 200.
            """
            if response.content.decode('utf-8') == '{"errorCode":"error.prices.not-found"}':
                 response.status_code = 200
                 return response

            else:
                logger.error("request %s failed [%d,%s]",
                             url,
                             response.status_code,
                             response.content.decode('utf-8'))
                raise V10Error(response.status_code,
                               response.content.decode('utf-8'))
        return response

    def __stream_request(self, method, url, request_args, headers=None):
        """__stream_request.

        make a 'stream' request. This method is called by
        the 'request' method after it has determined which
        call applies: regular or streaming.
        """
        headers = headers if headers else {}
        response = self.__request(method, url, request_args,
                                  headers=headers, stream=True)
        lines = response.iter_lines(ITER_LINES_CHUNKSIZE)
        for line in lines:
            if line:
                data = json.loads(line.decode("utf-8"))
                yield data

    def request(self, endpoint):
        """Perform a request for the APIRequest instance 'endpoint'.

        Parameters
        ----------
        endpoint : APIRequest
            The endpoint parameter contains an instance of an APIRequest
            containing the endpoint, method and optionally other parameters
            or body data.

        Raises
        ------
            V10Error in case of HTTP response code >= 400
        """
        method = endpoint.method
        method = method.lower()
        params = None
        try:
            params = getattr(endpoint, "params")
        except AttributeError:
            # request does not have params
            params = {}

        headers = {}
        if hasattr(endpoint, "HEADERS"):
            headers = getattr(endpoint, "HEADERS")

        request_args = {}
        if method == 'get':
            request_args['params'] = params
        elif hasattr(endpoint, "data") and endpoint.data:
            request_args['data'] = endpoint.data
            #request_args = json.loads(endpoint.data)


        # if any parameter for request then merge them
        #request_args.update(self._request_params)

        # which API to access ?
        if not (hasattr(endpoint, "STREAM") and
                getattr(endpoint, "STREAM") is True):
            url = "{}/{}".format(
                TRADING_ENVIRONMENTS[self.environment]["api"],
                endpoint)

            response = self.__request(method, url,
                                      request_args, headers=headers)
            content = response.content.decode('utf-8')
            content = json.loads(content)

            # update endpoint
            endpoint.response = content
            endpoint.status_code = response.status_code

            if endpoint.ENDPOINT == "api/v1/session" :
                if endpoint.status_code == endpoint.expected_status:
                    del self.client.headers['X-CAP-API-KEY']
                    self.client.headers['X-SECURITY-TOKEN'] = response.headers['X-SECURITY-TOKEN']
                    self.client.headers['CST'] = response.headers['CST']

            return content

        else:
            url = "{}/{}".format(
                TRADING_ENVIRONMENTS[self.environment]["stream"],
                endpoint)
            endpoint.response = self.__stream_request(method,
                                                      url,
                                                      request_args,
                                                      headers=headers)
            return endpoint.response
