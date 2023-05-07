<a name="__pageTop"></a>
# flashcards_api_client.apis.tags.study_api.StudyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**first_card**](#first_card) | **get** /study/{deck_id}/start | First Card
[**next_card**](#next_card) | **post** /study/{deck_id}/next | Next Card

# **first_card**
<a name="first_card"></a>
> CardRead first_card(deck_id)

First Card

Get the first card to study.  :param deck_id: the deck being studied :returns: the next card to study

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards_api_client
from flashcards_api_client.apis.tags import study_api
from flashcards_api_client.model.http_validation_error import HTTPValidationError
from flashcards_api_client.model.card_read import CardRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = flashcards_api_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flashcards_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = study_api.StudyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    try:
        # First Card
        api_response = api_instance.first_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards_api_client.ApiException as e:
        print("Exception when calling StudyApi->first_card: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deck_id | DeckIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#first_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#first_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#first_card.ApiResponseFor422) | Validation Error

#### first_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### first_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### first_card.ApiResponseFor422
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

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **next_card**
<a name="next_card"></a>
> CardRead next_card(deck_idtest_data)

Next Card

Processes the result of the previous test and returns the next card to study.  :param deck_id: the deck being studied :param result: the result of the test (algorithm dependent) :returns: the next card to study

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards_api_client
from flashcards_api_client.apis.tags import study_api
from flashcards_api_client.model.test_data import TestData
from flashcards_api_client.model.http_validation_error import HTTPValidationError
from flashcards_api_client.model.card_read import CardRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flashcards_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = flashcards_api_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flashcards_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = study_api.StudyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    body = TestData(
        card_id="card_id_example",
        result=None,
    )
    try:
        # Next Card
        api_response = api_instance.next_card(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flashcards_api_client.ApiException as e:
        print("Exception when calling StudyApi->next_card: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TestData**](../../models/TestData.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deck_id | DeckIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#next_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#next_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#next_card.ApiResponseFor422) | Validation Error

#### next_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### next_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### next_card.ApiResponseFor422
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

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

