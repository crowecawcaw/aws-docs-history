

# Configuring Kommo connections
<a name="kommo-configuring-connections"></a>

Kommo connections support two authentication types: a long-lived API access token, or OAuth 2.0 (authorization code). For the token, store it in Secrets Manager; for OAuth 2.0, see [Setting up the authorization code flow for Kommo](kommo-setup-authorization-code-flow.md).

To configure a Kommo connection:

1. Obtain your Kommo API credential (see the Kommo API documentation on the Kommo website).

1. In Secrets Manager, create a secret containing the key `access_token` set to your Kommo credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Kommo as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.