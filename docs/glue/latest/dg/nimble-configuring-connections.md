

# Configuring Nimble connections
<a name="nimble-configuring-connections"></a>

Nimble connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Nimble connection:

1. Obtain your Nimble API credential (see the Nimble API documentation on the Nimble website).

1. In Secrets Manager, create a secret containing the key `api_key` set to your Nimble credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Nimble as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.