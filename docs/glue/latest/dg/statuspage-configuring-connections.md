

# Configuring Statuspage connections

Statuspage connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Statuspage connection:

1. In the Statuspage management interface, choose your avatar, then choose **API info** and copy your API key. For more information, see [Authentication](https://developer.statuspage.io/#section/Authentication) on the Statuspage developer website.

1. In Secrets Manager, create a secret containing the key `api_key` set to your Statuspage API key. Store only the key value. The connector adds the `OAuth` prefix that Statuspage requires in the `Authorization` header. The connection doesn't use an OAuth flow.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Statuspage as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.