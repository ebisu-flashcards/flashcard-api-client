# flashcards_api_client.model.related_card.RelatedCard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**answer** | [**FactRead**](FactRead.md) | [**FactRead**](FactRead.md) |  | 
**question** | [**FactRead**](FactRead.md) | [**FactRead**](FactRead.md) |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**deck_id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**relationship** | str,  | str,  |  | 
**[answer_context_facts](#answer_context_facts)** | list, tuple,  | tuple,  |  | 
**[question_context_facts](#question_context_facts)** | list, tuple,  | tuple,  |  | 
**[tags](#tags)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# question_context_facts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FactRead**](FactRead.md) | [**FactRead**](FactRead.md) | [**FactRead**](FactRead.md) |  | 

# answer_context_facts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FactRead**](FactRead.md) | [**FactRead**](FactRead.md) | [**FactRead**](FactRead.md) |  | 

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TagRead**](TagRead.md) | [**TagRead**](TagRead.md) | [**TagRead**](TagRead.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

