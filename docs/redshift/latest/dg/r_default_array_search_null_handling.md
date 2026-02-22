Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# default_array_search_null_handling

## Values (default in bold)

**TRUE**, FALSE

## Description

Specifies the null handling behavior for array search operations. When `default_array_search_null_handling` is `TRUE`, NULL values are treated as valid elements that can be searched within arrays. When `default_array_search_null_handling` is `FALSE`, NULL key searches return NULL, and if the array contains NULL values with no match found, the search returns NULL.

## Examples

```
SET default_array_search_null_handling to TRUE;

-- ARRAY_CONTAINS: NULL search is allowed
SELECT ARRAY_CONTAINS(ARRAY('red', NULL, 'green'), NULL);
array_contains
----------------
 t
(1 row)

-- ARRAY_POSITION: Array can contain NULLs
SELECT ARRAY_POSITION(ARRAY('red', NULL, 'green'), 'blue');
 array_position
----------------
             -1
(1 row)
```

```
SET default_array_search_null_handling to FALSE;

-- ARRAY_CONTAINS: NULL search is disabled
SELECT ARRAY_CONTAINS(ARRAY('red', 'green'), NULL);
array_contains
----------------

(1 row)

-- ARRAY_POSITION: Array contains NULL but no match is found
SELECT ARRAY_POSITION(ARRAY('red', NULL, 'green'), 'blue');
 array_position
----------------

(1 row)
```
