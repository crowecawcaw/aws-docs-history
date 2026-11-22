

# Configuring Teamwork connections

Teamwork connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Teamwork connection:

1. In Teamwork, get the account's API token (your profile → Edit → API and Mobile / API keys). Store it in Secrets Manager as the HTTP Basic username. No password is required.

1. In Secrets Manager, create a secret with the key `USERNAME` set to your Teamwork API token. The `PASSWORD` key is optional.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Teamwork as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.