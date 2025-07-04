"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .granularity import Granularity
from datetime import datetime
from opperai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from opperai.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class UsageAnalyticsUsageGetRequestTypedDict(TypedDict):
    from_date: NotRequired[Nullable[datetime]]
    r"""Start date for the time range (inclusive). If not provided, defaults to the first day of the current month."""
    to_date: NotRequired[Nullable[datetime]]
    r"""End date for the time range (exclusive). If not provided, defaults to the last day of the current month."""
    granularity: NotRequired[Nullable[Granularity]]
    r"""Time granularity for grouping (minute, hour, day, month, year)"""
    fields: NotRequired[Nullable[List[str]]]
    r"""Fields from event_metadata to include and sum"""
    group_by: NotRequired[Nullable[List[str]]]
    r"""Fields from tags to group by"""


class UsageAnalyticsUsageGetRequest(BaseModel):
    from_date: Annotated[
        OptionalNullable[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Start date for the time range (inclusive). If not provided, defaults to the first day of the current month."""

    to_date: Annotated[
        OptionalNullable[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""End date for the time range (exclusive). If not provided, defaults to the last day of the current month."""

    granularity: Annotated[
        OptionalNullable[Granularity],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Time granularity for grouping (minute, hour, day, month, year)"""

    fields: Annotated[
        OptionalNullable[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Fields from event_metadata to include and sum"""

    group_by: Annotated[
        OptionalNullable[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Fields from tags to group by"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["from_date", "to_date", "granularity", "fields", "group_by"]
        nullable_fields = ["from_date", "to_date", "granularity", "fields", "group_by"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
