

# Configuring Copper connections

Copper connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Copper connection:

1. In Copper, open Settings → Integrations → API Keys and generate an API key (tied to a user email). Store the key and that email in Secrets Manager. The connector sends them as the `X-PW-AccessToken` and `X-PW-UserEmail` headers.

1. In Secrets Manager, create a secret containing the keys `apiKey` and `email` set to your Copper credentials.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Copper as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.