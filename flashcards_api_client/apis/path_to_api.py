import typing_extensions

from flashcards_api_client.paths import PathValues
from flashcards_api_client.apis.paths.algorithms_ import Algorithms
from flashcards_api_client.apis.paths.decks import Decks
from flashcards_api_client.apis.paths.decks_deck_id import DecksDeckId
from flashcards_api_client.apis.paths.decks_ import Decks
from flashcards_api_client.apis.paths.decks_deck_id_cards import DecksDeckIdCards
from flashcards_api_client.apis.paths.decks_deck_id_cards_card_id import DecksDeckIdCardsCardId
from flashcards_api_client.apis.paths.decks_deck_id_cards_card_id_reviews import DecksDeckIdCardsCardIdReviews
from flashcards_api_client.apis.paths.decks_deck_id_cards_card_id_tags_tag_name import DecksDeckIdCardsCardIdTagsTagName
from flashcards_api_client.apis.paths.decks_deck_id_cards_card_id_context_question_fact_id import DecksDeckIdCardsCardIdContextQuestionFactId
from flashcards_api_client.apis.paths.decks_deck_id_cards_card_id_context_answer_fact_id import DecksDeckIdCardsCardIdContextAnswerFactId
from flashcards_api_client.apis.paths.decks_deck_id_cards_card_id_related import DecksDeckIdCardsCardIdRelated
from flashcards_api_client.apis.paths.facts_ import Facts
from flashcards_api_client.apis.paths.facts_fact_id import FactsFactId
from flashcards_api_client.apis.paths.facts_tag_tag_name import FactsTagTagName
from flashcards_api_client.apis.paths.facts_fact_id_tags_tag_name import FactsFactIdTagsTagName
from flashcards_api_client.apis.paths.facts_fact_id_related_ import FactsFactIdRelated
from flashcards_api_client.apis.paths.tags_ import Tags
from flashcards_api_client.apis.paths.tags_tag_id import TagsTagId
from flashcards_api_client.apis.paths.study_deck_id_start import StudyDeckIdStart
from flashcards_api_client.apis.paths.study_deck_id_next import StudyDeckIdNext
from flashcards_api_client.apis.paths.auth_jwt_login import AuthJwtLogin
from flashcards_api_client.apis.paths.auth_jwt_logout import AuthJwtLogout
from flashcards_api_client.apis.paths.register import Register
from flashcards_api_client.apis.paths.forgot_password import ForgotPassword
from flashcards_api_client.apis.paths.reset_password import ResetPassword
from flashcards_api_client.apis.paths.request_verify_token import RequestVerifyToken
from flashcards_api_client.apis.paths.verify import Verify
from flashcards_api_client.apis.paths.users_me import UsersMe
from flashcards_api_client.apis.paths.users_id import UsersId
from flashcards_api_client.apis.paths. import 

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ALGORITHMS_: Algorithms,
        PathValues.DECKS: Decks,
        PathValues.DECKS_DECK_ID: DecksDeckId,
        PathValues.DECKS_: Decks,
        PathValues.DECKS_DECK_ID_CARDS: DecksDeckIdCards,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID: DecksDeckIdCardsCardId,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_REVIEWS: DecksDeckIdCardsCardIdReviews,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_TAGS_TAG_NAME: DecksDeckIdCardsCardIdTagsTagName,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_CONTEXT_QUESTION_FACT_ID: DecksDeckIdCardsCardIdContextQuestionFactId,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_CONTEXT_ANSWER_FACT_ID: DecksDeckIdCardsCardIdContextAnswerFactId,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_RELATED: DecksDeckIdCardsCardIdRelated,
        PathValues.FACTS_: Facts,
        PathValues.FACTS_FACT_ID: FactsFactId,
        PathValues.FACTS_TAG_TAG_NAME: FactsTagTagName,
        PathValues.FACTS_FACT_ID_TAGS_TAG_NAME: FactsFactIdTagsTagName,
        PathValues.FACTS_FACT_ID_RELATED_: FactsFactIdRelated,
        PathValues.TAGS_: Tags,
        PathValues.TAGS_TAG_ID: TagsTagId,
        PathValues.STUDY_DECK_ID_START: StudyDeckIdStart,
        PathValues.STUDY_DECK_ID_NEXT: StudyDeckIdNext,
        PathValues.AUTH_JWT_LOGIN: AuthJwtLogin,
        PathValues.AUTH_JWT_LOGOUT: AuthJwtLogout,
        PathValues.REGISTER: Register,
        PathValues.FORGOTPASSWORD: ForgotPassword,
        PathValues.RESETPASSWORD: ResetPassword,
        PathValues.REQUESTVERIFYTOKEN: RequestVerifyToken,
        PathValues.VERIFY: Verify,
        PathValues.USERS_ME: UsersMe,
        PathValues.USERS_ID: UsersId,
        PathValues.SOLIDUS: ,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ALGORITHMS_: Algorithms,
        PathValues.DECKS: Decks,
        PathValues.DECKS_DECK_ID: DecksDeckId,
        PathValues.DECKS_: Decks,
        PathValues.DECKS_DECK_ID_CARDS: DecksDeckIdCards,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID: DecksDeckIdCardsCardId,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_REVIEWS: DecksDeckIdCardsCardIdReviews,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_TAGS_TAG_NAME: DecksDeckIdCardsCardIdTagsTagName,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_CONTEXT_QUESTION_FACT_ID: DecksDeckIdCardsCardIdContextQuestionFactId,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_CONTEXT_ANSWER_FACT_ID: DecksDeckIdCardsCardIdContextAnswerFactId,
        PathValues.DECKS_DECK_ID_CARDS_CARD_ID_RELATED: DecksDeckIdCardsCardIdRelated,
        PathValues.FACTS_: Facts,
        PathValues.FACTS_FACT_ID: FactsFactId,
        PathValues.FACTS_TAG_TAG_NAME: FactsTagTagName,
        PathValues.FACTS_FACT_ID_TAGS_TAG_NAME: FactsFactIdTagsTagName,
        PathValues.FACTS_FACT_ID_RELATED_: FactsFactIdRelated,
        PathValues.TAGS_: Tags,
        PathValues.TAGS_TAG_ID: TagsTagId,
        PathValues.STUDY_DECK_ID_START: StudyDeckIdStart,
        PathValues.STUDY_DECK_ID_NEXT: StudyDeckIdNext,
        PathValues.AUTH_JWT_LOGIN: AuthJwtLogin,
        PathValues.AUTH_JWT_LOGOUT: AuthJwtLogout,
        PathValues.REGISTER: Register,
        PathValues.FORGOTPASSWORD: ForgotPassword,
        PathValues.RESETPASSWORD: ResetPassword,
        PathValues.REQUESTVERIFYTOKEN: RequestVerifyToken,
        PathValues.VERIFY: Verify,
        PathValues.USERS_ME: UsersMe,
        PathValues.USERS_ID: UsersId,
        PathValues.SOLIDUS: ,
    }
)
