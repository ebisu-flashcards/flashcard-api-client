from flashcards_api_client.paths.users_id.get import ApiForget
from flashcards_api_client.paths.users_id.delete import ApiFordelete
from flashcards_api_client.paths.users_id.patch import ApiForpatch


class UsersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
