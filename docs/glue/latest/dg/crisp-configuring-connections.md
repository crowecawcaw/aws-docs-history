

# Configuring Crisp connections

Crisp connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Crisp connection:

1. In the Crisp Marketplace, create a plugin and open its Tokens tab to generate a plugin token—an `identifier` and `key` pair. Store them in Secrets Manager as the connection's Basic-auth username (`identifier`) and password (`key`). The plugin must be granted the scopes for the data it reads (conversations and people, read access) and connected to the target website.

1. In Secrets Manager, create a secret containing your Crisp credential with the keys `USERNAME` and `PASSWORD`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Crisp as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.