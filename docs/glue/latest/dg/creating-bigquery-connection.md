# Creating a BigQuery connection

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

3. In AWS Secrets Manager, create a secret using your downloaded credentials file. You can choose the **Plaintext** tab and paste the JSON formatted file content.
   To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
4. In the AWS Glue Data Catalog, create a connection by following the steps in [https://docs.aws.amazon.com/glue/latest/dg/console-connections.html](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for the next step.
   - When selecting a **Connection type**, select Google BigQuery.
   - When selecting an **AWS Secret**, provide `secretName`.

5. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
6. In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.
