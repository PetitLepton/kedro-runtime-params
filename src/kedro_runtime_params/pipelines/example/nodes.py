"""
This is a boilerplate pipeline 'example'
generated using Kedro 0.19.8
"""

"""This is a boilerplate pipeline 'example' generated using Kedro 0.18.12."""

import logging
from typing import Any


logger = logging.getLogger(__name__)


def log_value(value: Any) -> None:
    logger.info(f"Loaded {value} of type {type(value)}")
