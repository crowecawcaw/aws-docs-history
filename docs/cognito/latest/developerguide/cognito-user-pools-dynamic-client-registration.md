

# Dynamic client registration

With dynamic client registration, applications and AI agents can register their own OAuth app clients in your user pool at runtime. They call the registration endpoint of your user pool domain, which follows the OAuth 2.0 Dynamic Client Registration Protocol. For more information, see [RFC 7591](https://www.rfc-editor.org/rfc/rfc7591) on the RFC Editor website. Registered clients count toward the [app client quota](#cognito-user-pools-dynamic-client-registration-quota) of your user pool. Dynamic client registration is available with the **Essentials** and **Plus** feature plans.

The registration endpoint is `https://{{your user pool domain}}/oauth2/register`. You can allow two kinds of registration. With *open registration*, applications register without an initial access token. With *authenticated registration*, an application first obtains an initial access token by authenticating as an app client that holds the `aws.cognito/dcr/register` scope. This scope is a system-managed scope. You don't create a resource server for it. Amazon Cognito doesn't use your resource servers when it evaluates this scope. The application then sends the initial access token in the `Authorization` header of the registration request as a bearer token.

When dynamic client registration is on and your user pool has a domain, the OpenID Connect discovery document of your user pool lists the registration endpoint as `registration_endpoint`. Applications that support discovery can find the endpoint there. For more information, see [Amazon Cognito user pools as an OIDC issuer](federation-endpoints.md#user-pool-oidc-issuer).

While dynamic client registration is off, the registration endpoint returns HTTP `404`. While open registration is off, a request without an initial access token returns HTTP `401` with the error `invalid_token`.

After you turn on dynamic client registration, the registration endpoint returns HTTP `404` until the change takes effect. If you also add a domain to your user pool, the endpoint is available after the domain is. For more information, see [Configuring a user pool domain](cognito-user-pools-assign-domain.md).

**Topics**
+ [Before you turn on dynamic client registration](#cognito-user-pools-dynamic-client-registration-enable)
+ [Setting up dynamic client registration (AWS Management Console)](#cognito-user-pools-dynamic-client-registration-console)
+ [Configuring dynamic client registration (AWS CLI and AWS API)](#cognito-user-pools-dynamic-client-registration-cli-api)
+ [Assigning the register scope to an app client](#cognito-user-pools-dynamic-client-registration-register-scope)
+ [Registering app clients](#cognito-user-pools-dynamic-client-registration-register)
+ [Using dynamic client registration with MCP clients](#cognito-user-pools-dynamic-client-registration-mcp)
+ [Using dynamically registered clients](#cognito-user-pools-dynamic-client-registration-using)
+ [Deleting dynamically registered clients](#cognito-user-pools-dynamic-client-registration-delete)
+ [Security considerations for dynamic client registration](#cognito-user-pools-dynamic-client-registration-security)
+ [App client quota with dynamic client registration](#cognito-user-pools-dynamic-client-registration-quota)

## Before you turn on dynamic client registration
<a name="cognito-user-pools-dynamic-client-registration-enable"></a>

Before you turn on dynamic client registration, check the following. These checks apply even if you plan to use only open registration, because authenticated registration doesn't have a separate setting to turn it off.
+ If a resource server in your user pool has the identifier `aws.cognito/dcr` and a `register` scope, remove it before you turn on dynamic client registration. Amazon Cognito treats `aws.cognito/dcr/register` as the system-managed register scope and ignores the resource server.
+ No app client lists `aws.cognito/dcr/register` in its allowed OAuth scopes unless you intend that client to authorize registrations. After you turn on dynamic client registration, any access token that your user pool issues with this scope can register app clients.
+ Every domain of your user pool uses managed login. While a domain uses the classic hosted UI, you can't turn on dynamic client registration. For more information, see [Using dynamically registered clients](#cognito-user-pools-dynamic-client-registration-using).

While dynamic client registration is off, you can't assign the `aws.cognito/dcr/register` scope to an app client.

Before you turn on open registration, review [Security considerations for dynamic client registration](#cognito-user-pools-dynamic-client-registration-security).

## Setting up dynamic client registration (AWS Management Console)
<a name="cognito-user-pools-dynamic-client-registration-console"></a>

You can use the AWS Management Console to turn on dynamic client registration and set the grant types and scopes that registered clients can request. When you save these settings, Amazon Cognito turns on dynamic client registration. You can't turn off dynamic client registration in the console.

**To set up dynamic client registration**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. In the navigation pane, choose **User pools**, and choose your user pool.

1. Under **Applications**, choose **MCP auth**. In **Dynamic client registration settings**, choose **Edit**.

1. To let applications register without an initial access token, turn on **Enable open registration**.

1. For **Authenticated registration grant types**, choose the grant types that clients registered with an initial access token can request.

1. If you turned on open registration, choose the **Open registration grant types** that clients registered without an initial access token can request. If you choose **Client credentials**, select **I understand the billing risk of enabling client credentials for open registration**.

1. Choose the **Allowed scopes** that registered clients can request.

1. Choose **Save changes**.

To use authenticated registration, assign the `aws.cognito/dcr/register` scope to an app client. For more information, see [Assigning the register scope to an app client](#cognito-user-pools-dynamic-client-registration-register-scope).

## Configuring dynamic client registration (AWS CLI and AWS API)
<a name="cognito-user-pools-dynamic-client-registration-cli-api"></a>

Use the following operations to configure dynamic client registration for your user pool.

**To turn on dynamic client registration**
+ AWS CLI: `aws cognito-idp create-user-pool` or `aws cognito-idp update-user-pool`
+ AWS API: [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) or [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) with a `DcrConfiguration`

If you omit `EnableStatus`, Amazon Cognito turns on dynamic client registration. Amazon Cognito replaces the whole `DcrConfiguration` with the one in your request, so include every member that you want to keep. If you omit `DcrConfiguration` from an `UpdateUserPool` request, your configuration doesn't change. `UpdateUserPool` resets other user pool settings that you omit. For more information, see [Updating a user pool with an AWS SDK, AWS CDK, or REST API](cognito-user-pool-updating.md#cognito-user-pool-updating-api-cli).

To turn off dynamic client registration, call [DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html) (`aws cognito-idp describe-user-pool`), and then call [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) (`aws cognito-idp update-user-pool`) with the returned settings that it accepts. In the `DcrConfiguration`, set `EnableStatus` to `Disabled`, and include the other members to keep them for when you turn registration back on.

Turning off dynamic client registration stops new registrations. It doesn't delete or deactivate app clients that applications already registered. To remove them, call `ListUserPoolClients` with `ClientType` set to `DCR`, and then call `DeleteUserPoolClient`.

While dynamic client registration is off, `UpdateUserPoolClient` rejects requests that include `aws.cognito/dcr/register`, even for an app client that already has it. Before you turn off dynamic client registration, remove the scope from those app clients, or turn registration back on before you update them.

## Assigning the register scope to an app client
<a name="cognito-user-pools-dynamic-client-registration-register-scope"></a>

Authenticated registration needs an app client that issues initial access tokens. Use a regular app client that has a client secret and that uses only the client credentials grant. The client credentials grant requires a client secret, and an app client can't combine it with the authorization code or implicit grant. You can assign the `aws.cognito/dcr/register` scope only while dynamic client registration is on, and a dynamically registered client can't hold it.

**To assign the register scope (console)**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. In the navigation pane, choose **User pools**, and choose your user pool.

1. From the **App clients** menu, choose an app client that has a client secret.

1. On the **Login pages** tab, choose **Edit** on **Managed login pages configuration**.

1. Under **OAuth 2.0 grant types**, choose only **Client credentials**.

1. Under **Custom scopes**, choose `aws.cognito/dcr/register`.

1. Choose **Save changes**.

To assign the scope with the API, call [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) (`aws cognito-idp describe-user-pool-client`), and then call [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html) (`aws cognito-idp update-user-pool-client`) with the returned settings that it accepts. In the request, set `AllowedOAuthFlows` to `client_credentials`, add `aws.cognito/dcr/register` to `AllowedOAuthScopes`, and set `AllowedOAuthFlowsUserPoolClient` to `true`. `UpdateUserPoolClient` resets settings that you omit. For more information, see [Updating a user pool with an AWS SDK, AWS CDK, or REST API](cognito-user-pool-updating.md#cognito-user-pool-updating-api-cli).

## Registering app clients
<a name="cognito-user-pools-dynamic-client-registration-register"></a>

After you turn on dynamic client registration, applications register app clients by sending a `POST` request with a JSON body to the registration endpoint of your user pool domain. Applications that support discovery read the endpoint from `registration_endpoint` in the discovery document of your user pool. Applications can send the following metadata.
+ `redirect_uris`: The callback URLs of the client. Required for the authorization code grant.
+ `grant_types`: `authorization_code` or `client_credentials`. A client can't have both. If an application omits this field, Amazon Cognito uses `authorization_code`.
+ `scope`: A space-separated list of scopes. Scopes other than `openid`, `email`, `phone`, and `profile` must be in your allowed scopes. Required for the client credentials grant.
+ `client_name` and `token_endpoint_auth_method`: Optional. For details, see [Using dynamically registered clients](#cognito-user-pools-dynamic-client-registration-using).

The following example registers a public client for the authorization code grant. With authenticated registration, the request also includes an `Authorization` header with an initial access token.

```
POST https://{{example.auth.us-east-1.amazoncognito.com}}/oauth2/register
Content-Type: application/json

{
    "client_name": "{{Example MCP client}}",
    "redirect_uris": ["{{https://app.example.com/callback}}"],
    "grant_types": ["authorization_code"],
    "token_endpoint_auth_method": "none",
    "scope": "openid email"
}
```

Amazon Cognito returns HTTP `201` with the new client. When the application doesn't request `none`, the response also includes a `client_secret`, and `client_secret_expires_at` is `0` because the secret doesn't expire.

```json
{
    "client_id": "{{dcr_1example23456789}}",
    "client_id_issued_at": {{1767225600}},
    "client_name": "{{Example MCP client}}",
    "redirect_uris": ["{{https://app.example.com/callback}}"],
    "grant_types": ["authorization_code"],
    "response_types": ["code"],
    "scope": "openid email",
    "token_endpoint_auth_method": "none"
}
```

The application then uses the client ID like any other app client. With the authorization code grant, it sends users to the [Authorize endpoint](authorization-endpoint.md), and a public client must use PKCE with `S256`. With the client credentials grant, it requests tokens from the [Token endpoint](token-endpoint.md) with its client ID and secret.

### With open registration
<a name="cognito-user-pools-dynamic-client-registration-register-open"></a>

Give the registration endpoint URL to the applications that you want to register, for example in your developer documentation or in the configuration of a Model Context Protocol (MCP) server. Applications send registration requests without an `Authorization` header. Monitor new clients with `ListUserPoolClients` and the `ClientType` filter set to `DCR`, and delete clients that you don't want.

### With authenticated registration
<a name="cognito-user-pools-dynamic-client-registration-register-authenticated"></a>

An application that registers through authenticated registration first needs an initial access token. To get one, request the client credentials grant from the [Token endpoint](token-endpoint.md) with the app client that holds the `aws.cognito/dcr/register` scope. Authorize the request with the client ID and client secret of that app client.

```
POST https://{{example.auth.us-east-1.amazoncognito.com}}/oauth2/token
Content-Type: application/x-www-form-urlencoded
Authorization: Basic {{EXAMPLEBASE64CREDENTIAL}}

grant_type=client_credentials&scope=aws.cognito%2Fdcr%2Fregister
```

The `access_token` in the response is the initial access token. Send it in the `Authorization` header of the registration request.

```
Authorization: Bearer {{eyJra789ghiEXAMPLE}}
```

An initial access token can register any number of app clients until it expires, and it works only in the user pool that issued it. Its lifetime is the access token validity of the app client that holds the register scope. Request a new token when it expires. Keep the client secret of that app client on a server that you control, and give initial access tokens only to applications that you trust.

## Using dynamic client registration with MCP clients
<a name="cognito-user-pools-dynamic-client-registration-mcp"></a>

Model Context Protocol (MCP) clients, such as AI agents and developer tools, can use dynamic client registration to connect to an MCP server that your user pool protects. The MCP client registers its own app client, signs the user in with the authorization code grant, and calls the MCP server with the access token. To set this up, do the following.

1. Create a resource server for your MCP server, with custom scopes for the access that it grants. Use the URL of your MCP server as the resource server identifier. For more information, see [Scopes, M2M, and resource servers](cognito-user-pools-define-resource-servers.md).

1. Add a domain to your user pool, and set its **Branding version** to **Managed login**. Dynamic client registration requires managed login on every domain of your user pool. With a domain, the discovery document lists the registration endpoint. With managed login, MCP clients can get access tokens that are bound to your MCP server. For more information, see [Configuring a user pool domain](cognito-user-pools-assign-domain.md) and [Setting up managed login with the Amazon Cognito console](cognito-user-pools-managed-login.md#set-up-managed-login).

1. Turn on dynamic client registration with open registration and the authorization code grant, and add the scopes of your MCP server to the allowed scopes.

1. Configure your MCP server to name your user pool as its authorization server, and to accept access tokens from your user pool that carry its scopes.

MCP clients usually register as public clients. They set `token_endpoint_auth_method` to `none` and use PKCE with `S256`. Clients that run on a user's computer often use a loopback redirect URI, such as `http://localhost:{{port}}/callback`. Amazon Cognito accepts the `http` scheme only for loopback hosts. A client can register a loopback redirect URI without a port, for example `http://localhost/callback`, and then use any port at runtime, such as `http://localhost:8080/callback`. This is the same rule that applies to other [app client callback URLs](user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-about): for loopback hosts, Amazon Cognito accepts any port at runtime.

MCP clients include the `resource` parameter to name the MCP server. With managed login, the audience (`aud`) of the access token is the requested resource. Custom scopes in the request must belong to the resource server whose identifier matches the value of `resource` exactly. For more information, see [Resource binding](cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding).

## Using dynamically registered clients
<a name="cognito-user-pools-dynamic-client-registration-using"></a>

When an application registers a client with the authorization code grant, Amazon Cognito assigns the client `COGNITO` and every identity provider in your user pool. Your users can then sign in to the client through managed login with any of these identity providers. Amazon Cognito leaves out SAML providers that accept IdP-initiated sign-in, because an app client can't combine them with `COGNITO`. If your users sign in only through such a provider, they can't sign in to registered clients. A client that uses only the client credentials grant gets no identity providers. Identity providers that you add to your user pool later aren't added to clients that are already registered.

While dynamic client registration is on, every domain of your user pool must use managed login (`ManagedLoginVersion` 2). Amazon Cognito rejects the following requests with `InvalidParameterException`:
+ `UpdateUserPool` requests that turn on dynamic client registration while a domain of the user pool uses the classic hosted UI.
+ `CreateUserPoolDomain` requests that set `ManagedLoginVersion` to 1 or omit it.
+ `UpdateUserPoolDomain` requests that change a domain to the classic hosted UI.

A registered client that doesn't have a style of its own uses the default managed login style, the same as a style that you create with `UseCognitoProvidedValues`. The default style doesn't count toward the quota of styles in your user pool. To brand the sign-in pages of a registered client, create a style for it. For more information, see [Apply branding to managed login pages](managed-login-branding.md).

To change the identity providers or other settings of a registered client, call [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html), and then call [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html) with the returned settings that it accepts and your changes. `UpdateUserPoolClient` resets settings that you omit, such as `SupportedIdentityProviders`, `CallbackURLs`, `LogoutURLs`, `AllowedOAuthFlows`, `AllowedOAuthScopes`, `AllowedOAuthFlowsUserPoolClient`, and `ExplicitAuthFlows`. Don't include `PublishSecretsInAWSSecretsManager` or the `aws.cognito/dcr/register` scope, because Amazon Cognito rejects both for these clients. For more information, see [Updating a user pool with an AWS SDK, AWS CDK, or REST API](cognito-user-pool-updating.md#cognito-user-pool-updating-api-cli). In the AWS Management Console, you can change identity providers on the **Login pages** tab of the app client, and the console keeps the other settings of the client.

The application that registered a client chose its `CallbackURLs`. Users who already have a managed login session can be signed in to a registered client without a prompt, so review the `CallbackURLs` of registered clients.

Registered clients support the default authentication flows of the user pools API, which are `ALLOW_USER_SRP_AUTH`, `ALLOW_CUSTOM_AUTH`, and `ALLOW_REFRESH_TOKEN_AUTH`. With `ALLOW_CUSTOM_AUTH`, a registered client can start custom authentication, which invokes the [custom authentication challenge Lambda triggers](user-pool-lambda-challenge.md) of your user pool. With open registration, anyone can register a client that starts custom authentication. If your custom authentication triggers send messages, such as SMS or email codes, limit the rate at which they send, or don't turn on open registration. Applications can also sign users in to a registered client with `InitiateAuth`, for example from their own sign-in pages. Access tokens from `InitiateAuth` carry the `aws.cognito.signin.user.admin` scope, which lets the token holder read and change the profile of the signed-in user, even if `aws.cognito.signin.user.admin` isn't in your allowed scopes. To limit the authentication flows of a registered client, set `ExplicitAuthFlows` when you update the client, for example to `ALLOW_REFRESH_TOKEN_AUTH` only. Include `ExplicitAuthFlows` in each later update, because `UpdateUserPoolClient` resets it when you omit it.

Amazon Cognito doesn't enforce `token_endpoint_auth_method`. If an application requests `client_secret_basic` or `client_secret_post`, or omits the field, Amazon Cognito issues a client secret, and the client can authenticate at the token endpoint with either HTTP Basic authentication or a `client_secret` in the request body. The registration response returns the value that the application requested, or `client_secret_basic` if it omitted the field. If an application requests `none`, Amazon Cognito creates a public client with no client secret. Amazon Cognito rejects other values, such as `private_key_jwt`, with `invalid_client_metadata`.

A `client_name` follows the same rules as other app client names. For the length and characters that you can use, see the `ClientName` parameter of [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html#CognitoUserPools-CreateUserPoolClient-request-ClientName). If an application omits the name, Amazon Cognito uses the client ID as the name. Registered clients use the default token validity periods, have token revocation turned on, and have `PreventUserExistenceErrors` set to `ENABLED`, so they don't reveal whether a user exists.

Dynamically registered clients don't support client secret operations such as `AddUserPoolClientSecret`, `DeleteUserPoolClientSecret`, and `ListUserPoolClientSecrets`, and they can't publish secrets to AWS Secrets Manager. You can't rotate the secret of a registered client, and the secret doesn't expire. If the secret is exposed, delete the app client.

## Deleting dynamically registered clients
<a name="cognito-user-pools-dynamic-client-registration-delete"></a>

You delete a dynamically registered client the same way as any other app client.

**To delete a dynamically registered client (console)**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. In the navigation pane, choose **User pools**, and choose your user pool.

1. From the **App clients** menu, choose the app client.

1. Choose **Delete**, and confirm.

To delete registered clients with the API, call [ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html) with `ClientType` set to `DCR` to find registered clients, and then call [DeleteUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html) for each client that you want to remove. Each deleted client frees one place in the app client quota of your user pool.

Applications can't update or delete their own registrations. The registration endpoint accepts only `POST` requests that create clients, and Amazon Cognito doesn't support the client configuration endpoint of RFC 7592. Turning off dynamic client registration doesn't delete clients that applications already registered.

## Security considerations for dynamic client registration
<a name="cognito-user-pools-dynamic-client-registration-security"></a>

Dynamic client registration lets applications that you don't administer create app clients in your user pool. Review the following considerations before you turn it on.

### Preventative security best practices
<a name="cognito-user-pools-dynamic-client-registration-security-preventative"></a>
+ **Limit the rate of open registration.** Anyone who can reach your user pool domain can register an app client through open registration. [Associate an AWS WAF web ACL](user-pool-waf.md) with your user pool and add a rate-based rule for requests to the `/oauth2/register` path. AWS WAF doesn't receive the body of registration requests, so match on the path, the source IP address, and headers. AWS WAF receives the `Authorization` header, which carries the initial access token in authenticated registration. If you turn on logging for your web ACL, redact the `authorization` header.
+ **Choose grant types for each registration mode.** In the API, if you omit `OpenDcrGrantTypes`, open registration permits only the authorization code grant. If you omit `AuthenticatedGrantTypes`, authenticated registration permits the authorization code and client credentials grants. An empty list permits no grant types in that mode. In the console, choose at least one grant type for each registration mode that you use. A registered client can use the authorization code grant or the client credentials grant, but not both. If you add the client credentials grant to open registration, anyone can register an app client and get machine-to-machine access tokens with any custom scope in your allowed scopes. Your resource servers then accept requests from callers that you can't identify, and you're billed for those token requests.
+ **Choose allowed scopes for unknown callers.** Registered clients can request the scopes in your allowed scopes, and they can always request the `openid`, `email`, `phone`, and `profile` scopes. If an application requests no scopes, Amazon Cognito assigns `openid` to a client with the authorization code grant. Allow only scopes that are safe for callers that you can't identify. Don't add `aws.cognito.signin.user.admin` to the allowed scopes, because it lets registered clients read and change the profiles of users who sign in through them. Allowed scopes apply to tokens from the authorization and token endpoints. Tokens from `InitiateAuth` carry `aws.cognito.signin.user.admin` regardless.
+ **Protect the register scope.** Any access token that carries the `aws.cognito/dcr/register` scope can register app clients. Assign this scope only to a confidential app client that you control and that uses only the client credentials grant. If an app client that holds this scope also allows the authorization code or implicit grant, users who sign in through that client receive access tokens that can register app clients. Protect the client secret as you would administrator credentials. While dynamic client registration is on, any principal with permission to call `CreateUserPoolClient` or `UpdateUserPoolClient` can assign this scope to an app client.
+ **Keep initial access tokens short-lived.** An initial access token can register any number of app clients until it expires, and it works only in the user pool that issued it. An initial access token from a user sign-in stops working when you revoke its refresh token, when the user signs out globally, or when you disable or delete the user. It also stops working while the user is unconfirmed or must reset their password. An initial access token from the client credentials grant stops working when you delete its app client. The registration endpoint then returns HTTP 401 with the error `invalid_token`. Removing the register scope from the app client doesn't invalidate tokens that are already issued. Set a short access token validity on the app client that holds the register scope. A dynamically registered client can't hold the register scope, so it can't register more app clients.
+ **Use PKCE in public clients.** A dynamically registered client without a client secret must include a [PKCE](using-pkce-in-authorization-code.md) code challenge with the `S256` method in each authorization request. Amazon Cognito checks the redirect URIs of registered clients with the same rules as other [app clients](user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-about).

### Detective security best practices
<a name="cognito-user-pools-dynamic-client-registration-security-detective"></a>
+ **Monitor registrations.** Amazon Cognito logs requests to the registration endpoint to AWS CloudTrail as `Register_POST` events, including requests that it rejects. When a request passes basic validation, the event records the submitted client metadata and the registration mode (`OPEN` or `AUTHENTICATED`). When registration succeeds, the event also records the ID of the new app client. The event doesn't record initial access tokens or client secrets. Requests that your web ACL blocks don't produce an event. To find dynamically registered clients, call [ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html) with the `ClientType` filter set to `DCR`. To remove a client that you don't want, call [DeleteUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html).

## App client quota with dynamic client registration
<a name="cognito-user-pools-dynamic-client-registration-quota"></a>

Regular and dynamically registered app clients share one quota for each user pool. When you turn on dynamic client registration, each user pool can have 10,000 app clients, counting both kinds together. If your account already has an approved increase to the app client quota, that value applies instead, even when it's lower than 10,000. Because the quota is shared, open registration can let unknown callers use up the quota, and then you can't create app clients until you delete some. If you turn off dynamic client registration, the default quota of 1,000 applies again. When your user pool reaches the quota or when Amazon Cognito throttles registration requests, the registration endpoint returns HTTP `429`. The response body has the error `temporarily_unavailable`, or `Rate exceeded` when the endpoint itself limits the request rate. Applications should treat any `429` response as a signal to retry later.