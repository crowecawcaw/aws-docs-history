

# Configuring DevRev connections

DevRev connections authenticate with a DevRev personal access token (PAT), which the connector sends as a bearer token. You store the PAT in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a DevRev connection:

1. Create a DevRev personal access token. In the DevRev app, choose **Settings**, **Account**, **Personal Access Token**, and **New token**. Copy the token before leaving the page.

1. In Secrets Manager, create a secret containing the key `api_key` set to the raw PAT. Don't include the `Bearer` prefix; the connector adds it.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose DevRev as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.