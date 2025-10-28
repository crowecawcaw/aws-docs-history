# Querying Worldwide Event Attendance (Test Product)

data on Amazon Redshift (SQL)

The following procedure shows how to set up and query the datashare using the SQL
commands.

###### To query Worldwide Event Attendance (Test Product) data on Amazon Redshift (SQL)

1. To find the datashare, run the following command.

`SHOW DATASHARES [ LIKE 'namepattern' ]`

This command lists all datashares, including the one from Worldwide Event
Attendance (Test Product), in addition to the provider's `account_id`
and `namespace`. For more information, see [Show Datashares](../../../redshift/latest/dg/r_SHOW_DATASHARES.md "../../../redshift/latest/dg/r_SHOW_DATASHARES.md") in the _Amazon Redshift Database
Developer Guide_. 2. Run the following command to create a database from the datashare.

`CREATE DATABASE database_name`

`FROM DATASHARE datashare_name OF ACCOUNT account_id NAMESPACE
 namespace_guid`

For more information, see [Create Database](../../../redshift/latest/dg/r_CREATE_DATABASE.md "../../../redshift/latest/dg/r_CREATE_DATABASE.md") in the _Amazon Redshift Database
Developer Guide_. 3. Run the following SQL query.

`select * from database.schema.table`
