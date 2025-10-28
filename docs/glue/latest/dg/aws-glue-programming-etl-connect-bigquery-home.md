# BigQuery connections

You can use AWS Glue for Spark to read from and write to tables in Google BigQuery in AWS Glue 4.0 and later
versions. You can read from BigQuery with a Google SQL query. You connect to BigQuery using credentials stored
in AWS Secrets Manager through a AWS Glue connection.

For more information about Google BigQuery, see the [Google Cloud BigQuery website](https://cloud.google.com/bigquery "https://cloud.google.com/bigquery").

## Configuring BigQuery connections

To connect to Google BigQuery from AWS Glue, you will need to create and store your Google Cloud Platform credentials
in a AWS Secrets Manager secret, then associate that secret with a Google BigQuery AWS Glue connection.

###### To configure a connection to BigQuery:

1. In Google Cloud Platform, create and identify relevant resources:
   - Create or identify a GCP project containing BigQuery tables you would like to connect to.
   - Enable the BigQuery API. For more information, see [Use the BigQuery Storage Read API to read table data](https://cloud.google.com/bigquery/docs/reference/storage/#enabling_the_api "https://cloud.google.com/bigquery/docs/reference/storage/#enabling_the_api") .

2. In Google Cloud Platform, create and export service account credentials:

You can use the BigQuery credentials wizard to expedite this step: [Create credentials](https://console.cloud.google.com/apis/credentials/wizard?api=bigquery.googleapis.com "https://console.cloud.google.com/apis/credentials/wizard?api=bigquery.googleapis.com").

To create a service account in GCP, follow the tutorial available in [Create service accounts](https://cloud.google.com/iam/docs/service-accounts-create "https://cloud.google.com/iam/docs/service-accounts-create").

    * When selecting **project**, select the project containing your BigQuery table.
    * When selecting GCP IAM roles for your service account, add or create a role that would
     grant appropriate permissions to run BigQuery jobs to read, write or create BigQuery
     tables.

To create credentials for your service account, follow the tutorial available in [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating "https://cloud.google.com/iam/docs/keys-create-delete#creating").

    * When selecting key type, select **JSON**.

You should now have downloaded a JSON file with credentials for your service account. It should look similar to the following:

```
{
  "type": "service_account",
  "project_id": "*****",
  "private_key_id": "*****",
  "private_key": "*****",
  "client_email": "*****",
  "client_id": "*****",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "*****",
  "universe_domain": "googleapis.com"
}
```

3. Upload your credentials JSON file to an appropriately secure Amazon S3 location. Retain the path to the file, `s3secretpath` for future steps.
4. In AWS Secrets Manager, create a secret using your Google Cloud Platform credentials.
   To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.

When creating Key/value pairs, specify keys and values as followings:

    * For `token_uri`, `client_x509_cert_url`, `private_key_id`, `project_id`, `universe_domain`, `auth_provider_x509_cert_url`, `auth_uri`, `client_email`, `private_key`, `type`, `client_id` keys, specify the corresponding values in the downloaded JSON file.
    * For `spark.hadoop.google.cloud.auth.service.account.json.keyfile` key, specify the `s3secretpath`.

5. In the AWS Glue Data Catalog, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for the next step.
   - When selecting a **Connection type**, select Google BigQuery.
   - When selecting an **AWS Secret**, provide `secretName`.

6. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
7. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

## Reading from BigQuery tables

**Prerequisites:**

- A BigQuery table you would like to read from. You will need the BigQuery table and dataset names,
  in the form `[dataset].[table]`. Let's call this `tableName`.
- The billing project for the BigQuery table. You will need the name of the project,
  `parentProject`. If there is no billing parent project, use the project containing the table.
- BigQuery auth information. Complete the steps _To manage your connection
  credentials with AWS Glue_ to configure your auth information. You will need the name of the
  AWS Glue connection, `connectionName`.

For example:

```
bigquery_read = glueContext.create_dynamic_frame.from_options(
    connection_type="bigquery",
    connection_options={
        "connectionName": "`connectionName`",
        "parentProject": "`parentProject`",
        "sourceType": "table",
        "table": "`tableName`",
    }

```

You can also provide a query, to filter the results returned to your DynamicFrame. You will need to
configure `query`, `sourceType`, `viewsEnabled` and
`materializationDataset`.

For example:

**Additional prerequisites:**

You will need to create or identify a BigQuery dataset, `materializationDataset`, where BigQuery can write materialized views for your queries.

You will need to grant appropriate GCP IAM permissions to your service account to create tables in `materializationDataset`.

```
glueContext.create_dynamic_frame.from_options(
            connection_type="bigquery",
            connection_options={
                "connectionName": "`connectionName`",
                "materializationDataset": `materializationDataset`,
                "parentProject": "`parentProject`",
                "viewsEnabled": "true",
                "sourceType": "query",
                "query": "select * from bqtest.test"
            }
        )
```

## Writing to BigQuery tables

This example writes directly to the BigQuery service. BigQuery also supports the "indirect" writing
method. For more information about configuring indirect writes, see [Using indirect write with Google BigQuery](#aws-glue-programming-etl-connect-bigquery-indirect-write "#aws-glue-programming-etl-connect-bigquery-indirect-write").

**Prerequisites:**

- A BigQuery table you would like to write to. You will need the BigQuery table and dataset names,
  in the form `[dataset].[table]`. You can also provide a new table name that will
  automatically be created. Let's call this `tableName`.
- The billing project for the BigQuery table. You will need the name of the project,
  `parentProject`. If there is no billing parent project, use the project containing the table.
- BigQuery auth information. Complete the steps _To manage your connection
  credentials with AWS Glue_ to configure your auth information. You will need the name of the
  AWS Glue connection, `connectionName`.

For example:

```
bigquery_write = glueContext.write_dynamic_frame.from_options(
    frame=`frameToWrite`,
    connection_type="bigquery",
    connection_options={
        "connectionName": "`connectionName`",
        "parentProject": "`parentProject`",
        "writeMethod": "direct",
        "table": "`tableName`",
    }
)

```

## BigQuery connection option reference

- `project` — Default: Google Cloud service account default. Used for Read/Write. The name of a
  Google Cloud project associated with your table.
- `table` — (Required) Used for Read/Write. The name of your BigQuery table in the format
  `[[project:]dataset.]`.
- `dataset` — Required when not defined through the `table` option. Used for Read/Write. The
  name of the dataset containing your BigQuery table.
- `parentProject` — Default: Google Cloud service account default. Used for Read/Write. The name
  of a Google Cloud project associated with `project` used for billing.
- `sourceType` — Used for Read. Required when reading. Valid Values: `table`, `query`
  Informs AWS Glue of whether you will read by table or by query.
- `materializationDataset` — Used for Read. Valid Values: strings. The name of a BigQuery dataset
  used to store materializations for views.
- `viewsEnabled` — Used for Read. Default: false. Valid Values: true, false. Configures whether
  BigQuery will use views.
- `query` — Used for Read. Used when `viewsEnabled` is true. A GoogleSQL DQL query.
- `temporaryGcsBucket` — Used for Write. Required when `writeMethod` is set to default (`indirect`).
  Name of a Google Cloud Storage bucket used to store an intermediate form of your data while writing to BigQuery.
- `writeMethod` — Default: `indirect`. Valid Values: `direct`, `indirect`.
  Used for Write. Specifies the method used to write your data.
  - If set to `direct`, your connector will write using the BigQuery Storage Write API.
  - If set to `indirect`, you connector will write to Google Cloud Storage, then
    transfer it to BigQuery using a load operation. Your Google Cloud service account will need appropriate GCS permissions.

## Using indirect write with Google BigQuery

This example uses indirect write, which writes data to Google Cloud Storage and copies it to Google BigQuery.

**Prerequisites:**

You will need a temporary Google Cloud Storage bucket, `temporaryBucket`.

The GCP IAM role for AWS Glue's GCP service account will need appropriate GCS permissions to access
`temporaryBucket`.

**Additional Configuration:**

###### To configure indirect write with BigQuery:

1. Assess [Configuring BigQuery connections](#aws-glue-programming-etl-connect-bigquery-configure "#aws-glue-programming-etl-connect-bigquery-configure") and locate or redownload your
   GCP credentials JSON file. Identify `secretName`, the AWS Secrets Manager secret for the
   Google BigQuery AWS Glue connection used in your job.
2. Upload your credentials JSON file to an appropriately secure Amazon S3 location. Retain the path to the
   file, `s3secretpath` for future steps.
3. Edit `secretName`, adding the `spark.hadoop.google.cloud.auth.service.account.json.keyfile` key.
   Set the value to `s3secretpath`.
4. Grant your AWS Glue job Amazon S3 IAM permissions to access `s3secretpath`.

You can now provide your temporary GCS bucket location to your write method. You do not need to provide
`writeMethod`, as `indirect` is historically the default.

```
bigquery_write = glueContext.write_dynamic_frame.from_options(
    frame=`frameToWrite`,
    connection_type="bigquery",
    connection_options={
        "connectionName": "`connectionName`",
        "parentProject": "`parentProject`",
        "temporaryGcsBucket": "`temporaryBucket`",
        "table": "`tableName`",
    }
)

```
