"""Python implementations of the Repository and UnitOfWork abstractions."""

import logging as _logging

from ._repo import BasicRepo, Repo, TaggedRepo


__all__ = ["BasicRepo", "Repo", "TaggedRepo"]

__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.3.0"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
