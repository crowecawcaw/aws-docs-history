

# Querying Worldwide Event Attendance (Test Product) data on Amazon Redshift (SQL)
<a name="query-RS-data-SQL"></a>

The following procedure shows how to set up and query the datashare using the SQL commands.

**To query Worldwide Event Attendance (Test Product) data on Amazon Redshift (SQL)**

1. To find the datashare, run the following command.

    `SHOW DATASHARES [ LIKE 'namepattern' ]`

    This command lists all datashares, including the one from Worldwide Event Attendance (Test Product), in addition to the provider's `account_id` and `namespace`. For more information, see [Show Datashares](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_DATASHARES.html) in the *Amazon Redshift Database Developer Guide*.

1. Run the following command to create a database from the datashare.

    `CREATE DATABASE database_name`

    `FROM DATASHARE datashare_name OF ACCOUNT account_id NAMESPACE namespace_guid`

   For more information, see [Create Database](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) in the *Amazon Redshift Database Developer Guide*.

1. Run the following SQL query. 

   `select * from database.schema.table`