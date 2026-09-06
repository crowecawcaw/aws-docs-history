

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ARRAY\_POSITIONS function
<a name="array_positions"></a>

Returns an array of positions (indices) where the specified element appears in the input array. The indices are 0-based, where 0 indicates the first element, 1 indicates the second element, and so on. Returns an empty array if the element is not found.

## Syntax
<a name="array_positions-syntax"></a>

```
ARRAY_POSITIONS( array, value [, null_match] )
```

## Arguments
<a name="array_positions-arguments"></a>

 *array*   
A SUPER expression that specifies the array in which to search.

 *value*   
A value that specifies the element to search for.

 *null\_match*   
A boolean value that specifies how NULL values are handled:  
+ *null\_match* = FALSE: Searching for NULL returns NULL. If the array contains NULL values and no match is found for a non-NULL search value, returns NULL.
+ *null\_match* = TRUE: NULLs are treated as valid, searchable elements. If the array contains NULL values and no match is found for a non-NULL search value, it returns an empty array.
The default is TRUE.  
Default NULL handling can also be specified by the configuration option:  

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;
```

## Return type
<a name="array_positions-return-type"></a>

The ARRAY\_POSITIONS function returns a SUPER type.

## Example
<a name="array_positions-example"></a>

The following examples show the ARRAY\_POSITIONS function.

```
SELECT ARRAY_POSITIONS(ARRAY('red', 'green', 'red'), 'red');
 array_positions 
-----------------
 [0,2]
(1 row)

SELECT ARRAY_POSITIONS(ARRAY(1, 2, 3), 4);
 array_positions 
-----------------
 []
(1 row)
```

The following examples show the function behavior with *null\_match* set to TRUE.

```
SET default_array_search_null_handling to TRUE;

-- NULL search is enabled
SELECT ARRAY_POSITIONS(ARRAY('red', NULL, 'green', NULL), NULL);
 array_positions 
-----------------
 [1,3]
(1 row)

-- The array can contain NULLs
SELECT ARRAY_POSITIONS(ARRAY('red', NULL, 'green'), 'blue', TRUE);
 array_positions 
-----------------
 []
(1 row)
```

The following examples show the function behavior with *null\_match* set to FALSE. Note that specifying the *null\_match* behavior in the function will override the default configuration setting.

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;

-- NULL search is disabled. The default behavior is overridden
SELECT ARRAY_POSITIONS(ARRAY('red', 'green'), NULL, FALSE);
 array_positions 
-----------------
 
(1 row)

-- same as null_match = FALSE
SET default_array_search_null_handling to FALSE;

-- The array contains NULL and a match is found
SELECT ARRAY_POSITIONS(ARRAY('red', NULL, 'green'), 'green');
 array_positions 
-----------------
 [2]
(1 row)

-- The array contains NULL but no match is found
SELECT ARRAY_POSITIONS(ARRAY('red', NULL, 'green'), 'blue');
 array_positions 
-----------------
 
(1 row)
```

## See also
<a name="array_positions-see-also"></a>
+ [ARRAY\_POSITION function](array_position.md)
+ [ARRAY\_CONTAINS function](array_contains.md)
+ [SUBARRAY function](r_subarray.md)