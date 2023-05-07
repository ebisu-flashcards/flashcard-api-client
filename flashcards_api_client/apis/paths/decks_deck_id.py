from flashcards_api_client.paths.decks_deck_id.get import ApiForget
from flashcards_api_client.paths.decks_deck_id.delete import ApiFordelete
from flashcards_api_client.paths.decks_deck_id.patch import ApiForpatch


class DecksDeckId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
