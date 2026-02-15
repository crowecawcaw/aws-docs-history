# CyberArk

CyberArk can be configured as an AgentCore Identity credential provider for outbound
resource access. This allows your agents to authenticate users through CyberArk's OAuth2
service and obtain access tokens for CyberArk API resources.

## Outbound

**Step 1**

Use the following procedure to set up a CyberArk OpenID Connect application and
obtain the necessary client credentials for AgentCore Identity.

###### To configure a CyberArk OAuth2 application

1. Open the developer console for CyberArk.
2. Open **Identity Administration** and then choose
   **Web Apps**.
3. Open the **Custom** tab.
4. Create a custom **OpenID Connect** application.
5. Open the **Trust** page, and use the following in the
   **Authorized Redirect URIs**:

```
https://bedrock-agentcore.`region`.amazonaws.com/identities/oauth2/callback
```

6. Record the client ID and client secret generated as you'll need this
   information to configure the CyberArk resource provider in
   AgentCore Identity.
7. Configure any scopes necessary for your application.
8. Deploy the application by setting the appropriate permissions by opening
   the **Permissions** page and adding the relevant
   permissions.

For more details, refer to [CyberArk's OpenID Connect documentation](https://docs.cyberark.com/identity/latest/en/content/applications/appscustom/openidaddconfigapp.htm "https://docs.cyberark.com/identity/latest/en/content/applications/appscustom/openidaddconfigapp.htm").

**Step 2**

To configure CyberArk as an outbound resource provider, use the following:

```
{
  "name": "CyberArk",
  "credentialProviderVendor": "CyberArkOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`",
      "authorizationEndpoint": "https://`your-tenant-id`.id.cyberark.cloud/OAuth2/Authorize/__idaptive_cybr_user_oidc",
      "tokenEndpoint": "https://`your-tenant-id`.id.cyberark.cloud/OAuth2/Token/__idaptive_cybr_user_oidc",
      "issuer": "https://`your-tenant-id`.id.cyberark.cloud/__idaptive_cybr_user_oidc"
    }
  }
}
```
