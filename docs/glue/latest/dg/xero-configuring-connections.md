

# Configuring Xero connections
<a name="xero-configuring-connections"></a>

Xero connections use OAuth 2.0. You register an OAuth application with Xero, store its client credentials in Secrets Manager, and authorize the connection through the Xero consent screen when you create it in AWS Glue Studio. AWS Glue obtains and refreshes the access token for you.

To configure a Xero connection:

1. Register an OAuth application with Xero to obtain a client ID and client secret, and add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL (see the Xero API documentation).

1. In Secrets Manager, create a secret containing `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` set to your Xero OAuth application's client secret. Enter the OAuth client ID in the **Client ID** field in AWS Glue Studio when you create the connection.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Xero as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.