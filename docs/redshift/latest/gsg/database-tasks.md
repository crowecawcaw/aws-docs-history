Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Run commands to define and use a database in your data warehouse

Both Redshift Serverless data warehouses and Amazon Redshift provisoned data warehouses contain databases.
After you have launched your data warehouse, you can manage most database actions using SQL commands.
With few exceptions, the functionality and syntax of SQL is the same for all Amazon Redshift databases.
For details of SQL commands available with Amazon Redshift, see
[SQL commands](../dg/c_SQL_commands.md "../dg/c_SQL_commands.md") in the
_Amazon Redshift Database Developer Guide_.

When you create your data warehouse, in most scenarios, Amazon Redshift also creates the default `dev` database.
After you connect to the `dev` database, you can create another database.

The following sections walk through common database tasks when working with Amazon Redshift databases.
The tasks begin with creating a database and if you continue to the last task you can delete all the resources you create by dropping the database.

The examples in this section assume the following:

- You have created an Amazon Redshift data warehouse.
- You have established a connection to the data warehouse from your SQL client tool, such as the Amazon Redshift query editor v2.
  For more information about query editor v2, see
  [Querying a database using the Amazon Redshift query editor v2](../mgmt/query-editor-v2.md "../mgmt/query-editor-v2.md") in the
  _Amazon Redshift Management Guide_.

###### Topics

- [Connecting to Amazon Redshift data warehouses](#connection "#connection")
- [Create a database](t_creating_database.md "t_creating_database.md")
- [Create a user](t_adding_redshift_user_cmd.md "t_adding_redshift_user_cmd.md")
- [Create a schema](t_creating_schema.md "t_creating_schema.md")
- [Create a table](t_creating_table.md "t_creating_table.md")
- [Load data](cm-dev-t-load-sample-data.md "cm-dev-t-load-sample-data.md")
- [Query the system tables and views](t_querying_redshift_system_tables.md "t_querying_redshift_system_tables.md")
- [Cancel a query](cancel_query.md "cancel_query.md")

## Connecting to Amazon Redshift data warehouses

To connect to Amazon Redshift clusters, from the Amazon Redshift console **Clusters** page, expand **Connect to Amazon Redshift clusters** and do one of the following:

- Choose **Query data** to use the query editor v2 to run queries on databases hosted by your Amazon Redshift cluster. After
  creating your cluster, you can immediately run queries by using the query editor v2.

For more information, see [Querying a database using the Amazon Redshift query editor v2](../mgmt/query-editor-v2.md "../mgmt/query-editor-v2.md") in the
_Amazon Redshift Management Guide_.

- In **Work with your client tools**, choose your cluster and connect to Amazon Redshift from your client tools using JDBC or ODBC
  drivers by copying the JDBC or ODBC driver URL.
  Use this URL from your client computer or instance. Code your applications to use JDBC or ODBC data
  access API operations, or use SQL client tools that support either JDBC or ODBC.

For more information on how to find your cluster connection string,
see [Finding your cluster connection string](../mgmt/configuring-connections.md#connecting-drivers.html "../mgmt/configuring-connections.md#connecting-drivers.html").

- If your SQL client tool requires a driver, you can **Choose your JDBC or ODBC driver** to download an operating
  system-specific driver to connect to Amazon Redshift from your client tools.

For more information on how to install the appropriate driver for your SQL client,
see [Configuring a JDBC driver version 2.2
connection](../mgmt/jdbc20-install.md "../mgmt/jdbc20-install.md").

For more information on how to configure an ODBC connection, see [Configuring an ODBC connection](../mgmt/configure-odbc-connection.md "../mgmt/configure-odbc-connection.md").

To connect to Redshift Serverless data warehouse, from the Amazon Redshift console **Serverless dashboard** page, do one of the following:

- Use the Amazon Redshift query editor v2 to run queries on databases hosted by your Redshift Serverless data warehouse.
  After creating your data warehouse, you can immediately run queries by using the query editor v2.

For more information, see [Querying a database using the Amazon Redshift query editor v2](../mgmt/query-editor-v2.md "../mgmt/query-editor-v2.md").

- Connect to Amazon Redshift from your client tools using JDBC or ODBC
  drivers by copying the JDBC or ODBC driver URL.

To work with data in your data warehouse, you need JDBC or ODBC drivers for connectivity
from your client computer or instance. Code your applications to use JDBC or ODBC data
access API operations, or use SQL client tools that support either JDBC or ODBC.

For more information on how to find your connection string, see
[Connecting to Redshift Serverless](../mgmt/serverless-connecting.md "../mgmt/serverless-connecting.md") in the
_Amazon Redshift Management Guide_.
