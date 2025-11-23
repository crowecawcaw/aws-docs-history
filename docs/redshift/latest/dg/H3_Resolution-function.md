Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_Resolution

H3_Resolution returns the resolution of an H3 cell ID from an input index. Resolution is an integer from 0 (coarsest) to 15 (finest).
For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_Resolution(*index*)
```

## Arguments

_index_

A value of data type `BIGINT` or `VARCHAR` that represents the index of an H3 cell, or an expression that evaluates to one of these data types.

## Return type

`INTEGER` – represents the resolution of the input H3 cell ID.

If _index_ is NULL, then NULL is returned.

If _index_ is not valid, then an error is returned.

## Examples

The following SQL inputs a VARCHAR that represents the index of an H3 cell, and returns an INTEGER that represents the resolution of the input H3 cell.

```
SELECT H3_Resolution('8025fffffffffff');
```

```

 h3_resolution
---------------
 0

```

The following SQL inputs a BIGINT that represents the index of an H3 cell, and returns an INTEGER that represents the resolution of the input H3 cell.

```
SELECT H3_Resolution(614553222213795839);
```

```

 h3_resolution
---------------
 8

```
