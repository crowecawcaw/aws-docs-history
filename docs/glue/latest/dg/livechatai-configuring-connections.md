

# Configuring LiveChatAI connections
<a name="livechatai-configuring-connections"></a>

LiveChatAI connections authenticate with an API key, which the connector sends as a bearer token. You store the API key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a LiveChatAI connection:

1. Create or copy an API key in your LiveChatAI account.

1. In Secrets Manager, create a secret containing the key `api_key` set to the raw LiveChatAI API key. Don't include the `Bearer` prefix; the connector adds it.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose LiveChatAI as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.