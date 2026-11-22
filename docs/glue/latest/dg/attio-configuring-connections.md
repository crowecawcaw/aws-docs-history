

# Configuring Attio connections

Attio connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Attio connection:

1. In Attio, open Workspace settings → Developers and create an access token. Store it in Secrets Manager. The connector sends it as `Authorization: Bearer <value>`.

1. In Secrets Manager, create a secret containing the key `api_key` set to your Attio credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Attio as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.