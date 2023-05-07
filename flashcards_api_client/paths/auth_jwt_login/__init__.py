# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flashcards_api_client.paths.auth_jwt_login import Api

from flashcards_api_client.paths import PathValues

path = PathValues.AUTH_JWT_LOGIN