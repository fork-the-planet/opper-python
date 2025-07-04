"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from opperai.types import BaseModel
from opperai.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ResponseFormatJSONObjectTypedDict(TypedDict):
    type: Literal["json_object"]


class ResponseFormatJSONObject(BaseModel):
    TYPE: Annotated[
        Annotated[
            Literal["json_object"], AfterValidator(validate_const("json_object"))
        ],
        pydantic.Field(alias="type"),
    ] = "json_object"
