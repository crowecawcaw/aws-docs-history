

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# IS\_VALID\_JSON\_ARRAY function
<a name="IS_VALID_JSON_ARRAY"></a>

**Note**  
JSON\_PARSE and its associated functions parse JSON values as SUPER, which Amazon Redshift parses more efficiently than VARCHAR.   
 Instead of using IS\_VALID\_JSON\_ARRAY, we recommend that you parse your JSON strings using the [JSON\_PARSE function](JSON_PARSE.md) to get a SUPER value. Then, use the [IS\_ARRAY function](r_is_array.md) function to confirm that the array is properly formed. 

The IS\_VALID\_JSON\_ARRAY function validates a JSON array. The function returns Boolean `true` if the array is properly formed JSON or `false` if the array is malformed. To validate a JSON string, use [IS\_VALID\_JSON function](IS_VALID_JSON.md)

For more information, see [JSON functions](json-functions.md). 

## Syntax
<a name="IS_VALID_JSON_ARRAY-synopsis"></a>

```
IS_VALID_JSON_ARRAY('json_array') 
```

## Arguments
<a name="IS_VALID_JSON_ARRAY-arguments"></a>

 *json\_array*  
A string or expression that evaluates to a JSON array.

## Return type
<a name="IS_VALID_JSON_ARRAY-return"></a>

`BOOLEAN`

## Examples
<a name="IS_VALID_JSON_ARRAY-examples"></a>

To create a table and insert JSON strings for testing, use the following example.

```
CREATE TABLE test_json_arrays(id int IDENTITY(0,1), json_arrays VARCHAR);

-- Insert valid JSON array strings --
INSERT INTO test_json_arrays(json_arrays) 
VALUES('[]'), 
('["a","b"]'), 
('["a",["b",1,["c",2,3,null]]]');

-- Insert invalid JSON array strings --
INSERT INTO test_json_arrays(json_arrays) 
VALUES('{"a":1}'),
('a'),
('[1,2,]');
```

To validate the strings in the preceding example, use the following example.

```
SELECT json_arrays, IS_VALID_JSON_ARRAY(json_arrays) 
FROM test_json_arrays ORDER BY id;

+------------------------------+---------------------+
|         json_arrays          | is_valid_json_array |
+------------------------------+---------------------+
| []                           | true                |
| ["a","b"]                    | true                |
| ["a",["b",1,["c",2,3,null]]] | true                |
| {"a":1}                      | false               |
| a                            | false               |
| [1,2,]                       | false               |
+------------------------------+---------------------+
```