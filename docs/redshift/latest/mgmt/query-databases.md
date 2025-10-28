Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query a database

To query databases hosted by your Amazon Redshift cluster, you have two options:

- Connect to your cluster and run queries on the AWS Management Console with the query editor.

If you use the query editor on the Amazon Redshift console, you don't have to download
and set up a SQL client application.

- Connect to your cluster through a SQL client tool, such as SQL Workbench/J.

Amazon Redshift supports SQL client tools connecting through Java Database Connectivity
(JDBC) and Open Database Connectivity (ODBC). Amazon Redshift doesn't provide or install
any SQL client tools or libraries, so you must install them on your client computer
or Amazon EC2 instance to use them. You can use most SQL client tools that support
JDBC or ODBC drivers.

###### Note

When you write stored procedures, we recommend a best practice for securing sensitive
values:

Don't hard code any sensitive information in stored procedure logic. For example,
don't assign a user password in a CREATE USER statement in the body of a stored
procedure. This poses a security risk, because hard-coded values can be recorded as
schema metadata in catalog tables. Instead, pass sensitive values, such as passwords, as
arguments to the stored procedure, by means of parameters.

For more information about stored procedures, see [CREATE PROCEDURE](../dg/r_CREATE_PROCEDURE.md "../dg/r_CREATE_PROCEDURE.md") and [Creating stored procedures in
Amazon Redshift](../dg/stored-procedure-overview.md "../dg/stored-procedure-overview.md"). For more information about catalog tables, see [System catalog tables](../dg/c_intro_catalog_views.md "../dg/c_intro_catalog_views.md").
