Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using prepared statement

support

The Amazon Redshift JDBC driver supports prepared statements. You can use prepared statements
to improve the performance of parameterized queries that need to be run multiple times
during the same connection.

A _prepared statement_ is a SQL statement that is
compiled on the server side but not run immediately. The compiled statement is stored on
the server as a PreparedStatement object until you close the object or the connection.
While that object exists, you can run the prepared statement as many times as needed
using different parameter values, without having to compile the statement again. This
reduced overhead enables the set of queries to be run more quickly.

For more information about prepared statements, see "Using Prepared Statements" in
[JDBC
Basics tutorial from Oracle](https://docs.oracle.com/javase/tutorial/jdbc/basics/prepared.html "https://docs.oracle.com/javase/tutorial/jdbc/basics/prepared.html").

You can prepare a statement that contains multiple queries. For example, the following
prepared statement contains two INSERT queries:

```
PreparedStatement pstmt = conn.prepareStatement("INSERT INTO
MyTable VALUES (1, 'abc'); INSERT INTO CompanyTable VALUES
(1, 'abc');");
```

Take care that these queries don't depend on the results of other queries that are
specified within the same prepared statement. Because queries don't run during the
prepare step, the results have not been returned yet, and aren't available to other
queries in the same prepared statement.

For example, the following prepared statement, which creates a table and then inserts
values into that newly-created table, is not allowed:

```
PreparedStatement pstmt = conn.prepareStatement("CREATE
TABLE MyTable(col1 int, col2 varchar); INSERT INTO myTable
VALUES (1, 'abc');");
```

If you try to prepare this statement, the server returns an error stating that the
destination table (myTable) doesn't exist yet. The CREATE query must be run before
the INSERT query can be prepared.
