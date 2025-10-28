Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create a database

After you verify that your data warehouse is up and running, you can create a database.
This database is where you actually create tables, load data, and run queries.
A data warehouse can host multiple databases. For example, you can have a database for sales data named
`SALESDB` and a database for orders data named `ORDERSDB` in the same data warehouse.

To create a database named `SALESDB`, run the
following command in your SQL client tool.

```
CREATE DATABASE salesdb;
```

###### Note

After running the command, make sure to refresh your SQL client tool list of objects in your data warehouse to see the new `salesdb`.

For this exercise, accept the defaults. For information about more command options, see
[CREATE DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") in the
_Amazon Redshift Database Developer Guide_. To delete a database and its contents, see
[DROP DATABASE](../dg/r_DROP_DATABASE.md "../dg/r_DROP_DATABASE.md") in the
_Amazon Redshift Database Developer Guide_.

After you have created the SALESDB database, you can connect to the new database from
your SQL client. Use the same connection parameters as you used for your current
connection, but change the database name to `SALESDB`.
