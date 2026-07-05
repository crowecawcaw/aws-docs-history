Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# pg\_federation\_repeatable\_read

## Values (default in bold)

**true**, _false_

## Description

Specifies the federated query transaction isolation level for the results from the PostgreSQL database.

- When `pg_federation_repeatable_read` is true, federated transactions are processed with REPEATABLE READ isolation level semantics. This is the default.
- When `pg_federation_repeatable_read` is false, federated transactions are processed with READ COMMITTED isolation level semantics.

For more information, see the following:

- [Considerations when accessing federated data with Amazon Redshift](federated-limitations.md "federated-limitations.md").
- [Managing concurrent write operations](c_Concurrent_writes.md "c_Concurrent_writes.md").

## Examples

The following command sets `pg_federation_repeatable_read` to `on` for a session.
The show command shows the value of the set value.

```
set pg_federation_repeatable_read to on;

```

```
show pg_federation_repeatable_read;

pg_federation_repeatable_read
-----------------------------
on

```
