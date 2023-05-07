import typing_extensions

from flashcards_api_client.apis.tags import TagValues
from flashcards_api_client.apis.tags.algorithms_api import AlgorithmsApi
from flashcards_api_client.apis.tags.auth_api import AuthApi
from flashcards_api_client.apis.tags.decks_api import DecksApi
from flashcards_api_client.apis.tags.default_api import DefaultApi
from flashcards_api_client.apis.tags.facts_api import FactsApi
from flashcards_api_client.apis.tags.study_api import StudyApi
from flashcards_api_client.apis.tags.tags_api import TagsApi
from flashcards_api_client.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ALGORITHMS: AlgorithmsApi,
        TagValues.AUTH: AuthApi,
        TagValues.DECKS: DecksApi,
        TagValues.DEFAULT: DefaultApi,
        TagValues.FACTS: FactsApi,
        TagValues.STUDY: StudyApi,
        TagValues.TAGS: TagsApi,
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ALGORITHMS: AlgorithmsApi,
        TagValues.AUTH: AuthApi,
        TagValues.DECKS: DecksApi,
        TagValues.DEFAULT: DefaultApi,
        TagValues.FACTS: FactsApi,
        TagValues.STUDY: StudyApi,
        TagValues.TAGS: TagsApi,
        TagValues.USERS: UsersApi,
    }
)
