

# Setting up the authorization code flow for Constant Contact
<a name="constantcontact-setup-authorization-code-flow"></a>

Constant Contact uses the OAuth 2.0 authorization code flow. When you create the connection in AWS Glue Studio, you are redirected to Constant Contact to authorize AWS Glue, and AWS Glue then obtains and refreshes the access token for you.

To create your client app:

1. In Constant Contact, register an OAuth application to obtain a client ID and client secret.

1. Add the AWS Glue Studio OAuth redirect URI as an authorized redirect URL: `https://{region}.console.aws.amazon.com/gluestudio/oauth`.

1. Request the scopes `contact_data`, `campaign_data`, `account_read`, and `offline_access`.