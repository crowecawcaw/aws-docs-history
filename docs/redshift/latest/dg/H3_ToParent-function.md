Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# H3_ToParent

H3_ToParent returns the parent H3 cell ID at a specified parent resolution for a given H3 index. For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3 "spatial-terminology.md#spatial-terminology-h3").

## Syntax

```
H3_ToParent(*index*, *resolution*)
```

## Arguments

_index_

A value of data type `BIGINT` or `VARCHAR` that represents the index of an H3 cell, or an expression that evaluates to one of these data types.

_resolution_

A value of data type `INTEGER` or an expression that evaluates to an `INTEGER` type. The value represents the resolution of the parent cell ID. The value must be between 0 and the resolution of _index_, inclusive.

## Return type

`BIGINT` – represents the parent's H3 cell ID.

If either _index_ or _resolution_ is NULL, then NULL is returned.

If _index_ is not valid, then an error is returned.

If _resolution_ is less than 0 or greater than the resolution of _index_, then an error is returned.

## Examples

The following SQL inputs a VARCHAR that represents the index of an H3 cell, and an INTEGER that represents the desired resolution of the desired parent, and returns a BIGINT that represents the parent at resolution 0 of the input H3 cell.

```
SELECT H3_ToParent('85283473fffffff', 0);
```

```

 h3_toparent
--------------------
 577199624117288959

```

The following SQL inputs a BIGINT that represents the index of an H3 cell, and an INTEGER that represents the desired resolution of the desired parent, and returns a BIGINT that represents the parent at resolution 0 of the input H3 cell.

```
SELECT H3_ToParent(646078419604526808, 8);
```

```

 h3_toparent
--------------------
 614553222213795839

```
