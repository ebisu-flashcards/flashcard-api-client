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

from flashcards-api-client import schemas  # noqa: F401


class DeckCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "description",
            "algorithm",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            algorithm = schemas.StrSchema
            parameters = schemas.DictSchema
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TagCreate']:
                        return TagCreate
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TagCreate'], typing.List['TagCreate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TagCreate':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "description": description,
                "algorithm": algorithm,
                "parameters": parameters,
                "tags": tags,
            }
    
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    algorithm: MetaOapg.properties.algorithm
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithm"]) -> MetaOapg.properties.algorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "algorithm", "parameters", "tags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithm"]) -> MetaOapg.properties.algorithm: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union[MetaOapg.properties.parameters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "algorithm", "parameters", "tags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        algorithm: typing.Union[MetaOapg.properties.algorithm, str, ],
        parameters: typing.Union[MetaOapg.properties.parameters, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeckCreate':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            algorithm=algorithm,
            parameters=parameters,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )

from flashcards-api-client.model.tag_create import TagCreate
