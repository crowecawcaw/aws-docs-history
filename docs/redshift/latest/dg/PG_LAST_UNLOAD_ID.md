Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_LAST_UNLOAD_ID

Returns the query ID of the most recently completed UNLOAD command in the current
session. If no UNLOAD commands have been run in the current session, PG_LAST_UNLOAD_ID
returns -1.

The value for PG_LAST_UNLOAD_ID is updated when the UNLOAD command begins the load
process. If the UNLOAD fails because of invalid load data, the UNLOAD ID is updated, so you
can use the UNLOAD ID for further investigation. If the UNLOAD transaction is
rolled back, the UNLOAD ID is not updated.

The UNLOAD ID is not updated if the UNLOAD command fails because of an error that occurs
before the load process begins, such as a syntax error, access error, invalid
credentials, or insufficient privileges.

## Syntax

```
PG_LAST_UNLOAD_ID()
```

## Return type

Returns an integer.

## Example

The following query returns the query ID of the latest UNLOAD command in the current
session.

```
select PG_LAST_UNLOAD_ID();

PG_LAST_UNLOAD_ID
---------------
          5437
(1 row)
```
