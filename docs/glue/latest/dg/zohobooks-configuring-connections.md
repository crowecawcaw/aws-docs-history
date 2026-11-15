

# Configuring Zoho Books connections
<a name="zohobooks-configuring-connections"></a>

Zoho Books connections use OAuth 2.0 with the authorization code (three-legged) grant. You register a server-based OAuth application with Zoho Books, store its client secret in Secrets Manager, and authorize the connection through the Zoho Books consent screen when you create it in AWS Glue Studio. AWS Glue obtains and refreshes the access token for you.

To configure a Zoho Books connection:

1. Register a server-based application in the Zoho Developer Console to obtain a client ID and client secret, and add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL on that client. Only a server-based client is supported; the self client type is not supported.

1. In Secrets Manager, create a secret containing `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` set to your Zoho Books OAuth application's client secret. Enter the OAuth client ID in the **Client ID** field in AWS Glue Studio when you create the connection.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Zoho Books as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.