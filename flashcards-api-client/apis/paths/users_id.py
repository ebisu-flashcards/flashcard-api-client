from flashcards-api-client.paths.users_id.get import ApiForget
from flashcards-api-client.paths.users_id.delete import ApiFordelete
from flashcards-api-client.paths.users_id.patch import ApiForpatch


class UsersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
