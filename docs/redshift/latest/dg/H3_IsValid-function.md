Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_IsValid

H3_IsValid returns true if the input represents an H3 cell ID, otherwise false.
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_IsValid(*index*)
```

## Arguments

_index_

A value of data type `BIGINT` or `VARCHAR`, or an expression that evaluates to one of these data types.

## Return type

`BOOLEAN` – true if the input represents a valid H3 cell ID, false otherwise.

If _index_ is NULL, then NULL is returned.

## Examples

The following SQL inputs a VARCHAR that represents an H3 cell ID, and returns true.

```
SELECT H3_IsValid('8025fffffffffff');
```

```

 h3_isvalid
------------
 true

```

The following SQL inputs a BIGINT that represents an H3 cell ID, and returns true.

```
SELECT H3_IsValid(577129255373111295);
```

```

 h3_isvalid
------------
 true

```

The following SQL inputs an invalid H3 cell ID and returns false.

```
SELECT H3_IsValid('');
```

```

 h3_isvalid
------------
 false

```
