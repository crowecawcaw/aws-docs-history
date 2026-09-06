

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ARRAY\_POSITION function
<a name="array_position"></a>

Returns the position (index) of the first occurrence of a specified element in an array. The index is 0-based, where 0 indicates the first element, 1 indicates the second element, and so on. Returns -1 if the element is not found in the array.

The function returns only the position of the first occurrence. To find all occurrences, consider using the [ARRAY\_POSITIONS function](array_positions.md) function.

## Syntax
<a name="array_position-syntax"></a>

```
ARRAY_POSITION( array, value [, null_match] )
```

## Arguments
<a name="array_position-arguments"></a>

 *array*   
A SUPER expression that specifies the array in which to search.

 *value*   
A value that specifies the element to search for.

 *null\_match*   
A boolean value that specifies how NULL values are handled:  
+ *null\_match* = FALSE: Searching for NULL returns NULL. If the array contains NULL values and no match is found for a non-NULL search value, returns NULL.
+ *null\_match* = TRUE: NULLs are treated as valid, searchable elements. If the array contains NULL values and no match is found for a non-NULL search value, it returns -1.
The default is TRUE.  
Default NULL handling can also be specified by the configuration option:  

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;
```

## Return type
<a name="array_position-return-type"></a>

The ARRAY\_POSITION function returns an INT type.

## Example
<a name="array_position-example"></a>

The following examples show the ARRAY\_POSITION function.

```
SELECT ARRAY_POSITION(ARRAY('red', 'green'), 'red');
 array_position 
----------------
              0
(1 row)

SELECT ARRAY_POSITION(ARRAY(1, 2, 3), 4);
 array_position 
----------------
             -1
(1 row)

-- only the position of the first occurrence is returned
SELECT ARRAY_POSITION(ARRAY('red', 'green', 'red'), 'red');
 array_position 
----------------
              0
(1 row)
```

The following examples show the function behavior with *null\_match* set to TRUE.

```
SET default_array_search_null_handling to TRUE;

-- NULL search is enabled
SELECT ARRAY_POSITION(ARRAY('red', NULL, 'green'), NULL);
 array_position 
----------------
              1
(1 row)

-- The array can contain NULLs
SELECT ARRAY_POSITION(ARRAY('red', NULL, 'green'), 'blue', TRUE);
 array_position 
----------------
             -1
(1 row)
```

The following examples show the function behavior with *null\_match* set to FALSE. Note that specifying the *null\_match* behavior in the function will override the default configuration setting.

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;

-- NULL search is disabled. The default behavior is overridden
SELECT ARRAY_POSITION(ARRAY('red', 'green'), NULL, FALSE);
 array_position 
----------------
               
(1 row)

-- same as null_match = FALSE
SET default_array_search_null_handling to FALSE;

-- The array contains NULL and a match is found
SELECT ARRAY_POSITION(ARRAY('red', NULL, 'green'), 'green');
 array_position 
----------------
              2
(1 row)

-- The array contains NULL but no match is found
SELECT ARRAY_POSITION(ARRAY('red', NULL, 'green'), 'blue');
 array_position 
----------------
               
(1 row)
```

## See also
<a name="array_position-see-also"></a>
+ [ARRAY\_POSITIONS function](array_positions.md)
+ [ARRAY\_CONTAINS function](array_contains.md)
+ [SUBARRAY function](r_subarray.md)