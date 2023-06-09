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


class CardPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            question_id = schemas.UUIDSchema
            answer_id = schemas.UUIDSchema
            __annotations__ = {
                "question_id": question_id,
                "answer_id": answer_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question_id"]) -> MetaOapg.properties.question_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_id"]) -> MetaOapg.properties.answer_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["question_id", "answer_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question_id"]) -> typing.Union[MetaOapg.properties.question_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_id"]) -> typing.Union[MetaOapg.properties.answer_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["question_id", "answer_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        question_id: typing.Union[MetaOapg.properties.question_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        answer_id: typing.Union[MetaOapg.properties.answer_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardPatch':
        return super().__new__(
            cls,
            *_args,
            question_id=question_id,
            answer_id=answer_id,
            _configuration=_configuration,
            **kwargs,
        )
