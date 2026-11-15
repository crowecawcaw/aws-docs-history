

# Setting up the authorization code flow for Contentful
<a name="contentful-setup-authorization-code-flow"></a>

Contentful uses the OAuth 2.0 authorization code flow. When you create the connection in AWS Glue Studio, you are redirected to Contentful to authorize AWS Glue, and AWS Glue then obtains and refreshes the access token for you.

To set up the authorization code flow for Contentful:

1. In Contentful, create an OAuth application to obtain a client ID and client secret. For more information, see [OAuth](https://www.contentful.com/developers/docs/extensibility/oauth/) on the Contentful website.

1. For the redirect URI, enter the redirect URI that the AWS Glue console uses:
   + If multi-session support is turned on in the AWS Management Console, use `https://3rdp.oauth.console.api.aws`.
   + Otherwise, use `https://{{region}}.console.aws.amazon.com/gluestudio/oauth`.

   Replace the following value:
   + {{region}} – The AWS Region where you create the connection.

1. Grant the read-only scope `content_management_read`.

1. In Secrets Manager, create a secret with the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` set to the client secret.

1. When you create the connection, choose OAuth 2.0 and enter the client ID in the **Client ID** field. Choose the secret and the IAM role that AWS Glue assumes to read and update the secret. Then complete the authorization in Contentful.

After you authorize the connection, AWS Glue stores the access token in your secret and refreshes it automatically.