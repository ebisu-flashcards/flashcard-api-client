<a name="__pageTop"></a>
# flashcards-api-client.apis.tags.decks_api.DecksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_related_card_to_card**](#add_related_card_to_card) | **put** /decks/{deck_id}/cards/{card_id}/related | Add Related Card To Card
[**assign_answer_context_to_card**](#assign_answer_context_to_card) | **put** /decks/{deck_id}/cards/{card_id}/context/answer/{fact_id} | Assign Answer Context To Card
[**assign_question_context_to_card**](#assign_question_context_to_card) | **put** /decks/{deck_id}/cards/{card_id}/context/question/{fact_id} | Assign Question Context To Card
[**assign_tag_to_card**](#assign_tag_to_card) | **put** /decks/{deck_id}/cards/{card_id}/tags/{tag_name} | Assign Tag To Card
[**create_card**](#create_card) | **post** /decks/{deck_id}/cards | Create Card
[**create_deck**](#create_deck) | **post** /decks/ | Create Deck
[**delete_card**](#delete_card) | **delete** /decks/{deck_id}/cards/{card_id} | Delete Card
[**delete_deck**](#delete_deck) | **delete** /decks/{deck_id} | Delete Deck
[**edit_card**](#edit_card) | **patch** /decks/{deck_id}/cards/{card_id} | Edit Card
[**edit_deck**](#edit_deck) | **patch** /decks/{deck_id} | Edit Deck
[**get_card**](#get_card) | **get** /decks/{deck_id}/cards/{card_id} | Get Card
[**get_cards**](#get_cards) | **get** /decks/{deck_id}/cards | Get Cards
[**get_deck**](#get_deck) | **get** /decks/{deck_id} | Get Deck
[**get_my_decks**](#get_my_decks) | **get** /decks | Get My Decks
[**get_reviews**](#get_reviews) | **get** /decks/{deck_id}/cards/{card_id}/reviews | Get Reviews
[**remove_answer_context_from_card**](#remove_answer_context_from_card) | **delete** /decks/{deck_id}/cards/{card_id}/context/answer/{fact_id} | Remove Answer Context From Card
[**remove_question_context_from_card**](#remove_question_context_from_card) | **delete** /decks/{deck_id}/cards/{card_id}/context/question/{fact_id} | Remove Question Context From Card
[**remove_related_card**](#remove_related_card) | **delete** /decks/{deck_id}/cards/{card_id}/related | Remove Related Card
[**remove_tag_from_card**](#remove_tag_from_card) | **delete** /decks/{deck_id}/cards/{card_id}/tags/{tag_name} | Remove Tag From Card

# **add_related_card_to_card**
<a name="add_related_card_to_card"></a>
> CardRead add_related_card_to_card(deck_idcard_idrelated_card_idrelationship)

Add Related Card To Card

Create a relationship between these two cards.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param card_id: the id of the related card :param relationship: the type of relationship between the cards :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
    }
    query_params = {
        'related_card_id': "related_card_id_example",
        'relationship': "relationship_example",
    }
    try:
        # Add Related Card To Card
        api_response = api_instance.add_related_card_to_card(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->add_related_card_to_card: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
related_card_id | RelatedCardIdSchema | | 
relationship | RelationshipSchema | | 


# RelatedCardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# RelationshipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deck_id | DeckIdSchema | | 
card_id | CardIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_related_card_to_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#add_related_card_to_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#add_related_card_to_card.ApiResponseFor422) | Validation Error

#### add_related_card_to_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### add_related_card_to_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### add_related_card_to_card.ApiResponseFor422
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

# **assign_answer_context_to_card**
<a name="assign_answer_context_to_card"></a>
> CardRead assign_answer_context_to_card(deck_idcard_idfact_id)

Assign Answer Context To Card

Assign this fact as a context for the answer of the card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param fact_id: the fact to assign as answer context to this card :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
        'fact_id': "fact_id_example",
    }
    try:
        # Assign Answer Context To Card
        api_response = api_instance.assign_answer_context_to_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->assign_answer_context_to_card: %s\n" % e)
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
card_id | CardIdSchema | | 
fact_id | FactIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_answer_context_to_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#assign_answer_context_to_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#assign_answer_context_to_card.ApiResponseFor422) | Validation Error

#### assign_answer_context_to_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### assign_answer_context_to_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### assign_answer_context_to_card.ApiResponseFor422
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

# **assign_question_context_to_card**
<a name="assign_question_context_to_card"></a>
> CardRead assign_question_context_to_card(deck_idcard_idfact_id)

Assign Question Context To Card

Assign this fact as a context for the question of the card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param fact_id: the fact to assign as question context to this card :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
        'fact_id': "fact_id_example",
    }
    try:
        # Assign Question Context To Card
        api_response = api_instance.assign_question_context_to_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->assign_question_context_to_card: %s\n" % e)
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
card_id | CardIdSchema | | 
fact_id | FactIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_question_context_to_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#assign_question_context_to_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#assign_question_context_to_card.ApiResponseFor422) | Validation Error

#### assign_question_context_to_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### assign_question_context_to_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### assign_question_context_to_card.ApiResponseFor422
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

# **assign_tag_to_card**
<a name="assign_tag_to_card"></a>
> CardRead assign_tag_to_card(deck_idcard_idtag_name)

Assign Tag To Card

Assign this tag to the card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param tag_name: the tag to assign to this card :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
        'tag_name': "tag_name_example",
    }
    try:
        # Assign Tag To Card
        api_response = api_instance.assign_tag_to_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->assign_tag_to_card: %s\n" % e)
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
card_id | CardIdSchema | | 
tag_name | TagNameSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# TagNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_tag_to_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#assign_tag_to_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#assign_tag_to_card.ApiResponseFor422) | Validation Error

#### assign_tag_to_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### assign_tag_to_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### assign_tag_to_card.ApiResponseFor422
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

# **create_card**
<a name="create_card"></a>
> CardRead create_card(deck_idcard_create)

Create Card

Creates a new card with the given data.  :param deck_id: the id of the deck this card will belong to :param card: the details of the new card. :returns: The new card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_create import CardCreate
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    body = CardCreate(
        question_id="question_id_example",
        answer_id="answer_id_example",
        question_context_facts=[
            "question_context_facts_example"
        ],
        answer_context_facts=[
            "answer_context_facts_example"
        ],
        tags=[
            TagCreate(
                name="name_example",
            )
        ],
    )
    try:
        # Create Card
        api_response = api_instance.create_card(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->create_card: %s\n" % e)
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
[**CardCreate**](../../models/CardCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#create_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#create_card.ApiResponseFor422) | Validation Error

#### create_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### create_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_card.ApiResponseFor422
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

# **create_deck**
<a name="create_deck"></a>
> DeckRead create_deck(deck_create)

Create Deck

Creates a new deck with the given data.  :param deck: the details of the new deck. :returns: The new deck

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.deck_create import DeckCreate
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.deck_read import DeckRead
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    body = DeckCreate(
        name="name_example",
        description="description_example",
        algorithm="algorithm_example",
        parameters=dict(),
        tags=[
            TagCreate(
                name="name_example",
            )
        ],
    )
    try:
        # Create Deck
        api_response = api_instance.create_deck(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->create_deck: %s\n" % e)
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
[**DeckCreate**](../../models/DeckCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_deck.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#create_deck.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#create_deck.ApiResponseFor422) | Validation Error

#### create_deck.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeckRead**](../../models/DeckRead.md) |  | 


#### create_deck.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_deck.ApiResponseFor422
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

# **delete_card**
<a name="delete_card"></a>
> bool, date, datetime, dict, float, int, list, str, none_type delete_card(deck_idcard_id)

Delete Card

Removes the given card from this deck  :param deck_id: the id of the deck to remove the card from :param card_id: the id of the card to delete :returns: None

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
    }
    try:
        # Delete Card
        api_response = api_instance.delete_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->delete_card: %s\n" % e)
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
card_id | CardIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#delete_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#delete_card.ApiResponseFor422) | Validation Error

#### delete_card.ApiResponseFor200
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

#### delete_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_card.ApiResponseFor422
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

# **delete_deck**
<a name="delete_deck"></a>
> bool, date, datetime, dict, float, int, list, str, none_type delete_deck(deck_id)

Delete Deck

Removes the given deck  :param deck_id: the id of the deck to remove :returns: None

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    try:
        # Delete Deck
        api_response = api_instance.delete_deck(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->delete_deck: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_deck.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#delete_deck.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#delete_deck.ApiResponseFor422) | Validation Error

#### delete_deck.ApiResponseFor200
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

#### delete_deck.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_deck.ApiResponseFor422
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

# **edit_card**
<a name="edit_card"></a>
> CardRead edit_card(deck_idcard_idcard_patch)

Edit Card

Edits the details of the given card  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param new_card_data: the new details of the card. Can be partial. :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_patch import CardPatch
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
    }
    body = CardPatch(
        question_id="question_id_example",
        answer_id="answer_id_example",
    )
    try:
        # Edit Card
        api_response = api_instance.edit_card(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->edit_card: %s\n" % e)
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
[**CardPatch**](../../models/CardPatch.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deck_id | DeckIdSchema | | 
card_id | CardIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#edit_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#edit_card.ApiResponseFor422) | Validation Error

#### edit_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### edit_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_card.ApiResponseFor422
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

# **edit_deck**
<a name="edit_deck"></a>
> DeckRead edit_deck(deck_iddeck_patch)

Edit Deck

Edits the details of the given deck  :param deck_id: the id of the deck to be modified :param new_deck_data: the new details of the deck. Can be partial. :returns: The modified deck. Cards list not included, use ``/deck/<uuid>/cards``

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.deck_patch import DeckPatch
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.deck_read import DeckRead
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    body = DeckPatch(
        name="name_example",
        description="description_example",
        algorithm="algorithm_example",
        parameters=dict(),
        tags=[
            TagCreate(
                name="name_example",
            )
        ],
        state=dict(),
    )
    try:
        # Edit Deck
        api_response = api_instance.edit_deck(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->edit_deck: %s\n" % e)
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
[**DeckPatch**](../../models/DeckPatch.md) |  | 


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
200 | [ApiResponseFor200](#edit_deck.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#edit_deck.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#edit_deck.ApiResponseFor422) | Validation Error

#### edit_deck.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeckRead**](../../models/DeckRead.md) |  | 


#### edit_deck.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_deck.ApiResponseFor422
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

# **get_card**
<a name="get_card"></a>
> CardRead get_card(deck_idcard_id)

Get Card

Get all the details of one card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to get :returns: The details of the card.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
    }
    try:
        # Get Card
        api_response = api_instance.get_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->get_card: %s\n" % e)
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
card_id | CardIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_card.ApiResponseFor422) | Validation Error

#### get_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### get_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_card.ApiResponseFor422
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

# **get_cards**
<a name="get_cards"></a>
> [CardRead] get_cards(deck_id)

Get Cards

Get all the cards for a deck (paginated, if needed).  :param deck_id: the id of the deck this card belongs to :param offset: for pagination, index at which to start returning cards. :param limit: for pagination, maximum number of cards to return. :returns: List of cards.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    query_params = {
    }
    try:
        # Get Cards
        api_response = api_instance.get_cards(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->get_cards: %s\n" % e)

    # example passing only optional values
    path_params = {
        'deck_id': "deck_id_example",
    }
    query_params = {
        'offset': 0,
        'limit': 100,
    }
    try:
        # Get Cards
        api_response = api_instance.get_cards(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->get_cards: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 100

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
200 | [ApiResponseFor200](#get_cards.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_cards.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_cards.ApiResponseFor422) | Validation Error

#### get_cards.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CardRead**]({{complexTypePrefix}}CardRead.md) | [**CardRead**]({{complexTypePrefix}}CardRead.md) | [**CardRead**]({{complexTypePrefix}}CardRead.md) |  | 

#### get_cards.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_cards.ApiResponseFor422
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

# **get_deck**
<a name="get_deck"></a>
> DeckRead get_deck(deck_id)

Get Deck

Get all the details of a deck.  :param deck_id: the id of the deck to get :returns: The details of the deck. Cards list not included, use ``/deck/<uuid>/cards``

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.deck_read import DeckRead
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
    }
    try:
        # Get Deck
        api_response = api_instance.get_deck(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->get_deck: %s\n" % e)
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
200 | [ApiResponseFor200](#get_deck.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_deck.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_deck.ApiResponseFor422) | Validation Error

#### get_deck.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeckRead**](../../models/DeckRead.md) |  | 


#### get_deck.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_deck.ApiResponseFor422
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

# **get_my_decks**
<a name="get_my_decks"></a>
> [DeckRead] get_my_decks()

Get My Decks

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.deck_read import DeckRead
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
    api_instance = decks_api.DecksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get My Decks
        api_response = api_instance.get_my_decks()
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->get_my_decks: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_my_decks.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_my_decks.ApiResponseFor404) | Not found

#### get_my_decks.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DeckRead**]({{complexTypePrefix}}DeckRead.md) | [**DeckRead**]({{complexTypePrefix}}DeckRead.md) | [**DeckRead**]({{complexTypePrefix}}DeckRead.md) |  | 

#### get_my_decks.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_reviews**
<a name="get_reviews"></a>
> [Review] get_reviews(deck_idcard_id)

Get Reviews

Get all the reviews done on this card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to get the reviews of :returns: The reviews of the card.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.http_validation_error import HTTPValidationError
from flashcards-api-client.model.review import Review
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
    }
    try:
        # Get Reviews
        api_response = api_instance.get_reviews(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->get_reviews: %s\n" % e)
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
card_id | CardIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_reviews.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_reviews.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_reviews.ApiResponseFor422) | Validation Error

#### get_reviews.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Review**]({{complexTypePrefix}}Review.md) | [**Review**]({{complexTypePrefix}}Review.md) | [**Review**]({{complexTypePrefix}}Review.md) |  | 

#### get_reviews.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reviews.ApiResponseFor422
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

# **remove_answer_context_from_card**
<a name="remove_answer_context_from_card"></a>
> CardRead remove_answer_context_from_card(deck_idcard_idfact_id)

Remove Answer Context From Card

Remove this fact from the answer context of the card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param fact_id: the id of the fact to remove from the answer context :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
        'fact_id': "fact_id_example",
    }
    try:
        # Remove Answer Context From Card
        api_response = api_instance.remove_answer_context_from_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->remove_answer_context_from_card: %s\n" % e)
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
card_id | CardIdSchema | | 
fact_id | FactIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_answer_context_from_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#remove_answer_context_from_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#remove_answer_context_from_card.ApiResponseFor422) | Validation Error

#### remove_answer_context_from_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### remove_answer_context_from_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_answer_context_from_card.ApiResponseFor422
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

# **remove_question_context_from_card**
<a name="remove_question_context_from_card"></a>
> CardRead remove_question_context_from_card(deck_idcard_idfact_id)

Remove Question Context From Card

Remove this fact from the question context of the card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param fact_id: the id of the fact to remove from the question context :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
        'fact_id': "fact_id_example",
    }
    try:
        # Remove Question Context From Card
        api_response = api_instance.remove_question_context_from_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->remove_question_context_from_card: %s\n" % e)
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
card_id | CardIdSchema | | 
fact_id | FactIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_question_context_from_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#remove_question_context_from_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#remove_question_context_from_card.ApiResponseFor422) | Validation Error

#### remove_question_context_from_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### remove_question_context_from_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_question_context_from_card.ApiResponseFor422
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

# **remove_related_card**
<a name="remove_related_card"></a>
> CardRead remove_related_card(deck_idcard_idrelated_card_idrelationship)

Remove Related Card

Remove a relationship between these two cards.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param card_id: the id of the related card :param relationship: the type of relationship between the cards :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
    }
    query_params = {
        'related_card_id': "related_card_id_example",
        'relationship': "relationship_example",
    }
    try:
        # Remove Related Card
        api_response = api_instance.remove_related_card(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->remove_related_card: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
related_card_id | RelatedCardIdSchema | | 
relationship | RelationshipSchema | | 


# RelatedCardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# RelationshipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deck_id | DeckIdSchema | | 
card_id | CardIdSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_related_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#remove_related_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#remove_related_card.ApiResponseFor422) | Validation Error

#### remove_related_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### remove_related_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_related_card.ApiResponseFor422
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

# **remove_tag_from_card**
<a name="remove_tag_from_card"></a>
> CardRead remove_tag_from_card(deck_idcard_idtag_name)

Remove Tag From Card

Remove this tag from the card.  :param deck_id: the id of the deck this card belongs to :param card_id: the id of the card to edit :param tag_name: the tag to remove from this card :returns: The modified card

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import decks_api
from flashcards-api-client.model.card_read import CardRead
from flashcards-api-client.model.http_validation_error import HTTPValidationError
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
    api_instance = decks_api.DecksApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'deck_id': "deck_id_example",
        'card_id': "card_id_example",
        'tag_name': "tag_name_example",
    }
    try:
        # Remove Tag From Card
        api_response = api_instance.remove_tag_from_card(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling DecksApi->remove_tag_from_card: %s\n" % e)
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
card_id | CardIdSchema | | 
tag_name | TagNameSchema | | 

# DeckIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# TagNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_tag_from_card.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#remove_tag_from_card.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#remove_tag_from_card.ApiResponseFor422) | Validation Error

#### remove_tag_from_card.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CardRead**](../../models/CardRead.md) |  | 


#### remove_tag_from_card.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_tag_from_card.ApiResponseFor422
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

