Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing zero-ETL integrations

You can view your zero-ETL integrations from the Amazon Redshift console. Here you can view its configuration
information and current status, and open screens to query and share data.

Amazon Redshift console

###### To view the details of a zero-ETL integration

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. From the left navigation pane, choose either the
   **Serverless** or **Provisioned clusters**
   dashboard. Then, choose **Zero-ETL integrations**.
3. Select the zero-ETL integration that you want to view. For each integration, the
   following information is provided:
   - **Integration ID** is the identifier returned when the
     integration is created.
   - **Status** can be one of the following:
     - `Active` – The zero-ETL integration is sending transactional
       data to the target Amazon Redshift data warehouse.
     - `Syncing` – The zero-ETL integration has encountered a
       recoverable error and is reseeding data. Affected tables aren’t available
       for querying in Amazon Redshift until they finish resyncing.
     - `Failed` – The zero-ETL integration encountered an
       unrecoverable event or error that can't be fixed. You must delete and
       recreate the zero-ETL integration.
     - `Creating` – The zero-ETL integration is being created.
     - `Deleting` – The zero-ETL integration is being deleted.
     - `Needs attention` – The zero-ETL integration encountered an
       event or error that requires manual intervention to resolve it. To fix the
       issue, follow the steps in the error message.

   - **Source type** is the type of source data replicating to
     the target. Types can specify other database managers, such as Aurora MySQL-Compatible Edition,
     Amazon Aurora PostgreSQL, RDS for MySQL, and from applications (`GlueSAAS`).
   - **Source ARN** is the ARN of the source data. For most
     sources this is the ARN of the source database or table. For zero-ETL integration with
     applications sources, this is the ARN of the AWS Glue connection object.
   - **Target** is the namespace of the Amazon Redshift data warehouse
     receiving source data.
   - **Database** can be one of the following:
     - `No database` – There is no destination database for
       the integration.
     - `Creating` – Amazon Redshift is creating the destination
       database for the integration.
     - `Active` – Data is being replicated from the
       integration source to Amazon Redshift.
     - `Error` – There is an error with the
       integration.
     - `Recovering` – The integration is recovering after
       the data warehouse restarted.
     - `Resyncing` – Amazon Redshift is resynchronizing the tables
       in the integration.

   - **Target type** is the type of Amazon Redshift data
     warehouse.
   - **Creation date** is the date and time (UTC) when the
     integration was created.

###### Note

To view integration details for a data warehouse, choose the details page for
your provisioned cluster or serverless namespace and then choose the
**Zero-ETL integrations** tab.

From the **Zero-ETL integrations** list, you can choose **Query
data** to jump to Amazon Redshift query editor v2. The Amazon Redshift target database has the [enable_case_sensitive_identifier](../dg/r_enable_case_sensitive_identifier.md "../dg/r_enable_case_sensitive_identifier.md") parameter enabled. When you write SQL, you
might need to surround schemas, tables, and column names with double quotes
("<name>"). For more information about querying data in your Amazon Redshift data
warehouse, see [Querying a database using the query editor v2](query-editor-v2.md "query-editor-v2.md").

From the **Zero-ETL integrations** list, you can choose **Share
data** to create a datashare. To create a datashare for the Amazon Redshift database,
follow the instructions on the **Create datashare** page. Before you
can share data in your Amazon Redshift database, you must first create a destination database.
For more information about data sharing, see [Data sharing concepts for
Amazon Redshift](../dg/concepts.md "../dg/concepts.md").

To refresh your integration, you can use the [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") command. Doing
so replicates all of the data from your integration source into your destination
database. The following example refreshes all synced and failed tables within your
zero-ETL integration.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH ALL tables;
```

AWS CLI
To describe an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the AWS CLI, use the
`describe-integrations` command with the following options:

- `integration-arn` – Specify the ARN of the DynamoDB integration
  to describe.
- `integration-name` – Specify an optional filter that
  specifies one or more resources to return.

The follow example describes an integration by providing the integration
ARN.

```
`aws redshift describe-integrations`
         `{
 "Integrations": [
 {
 "Status": "failed",
 "IntegrationArn": "arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "Errors": [
 {
 "ErrorCode": "INVALID_TABLE_PERMISSIONS",
 "ErrorMessage": "Redshift does not have sufficient access on the table key. Refer to the Amazon DynamoDB Developer Guide."
 }
 ],
 "Tags": [],
 "CreateTime": "2023-11-09T00:32:46.444Z",
 "KMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
 "TargetArn": "arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "IntegrationName": "ddb-to-provisioned-02",
 "SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/mytable"
 }
 ]
}`

```

You can also filter the results of `describe-integrations` by the
`integration-arn`, `source-arn`, `source-types`, or
`status`. For more information, see [describe-integrations](../../../cli/latest/reference/redshift/describe-integrations.md "../../../cli/latest/reference/redshift/describe-integrations.md") in the _Amazon Redshift CLI Guide_.
