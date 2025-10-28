# Salesforce

Salesforce can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through Salesforce's
OAuth2 service and obtain access tokens for Salesforce API resources.

## Outbound

**Step 1**

Use the following procedure to set up a Salesforce OAuth2 application and obtain
the necessary client credentials for AgentCore Identity.

###### To configure a Salesforce OAuth2 application

1. In the developer portal for Salesforce, create a connected app and enter
   the name and other requested information specific to your
   application.
2. Enable and configure the OAuth settings for the application, providing the
   following as the callback URL:
   - `https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback`

3. Choose the necessary scopes and permissions your application will
   need.
4. Choose **Require Proof Key for Code Exchange (PKCE) Extension for
   Supported Authorization Flows**.
5. Choose **Require Secret for the Web Server Flow**.
6. Choose **Enable Authorization Code and Credentials
   Flow**.
7. If you wish to use Salesforce as a ClientCredentials/M2M provider then
   choose **Enable Client Credentials Flow** and follow the
   prompts.
8. Save your application and copy the client ID and client secret that is
   issued for the application. You will need these to configure Salesforce in
   AgentCore Identity.

For more details, refer to Salesforce's documentation [Define an OpenID Connect Provider](https://help.salesforce.com/s/articleView?id=xcloud.service_provider_define_oid.htm "https://help.salesforce.com/s/articleView?id=xcloud.service_provider_define_oid.htm").

**Step 2**

To configure the outbound Salesforce resource provider, use the following:

```
{
        "name": "NAME",
        "credentialProviderVendor": "SalesforceOauth2",
        "oauth2ProviderConfigInput": {
            "SalesforceOauth2ProviderConfigInput": {
                "clientId": "`your-client-id`",
                "clientSecret": "`your-client-secret`",
            }
        },
    }
```
