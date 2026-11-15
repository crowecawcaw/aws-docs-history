

# Configuring Sentry connections
<a name="sentry-configuring-connections"></a>

Sentry connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Sentry connection:

1. Create a Sentry auth token with read scopes for the data that you want to read, such as `org:read`, `project:read`, and `event:read`. You can create the token from an internal integration or from your personal token settings. For more information, see [Authentication](https://docs.sentry.io/api/auth/) on the Sentry website.

1. In Secrets Manager, create a secret containing the key `auth_token` set to your Sentry auth token. Store only the token value. The connector adds the `Bearer` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Sentry as the data source.

1. For the URL, keep the default `https://sentry.io`. If your Sentry organization stores its data in the DE region, choose `https://de.sentry.io`. Self-hosted Sentry is not supported.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.