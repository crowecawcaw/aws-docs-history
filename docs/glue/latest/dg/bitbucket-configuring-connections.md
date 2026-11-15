

# Configuring Bitbucket connections
<a name="bitbucket-configuring-connections"></a>

Bitbucket connections support two authentication types: an Atlassian API token sent with HTTP Basic authentication, and OAuth 2.0 with the authorization code grant. For either type, you store the credential in an Secrets Manager secret and reference that secret when you create the connection.

To configure a Bitbucket connection:

1. For API token authentication, create an Atlassian API token for Bitbucket with read scopes for the data you want to read. For instructions on using API tokens, see [Using API tokens](https://support.atlassian.com/bitbucket-cloud/docs/using-api-tokens/) on the Atlassian Support website.

1. For API token authentication, create a secret in Secrets Manager with the key `api_key`. Set its value to the Base64 encoding of `{{email}}:{{apiToken}}`, where {{email}} is your Atlassian account email address. Don't include the `Basic` prefix. For OAuth 2.0, see [Setting up the authorization code flow for Bitbucket](bitbucket-setup-authorization-code-flow.md).

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Bitbucket as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.