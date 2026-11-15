

# Configuring Trello connections
<a name="trello-configuring-connections"></a>

Trello connections authenticate with an API key and an API token. You store both values in one Secrets Manager secret and reference that secret when you create the connection in AWS Glue Studio.

To configure a Trello connection:

1. Create a Trello API key for a Power-Up in the Trello Power-Up admin portal, and then use the **Token** link next to the key to generate an API token for your account. For more information, see [API introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) on the Atlassian Developer website.

1. In Secrets Manager, create a secret with two keys: `key`, set to your API key, and `token`, set to your API token. Store the plain values.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Trello as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.