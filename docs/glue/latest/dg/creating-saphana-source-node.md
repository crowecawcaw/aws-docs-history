

# Creating a SAP HANA source node
<a name="creating-saphana-source-node"></a>

## Prerequisites needed
<a name="creating-saphana-source-node-prerequisites"></a>
+ An AWS Glue SAP HANA connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a SAP HANA connection](creating-saphana-connection.md).
+ Appropriate permissions on your job to read the secret used by the connection.
+ A SAP HANA table you would like to read from, {{tableName}}, or query {{targetQuery}}.

  A table can be specified with a SAP HANA table name and schema name, in the form `{{schemaName}}.{{tableName}}`. The schema name and "." separator are not required if the table is in the default schema, "public". Call this {{tableIdentifier}}. Note that the database is provided as a JDBC URL parameter in `connectionName`.

## Adding a SAP HANA data source
<a name="creating-saphana-source-node-add"></a>

**To add a **Data source – SAP HANA** node:**

1.  Choose the connection for your SAP HANA data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create SAP HANA connection**. For more information see the previous section, [Creating a SAP HANA connection](creating-saphana-connection.md). 

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**. 

1.  Choose a **SAP HANA Source** option: 
   +  **Choose a single table** – access all data from a single table. 
   +  **Enter custom query ** – access a dataset from multiple tables based on your custom query. 

1.  If you chose a single table, enter {{tableName}}. 

    If you chose **Enter custom query**, enter a SQL SELECT query. 

1.  In **Custom SAP HANA properties**, enter parameters and values as needed. 