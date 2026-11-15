

# Configuring Shortcut connections
<a name="shortcut-configuring-connections"></a>

Shortcut connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Shortcut connection:

1. In Shortcut, open Settings → API Tokens and generate a token. Store it in Secrets Manager. The connector sends it as the `Shortcut-Token` header.

1. In Secrets Manager, create a secret containing the key `Shortcut-Token` set to your Shortcut credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Shortcut as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.