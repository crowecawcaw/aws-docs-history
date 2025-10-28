# Creating a SAP HANA target node

## Prerequisites needed

- A AWS Glue SAP HANA connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a SAP HANA connection](creating-saphana-connection.md "creating-saphana-connection.md").
- Appropriate permissions on your job to read the secret used by the connection.
- A SAP HANA table you would like to write to, `tableName`.

A table can be specified with a SAP HANA table name and schema name, in the form
``schemaName`.`tableName``. The schema
name and "." separator are not required if the table is in the default schema, "public". Call this
`tableIdentifier`. Note that the database is provided as a JDBC URL parameter in `connectionName`.

## Adding a SAP HANA data target

###### To add a **Data target – SAP HANA** node:

1. Choose the connection for your SAP HANA data source. Since you have created it, it should be
   available in the dropdown. If you need to create a
   connection, choose **Create SAP HANA connection**. For more information see
   the previous section, [Creating a SAP HANA connection](creating-saphana-connection.md "creating-saphana-connection.md").

Once you have chosen a connection, you can view the connection properties by clicking
**View properties**. 2. Configure **Table name** by providing
`tableName`. 3. In **Custom Teradata properties**, enter parameters and values as needed.
