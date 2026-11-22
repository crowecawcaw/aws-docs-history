

# Configuring Twenty CRM connections

Twenty CRM connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Twenty CRM connection:

1. In Twenty CRM, create an API key under **Settings**, **Developers**, **API**, and then choose **Create key**. Copy the key immediately, because Twenty CRM shows it only once. For more information, see the Twenty CRM API documentation on the Twenty CRM website.

1. In Secrets Manager, create a secret containing the key `api_token` set to your Twenty CRM API key.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Twenty CRM as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.