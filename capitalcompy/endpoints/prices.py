# -*- coding: utf-8 -*-
"""Handle Prices endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.prices import responses
from abc import abstractmethod


class prices(APIRequest):
    """Instruments - abstract class to handle Prices endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, epic):
        """Instantiate a Prices APIRequest instance.

        Parameters
        ----------
        EPIC : string (required)
            the epic to operate on

        params : dict with query parameters
        """
        endpoint = self.ENDPOINT.format(epic=epic)
        super(prices, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/prices/{epic}")
class EpicCandles(prices):
    """Get candle data for a specified epic."""

    @dyndoc_insert(responses)
    def __init__(self, epic, params=None):
        """Instantiate an EpicCandles request.

        Parameters
        ----------
        EPIC : string (required)
            the epic to fetch candle data for

        params : dict
            Resolution (or timeframe)
            Max number of bars to retrieve for the call (max 1000)
            Start datetime for the request
            End datetime for the request

        """
        super(EpicCandles, self).__init__(epic)
        self.params = params



