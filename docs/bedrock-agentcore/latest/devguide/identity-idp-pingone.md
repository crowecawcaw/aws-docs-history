# PingOne

PingOne can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through PingOne's OAuth2
service and obtain access tokens for PingOne API resources.

## Outbound

###### Note

You can only configure a PingOne OAuth2 application as either a user
federation or M2M OAuth2 client but not both.

**Step 1**

Use the following procedure to set up a PingOne OAuth2 application and obtain the
necessary client credentials for AgentCore Identity.

###### To configure a PingOne OAuth2 application

1. Sign onto the PingOne admin console.
2. In the left navigation bar, under **Applications**, choose **Application**.
3. On the page, choose the **+** icon next to **Applications** to create a new application.
4. To configure your application as a M2M OAuth2 client:
   - Select **Client Credentials** for Grant
     Type.
   - Select **Client Secret Post** for Token Endpoint
     Authentication Method.
   - Create a custom resource under Applications→Resources in the tabs
     on the left side of the page, including a scope. Then, add that
     scope to the application under its personal
     **Resources** tab. Then, make sure that scope
     is present in the 'scopes' field of
     GetResourceOauth2AccessToken.

5. To configure your application as a user federation Oauth2 client:
   - Select **Code** for Response Type.
   - Select **Authorization Code** for Grant
     Type.
   - Select **Client Secret Basic** for Token Endpoint
     Authentication Method.

For more details, refer to [PingOne's
API documentation](https://apidocs.pingidentity.com/pingone/getting-started/v1/api "https://apidocs.pingidentity.com/pingone/getting-started/v1/api").

**Step 2**

To configure PingOne as an outbound resource provider use the following:

```
{
  "name": "PingOne",
  "credentialProviderVendor": "PingOneOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`",
      "authorizeEndpoint": "https://auth.pingone.com/`your-env-id`/as/authorize",
      "tokenEndpoint": "https://auth.pingone.com/`your-env-id`/as/token",
      "issuer": "https://auth.pingone.com/`your-env-id`/as"
    }
  }
}
```
