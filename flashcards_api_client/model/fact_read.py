# coding: utf-8

"""
    Flashcards API

    API Docs for flashcards-server  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from flashcards_api_client import schemas  # noqa: F401


class FactRead(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "format",
            "id",
            "value",
            "tags",
        }
        
        class properties:
            value = schemas.StrSchema
            format = schemas.StrSchema
            id = schemas.UUIDSchema
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TagRead']:
                        return TagRead
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TagRead'], typing.List['TagRead']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TagRead':
                    return super().__getitem__(i)
            
            
            class related(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RelatedFact']:
                        return RelatedFact
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RelatedFact'], typing.List['RelatedFact']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'related':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RelatedFact':
                    return super().__getitem__(i)
            __annotations__ = {
                "value": value,
                "format": format,
                "id": id,
                "tags": tags,
                "related": related,
            }
    
    format: MetaOapg.properties.format
    id: MetaOapg.properties.id
    value: MetaOapg.properties.value
    tags: MetaOapg.properties.tags
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["related"]) -> MetaOapg.properties.related: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["value", "format", "id", "tags", "related", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["related"]) -> typing.Union[MetaOapg.properties.related, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["value", "format", "id", "tags", "related", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        format: typing.Union[MetaOapg.properties.format, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, ],
        related: typing.Union[MetaOapg.properties.related, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FactRead':
        return super().__new__(
            cls,
            *_args,
            format=format,
            id=id,
            value=value,
            tags=tags,
            related=related,
            _configuration=_configuration,
            **kwargs,
        )

from flashcards_api_client.model.related_fact import RelatedFact
from flashcards_api_client.model.tag_read import TagRead