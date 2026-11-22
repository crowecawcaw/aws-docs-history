

# Configuring ClickUp connections

ClickUp connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a ClickUp connection:

1. In ClickUp, generate a personal API token under **Settings**, **Apps**. Personal tokens begin with `pk_`. For more information, see [Authentication](https://developer.clickup.com/docs/authentication) on the ClickUp developer website.

1. In Secrets Manager, create a secret with the key `api_token` set to the token value. Don't add a `Bearer` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose ClickUp as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.