Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_POSITION function

Returns the position (index) of the first occurrence of a specified element in an array. The index is 0-based, where 0 indicates the first element, 1 indicates the second element, and so on. Returns -1 if the element is not found in the array.

The function returns only the position of the first occurrence. To find all occurrences, consider using the [ARRAY_POSITIONS function](array_positions.md "array_positions.md") function.

## Syntax

```
ARRAY_POSITION( *array*, *value* [, *null\_match*] )
```

## Arguments

_array_

A SUPER expression that specifies the array in which to search.

_value_

A value that specifies the element to search for.

_null_match_

A boolean value that specifies how NULL values are handled:

- _null_match_ = FALSE: Searching for NULL returns NULL. If the array contains NULL values and no match is found for a non-NULL search value, returns NULL.
- _null_match_ = TRUE: NULLs are treated as valid, searchable elements. If the array contains NULL values and no match is found for a non-NULL search value, it returns -1.

The default is TRUE.

Default NULL handling can also be specified by the configuration option:

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;
```

## Return type

The ARRAY_POSITION function returns an INT type.

## Example

The following examples show the ARRAY_POSITION function.

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

The following examples show the function behavior with _null_match_ set to TRUE.

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

The following examples show the function behavior with _null_match_ set to FALSE. Note that specifying the _null_match_ behavior in the function will override the default configuration setting.

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

- [ARRAY_POSITIONS function](array_positions.md "array_positions.md")
- [ARRAY_CONTAINS function](array_contains.md "array_contains.md")
- [SUBARRAY function](r_subarray.md "r_subarray.md")
