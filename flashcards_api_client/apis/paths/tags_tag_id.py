from flashcards_api_client.paths.tags_tag_id.get import ApiForget
from flashcards_api_client.paths.tags_tag_id.delete import ApiFordelete
from flashcards_api_client.paths.tags_tag_id.patch import ApiForpatch


class TagsTagId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
