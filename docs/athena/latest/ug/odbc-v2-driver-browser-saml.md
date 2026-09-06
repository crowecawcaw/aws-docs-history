

# Browser SAML
<a name="odbc-v2-driver-browser-saml"></a>

Browser SAML is a generic authentication plugin that can work with SAML based identity providers and support multi-factor authentication. For detailed configuration information, see [Configure single sign-on using ODBC, SAML 2.0, and the Okta Identity Provider](okta-saml-sso.md).

**Note**  
**v2.1.0.0 security update:** Starting in v2.1.0.0, the BrowserSAML plugin includes CSRF protection via RelayState validation. The driver generates a random state token, includes it as a RelayState parameter in the login URL, and validates it against the received response before accepting SAML assertions.

## Authentication type
<a name="odbc-v2-driver-browser-saml-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=BrowserSAML; | 

## Preferred role
<a name="odbc-v2-driver-browser-saml-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has multiple roles, you can specify this parameter to choose the role to be assumed. This role should be present in the SAML assertion. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:IAM::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-browser-saml-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## Login URL
<a name="odbc-v2-driver-browser-saml-login-url"></a>

The single sign-on URL that is displayed for your application.

**Important**  
Starting in v2.1.0.0, the login URL must use HTTP or HTTPS protocol with a valid authority. The driver validates the URL format before initiating the authentication flow.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| login\_url | Required | none | login\_url=https://trial-1234567.okta.com/app/trial-1234567\_oktabrowsersaml\_1/zzz4izzzAzDFBzZz1234/sso/saml; | 

## Listen port
<a name="odbc-v2-driver-browser-saml-listen-port"></a>

The port number that is used to listen for the SAML response. This value should match the IAM Identity Center URL that you configured the IdP with (for example, `http://localhost:7890/athena`).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| listen\_port | Optional | 7890 | listen\_port=7890; | 

## Timeout
<a name="odbc-v2-driver-browser-saml-timeout"></a>

The duration, in seconds, before the plugin stops waiting for the SAML response from the identity provider.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| timeout | Optional | 120 | timeout=90; | 