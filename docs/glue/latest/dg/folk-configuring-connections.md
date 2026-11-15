

# Configuring Folk connections
<a name="folk-configuring-connections"></a>

Folk connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Folk connection:

1. Create and manage an API key in Folk workspace settings under the API section. The connector sends it as a Bearer token.

1. In Secrets Manager, create a secret containing the key `api_key` set to your Folk API key. Store only the key value. The connector adds the `Bearer` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Folk as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.