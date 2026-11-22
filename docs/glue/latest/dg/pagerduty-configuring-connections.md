

# Configuring PagerDuty connections

PagerDuty connections authenticate with a PagerDuty REST API key. OAuth access tokens aren't supported. You store the API key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a PagerDuty connection:

1. Create or obtain a PagerDuty REST API key with permission to read the data that you want to transfer.

1. In Secrets Manager, create a secret containing the key `apiKey` set to your raw PagerDuty REST API key. Don't include the `Token token=` prefix; the connector adds it.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose PagerDuty as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.