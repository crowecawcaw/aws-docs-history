Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_LAST_UNLOAD_COUNT

Returns the number of rows that were unloaded by the last UNLOAD command completed in
the current session. PG_LAST_UNLOAD_COUNT is updated with the query ID of the last
UNLOAD, even if the operation failed. The query ID is updated when the UNLOAD is
completed. If the UNLOAD fails because of a syntax error or because of insufficient
privileges, PG_LAST_UNLOAD_COUNT returns the count for the previous UNLOAD. If no UNLOAD
commands were completed in the current session, or if the last UNLOAD failed during the
unload operation, PG_LAST_UNLOAD_COUNT returns 0.

## Syntax

```
pg_last_unload_count()
```

## Return type

Returns BIGINT.

## Example

The following query returns the number of rows unloaded by the latest UNLOAD
command in the current session.

```
select pg_last_unload_count();

pg_last_unload_count
--------------------
             192497
(1 row)

```
