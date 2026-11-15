

# Configuring Ghost connections
<a name="ghost-configuring-connections"></a>

Ghost connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Ghost connection:

1. In Ghost Admin, create a Custom Integration (Settings → Integrations) and copy its Content API Key. Store the key in Secrets Manager. The connector sends it as the `key` query parameter. Set the connection URL to your Ghost site's base URL.

1. In Secrets Manager, create a secret containing the key `key` set to your Ghost credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Ghost as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.