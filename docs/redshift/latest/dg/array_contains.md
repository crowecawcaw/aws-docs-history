

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ARRAY\_CONTAINS function
<a name="array_contains"></a>

Checks if the array contains the given value and returns TRUE if found.

## Syntax
<a name="array_contains-syntax"></a>

```
ARRAY_CONTAINS( array, value [, null_match] )
```

## Arguments
<a name="array_contains-arguments"></a>

 *array*   
A SUPER expression that specifies the array in which to search.

 *value*   
A value that specifies the element to search for.

 *null\_match*   
A boolean value that specifies how NULL values are handled:  
+ *null\_match* = FALSE: Searching for NULL returns NULL. If the array contains NULL values and no match is found for a non-NULL search value, returns NULL.
+ *null\_match* = TRUE: NULLs are treated as valid, searchable elements. If the array contains NULL values and no match is found for a non-NULL search value, it returns FALSE.
The default is TRUE.  
Default NULL handling can also be specified by the configuration option:  

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;
```

## Return type
<a name="array_contains-return-type"></a>

The ARRAY\_CONTAINS function returns a BOOLEAN type.

## Example
<a name="array_contains-example"></a>

The following examples show the ARRAY\_CONTAINS function.

```
SELECT ARRAY_CONTAINS(ARRAY('red', 'green'), 'red');
array_contains
----------------
 t
(1 row)
```

The following examples show the function behavior with *null\_match* set to TRUE.

```
SET default_array_search_null_handling to TRUE;

-- NULL search is enabled
SELECT ARRAY_CONTAINS(ARRAY('red', NULL, 'green'), NULL);
array_contains
----------------
 t
(1 row)

-- The array can contain NULLs
SELECT ARRAY_CONTAINS(ARRAY('red', NULL, 'green'), 'blue', TRUE);
array_contains
----------------
 f
(1 row)
```

The following examples show the function behavior with *null\_match* set to FALSE. Note that specifying the *null\_match* behavior in the function will override the default configuration setting.

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;

-- NULL search is disabled. The default behavior is overridden
SELECT ARRAY_CONTAINS(ARRAY('red', 'green'), NULL, FALSE);
array_contains
----------------
 
(1 row)

-- same as null_match = FALSE
SET default_array_search_null_handling to FALSE;

-- The array contains NULL and a match is found
SELECT ARRAY_CONTAINS(ARRAY('red', NULL, 'green'), 'green');
array_contains
----------------
 t
(1 row)

-- The array contains NULL but no match is found
SELECT ARRAY_CONTAINS(ARRAY('red', NULL, 'green'), 'blue');
array_contains
----------------
 
(1 row)
```

## See also
<a name="array_contains-see-also"></a>
+ [ARRAY\_POSITION function](array_position.md)
+ [ARRAY\_POSITIONS function](array_positions.md)
+ [ARRAYS\_OVERLAP function](arrays_overlap.md)