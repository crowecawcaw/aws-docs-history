# Okta

Okta can be configured as an identity provider for accessing AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource access. This allows your agents to authenticate and authorize agent users with Okta as the identity provider and authorization server, or your agents to obtain credentials to access resources authorized by Okta.

## Inbound

To add Okta as an identity provider and authorization server for accessing AgentCore Gateway and Runtime, you must:

- Configure a discovery URL from your Okta tenant. This helps AgentCore Identity get the metadata related to your OAuth authorization server and token verification keys.
- Enter valid `aud` claims for the token. This helps validate the tokens coming from your IdP and allows access for tokens that contain expected claims.

###### To configure Okta for inbound authentication

1. Open the Okta developer console.
2. In the left navigation bar, choose **Applications**.
3. Choose **Create App Integration**.
4. Choose **OIDC - OpenID Connect** as the sign-in method for your application.
5. Choose **Web Application** as your application type.
6. Provide a name for your application.
7. Select **Authorization Code** and/or **Client Credentials** depending on your needs.
8. For **Sign-in redirect URIs** add your application endpoint that will receive the Okta token.
9. Adjust the **Assignments** section as necessary depending on your needs.
10. Choose **Save**.
11. Create an Okta API to represent your application:
    - In the left navigation bar, choose **Security**.
    - Go to **API** and choose **Add Authorization Server**.
    - Follow the flow to create an authorization server dedicated to your Okta tenant.
    - Once the authorization server has been created, choose the **Access Policies** tab on the overview page to configure an appropriate access policy.
    - Define the necessary custom scopes for the authorization server that is needed for your application.

12. Construct the discovery URL for your Okta tenant:

```
https://`your-tenant`.okta.com/oauth2/`your-authorization-server`
```

13. Configure Inbound Auth with the following values:
    - **Discovery URL:** The URL constructed in the previous step
    - **Allowed Audiences:** The audience value you provided when creating the API in step 11

For more details, refer to [Okta's documentation](https://developer.okta.com/docs/concepts/oauth-openid/ "https://developer.okta.com/docs/concepts/oauth-openid/").

### Add a client_id claim into access token claims

Okta by default does not include `client_id` as a standard claim in their tokens. To populate the claim in the token, you need to customize the claims through the authorization server that you use to issue tokens.

###### To add client_id claim to access tokens

1. In the left navigation bar, choose **Security**. Go to **API** and choose the authorization server that you intend to use for your application.
2. In the details page for the authorization server, choose the **Claims** tab and choose **Add Claim**.
3. Name the new claim **client_id** and set the value to **app.clientId**.
4. Set **Include in token type** to **Access Token**.
5. Choose **Save**.

For more details, refer to [Okta's documentation](https://developer.okta.com/docs/guides/customize-tokens-returned-from-okta/main/ "https://developer.okta.com/docs/guides/customize-tokens-returned-from-okta/main/").

## Outbound

Follow the same steps for configuring Okta as an inbound provider; however, when configuring the **Sign-in redirect URIs** add the callback URL that is assigned to your provider when creating the provider in AgentCore Identity.

To configure Okta as an outbound resource provider in AgentCore Identity, use the following:

```
{
  "name": "Okta",
  "credentialProviderVendor": "OktaOauth2",
  "oauth2ProviderConfigInput" : {
    "includedOauth2ProviderConfig": {
      "clientId": "`your-client-id`",
      "clientSecret": "`your-client-secret`",
      "authorizationEndpoint": "https://`your-tenant`.okta.com/oauth2/`your-authorization-server`/v1/authorize",
      "tokenEndpoint": "https://`your-tenant`.okta.com/oauth2/`your-authorization-server`/v1/token",
      "issuer": "https://`your-tenant`.okta.com/oauth2/`your-authorization-server`"
    }
  }
}
```
