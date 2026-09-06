

# GET\_JSON\_OBJECT function
<a name="GET_JSON_OBJECT"></a>

The GET\_JSON\_OBJECT function extracts a json object from `path`. 

## Syntax
<a name="GET_JSON_OBJECT-syntax"></a>

```
get_json_object(json_txt, path)
```

## Arguments
<a name="GET_JSON_OBJECT-arguments"></a>

*json\_txt*  
A STRING expression containing well formed JSON.

*path*  
A STRING literal with a well formed JSON path expression.

## Returns
<a name="GET_JSON_OBJECT-returns"></a>

Returns a STRING.

A NULL is returned if the object can't be found.

## Example
<a name="GET_JSON_OBJECT-example"></a>

The following example extracts a value from a JSON object.. The first argument is a JSON string that represents a simple object with a single key-value pair. The second argument is a JSON path expression. The `$` symbol represents the root of the JSON object, and the `.a` part specifies that we want to extract the value associated with the "`a`" key. The output of the function is '`b`', which is the value associated with the "`a`" key in the input JSON object.

```
SELECT get_json_object('{"a":"b"}', '$.a');
 b
```