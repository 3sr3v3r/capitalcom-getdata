import logging
from .capitalcompy import API
from .exceptions import V10Error

__title__ = "CAPITAL.COM REST V1 API Wrapper"
__version__ = "0.0.1"
__author__ = "Jelle Bloemsma"
__license__ = "MIT"
__copyright__ = "Copyright 2023 Jelle Bloemsma"

# Version synonym
VERSION = __version__

# Set default logging handler to avoid "No handler found" warnings.
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__all__ = (
    'API',
    'V10Error'
)
