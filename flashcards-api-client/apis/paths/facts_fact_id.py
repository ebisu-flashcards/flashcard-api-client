from flashcards-api-client.paths.facts_fact_id.get import ApiForget
from flashcards-api-client.paths.facts_fact_id.delete import ApiFordelete
from flashcards-api-client.paths.facts_fact_id.patch import ApiForpatch


class FactsFactId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
