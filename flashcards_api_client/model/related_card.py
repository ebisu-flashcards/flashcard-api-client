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


class RelatedCard(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "answer",
            "question",
            "id",
            "deck_id",
            "relationship",
            "answer_context_facts",
            "question_context_facts",
            "tags",
        }
        
        class properties:
            id = schemas.UUIDSchema
            deck_id = schemas.UUIDSchema
        
            @staticmethod
            def question() -> typing.Type['FactRead']:
                return FactRead
        
            @staticmethod
            def answer() -> typing.Type['FactRead']:
                return FactRead
            
            
            class question_context_facts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FactRead']:
                        return FactRead
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FactRead'], typing.List['FactRead']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'question_context_facts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FactRead':
                    return super().__getitem__(i)
            
            
            class answer_context_facts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FactRead']:
                        return FactRead
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FactRead'], typing.List['FactRead']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'answer_context_facts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FactRead':
                    return super().__getitem__(i)
            
            
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
            relationship = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "deck_id": deck_id,
                "question": question,
                "answer": answer,
                "question_context_facts": question_context_facts,
                "answer_context_facts": answer_context_facts,
                "tags": tags,
                "relationship": relationship,
            }
    
    answer: 'FactRead'
    question: 'FactRead'
    id: MetaOapg.properties.id
    deck_id: MetaOapg.properties.deck_id
    relationship: MetaOapg.properties.relationship
    answer_context_facts: MetaOapg.properties.answer_context_facts
    question_context_facts: MetaOapg.properties.question_context_facts
    tags: MetaOapg.properties.tags
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deck_id"]) -> MetaOapg.properties.deck_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> 'FactRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer"]) -> 'FactRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question_context_facts"]) -> MetaOapg.properties.question_context_facts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_context_facts"]) -> MetaOapg.properties.answer_context_facts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "deck_id", "question", "answer", "question_context_facts", "answer_context_facts", "tags", "relationship", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deck_id"]) -> MetaOapg.properties.deck_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> 'FactRead': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer"]) -> 'FactRead': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question_context_facts"]) -> MetaOapg.properties.question_context_facts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_context_facts"]) -> MetaOapg.properties.answer_context_facts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "deck_id", "question", "answer", "question_context_facts", "answer_context_facts", "tags", "relationship", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        answer: 'FactRead',
        question: 'FactRead',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        deck_id: typing.Union[MetaOapg.properties.deck_id, str, uuid.UUID, ],
        relationship: typing.Union[MetaOapg.properties.relationship, str, ],
        answer_context_facts: typing.Union[MetaOapg.properties.answer_context_facts, list, tuple, ],
        question_context_facts: typing.Union[MetaOapg.properties.question_context_facts, list, tuple, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RelatedCard':
        return super().__new__(
            cls,
            *_args,
            answer=answer,
            question=question,
            id=id,
            deck_id=deck_id,
            relationship=relationship,
            answer_context_facts=answer_context_facts,
            question_context_facts=question_context_facts,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )

from flashcards_api_client.model.fact_read import FactRead
from flashcards_api_client.model.tag_read import TagRead
