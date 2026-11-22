

# Configuring Airship connections

Airship connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Airship connection:

1. Obtain your Airship API credential (see the Airship API documentation on the Airship website).

1. In Secrets Manager, create a secret containing the key `access_token` set to your Airship credential. The connector sets the `Accept` version header automatically, so don't include the `AcceptVersion` parameter in the secret.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Airship as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.