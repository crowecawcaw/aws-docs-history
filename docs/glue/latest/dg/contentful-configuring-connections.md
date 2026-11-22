

# Configuring Contentful connections

Contentful connections support two authentication types: a Content Management API personal access token, or OAuth 2.0 (authorization code). For the token, store it in Secrets Manager; for OAuth 2.0, see [Setting up the authorization code flow for Contentful](contentful-setup-authorization-code-flow.md).

To configure a Contentful connection:

1. In the Contentful web app, Settings → API keys → Content management tokens → generate a Personal Access Token (`CFPAT-…`). Store it in Secrets Manager as `accessToken`. The connector sends it as `Authorization: Bearer <token>`. If the organization has token access control enabled, the token must be authorized for the organization first.

1. In Secrets Manager, create a secret containing the key `accessToken` set to your Contentful credential. For OAuth 2.0, see [Setting up the authorization code flow for Contentful](contentful-setup-authorization-code-flow.md).

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Contentful as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.