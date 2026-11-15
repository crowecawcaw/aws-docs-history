

# Configuring LaunchDarkly connections
<a name="launchdarkly-configuring-connections"></a>

LaunchDarkly connections authenticate with a LaunchDarkly personal or service access token. You can't use SDK keys, mobile keys, or client-side IDs. You store the access token in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a LaunchDarkly connection:

1. Create a LaunchDarkly personal or service access token. To read the `tokens` entity for all members, the token must have the Admin role. For more information, see [Using the LaunchDarkly REST API](https://launchdarkly.com/docs/guides/api/rest-api) in the LaunchDarkly documentation.

1. In Secrets Manager, create a secret containing the key `apiToken` set to your LaunchDarkly access token. Store the raw token without a `Bearer` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose LaunchDarkly as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.