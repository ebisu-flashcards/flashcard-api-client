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


class BodyAuthJwtLoginAuthJwtLoginPost(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "password",
            "username",
        }
        
        class properties:
            username = schemas.StrSchema
            password = schemas.StrSchema
            
            
            class grant_type(
                schemas.StrSchema
            ):
                pass
            scope = schemas.StrSchema
            client_id = schemas.StrSchema
            client_secret = schemas.StrSchema
            __annotations__ = {
                "username": username,
                "password": password,
                "grant_type": grant_type,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
            }
    
    password: MetaOapg.properties.password
    username: MetaOapg.properties.username
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["username", "password", "grant_type", "scope", "client_id", "client_secret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grant_type"]) -> typing.Union[MetaOapg.properties.grant_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union[MetaOapg.properties.scope, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> typing.Union[MetaOapg.properties.client_secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["username", "password", "grant_type", "scope", "client_id", "client_secret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        username: typing.Union[MetaOapg.properties.username, str, ],
        grant_type: typing.Union[MetaOapg.properties.grant_type, str, schemas.Unset] = schemas.unset,
        scope: typing.Union[MetaOapg.properties.scope, str, schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BodyAuthJwtLoginAuthJwtLoginPost':
        return super().__new__(
            cls,
            *_args,
            password=password,
            username=username,
            grant_type=grant_type,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            _configuration=_configuration,
            **kwargs,
        )