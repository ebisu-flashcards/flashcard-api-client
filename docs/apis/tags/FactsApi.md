<a name="__pageTop"></a>
# flashcards-api-client.apis.tags.facts_api.FactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_related_fact**](#assign_related_fact) | **put** /facts/{fact_id}/related/ | Assign Related Fact
[**assign_tag_to_fact**](#assign_tag_to_fact) | **put** /facts/{fact_id}/tags/{tag_name} | Assign Tag To Fact
[**create_fact**](#create_fact) | **post** /facts/ | Create Fact
[**delete_fact**](#delete_fact) | **delete** /facts/{fact_id} | Delete Fact
[**edit_fact**](#edit_fact) | **patch** /facts/{fact_id} | Edit Fact
[**get_fact**](#get_fact) | **get** /facts/{fact_id} | Get Fact
[**get_facts**](#get_facts) | **get** /facts/ | Get Facts
[**get_facts_by_tag**](#get_facts_by_tag) | **get** /facts/tag/{tag_name} | Get Facts By Tag
[**remove_related_fact**](#remove_related_fact) | **delete** /facts/{fact_id}/related/ | Remove Related Fact
[**remove_tag_from_fact**](#remove_tag_from_fact) | **delete** /facts/{fact_id}/tags/{tag_name} | Remove Tag From Fact

# **assign_related_fact**
<a name="assign_related_fact"></a>
> FactRead assign_related_fact(fact_idrelated_fact_idrelationship)

Assign Related Fact

Assign a related fact to the fact.  :param fact_id: the id of the fact to edit :param related_fact_id: the related fact to assign to this fact :param relationship: the type of relationship between these cards :returns: The modified fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
    }
    query_params = {
        'related_fact_id': "related_fact_id_example",
        'relationship': "relationship_example",
    }
    try:
        # Assign Related Fact
        api_response = api_instance.assign_related_fact(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->assign_related_fact: %s\n" % e)
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
related_fact_id | RelatedFactIdSchema | | 
relationship | RelationshipSchema | | 


# RelatedFactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RelationshipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fact_id | FactIdSchema | | 

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_related_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#assign_related_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#assign_related_fact.ApiResponseFor422) | Validation Error

#### assign_related_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### assign_related_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### assign_related_fact.ApiResponseFor422
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

# **assign_tag_to_fact**
<a name="assign_tag_to_fact"></a>
> FactRead assign_tag_to_fact(fact_idtag_name)

Assign Tag To Fact

Assign this tag to the fact.  :param fact_id: the id of the fact to edit :param tag_name: the tag to assign to this fact :returns: The modified fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
        'tag_name': "tag_name_example",
    }
    try:
        # Assign Tag To Fact
        api_response = api_instance.assign_tag_to_fact(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->assign_tag_to_fact: %s\n" % e)
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
fact_id | FactIdSchema | | 
tag_name | TagNameSchema | | 

# FactIdSchema

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
200 | [ApiResponseFor200](#assign_tag_to_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#assign_tag_to_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#assign_tag_to_fact.ApiResponseFor422) | Validation Error

#### assign_tag_to_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### assign_tag_to_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### assign_tag_to_fact.ApiResponseFor422
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

# **create_fact**
<a name="create_fact"></a>
> FactRead create_fact(fact_create)

Create Fact

Creates a new fact with the given data.  :param fact: the details of the new fact. :returns: The new fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
from flashcards-api-client.model.fact_create import FactCreate
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    body = FactCreate(
        value="value_example",
        format="format_example",
        tags=[
            TagCreate(
                name="name_example",
            )
        ],
        related=[
            FactBase(
                value="value_example",
                format="format_example",
            )
        ],
    )
    try:
        # Create Fact
        api_response = api_instance.create_fact(
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->create_fact: %s\n" % e)
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
[**FactCreate**](../../models/FactCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#create_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#create_fact.ApiResponseFor422) | Validation Error

#### create_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### create_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_fact.ApiResponseFor422
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

# **delete_fact**
<a name="delete_fact"></a>
> bool, date, datetime, dict, float, int, list, str, none_type delete_fact(fact_id)

Delete Fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
    }
    try:
        # Delete Fact
        api_response = api_instance.delete_fact(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->delete_fact: %s\n" % e)
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
fact_id | FactIdSchema | | 

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#delete_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#delete_fact.ApiResponseFor422) | Validation Error

#### delete_fact.ApiResponseFor200
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

#### delete_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_fact.ApiResponseFor422
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

# **edit_fact**
<a name="edit_fact"></a>
> FactRead edit_fact(fact_idfact_patch)

Edit Fact

Edits the details of the given fact  :param fact_id: the id of the fact to edit :param new_fact_data: the new details of the fact. Can be partial. :returns: The modified fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_patch import FactPatch
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
    }
    body = FactPatch(
        value="value_example",
        format="format_example",
    )
    try:
        # Edit Fact
        api_response = api_instance.edit_fact(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->edit_fact: %s\n" % e)
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
[**FactPatch**](../../models/FactPatch.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fact_id | FactIdSchema | | 

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#edit_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#edit_fact.ApiResponseFor422) | Validation Error

#### edit_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### edit_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_fact.ApiResponseFor422
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

# **get_fact**
<a name="get_fact"></a>
> FactRead get_fact(fact_id)

Get Fact

Get all the details of one fact.  :param fact_id: the id of the fact to get :returns: The details of the fact.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
    }
    try:
        # Get Fact
        api_response = api_instance.get_fact(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->get_fact: %s\n" % e)
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
fact_id | FactIdSchema | | 

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_fact.ApiResponseFor422) | Validation Error

#### get_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### get_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_fact.ApiResponseFor422
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

# **get_facts**
<a name="get_facts"></a>
> [FactRead] get_facts()

Get Facts

Get all facts.  :returns: All the facts, paginated.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'limit': 100,
    }
    try:
        # Get Facts
        api_response = api_instance.get_facts(
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->get_facts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_facts.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_facts.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_facts.ApiResponseFor422) | Validation Error

#### get_facts.ApiResponseFor200
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
[**FactRead**]({{complexTypePrefix}}FactRead.md) | [**FactRead**]({{complexTypePrefix}}FactRead.md) | [**FactRead**]({{complexTypePrefix}}FactRead.md) |  | 

#### get_facts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_facts.ApiResponseFor422
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

# **get_facts_by_tag**
<a name="get_facts_by_tag"></a>
> [FactRead] get_facts_by_tag(tag_name)

Get Facts By Tag

Get all the details of the facts which have this tag assigned.  :param tag_name: the name of the tag to filter facts on :param offset: for pagination, index at which to start returning values. :param limit: for pagination, maximum number of elements to return. :returns: The list of facts with this tag.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'tag_name': "tag_name_example",
    }
    query_params = {
    }
    try:
        # Get Facts By Tag
        api_response = api_instance.get_facts_by_tag(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->get_facts_by_tag: %s\n" % e)

    # example passing only optional values
    path_params = {
        'tag_name': "tag_name_example",
    }
    query_params = {
        'offset': 0,
        'limit': 100,
    }
    try:
        # Get Facts By Tag
        api_response = api_instance.get_facts_by_tag(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->get_facts_by_tag: %s\n" % e)
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
tag_name | TagNameSchema | | 

# TagNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_facts_by_tag.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_facts_by_tag.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#get_facts_by_tag.ApiResponseFor422) | Validation Error

#### get_facts_by_tag.ApiResponseFor200
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
[**FactRead**]({{complexTypePrefix}}FactRead.md) | [**FactRead**]({{complexTypePrefix}}FactRead.md) | [**FactRead**]({{complexTypePrefix}}FactRead.md) |  | 

#### get_facts_by_tag.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_facts_by_tag.ApiResponseFor422
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

# **remove_related_fact**
<a name="remove_related_fact"></a>
> FactRead remove_related_fact(fact_idrelated_fact_idrelationship)

Remove Related Fact

Remove the relationship between these two facts.  :param fact_id: the id of the fact to edit :param related_fact_id: the related fact to assign to this fact :returns: The modified fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
    }
    query_params = {
        'related_fact_id': "related_fact_id_example",
        'relationship': "relationship_example",
    }
    try:
        # Remove Related Fact
        api_response = api_instance.remove_related_fact(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->remove_related_fact: %s\n" % e)
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
related_fact_id | RelatedFactIdSchema | | 
relationship | RelationshipSchema | | 


# RelatedFactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RelationshipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fact_id | FactIdSchema | | 

# FactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_related_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#remove_related_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#remove_related_fact.ApiResponseFor422) | Validation Error

#### remove_related_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### remove_related_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_related_fact.ApiResponseFor422
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

# **remove_tag_from_fact**
<a name="remove_tag_from_fact"></a>
> FactRead remove_tag_from_fact(fact_idtag_name)

Remove Tag From Fact

Remove this tag from the fact.  :param fact_id: the id of the fact to edit :param tag_name: the tag to remove from this fact :returns: The modified fact

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import flashcards-api-client
from flashcards-api-client.apis.tags import facts_api
from flashcards-api-client.model.fact_read import FactRead
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
    api_instance = facts_api.FactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fact_id': "fact_id_example",
        'tag_name': "tag_name_example",
    }
    try:
        # Remove Tag From Fact
        api_response = api_instance.remove_tag_from_fact(
            path_params=path_params,
        )
        pprint(api_response)
    except flashcards-api-client.ApiException as e:
        print("Exception when calling FactsApi->remove_tag_from_fact: %s\n" % e)
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
fact_id | FactIdSchema | | 
tag_name | TagNameSchema | | 

# FactIdSchema

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
200 | [ApiResponseFor200](#remove_tag_from_fact.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#remove_tag_from_fact.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#remove_tag_from_fact.ApiResponseFor422) | Validation Error

#### remove_tag_from_fact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FactRead**](../../models/FactRead.md) |  | 


#### remove_tag_from_fact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_tag_from_fact.ApiResponseFor422
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

