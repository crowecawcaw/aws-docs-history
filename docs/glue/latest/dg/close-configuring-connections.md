

# Configuring Close CRM connections

Close CRM connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Close CRM connection:

1. In Close, open Settings → API Keys and create an API key. Store it in Secrets Manager as the basic-auth username (leave the password blank). The connector authenticates with HTTP basic auth.

1. In Secrets Manager, create a secret containing your Close CRM credential with the `username` and `password` keys.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Close CRM as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.