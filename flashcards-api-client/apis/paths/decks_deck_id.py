from flashcards-api-client.paths.decks_deck_id.get import ApiForget
from flashcards-api-client.paths.decks_deck_id.delete import ApiFordelete
from flashcards-api-client.paths.decks_deck_id.patch import ApiForpatch


class DecksDeckId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
