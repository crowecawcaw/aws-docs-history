Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Differences between the 2.2 and 1.x

versions of the JDBC driver

This section describes the differences in the information returned by the 2.2 and 1.x
versions of the JDBC driver. The JDBC driver version 1.x is discontinued.

The following table lists the DatabaseMetadata information returned by the
getDatabaseProductName() and getDatabaseProductVersion() functions for each version of
the JDBC driver. JDBC driver version 2.2 obtains the values while establishing the
connection. JDBC driver version 1.x obtains the values as a result of a query.

| JDBC driver version | getDatabaseProductName() result | getDatabaseProductVersion() result |
| ------------------- | ------------------------------- | ---------------------------------- |
| 2.2                 | Redshift                        | 8.0.2                              |
| 1.x                 | PostgreSQL                      | 08.00.0002                         |

The following table lists the DatabaseMetadata information returned by the getTypeInfo
function for each version of the JDBC driver.

| JDBC driver version | getTypeInfo result                   |
| ------------------- | ------------------------------------ |
| 2.2                 | Consistent with Redshift datatypes   |
| 1.x                 | Consistent with PostgreSQL datatypes |
