Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_POSITIONS function

Returns an array of positions (indices) where the specified element appears in the input array. The indices are 0-based, where 0 indicates the first element, 1 indicates the second element, and so on. Returns an empty array if the element is not found.

## Syntax

```
ARRAY_POSITIONS( *array*, *value* [, *null\_match*] )
```

## Arguments

_array_

A SUPER expression that specifies the array in which to search.

_value_

A value that specifies the element to search for.

_null_match_

A boolean value that specifies how NULL values are handled:

- _null_match_ = FALSE: Searching for NULL returns NULL. If the array contains NULL values and no match is found for a non-NULL search value, returns NULL.
- _null_match_ = TRUE: NULLs are treated as valid, searchable elements. If the array contains NULL values and no match is found for a non-NULL search value, it returns an empty array.

The default is TRUE.

Default NULL handling can also be specified by the configuration option:

```
-- same as null_match = TRUE
SET default_array_search_null_handling to TRUE;
```

## Return type

The ARRAY_POSITIONS function returns a SUPER type.

## Example

The following examples show the ARRAY_POSITIONS function.

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

The following examples show the function behavior with _null_match_ set to TRUE.

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

The following examples show the function behavior with _null_match_ set to FALSE. Note that specifying the _null_match_ behavior in the function will override the default configuration setting.

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

- [ARRAY_POSITION function](array_position.md "array_position.md")
- [ARRAY_CONTAINS function](array_contains.md "array_contains.md")
- [SUBARRAY function](r_subarray.md "r_subarray.md")
