

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ARRAY\_EXCEPT function
<a name="array_except"></a>

Returns the difference between two arrays by keeping elements from the first array that do not exist in the second array. The function is NULL-safe, meaning it treats NULLs are treated as known objects.

## Syntax
<a name="array_except-syntax"></a>

```
ARRAY_EXCEPT( array1, array2 [, distinct] )
```

## Arguments
<a name="array_except-arguments"></a>

 *array1*   
A SUPER expression that specifies the first array.

 *array2*   
A SUPER expression that specifies the second array.

 *distinct*   
A boolean value that specifies whether to return distinct elements only:  
+ *distinct* = FALSE: Multi-set semantics apply. Each occurrence of an element in the first array is matched against occurrences in the second array. If the first array has more occurrences of an element than the second array, the extra occurrences are preserved in the result.
+ *distinct* = TRUE: Set semantics apply. Both arrays are treated as sets, ignoring duplicate elements. Elements from the first array are removed if they exist anywhere in the second array, regardless of occurrence count.
The default is FALSE.

## Return type
<a name="array_except-return-type"></a>

The ARRAY\_EXCEPT function returns a SUPER type.

## Example
<a name="array_except-example"></a>

The following examples show the ARRAY\_EXCEPT function.

```
SELECT ARRAY_EXCEPT(ARRAY('a','b','c'), ARRAY('b','c','d'));
 array_except
--------------
 ["a"]
(1 row)
```

Multi-set semantics:

```
SELECT ARRAY_EXCEPT(ARRAY('b','b','b','b'), ARRAY('b','b'));
 array_except
--------------
 ["b","b"]
(1 row)
```

Set semantics:

```
SELECT ARRAY_EXCEPT(ARRAY('a','b','b'), ARRAY('b'), TRUE);
 array_except
--------------
 ["a"]
(1 row)
```

NULLs are treated as known object.

```
SELECT ARRAY_EXCEPT(ARRAY('a',NULL), ARRAY(NULL));
 array_except
--------------
 ["a"]
(1 row)
```

## See also
<a name="array_except-see-also"></a>
+ [ARRAY\_INTERSECTION function](array_intersection.md)
+ [ARRAY\_UNION function](array_union.md)
+ [ARRAY\_DISTINCT function](array_distinct.md)
+ [ARRAYS\_OVERLAP function](arrays_overlap.md)