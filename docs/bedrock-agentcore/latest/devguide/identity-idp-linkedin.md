# LinkedIn

LinkedIn can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through LinkedIn's OAuth2
service and obtain access tokens for LinkedIn API resources.

## Outbound

**Step 1**

Use the following procedure to set up a LinkedIn OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a LinkedIn OAuth2 application

1. Open LinkedIn's developer portal and create an application.
2. In the Auth tab, note the client ID and client secret as you'll need this
   information to configure LinkedIn as a provider in AgentCore Identity.
3. Under the OAuth2 settings section, add the following as an authorized
   redirect URL for the application:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

4. Configure any scopes that are necessary for your application.

For more information about LinkedIn authentication, see [Authentication overview](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication") on the Microsoft website.

**Step 2**

To configure LinkedIn as an outbound resource provider, use the following
configuration:

```
{
   "name": "NAME",
   "credentialProviderVendor": "LinkedInOAuth2",
   "oauth2ProviderConfigInput": {
       "linkedInOauth2ProviderConfig": {
           "clientId": "`your-client-id`",
           "clientSecret": "`your-client-secret`"
       }
   }
}
```
