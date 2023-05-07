# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flashcards_api_client.paths.decks_deck_id_cards_card_id_related import Api

from flashcards_api_client.paths import PathValues

path = PathValues.DECKS_DECK_ID_CARDS_CARD_ID_RELATED