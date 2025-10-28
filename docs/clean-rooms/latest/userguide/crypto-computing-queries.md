# Queries with Cryptographic Computing for Clean Rooms

This topic provides information about writing queries that use data tables that have been
encrypted using
Cryptographic Computing for Clean Rooms.

###### Topics

- [Queries that branch on NULL](#queries-branch-on-null "#queries-branch-on-null")
- [Mapping one source column to multiple target columns](#queries-mapping "#queries-mapping")
- [Using the same data for both JOIN and
  SELECT queries](#queries-using-same-data "#queries-using-same-data")

## Queries that branch on NULL

To have a query branch on a NULL statement means to use syntax like
`IF x IS NULL THEN 0 ELSE 1`.

Queries can always branch on NULL statements in cleartext
columns.

Queries can branch on NULL statements in sealed columns and
fingerprint columns only when the value of the **Preserve NULL
values** parameter (`preserveNulls`) is set to `true`.

Queries that violate these constraints might yield incorrect results.

## Mapping one source column to multiple target columns

One source column can map to multiple target columns. For example, you might want to both
JOIN and SELECT on a column.

For more information, see [Using the same data for both JOIN and
SELECT queries](#queries-using-same-data "#queries-using-same-data").

## Using the same data for both JOIN and

SELECT queries

If the data in a column is not sensitive, it can appear in a cleartext
target column, which allows it to be used for any purpose.

If data in a column is sensitive and must be used for both JOIN and
SELECT queries, map that source column to two target columns in the output
file. One column is encrypted with the `type` as a fingerprint
column, and one column is encrypted with the `type` as a sealed column. The
interactive schema generation of the C3R encryption client suggests header suffixes of
`_fingerprint` and `_sealed`. These header suffixes can be a useful
convention for differentiating such columns quickly.
