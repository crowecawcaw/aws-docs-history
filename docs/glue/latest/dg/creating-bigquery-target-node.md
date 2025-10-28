# Creating a BigQuery target node

## Prerequisites needed

- A BigQuery type AWS Glue Data Catalog connection
- An AWS Secrets Manager secret for your Google BigQuery credentials, used by the connection.
- Appropriate permissions on your job to read the secret used by the connection.
- The name and dataset of the table and corresponding Google Cloud project you would like to write to.

## Adding a BigQuery data target

###### To add a **Data target – BigQuery** node:

1. Choose the connection for your BigQuery data target. Since you have created it, it should be
   available in the dropdown. If you need to create a
   connection, choose **Create BigQuery connection**. For more information, see
   [Overview of using connectors and connections](../ug/connectors-chapter.md#using-connectors-overview "../ug/connectors-chapter.md#using-connectors-overview") .

Once you have chosen a connection, you can view the connection properties by clicking
**View properties**. 2. Identify what BigQuery table you would like to write to, then choose a **Write method**.

    * Direct – writes to BigQuery directly using the BigQuery Storage Write API.
    * Indirect – writes to Google Cloud Storage, then copies to BigQuery.

If you would like to write indirectly, provide a destination GCS location with **Temporary GCS bucket**.
You will need to provide additional configuration in your AWS Glue connection. For more information, see
[Using indirect write with Google BigQuery](aws-glue-programming-etl-connect-bigquery-home.md#aws-glue-programming-etl-connect-bigquery-indirect-write "aws-glue-programming-etl-connect-bigquery-home.md#aws-glue-programming-etl-connect-bigquery-indirect-write"). 3. Describe the data you would like to read

**(Required)** set **Parent Project** to the
project containing your table, or a billing parent project, if relevant.

If you chose a single table, set **Table** to the name of a Google BigQuery
table in the following format: `[dataset].[table]`
