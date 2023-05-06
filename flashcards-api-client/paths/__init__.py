# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flashcards-api-client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ALGORITHMS_ = "/algorithms/"
    DECKS = "/decks"
    DECKS_DECK_ID = "/decks/{deck_id}"
    DECKS_ = "/decks/"
    DECKS_DECK_ID_CARDS = "/decks/{deck_id}/cards"
    DECKS_DECK_ID_CARDS_CARD_ID = "/decks/{deck_id}/cards/{card_id}"
    DECKS_DECK_ID_CARDS_CARD_ID_REVIEWS = "/decks/{deck_id}/cards/{card_id}/reviews"
    DECKS_DECK_ID_CARDS_CARD_ID_TAGS_TAG_NAME = "/decks/{deck_id}/cards/{card_id}/tags/{tag_name}"
    DECKS_DECK_ID_CARDS_CARD_ID_CONTEXT_QUESTION_FACT_ID = "/decks/{deck_id}/cards/{card_id}/context/question/{fact_id}"
    DECKS_DECK_ID_CARDS_CARD_ID_CONTEXT_ANSWER_FACT_ID = "/decks/{deck_id}/cards/{card_id}/context/answer/{fact_id}"
    DECKS_DECK_ID_CARDS_CARD_ID_RELATED = "/decks/{deck_id}/cards/{card_id}/related"
    FACTS_ = "/facts/"
    FACTS_FACT_ID = "/facts/{fact_id}"
    FACTS_TAG_TAG_NAME = "/facts/tag/{tag_name}"
    FACTS_FACT_ID_TAGS_TAG_NAME = "/facts/{fact_id}/tags/{tag_name}"
    FACTS_FACT_ID_RELATED_ = "/facts/{fact_id}/related/"
    TAGS_ = "/tags/"
    TAGS_TAG_ID = "/tags/{tag_id}"
    STUDY_DECK_ID_START = "/study/{deck_id}/start"
    STUDY_DECK_ID_NEXT = "/study/{deck_id}/next"
    AUTH_JWT_LOGIN = "/auth/jwt/login"
    AUTH_JWT_LOGOUT = "/auth/jwt/logout"
    REGISTER = "/register"
    FORGOTPASSWORD = "/forgot-password"
    RESETPASSWORD = "/reset-password"
    REQUESTVERIFYTOKEN = "/request-verify-token"
    VERIFY = "/verify"
    USERS_ME = "/users/me"
    USERS_ID = "/users/{id}"
    SOLIDUS = "/"
