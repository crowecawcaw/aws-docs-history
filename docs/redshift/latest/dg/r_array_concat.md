

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ARRAY\_CONCAT function
<a name="r_array_concat"></a>

Concatenates two arrays to create an array that contains all the elements in the first array followed by all the elements in the second array. The two arguments must be valid SUPER arrays.

## Syntax
<a name="r_array_concat-synopsis"></a>

```
ARRAY_CONCAT( array1, array2 )
```

## Arguments
<a name="r_array_concat-argument-arguments"></a>

 *array1*  
The value that specifies the first of the two arrays to concatenate.

 *array2*  
The value that specifies the second of the two arrays to concatenate.

## Return type
<a name="r_array_concat-return-type"></a>

The ARRAY\_CONCAT function returns a SUPER data value.

## Example
<a name="r_array_concat-example"></a>

The following examples shows concatenation of two arrays of the same type and concatenation of two arrays of different types.

```
-- concatenating two arrays 
SELECT ARRAY_CONCAT(ARRAY(10001,10002),ARRAY(10003,10004));
              array_concat
------------------------------------
 [10001,10002,10003,10004]
(1 row)

-- concatenating two arrays of different types 
SELECT ARRAY_CONCAT(ARRAY(10001,10002),ARRAY('ab','cd'));
          array_concat
------------------------------
 [10001,10002,"ab","cd"]
(1 row)
```

## See also
<a name="r_array_concat-see-also"></a>
+ [ARRAY\_UNION function](array_union.md)
+ [ARRAY\_FLATTEN function](array_flatten.md)
+ [SPLIT\_TO\_ARRAY function](split_to_array.md)
+ [ARRAY\_DISTINCT function](array_distinct.md)