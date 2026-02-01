Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing concurrent write operations

Some applications require not only concurrent querying and loading, but also the ability
to write to multiple tables or the same table concurrently. In this context,
_concurrently_ means overlapping, not scheduled to run at precisely
the same time. Two transactions are considered to be concurrent if the second one
starts before the first commits. Concurrent operations can originate from different
sessions that are controlled either by the same user or by different users.

Amazon Redshift supports these types of applications by allowing tables to be read while they
are being incrementally loaded or modified. Queries simply see the latest committed
version, or _snapshot_, of the data, rather than waiting for the next
version to be committed. If you want a particular query to wait for a commit from another
write operation, you have to schedule it accordingly.

###### Note

Amazon Redshift supports a default _automatic commit_ behavior in
which each separately run SQL command commits individually. If you enclose a set of
commands in a transaction block (defined by [BEGIN](r_BEGIN.md "r_BEGIN.md") and [END](r_END.md "r_END.md")
statements), the block commits as one transaction, so you can roll it back if
necessary. Exceptions to this behavior are the TRUNCATE and VACUUM commands, which
automatically commit all outstanding changes made in the current transaction.

Some SQL clients issue BEGIN and COMMIT commands automatically, so the client
controls whether a group of statements are run as a transaction or each individual
statement is run as its own transaction. Check the documentation for the interface
you are using. For example, when using the Amazon Redshift JDBC driver, a JDBC
`PreparedStatement` with a query string that contains multiple
(semicolon separated) SQL commands runs all the statements as a single transaction.
In contrast, if you use SQL Workbench/J and set AUTO COMMIT ON, then if you run
multiple statements, each statement runs as its own transaction.

The following topics describe some of the key concepts and use cases that involve
transactions, database snapshots, updates, and concurrent behavior.

###### Topics

- [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md")
- [Write and read/write operations](c_write_readwrite.md "c_write_readwrite.md")
- [Concurrent write examples](r_Serializable_isolation_example.md "r_Serializable_isolation_example.md")
- [Troubleshooting serializable isolation errors](c_serial_isolation-serializable-isolation-troubleshooting.md "c_serial_isolation-serializable-isolation-troubleshooting.md")
