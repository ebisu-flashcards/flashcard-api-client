<a name="__pageTop"></a>
# flashcards-api-client.apis.tags.auth_api.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_jwt_login**](#auth_jwt_login) | **post** /auth/jwt/login | Auth:Jwt.Login
[**auth_jwt_logout**](#auth_jwt_logout) | **post** /auth/jwt/logout | Auth:Jwt.Logout
[**register_register**](#register_register) | **post** /register | Register:Register
[**reset_forgot_password**](#reset_forgot_password) | **post** /forgot-password | Reset:Forgot Password
[**reset_reset_password**](#reset_reset_password) | **post** /reset-password | Reset:Reset Password
[**verify_request_token**](#verify_request_token) | **post** /request-verify-token | Verify:Request-Token
[**verify_verify**](#verify_verify) | **post** /verify | Verify:Verify

# **auth_jwt_login**
<a name="auth_jwt_login"></a>
> BearerResponse auth_jwt_login()

Auth:Jwt.Login

### Example

```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from flashcards-api-client.model.bearer_response import BearerResponse
from flashcards-api-client.model.error_model import ErrorModel
from flashcards-api-client.model.body_auth_jwt_login_auth_jwt_login_post import BodyAuthJwtLoginAuthJwtLoginPost
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only optional values
    body = dict(
        grant_type="password",
        username="username_example",
        password="password_example",
        scope="",
        client_id="client_id_example",
        client_secret="client_secret_example",
    )
    try:
        # Auth:Jwt.Login
        api_response = api_instance.auth_jwt_login(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_login: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyAuthJwtLoginAuthJwtLoginPost**](../../models/BodyAuthJwtLoginAuthJwtLoginPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_jwt_login.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#auth_jwt_login.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#auth_jwt_login.ApiResponseFor422) | Validation Error

#### auth_jwt_login.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BearerResponse**](../../models/BearerResponse.md) |  | 


#### auth_jwt_login.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### auth_jwt_login.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_jwt_logout**
<a name="auth_jwt_logout"></a>
> bool, date, datetime, dict, float, int, list, str, none_type auth_jwt_logout()

Auth:Jwt.Logout

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = flashcards-api-client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Auth:Jwt.Logout
        api_response = api_instance.auth_jwt_logout()
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_logout: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_jwt_logout.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#auth_jwt_logout.ApiResponseFor401) | Missing token or inactive user.

#### auth_jwt_logout.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### auth_jwt_logout.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **register_register**
<a name="register_register"></a>
> UserRead register_register(user_create)

Register:Register

### Example

```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from flashcards-api-client.model.error_model import ErrorModel
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.user_read import UserRead
from flashcards-api-client.model.user_create import UserCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserCreate(
        email="email_example",
        password="password_example",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )
    try:
        # Register:Register
        api_response = api_instance.register_register(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->register_register: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserCreate**](../../models/UserCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#register_register.ApiResponseFor201) | Successful Response
400 | [ApiResponseFor400](#register_register.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#register_register.ApiResponseFor422) | Validation Error

#### register_register.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserRead**](../../models/UserRead.md) |  | 


#### register_register.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### register_register.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **reset_forgot_password**
<a name="reset_forgot_password"></a>
> bool, date, datetime, dict, float, int, list, str, none_type reset_forgot_password(body_reset_forgot_password_forgot_password_post)

Reset:Forgot Password

### Example

```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.body_reset_forgot_password_forgot_password_post import BodyResetForgotPasswordForgotPasswordPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyResetForgotPasswordForgotPasswordPost(
        email="email_example",
    )
    try:
        # Reset:Forgot Password
        api_response = api_instance.reset_forgot_password(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->reset_forgot_password: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyResetForgotPasswordForgotPasswordPost**](../../models/BodyResetForgotPasswordForgotPasswordPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#reset_forgot_password.ApiResponseFor202) | Successful Response
422 | [ApiResponseFor422](#reset_forgot_password.ApiResponseFor422) | Validation Error

#### reset_forgot_password.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### reset_forgot_password.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **reset_reset_password**
<a name="reset_reset_password"></a>
> bool, date, datetime, dict, float, int, list, str, none_type reset_reset_password(body_reset_reset_password_reset_password_post)

Reset:Reset Password

### Example

```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from flashcards-api-client.model.error_model import ErrorModel
from flashcards-api-client.model.body_reset_reset_password_reset_password_post import BodyResetResetPasswordResetPasswordPost
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyResetResetPasswordResetPasswordPost(
        token="token_example",
        password="password_example",
    )
    try:
        # Reset:Reset Password
        api_response = api_instance.reset_reset_password(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->reset_reset_password: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyResetResetPasswordResetPasswordPost**](../../models/BodyResetResetPasswordResetPasswordPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#reset_reset_password.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#reset_reset_password.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#reset_reset_password.ApiResponseFor422) | Validation Error

#### reset_reset_password.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### reset_reset_password.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### reset_reset_password.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_request_token**
<a name="verify_request_token"></a>
> bool, date, datetime, dict, float, int, list, str, none_type verify_request_token(body_verify_request_token_request_verify_token_post)

Verify:Request-Token

### Example

```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from flashcards-api-client.model.body_verify_request_token_request_verify_token_post import BodyVerifyRequestTokenRequestVerifyTokenPost
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyVerifyRequestTokenRequestVerifyTokenPost(
        email="email_example",
    )
    try:
        # Verify:Request-Token
        api_response = api_instance.verify_request_token(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->verify_request_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyVerifyRequestTokenRequestVerifyTokenPost**](../../models/BodyVerifyRequestTokenRequestVerifyTokenPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#verify_request_token.ApiResponseFor202) | Successful Response
422 | [ApiResponseFor422](#verify_request_token.ApiResponseFor422) | Validation Error

#### verify_request_token.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### verify_request_token.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_verify**
<a name="verify_verify"></a>
> UserRead verify_verify(body_verify_verify_verify_post)

Verify:Verify

### Example

```python
import flashcards-api-client
from flashcards-api-client.apis.tags import auth_api
from flashcards-api-client.model.error_model import ErrorModel
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.user_read import UserRead
from flashcards-api-client.model.body_verify_verify_verify_post import BodyVerifyVerifyVerifyPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards-api-client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with flashcards-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyVerifyVerifyVerifyPost(
        token="token_example",
    )
    try:
        # Verify:Verify
        api_response = api_instance.verify_verify(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling AuthApi->verify_verify: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyVerifyVerifyVerifyPost**](../../models/BodyVerifyVerifyVerifyPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#verify_verify.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#verify_verify.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#verify_verify.ApiResponseFor422) | Validation Error

#### verify_verify.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserRead**](../../models/UserRead.md) |  | 


#### verify_verify.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### verify_verify.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

