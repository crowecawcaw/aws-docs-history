

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SUBARRAY function
<a name="r_subarray"></a>

Extracts a portion of an array starting from a specified position. Returns a new array containing the specified number of elements from the input array.

## Syntax
<a name="r_subarray-syntax"></a>

```
SUBARRAY( super_expr, start_position, length )
```

## Arguments
<a name="r_subarray-arguments"></a>

*super\_expr*  
A valid SUPER expression in array form.

*start\_position*  
An integer that specifies the starting position for extraction. The index is 0-based, where 0 indicates the first element. If start\_position is beyond the array length, an empty array is returned.

*length*  
An optional integer that specifies the number of elements to extract. If omitted, all elements from the start position to the end of the array are returned.

## Return type
<a name="r_subarray-return-type"></a>

The SUBARRAY function returns a SUPER data value.

## Examples
<a name="r_subarray-examples"></a>

The following is an example of a SUBARRAY function.

```
 SELECT SUBARRAY(ARRAY('a', 'b', 'c', 'd', 'e', 'f'), 2, 3);
   subarray
---------------
 ["c","d","e"]
(1 row)
```

## See also
<a name="r_subarray-see-also"></a>
+ [ARRAY\_POSITION function](array_position.md)
+ [ARRAY\_POSITIONS function](array_positions.md)
+ [ARRAY\_FLATTEN function](array_flatten.md)
+ [ARRAY\_CONCAT function](r_array_concat.md)