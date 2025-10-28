# Register your connection as a Glue Data

Catalog

After you create your data source, you can use the Athena console to register your
connection as a Glue Data Catalog. Once registered, you can manage your federated data
catalog and enable fine-grained access control using Lake Formation. For more information, see
[Creating a
federated catalog](../../../lake-formation/latest/dg/create-fed-catalog-data-source.md "../../../lake-formation/latest/dg/create-fed-catalog-data-source.md").

You can register the following connectors to integrate with AWS Glue for fine-grained
access control.

- Redshift
- BigQuery
- DynamoDB (Preview)
- Snowflake (Preview)
- MySQL
- PostgreSQL
- AWS CMDB
- Timestream
- Azure Data Lake Storage
- Azure Synapse
- IBM Db2
- IBM Db2 AS/400 (Db2 iSeries)
- DocumentDB
- Google Cloud Storage
- HBase
- OpenSearch
- Oracle
- SAP HANA
- SQL Server
- TPC-DS
- Cloudera Hive
- Cloudwatch
- Cloudwatch Metrics
- Teradata
- Vertica

## Prerequisites

Before you begin, you must complete the following prerequisites.

- Ensure that you have the roles and permissions needed to register locations. For more
  information, see the [Requirements for
  roles](../../../lake-formation/latest/dg/registration-role.md "../../../lake-formation/latest/dg/registration-role.md") in the AWS Lake Formation Developer Guide.
- Ensure that you have the required Lake Formation roles. For more information, see
  [Prerequisites for connecting the Data Catalog to external data
  sources](../../../lake-formation/latest/dg/federated-catalog-data-connection.md "../../../lake-formation/latest/dg/federated-catalog-data-connection.md") in the AWS Lake Formation Developer Guide.
- The role that you register in Glue must have the permissions as listed in
  the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource": [
 `"arn:aws:s3:::amzn-s3-demo-bucket/spill-prefix/*"`,
 `"arn:aws:s3:::amzn-s3-demo-bucket/spill-prefix"`
 ]
 },
 {
 "Sid": "lambdainvoke",
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": "`arn:aws:lambda:us-east-1:111122223333:function:lambda_function_name`"
 },
 {
 "Sid": "gluepolicy",
 "Effect": "Allow",
 "Action": "glue:*",
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/`<connection_name>`",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog"
 ]
 }
 ]
}`

```

- You are responsible to determine and manage the appropriate data access. With fine-grain
  access controls on federated queries, it is recommended that you use the
  [AmazonAthenaFullAccess](../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md") managed policy. If you want to use your
  own policy, you must ensure that the users executing federated queries do
  not have access to the following resources.
  - `lambda:InvokeFunction` on the Lambda connector that is
    specified in Glue connection
  - Spill bucket location access in IAM
  - Access to the Glue connection associated with your federated
    catalog
  - Lake Formation Role in IAM

## Register your connection using console

###### To register your connection as a Glue Data Catalog

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Data sources and
   catalogs**.
3. From the **Data sources** list, choose the data source that
   you created to open the **Data source details** page.
4. Choose **Get started with AWS Lake Formation**.

###### Note

After you choose this option, you must manage your Lambda function on
your own. Athena will not delete your Lambda function. 5. For **Data catalog name** provide a unique name for your
catalog. 6. Choose the **Lake Formation IAM role** that grants
permission to Lake Formation to invoke the Lambda function. Make sure the role has the
permissions as shown in [the example](#register-connection-as-gdc-pre "#register-connection-as-gdc-pre"). 7. In the text box, type **confirm** to delete the
Athena data source, replace it with a Glue data catalog registration.

###### Note

This action will delete your Athena data source and create a new Glue Data
Catalog in its place. After this process is completed, you may need to
update queries that access the data source to refer to the newly created
Glue data catalog instead. 8. Choose **Create catalog and go to Lake Formation**. This opens the Lake Formation
console where you can manage the catalog and grant permissions to users on
catalogs, databases and tables.
