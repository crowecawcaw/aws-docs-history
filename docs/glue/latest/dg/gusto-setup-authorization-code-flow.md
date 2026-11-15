

# Setting up the authorization code flow for Gusto
<a name="gusto-setup-authorization-code-flow"></a>

Gusto uses the OAuth 2.0 authorization code flow. When you create the connection in AWS Glue Studio, you are redirected to Gusto to authorize AWS Glue, and AWS Glue then obtains and refreshes the access token for you.

To create your client app:

1. In Gusto, register an OAuth application (connected app) to obtain a client ID and client secret.

1. Add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL: `https://{region}.console.aws.amazon.com/gluestudio/oauth`.

1. Grant the connected app read access to the data you want to query.