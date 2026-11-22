

# Configuring Insightly connections

Insightly connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Insightly connection:

1. Obtain your Insightly API credential (see the Insightly API documentation on the Insightly website).

1. In Secrets Manager, create a secret containing the key `api_key` set to your Insightly credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Insightly as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.