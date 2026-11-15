

# Configuring Webex connections
<a name="webex-configuring-connections"></a>

Webex connections authenticate with a Webex access token, which the connector sends as a bearer token. You store the access token in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Webex connection:

1. Obtain a Webex access token with permission to read the data that you want to transfer.

1. In Secrets Manager, create a secret containing the key `api_key` set to the raw Webex access token. Don't include the `Bearer` prefix; the connector adds it.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Webex as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.