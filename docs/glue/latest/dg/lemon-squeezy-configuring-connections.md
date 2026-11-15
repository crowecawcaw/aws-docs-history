

# Configuring Lemon Squeezy connections
<a name="lemon-squeezy-configuring-connections"></a>

Lemon Squeezy connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Lemon Squeezy connection:

1. In your Lemon Squeezy account settings, create an API key. Use a live-mode key to read production data or a test-mode key to read test-mode data. For more information, see [API requests](https://docs.lemonsqueezy.com/api/getting-started/requests) on the Lemon Squeezy website.

1. In Secrets Manager, create a secret with the key `api_key`. Set its value to the API key itself. Don't add a `Bearer` prefix, because the connector adds it.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Lemon Squeezy as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.