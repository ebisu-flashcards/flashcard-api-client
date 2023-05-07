from flashcards_api_client.paths.decks_deck_id_cards_card_id.get import ApiForget
from flashcards_api_client.paths.decks_deck_id_cards_card_id.delete import ApiFordelete
from flashcards_api_client.paths.decks_deck_id_cards_card_id.patch import ApiForpatch


class DecksDeckIdCardsCardId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
