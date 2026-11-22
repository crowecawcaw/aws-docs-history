

# Configuring Re:amaze connections

Re:amaze connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Re:amaze connection:

1. In Re:amaze, use an admin login email plus the account's API token (Settings → Developer/API). Store them in Secrets Manager as the HTTP Basic username and password. Set the connection URL with your brand subdomain.

1. In Secrets Manager, create a secret containing your Re:amaze credential with the keys `USERNAME` and `PASSWORD`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Re:amaze as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.