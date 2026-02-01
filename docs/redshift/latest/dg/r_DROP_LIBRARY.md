Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP LIBRARY

Removes a custom Python library from the database. Only the library owner or a superuser
can drop a library.

DROP LIBRARY can't be run inside a transaction block (BEGIN … END). For more
information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

This command isn't reversible. The DROP LIBRARY command commits immediately. If a
UDF that depends on the library is running concurrently, the UDF might fail, even if the
UDF is running within a transaction.

For more information, see [CREATE LIBRARY](r_CREATE_LIBRARY.md "r_CREATE_LIBRARY.md").

## Required privileges

Following are required privileges for DROPLIBRARY:

- Superuser
- Users with the DROP LIBRARY privilege
- Library owner

## Syntax

```
DROP LIBRARY *library\_name*
```

## Parameters

_library_name_

The name of the library.
