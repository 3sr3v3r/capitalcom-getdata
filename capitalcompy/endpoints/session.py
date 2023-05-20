# -*- coding: utf-8 -*-
"""Handle session endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.session import responses
from abc import abstractmethod


class Session(APIRequest):
    """Session - abstract class to handle session endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Session APIRequest instance.

        Parameters
        ----------
        instrument : None

        params : dict with query parameters
        """
        endpoint = self.ENDPOINT
        super(Session, self).__init__(endpoint, method=self.METHOD)


@endpoint("api/v1/session/encryptionKey")
class GetEncryptionKey(Session):
    """Get the encryptionkey for the session."""

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a EncryptionKey Request.

        Parameters
        ----------
        Requires the X-CAP-API-KEY but this has already been put in the header during API instantiation.

        Response: Encryption key and timestamp

        """
        super(GetEncryptionKey, self).__init__()


@endpoint("api/v1/session", "post")
class StartSession(Session):
    """Starts a session by sending accountID and password"""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Starts a session by sending accountID and password

        Body:
        ----------
        encryptedPassword": true,
        identifier: accountID,
        password: password

        Response: CST and X-SECURITY-TOKEN in the header. body:
        Account information
        """
        super(StartSession, self).__init__()
        self.data = data


@endpoint("api/v1/ping")
class Ping(Session):
    """Send a ping message to keep te session from expiring."""

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Send a ping message to keep te session from expiring.
        CST and X-SECURITY-TOKEN will expire in 10 minutes if session is not refreshed.

        Parameters
        ----------
        None. CST and X-SECURITY-TOKEN have been added to the headers of the requestclass after
        sucessfull session start call.

        """
        super(Ping, self).__init__()
