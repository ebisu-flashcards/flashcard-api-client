# coding: utf-8

"""
    Flashcards API

    API Docs for flashcards-server  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from flashcards-api-client.paths.tags_.post import CreateTag
from flashcards-api-client.paths.tags_tag_id.delete import DeleteTag
from flashcards-api-client.paths.tags_tag_id.patch import EditTag
from flashcards-api-client.paths.tags_tag_id.get import GetTag
from flashcards-api-client.paths.tags_.get import GetTags


class TagsApi(
    CreateTag,
    DeleteTag,
    EditTag,
    GetTag,
    GetTags,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
