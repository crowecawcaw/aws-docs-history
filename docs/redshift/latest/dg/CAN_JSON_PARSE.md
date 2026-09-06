

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CAN\_JSON\_PARSE function
<a name="CAN_JSON_PARSE"></a>

The CAN\_JSON\_PARSE function parses data in JSON format and returns `true` if the result can be converted to a `SUPER` value using the JSON\_PARSE function.

## Syntax
<a name="CAN_JSON_PARSE-synopsis"></a>

```
CAN_JSON_PARSE( {json_string | binary_value} )
```

## Arguments
<a name="CAN_JSON_PARSE-arguments"></a>

 *json\_string*  
An expression that returns serialized JSON in `VARCHAR` form. 

 *binary\_value*  
A VARBYTE type binary value.

## Return type
<a name="CAN_JSON_PARSE-return"></a>

`BOOLEAN`

## Usage notes
<a name="CAN_JSON_PARSE-usage-notes"></a>
+ CAN\_JSON\_PARSE returns false for empty strings. It returns NULL when the input argument is null. 

## Examples
<a name="CAN_JSON_PARSE-examples"></a>

 The following example shows CAN\_JSON\_PARSE running on a properly formed JSON array using a CASE condition. It returns true, so Amazon Redshift runs the JSON\_PARSE function on the example value. 

```
SELECT CASE 
            WHEN CAN_JSON_PARSE('[10001,10002,"abc"]')
            THEN JSON_PARSE('[10001,10002,"abc"]')
        END;

 case
---------------------
'[10001,10002,"abc"]'
```

 The following example shows CAN\_JSON\_PARSE running on a value that isn’t JSON format using a CASE condition. It returns false, so Amazon Redshift returns the segment in the ELSE clause of the CASE condition instead. 

```
SELECT CASE 
            WHEN CAN_JSON_PARSE('This is a string.')
            THEN JSON_PARSE('This is a string.')
            ELSE 'This is not JSON.'
        END;

 case
---------------------
"This is not JSON."
```