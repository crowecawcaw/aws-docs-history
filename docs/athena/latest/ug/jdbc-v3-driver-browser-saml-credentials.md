

# Browser SAML credentials
<a name="jdbc-v3-driver-browser-saml-credentials"></a>

Browser SAML is a generic authentication plugin that can work with SAML-based identity providers and supports multi-factor authentication.

## Credentials provider
<a name="jdbc-v3-driver-browser-saml-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `BrowserSaml`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | BrowserSaml | 

## Single sign-on login URL
<a name="jdbc-v3-driver-single-sign-on-login-url"></a>

The single sign-on URL for your application on the SAML-based identity provider.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| SsoLoginUrl | login\_url (deprecated) | Required | none | 

## Listen port
<a name="jdbc-v3-driver-listen-port"></a>

The port number that is used to listen for the SAML response. This value should match the URL with which you configured the SAML-based identity provider (for example, `http://localhost:7890/athena`).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| ListenPort | listen\_port (deprecated) | Optional | 7890 | 

## Identity provider response timeout
<a name="jdbc-v3-driver-single-sign-on-login-url-identity-provider-response-timeout"></a>

The duration, in seconds, before the driver stops waiting for the SAML response from Azure AD.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| IdpResponseTimeout | idp\_response\_timeout (deprecated) | Optional | 120 | 

## Preferred role
<a name="jdbc-v3-driver-single-sign-on-login-url-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PreferredRole | preferred\_role (deprecated) | Optional | none | 

## Role session duration
<a name="jdbc-v3-driver-single-sign-on-login-url-role-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 

## Lake Formation enabled
<a name="jdbc-v3-driver-single-sign-on-login-url-lake-formation-enabled"></a>

Specifies whether to use the [AssumeDecoratedRoleWithSAML](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.html) Lake Formation API action to retrieve temporary IAM credentials instead of the [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) AWS STS API action.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| LakeFormationEnabled | none | Optional | FALSE | 

## Enable token caching
<a name="jdbc-v3-driver-browser-saml-enable-token-caching"></a>

When enabled, caches the SAML assertion in memory across driver connections. This prevents SQL tools that create multiple driver connections from launching multiple browser windows.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| EnableTokenCaching | none | Optional | FALSE | 