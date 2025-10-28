# Creating a Amazon Redshift source node

## Permissions needed

AWS Glue Studio jobs using Amazon Redshift data sources require additional permissions. For more information on how to
add permissions to ETL jobs, see
[Review IAM permissions needed for ETL jobs](../ug/setting-up.md#getting-started-min-privs-job "../ug/setting-up.md#getting-started-min-privs-job").

The following permissions are needed in order to use an Amazon Redshift connection.

- redshift-data:ListSchemas
- redshift-data:ListTables
- redshift-data:DescribeTable
- redshift-data:ExecuteStatement
- redshift-data:DescribeStatement
- redshift-data:GetStatementResult

## Adding an Amazon Redshift data source

###### To add a **Data Source – Amazon Redshift** node:

1. Choose the Amazon Redshift access type:
   - Direct data connection (recommended) – choose this option if you want to access your Amazon Redshift
     data directly. This is the recommended option and also the default.
   - Data Catalog tables – choose this option if you have Data Catalog tables that you want to use.

2. If you choose Direct data connection, choose the connection for your Amazon Redshift data source.
   This assumes that the connection already exists and you can select from existing connections. If you need to create a
   connection, choose **Create Redshift connection**. For more information, see
   [Overview of using connectors and connections](../ug/connectors-chapter.md#using-connectors-overview "../ug/connectors-chapter.md#using-connectors-overview") .

Once you have chosen a connection, you can view the connection properties by clicking **View properties**.
Information about the connection are visible, including URL, security groups, subnet, availability zone, description, and
created (UTC) and last updated (UTC) timestamps. 3. Choose a Amazon Redshift source option:

    * **Choose a single table** – this is the table that contains the data you want to access from a
     single Amazon Redshift table.
    * **Enter custom query**  – allows you to access a dataset from multiple Amazon Redshift
     tables based on your custom query.

4. If you chose a single table, choose the Amazon Redshift schema. The list of available schema to choose from is
   determined by the selected table.

Or, choose **Enter custom query**. Choose this option to access a custom dataset from multiple
Amazon Redshift tables. When you choose this option, enter the Amazon Redshift query.

When connecting to an Amazon Redshift serverless environment, add the following permission to the custom query:

```

            GRANT SELECT ON ALL TABLES IN <schema> TO PUBLIC

```

You can choose **Infer schema** to read the schema based on the query that you entered. You can also
choose **Open Redshift query editor** to enter a Amazon Redshift query. For more information,
see [Querying a database using the query editor](../../../redshift/latest/mgmt/query-editor.md "../../../redshift/latest/mgmt/query-editor.md") . 5. In **Performance and security**, choose the Amazon S3 staging directory and IAM role.

    * **Amazon S3 staging directory** – choose the Amazon S3 location for temporarily staging data.
    * **IAM role** – choose the IAM role that can write to the Amazon S3 location you selected.

6. In **Custom Redshift paramters - optional**, enter the parameter and value.
