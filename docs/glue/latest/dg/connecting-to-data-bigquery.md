#

Connecting to Google BigQuery in AWS Glue Studio

###### Note

You can use AWS Glue for Spark to read from and write to tables in Google BigQuery in AWS Glue
4.0 and later versions. To configure Google BigQuery with AWS Glue jobs programmatically, see

[BigQuery connections](aws-glue-programming-etl-connect-bigquery-home.md "aws-glue-programming-etl-connect-bigquery-home.md").

AWS Glue Studio provides a visual interface to
connect to BigQuery, author data integration jobs, and run them on the AWS Glue Studio serverless Spark runtime.

When creating a connection to Google BigQuery in AWS Glue Studio, a unified connection is created. For more information,
see [Considerations](using-connectors-unified-connections.md#using-connectors-unified-connections-considerations "using-connectors-unified-connections.md#using-connectors-unified-connections-considerations").

Instead of creating a secret with the credentials in a specific format, `{"credentials": "base64 encoded JSON"}`,
now with unified connection to Google BigQuery, you can create a secret which directly includes the JSON from Goolge BigQuery:
`{"type": "service-account", ...}`.

###### Topics

- [Creating a BigQuery connection](creating-bigquery-connection.md "creating-bigquery-connection.md")
- [Creating a BigQuery source node](creating-bigquery-source-node.md "creating-bigquery-source-node.md")
- [Creating a BigQuery target node](creating-bigquery-target-node.md "creating-bigquery-target-node.md")
- [Advanced options](#creating-bigquery-connection-advanced-options "#creating-bigquery-connection-advanced-options")

## Advanced options

You can provide advanced options when creating a BigQuery node. These options are the same as those
available when programming AWS Glue for Spark scripts.

See
[BigQuery connection option reference](aws-glue-programming-etl-connect-bigquery-home.md "aws-glue-programming-etl-connect-bigquery-home.md") in the AWS Glue developer guide.
