"""Exceptions."""


class StreamTerminated(Exception):
    """StreamTerminated."""


class V10Error(Exception):
    """Generic error class.

    In case of HTTP response codes >= 400 this class can be used
    to raise an exception representing that error.
    """

    def __init__(self, code, msg):
        """Instantiate a V10Error.

        Parameters
        ----------
        code : int
            the HTTP-code of the response

        msg : str
            the message returned with the response
        """
        self.code = code
        self.msg = msg

        super(V10Error, self).__init__(msg)
