

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# GET\_ARRAY\_LENGTH function
<a name="get_array_length"></a>

Returns the length of a SUPER array given an object or array path.

## Syntax
<a name="get_array_length-syntax"></a>

```
GET_ARRAY_LENGTH( super_expr )
```

## Arguments
<a name="get_array_length-arguments"></a>

 *super\_expr*   
A valid SUPER expression of array form.

## Return type
<a name="get_array_length-returm-type"></a>

The GET\_ARRAY\_LENGTH function returns an INT. 

## Example
<a name="get_array_length-example"></a>

The following example shows the GET\_ARRAY\_LENGTH function.

```
SELECT GET_ARRAY_LENGTH(ARRAY(1,2,3,4,5,6,7,8,9,10));
 get_array_length
----------------------
            10
(1 row)
```