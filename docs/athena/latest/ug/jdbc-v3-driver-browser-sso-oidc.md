

# Browser SSO OIDC credentials
<a name="jdbc-v3-driver-browser-sso-oidc"></a>

Browser SSO OIDC is an authentication plugin that works with [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). The plugin performs dynamic client registration with SSO OIDC, opens your default browser to the SSO authorization URL, receives the authorization code through a local callback server, exchanges it for an SSO access token, and uses that token to obtain temporary AWS credentials. The plugin uses the Authorization Code with PKCE flow.

For information on enabling and using IAM Identity Center, see [Step 1: Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-enable-identity-center.html) in the *AWS IAM Identity Center User Guide*.

**Note**  
This plugin is designed for single-user desktop environments. In shared environments like Windows Terminal Servers or Remote Desktop Services, system administrators are responsible for establishing and maintaining security boundaries between users.

## Credentials provider
<a name="jdbc-v3-driver-browser-sso-oidc-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `BrowserSSOOIDC`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | BrowserSSOOIDC | 

## IAM Identity Center start URL
<a name="jdbc-v3-driver-browser-sso-oidc-sso-start-url"></a>

The URL for the AWS access portal. The IAM Identity Center [RegisterClient](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_RegisterClient.html) API action uses this value for the `issuerUrl` parameter.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| SsoStartUrl | sso\_oidc\_start\_url | Required | none | 

## IAM Identity Center region
<a name="jdbc-v3-driver-browser-sso-oidc-sso-region"></a>

The AWS Region where IAM Identity Center is configured. The `SSOOIDCClient` and `SSOClient` use this value for the `region` parameter.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| SsoOidcRegion | sso\_oidc\_region | Required | none | 

## Account ID
<a name="jdbc-v3-driver-browser-sso-oidc-account-id"></a>

The identifier for the AWS account that is assigned to the user. The IAM Identity Center [GetRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html) API action uses this value for the `accountId` parameter.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| SsoOidcAccountId | sso\_oidc\_account\_id | Required | none | 

## Role name
<a name="jdbc-v3-driver-browser-sso-oidc-role-name"></a>

The friendly name of the role that is assigned to the user. The name that you specify for this permission set appears in the AWS access portal as an available role. The IAM Identity Center [GetRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html) API action uses this value for the `roleName` parameter.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| SsoOidcRoleName | sso\_oidc\_role\_name | Required | none | 

## Listen port
<a name="jdbc-v3-driver-browser-sso-oidc-listen-port"></a>

The local port number to use for the OAuth 2.0 callback server. This is used as the redirect URI. You may need to allowlist this port on your network. The default generated redirect URI is `http://127.0.0.1:7890/oauth/callback`.

**Warning**  
In shared environments like Windows Terminal Servers or Remote Desktop Services, the loopback port (default: 7890) is shared among all users on the same machine. System administrators can mitigate potential port hijacking risks by:  
Configuring different port numbers for different user groups
Using Windows security policies to restrict port access
Implementing network isolation between user sessions



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| ListenPort | listen\_port | Optional | 7890 | 

## Identity provider response timeout
<a name="jdbc-v3-driver-browser-sso-oidc-idp-response-timeout"></a>

The duration, in seconds, before the driver stops waiting for the SSO authorization response. The minimum value is 60 seconds.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| IdpResponseTimeout | idp\_response\_timeout | Optional | 120 | 

## Enable token caching
<a name="jdbc-v3-driver-browser-sso-oidc-enable-token-caching"></a>

When enabled, allows the same SSO access token to be used across driver connections. This prevents SQL tools that create multiple driver connections from launching multiple browser windows.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| EnableTokenCaching | none | Optional | FALSE | 