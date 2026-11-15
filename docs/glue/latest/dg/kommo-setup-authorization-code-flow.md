

# Setting up the authorization code flow for Kommo
<a name="kommo-setup-authorization-code-flow"></a>

Kommo uses the OAuth 2.0 authorization code grant. You register an OAuth integration in Kommo to obtain a client ID and client secret, store the client secret in Secrets Manager, and authorize the connection through the Kommo consent screen when you create it in AWS Glue Studio. AWS Glue then obtains and refreshes the access token for you.

1. In Kommo, create an OAuth integration to obtain a client ID and client secret, and add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL on that integration: `https://{region}.console.aws.amazon.com/gluestudio/oauth`.

1. In Secrets Manager, create a secret containing the key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` set to your Kommo OAuth integration's client secret.

1. When you create the connection in AWS Glue Studio, choose OAuth 2.0 authentication, enter the client ID in the **Client ID** field, and set the token URL to your account subdomain (for example, `https://<subdomain>.kommo.com/oauth2/access_token`).

1. Choose the Secrets Manager secret that contains the client secret, select the IAM role that AWS Glue can assume to read the secret, and authorize the connection through Kommo to complete creation.