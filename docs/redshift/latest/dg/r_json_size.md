

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# JSON\_SIZE function
<a name="r_json_size"></a>

The JSON\_SIZE function returns the number of bytes in the given `SUPER` expression when serialized into a string. 

## Syntax
<a name="r_json_size-synopsis"></a>

```
JSON_SIZE(super_expression)
```

## Arguments
<a name="r_json_size-arguments"></a>

*super\_expression*  
A `SUPER` constant or expression.

## Return type
<a name="r_json_size-returns"></a>

`INTEGER`  
The JSON\_SIZE function returns an `INTEGER` indicating the number of bytes in the input string. This value is different from the number of characters. For example, the UTF-8 character ⬤, a black dot, is 3 bytes in size even though it is 1 character.

## Usage notes
<a name="r_json_size-usage_notes"></a>

JSON\_SIZE(x) is functionally identical to OCTET\_LENGTH(JSON\_SERIALIZE). However, note that JSON\_SERIALIZE returns an error when the provided `SUPER` expression would exceed the `VARCHAR` limit of the system when serialized. JSON\_SIZE does not have this limitation.

## Examples
<a name="r_json_size_example"></a>

To return the length of a `SUPER` value serialized to a string, use the following example.

```
SELECT JSON_SIZE(JSON_PARSE('[10001,10002,"⬤"]'));

+-----------+
| json_size |
+-----------+
|        19 |
+-----------+
```

Note that the provided `SUPER` expression is 17 characters long, but ⬤ is a 3-byte character, so JSON\_SIZE returns `19`.