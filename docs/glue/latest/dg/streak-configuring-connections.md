

# Configuring Streak connections

Streak connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Streak connection:

1. Obtain your Streak API credential (see the Streak API documentation on the Streak website).

1. Because Streak uses a single API key, create a secret in Secrets Manager with the key `USERNAME`, and set its value to your Streak API key. Do not add a `PASSWORD` key.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Streak as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.