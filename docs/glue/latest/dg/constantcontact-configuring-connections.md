

# Configuring Constant Contact connections
<a name="constantcontact-configuring-connections"></a>

To connect to Constant Contact, register an Open Authorization (OAuth) 2.0 application with Constant Contact, enter its client ID in AWS Glue Studio, store its client secret in Secrets Manager, and authorize the connection through the Constant Contact consent screen. With AWS Glue, you don't need to manually obtain or refresh the access token.

To configure a Constant Contact connection:

1. Register an OAuth application with Constant Contact to obtain a client ID and client secret, and add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL (see the Constant Contact API documentation).

1. In Secrets Manager, create a secret with the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`, and set its value to your OAuth application's client secret. Enter the OAuth client ID in the **Client ID** field in AWS Glue Studio when you create the connection.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Constant Contact as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.