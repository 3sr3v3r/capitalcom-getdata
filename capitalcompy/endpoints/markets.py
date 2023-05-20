# -*- coding: utf-8 -*-
"""Handle Markets endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.session import responses
from abc import abstractmethod


class Markets(APIRequest):
    """Markets - abstract class to handle Markets endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, nodeId):
        """Instantiate a Markets APIRequest instance.

        Parameters
        ----------
        NodeID : string (required)
            The nodename for which to get the sub-nodes or leaves

        params : dict with query parameters
        """
        endpoint = self.ENDPOINT.format(nodeId=nodeId)
        super(Markets, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/marketnavigation")
class Marketnavigation(Markets):
    """Get the top level market categories."""

    @dyndoc_insert(responses)
    def __init__(self,nodeId, params=None):
        """Instantiate a Maketnavigation request.

        Parameters
        ----------
        None

        Response: Top level Market hierarchy

        """
        super(Marketnavigation, self).__init__(nodeId)


@endpoint("api/v1/marketnavigation/{nodeId}?limit=500")
class Getnodes(Markets):
    """Get the nodes or the leaves based on nodeID in te market hierarchy"""

    @dyndoc_insert(responses)
    def __init__(self, nodeId, params=None):
        """Instantiate a Getnodes request.

        Parameters
        ----------
        Requires NodeId (nodename for which to get sub-nodes or leaves)

        Response: sub-nodes or leaves beneath the nodeId.

        """
        super(Getnodes, self).__init__(nodeId)



