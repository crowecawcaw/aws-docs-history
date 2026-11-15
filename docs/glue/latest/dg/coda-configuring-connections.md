

# Configuring Coda connections
<a name="coda-configuring-connections"></a>

Coda connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Coda connection:

1. Generate a Coda API token in your Coda account settings. For more information, see the [Coda API documentation](https://coda.io/developers/apis/v1) on the Coda website.

1. In Secrets Manager, create a secret containing the key `api_key` set to your Coda API token. Store only the token value. The connector adds the `Bearer` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Coda as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.