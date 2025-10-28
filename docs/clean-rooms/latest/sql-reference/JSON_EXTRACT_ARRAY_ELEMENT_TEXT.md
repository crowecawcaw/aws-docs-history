# JSON_EXTRACT_ARRAY_ELEMENT_TEXT

function

The JSON_EXTRACT_ARRAY_ELEMENT_TEXT function returns a JSON array element in the
outermost array of a JSON string, using a zero-based index. The first element in an array
is at position 0. If the index is negative or out of bound, JSON_EXTRACT_ARRAY_ELEMENT_TEXT
returns empty string. If the _null_if_invalid_ argument is set to
`true` and the JSON string is invalid, the function returns NULL instead of
returning an error.

For more information, see [JSON functions](json-functions.md "json-functions.md").

## Syntax

```
json_extract_array_element_text('*json string*', *pos* [, *null\_if\_invalid* ] )
```

## Arguments

_json_string_

A properly formatted JSON string.

_pos_

An integer representing the index of the array element to be returned, using
a zero-based array index.

_null_if_invalid_

A Boolean value that specifies whether to return NULL if the input JSON
string is invalid instead of returning an error. To return NULL if the JSON is
invalid, specify `true` (`t`). To return an error if the
JSON is invalid, specify `false` (`f`). The default is
`false`.

## Return type

A VARCHAR string representing the JSON array element referenced by
_pos_.

## Example

The following example returns array element at position 2, which is the third element
of a zero-based array index:

```
select json_extract_array_element_text('[111,112,113]', 2);

json_extract_array_element_text
-------------------------------
113
```

The following example returns an error because the JSON is invalid.

```
select json_extract_array_element_text('["a",["b",1,["c",2,3,null,]]]',1);

An error occurred when executing the SQL command:
select json_extract_array_element_text('["a",["b",1,["c",2,3,null,]]]',1)
```

The following example sets _null_if_invalid_ to
_true_, so the statement returns NULL instead of returning an
error for invalid JSON.

```
select json_extract_array_element_text('["a",["b",1,["c",2,3,null,]]]',1,true);

json_extract_array_element_text
-------------------------------

```
