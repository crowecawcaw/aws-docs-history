

# Configuring Finch connections

Finch connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Finch connection:

1. In the Finch Dashboard, copy the `client_id` and `client_secret` for your Production application. Connect the employer through Finch Connect, then exchange the authorization code for an access token with `POST https://api.tryfinch.com/auth/token`. Store that access token in Secrets Manager as `accessToken`. Sandbox, Development and Production each use separate credentials on the same `api.tryfinch.com` host.

1. In Secrets Manager, create a secret containing the key `accessToken` set to your Finch credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Finch as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.