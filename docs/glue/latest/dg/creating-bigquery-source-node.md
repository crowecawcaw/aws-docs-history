

# Creating a BigQuery source node
<a name="creating-bigquery-source-node"></a>

## Prerequisites needed
<a name="creating-bigquery-source-node-prerequisites"></a>
+ A BigQuery type AWS Glue Data Catalog connection
+ An AWS Secrets Manager secret for your Google BigQuery credentials, used by the connection.
+ Appropriate permissions on your job to read the secret used by the connection.
+ The name and dataset of the table and corresponding Google Cloud project you would like to read.

## Adding a BigQuery data source
<a name="creating-bigquery-source-node-add"></a>

**To add a **Data source – BigQuery** node:**

1.  Choose the connection for your BigQuery data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create BigQuery connection**. For more information, see [ Overview of using connectors and connections ](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html#using-connectors-overview). 

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**. 

1. Identify what BigQuery data you would like to read, then choose a **BigQuery Source** option
   + Choose a single table – allows you to pull all data from a table.
   + Enter a custom query – allows you to customize which data is retrieved by providing a query.

1.  Describe the data you would like to read

   **(Required) **set **Parent Project** to the project containing your table, or a billing parent project, if relevant.

   If you chose a single table, set **Table** to the name of a Google BigQuery table in the following format: `[dataset].[table]` 

   If you chose a query, provide it to **Query**. In your query, refer to tables with their fully qualified table name, in the format: `[project].[dataset].[tableName]`.

1.  Provide BigQuery properties 

   If you chose a single table, you do not need to provide additional properties.

   If you chose a query, you must provide the following **Custom Google BigQuery properties**:
   + Set `viewsEnabled` to true.
   + Set `materializationDataset` to a dataset. The GCP principal authenticated by the credentials provided through the AWS Glue connection must be able to create tables in this dataset.