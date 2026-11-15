

# Configuring Zoho Desk connections
<a name="zohodesk-configuring-connections"></a>

Zoho Desk connections use OAuth 2.0 (authorization code grant). You register a server-based OAuth application in the Zoho Developer Console to obtain a client ID and client secret, store them in Secrets Manager, and authorize the connection through the Zoho consent screen when you create it in AWS Glue Studio. AWS Glue obtains and refreshes the access token for you.

To configure a Zoho Desk connection:

1. Register a server-based application in the Zoho Developer Console to obtain a client ID and client secret, and add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL on that client (see the Zoho API documentation).

1. In Secrets Manager, create a secret containing your Zoho Desk OAuth application's `UserManagedClientApplicationClientId` and `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Zoho Desk as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.