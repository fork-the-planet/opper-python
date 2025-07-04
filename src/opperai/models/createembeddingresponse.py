"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from opperai.types import BaseModel
from typing import Any, Dict, List
from typing_extensions import TypedDict


class CreateEmbeddingResponseTypedDict(TypedDict):
    model: str
    r"""The model that was used to create the embedding"""
    data: List[Dict[str, Any]]
    r"""The embedding data"""
    usage: Dict[str, Any]
    r"""The usage information"""


class CreateEmbeddingResponse(BaseModel):
    model: str
    r"""The model that was used to create the embedding"""

    data: List[Dict[str, Any]]
    r"""The embedding data"""

    usage: Dict[str, Any]
    r"""The usage information"""
