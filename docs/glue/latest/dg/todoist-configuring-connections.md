

# Configuring Todoist connections
<a name="todoist-configuring-connections"></a>

Todoist connections authenticate with a Todoist personal API token or an OAuth 2.0 access token supplied as a static secret. The connector sends the token as a bearer token in the `Authorization` header and doesn't perform OAuth authorization or token refresh. You store the token in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Todoist connection:

1. Obtain a Todoist personal API token or OAuth 2.0 access token. For a personal API token, copy it from the **Integrations** settings of your Todoist account. For more information, see [Todoist API v1](https://developer.todoist.com/api/v1/) on the Todoist website.

1. In Secrets Manager, create a secret with the key `token` set to the raw token. Don't include the `Bearer` prefix; the connector adds it.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Todoist as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.