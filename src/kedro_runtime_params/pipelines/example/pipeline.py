"""
This is a boilerplate pipeline 'example'
generated using Kedro 0.19.8
"""

from typing import Any
from kedro.pipeline import Pipeline, node
from .nodes import log_value


def create_pipeline(**kwargs: Any) -> Pipeline:
    return Pipeline(
        [
            node(log_value, inputs="params:example-duration", outputs=None),
        ]
    )
