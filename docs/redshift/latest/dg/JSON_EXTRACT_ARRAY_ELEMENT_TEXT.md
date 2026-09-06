

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT function
<a name="JSON_EXTRACT_ARRAY_ELEMENT_TEXT"></a>

**Note**  
JSON\_PARSE and its associated functions parse JSON values as SUPER, which Amazon Redshift parses more efficiently than VARCHAR.  
Instead of using JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT, we recommend that you parse your JSON strings using the [JSON\_PARSE function](JSON_PARSE.md) to get a SUPER value. Then, query the element you want using its array index, using the `value[element position]` syntax. For more information on querying array elements in SUPER values, go to [Querying semi-structured data](query-super.md).

The JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT function returns a JSON array element in the outermost array of a JSON string, using a zero-based index. The first element in an array is at position 0. If the index is negative or out of bounds, JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT returns `NULL`. If the *null\_if\_invalid* argument is set to `TRUE` and the JSON string is invalid, the function returns `NULL` instead of returning an error.

For more information, see [JSON functions](json-functions.md). 

## Syntax
<a name="JSON_EXTRACT_ARRAY_ELEMENT_TEXT-synopsis"></a>

```
JSON_EXTRACT_ARRAY_ELEMENT_TEXT('json string', pos [, null_if_invalid ] )
```

## Arguments
<a name="JSON_EXTRACT_ARRAY_ELEMENT_TEXT-arguments"></a>

 *json\_string*  
A properly formatted JSON string.

*pos*  
An `INTEGER` representing the index of the array element to be returned, using a zero-based array index.

*null\_if\_invalid*  
(Optional) A `BOOLEAN` value that specifies whether to return `NULL` if the input JSON string is invalid instead of returning an error. To return `NULL` if the JSON is invalid, specify `true` (`t`). To return an error if the JSON is invalid, specify `false` (`f`). The default is `false`.

## Return type
<a name="JSON_EXTRACT_ARRAY_ELEMENT_TEXT-return"></a>

`VARCHAR`  
A `VARCHAR` string representing the JSON array element referenced by *pos*.

## Examples
<a name="JSON_EXTRACT_ARRAY_ELEMENT_TEXT-examples"></a>

To return array element at position 2, which is the third element of a zero-based array index, use the following example. 

```
SELECT JSON_EXTRACT_ARRAY_ELEMENT_TEXT('[111,112,113]', 2);
 
+---------------------------------+
| json_extract_array_element_text |
+---------------------------------+
|                             113 |
+---------------------------------+
```

To return an error because the JSON is invalid, use the following example.

```
SELECT JSON_EXTRACT_ARRAY_ELEMENT_TEXT('["a",["b",1,["c",2,3,null,]]]',1);
 
ERROR: invalid json array object ["a",["b",1,["c",2,3,null,]]]
```

To set *null\_if\_invalid* to *true*, so the statement returns `NULL` instead of returning an error for invalid JSON, use the following example.

```
SELECT JSON_EXTRACT_ARRAY_ELEMENT_TEXT('["a",["b",1,["c",2,3,null,]]]',1,true);
 
+---------------------------------+
| json_extract_array_element_text |
+---------------------------------+
| NULL                            |
+---------------------------------+
```

Consider the following example statements. If the provided JSON string or the index is NULL, JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT returns NULL regardless of the value of any other parameters. 

```
--Statement where json_string is NULL.
SELECT json_extract_array_element_text(NULL, 0)

 json_extract_array_element_text
---------------------------------
                            NULL

--Statement where pos is NULL and json_string is invalid JSON.
SELECT json_extract_array_element_text('invalid_json', NULL);

 json_extract_array_element_text
---------------------------------
                            NULL

--Statement where json_string is NULL and null_if_invalid is FALSE.
SELECT json_extract_array_element_text(NULL, 0, FALSE);

 json_extract_array_element_text
---------------------------------
                            NULL
```

Consider the following example statements. When *null\_if\_invalid* is TRUE, JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT returns NULL when *json\_string* is invalid JSON. If *null\_if\_invalid* is FALSE or isn’t set, the function returns an error when *json\_string* is invalid.

```
--Statement with invalid JSON where null_if_invalid is TRUE.
SELECT json_extract_array_element_text('invalid_json', 0, TRUE);

 json_extract_array_element_text
---------------------------------
                            NULL
                            
--Statement with invalid JSON where null_if_invalid is FALSE.
SELECT json_extract_array_element_text('invalid_json', 0);

ERROR:  JSON parsing error
```

Consider the following example, where *json\_string* is valid JSON, and *pos* refers to a JSON `null` value. In this case, JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT returns NULL, regardless of the value of *null\_if\_invalid*.

```
--Statement selecting a null value.
SELECT json_extract_array_element_text('[null]', 0);

  json_extract_array_element_text 
----------------------------------
                             NULL
```