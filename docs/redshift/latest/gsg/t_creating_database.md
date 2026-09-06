

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Create a database
<a name="t_creating_database"></a>

After you verify that your data warehouse is up and running, you can create a database. This database is where you actually create tables, load data, and run queries. A data warehouse can host multiple databases. For example, you can have a database for sales data named `SALESDB` and a database for orders data named `ORDERSDB` in the same data warehouse.

To create a database named **SALESDB**, run the following command in your SQL client tool.

```
CREATE DATABASE salesdb;
```

**Note**  
After running the command, make sure to refresh your SQL client tool list of objects in your data warehouse to see the new `salesdb`.

For this exercise, accept the defaults. For information about more command options, see [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE) in the *Amazon Redshift Database Developer Guide*. To delete a database and its contents, see [DROP DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_DATABASE) in the *Amazon Redshift Database Developer Guide*. 

After you have created the SALESDB database, you can connect to the new database from your SQL client. Use the same connection parameters as you used for your current connection, but change the database name to `SALESDB`.