

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# GET\_NUMBER\_ATTRIBUTES function
<a name="get_number_attributes"></a>

Returns a count of how many key-value pairs exist at the root level of a dictionary object.

## Syntax
<a name="get_number_attributes-syntax"></a>

```
GET_NUMBER_ATTRIBUTES( super_expression )
```

## Arguments
<a name="get_number_attributes-arguments"></a>

 *super\_expression*   
A SUPER expression of dictionary form.

## Return type
<a name="get_number_attributes-return-type"></a>

The GET\_NUMBER\_ATTRIBUTES function returns an INT type.

## Note
<a name="get_number_attributes-note"></a>

This function only counts direct attributes and does not include pairs within nested dictionaries.

## Example
<a name="get_number_attributes-example"></a>

The following example shows the GET\_NUMBER\_ATTRIBUTES function.

```
SELECT GET_NUMBER_ATTRIBUTES(JSON_PARSE('{"a": 1, "b": 2, "c": 3}'));
 get_number_attributes
-----------------------
            3
(1 row)
```

The GET\_NUMBER\_ATTRIBUTES function only operates on the first level of the dictionary.

```
SELECT GET_NUMBER_ATTRIBUTES(JSON_PARSE('{"a": 1, "b": {"c": 3}}'));
 get_number_attributes
-----------------------
            2
(1 row)
```