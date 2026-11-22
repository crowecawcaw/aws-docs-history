

# Configuring Hex connections

Hex connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Hex connection:

1. Create a Personal access token under User settings → API keys → New Token (with a description and expiration). An Admin must first enable API access from the Integrations tab in Workspace settings. The connector sends the token as a Bearer token.

1. In Secrets Manager, create a secret containing the key `accessToken` set to your Hex credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Hex as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.