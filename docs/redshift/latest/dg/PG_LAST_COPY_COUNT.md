Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_LAST_COPY_COUNT

Returns the number of rows that were loaded by the last COPY command run in the
current session. PG_LAST_COPY_COUNT is updated with the last COPY ID, which is the query
ID of the last COPY that began the load process, even if the load failed. The query ID
and COPY ID are updated when the COPY command begins the load process.

If the COPY fails because of a syntax error or because of insufficient privileges,
the COPY ID is not updated and PG_LAST_COPY_COUNT returns the count for the previous
COPY. If no COPY commands were run in the current session, or if the last COPY
failed during loading, PG_LAST_COPY_COUNT returns 0. For more information, see [PG_LAST_COPY_ID](PG_LAST_COPY_ID.md "PG_LAST_COPY_ID.md").

## Syntax

```
pg_last_copy_count()
```

## Return type

Returns BIGINT.

## Example

The following query returns the number of rows loaded by the latest COPY command
in the current session.

```
select pg_last_copy_count();

pg_last_copy_count
--------------------
             192497
(1 row)

```
