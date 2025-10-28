# FusionAuth

FusionAuth can be configured as an outbound resource credential provider for
AgentCore Identity. This allows your agents to authenticate users through FusionAuth's OAuth2
service and obtain access tokens for FusionAuth API resources.

## Outbound

**Step 1**

Use the following procedure to set up a FusionAuth OAuth2 application and obtain
the necessary client credentials for AgentCore Identity.

###### To configure a FusionAuth OAuth2 application

1. Open the developer console for FusionAuth.
2. In the main navigation bar, choose
   **Applications**.
3. Choose **Add** to create a new application.
4. Enter a name for your application.
5. In the form mark the following as required: **Client
   Authentication**, **PKCE**.
6. For authorized redirect URLs, add the following:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

7. Add the necessary scopes for your application.
8. Record the client ID and client secret. You'll need this information to
   configure the FusionAuth resource provider in AgentCore Identity.

For more details, refer to [FusionAuth's OAuth documentation](https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/ "https://fusionauth.io/docs/lifecycle/authenticate-users/oauth/").

**Step 2**

To configure FusionAuth as an outbound resource provider, use the
following:

```
{
  "name": "FusionAuth",
  "credentialProviderVendor": "FusionAuthOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`",
      "authorizeEndpoint": "https://`your-tenant-authorization-url`",
      "tokenEndpoint": "https://`your-tenant-token-endpoint`",
      "issuer": "https://`your-tenant-token-issuer`"
    }
  }
}
```
