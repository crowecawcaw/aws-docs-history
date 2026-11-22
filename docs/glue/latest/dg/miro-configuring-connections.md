

# Configuring Miro connections

Miro connections use the OAuth 2.0 `AUTHORIZATION_CODE` grant type with a client app that you create in Miro. This grant type is three-legged: AWS Glue redirects you to Miro to sign in and approve access. AWS Glue stores the resulting access token and refresh token in your Secrets Manager secret and refreshes the access token automatically.

To configure a Miro connection:

1. Create and configure a Miro client app. For more information, see [Setting up the authorization code flow for Miro](miro-setup-authorization-code-flow.md).

1. In Secrets Manager, create a secret that stores your Miro app's client secret with the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`. Don't store the client ID in the secret.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Miro as the data source.

1. For **Client ID**, enter your Miro app's client ID.

1. Choose the Secrets Manager secret you created and the IAM role that AWS Glue assumes to read and update the secret. Optionally, set network options.

1. Sign in to Miro when you are redirected, approve access for the app, and then complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret. If the secret uses a customer managed key, also grant permission to use that key.