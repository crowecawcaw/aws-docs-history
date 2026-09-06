

# Browser SSO OIDC
<a name="odbc-v2-driver-browser-sso-oidc"></a>

Browser SSO OIDC is an authentication plugin that works with AWS IAM Identity Center. For information on enabling and using IAM Identity Center, see [Step 1: Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-enable-identity-center.html) in the *AWS IAM Identity Center User Guide*.

**Note**  
**v2.1.0.0 security update:** Starting in version 2.1.0.0, the BrowserSSOOIDC plugin uses Authorization Code with PKCE instead of Device Code Authorization for improved security. This change eliminates the device code display step and provides faster authentication. A new `listen_port` parameter (default 7890) is used for the OAuth 2.0 callback server. You may need to allowlist this port on your network. The default scope has changed to `sso:account:access`.

## Authentication type
<a name="odbc-v2-driver-browser-sso-oidc-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=BrowserSSOOIDC; | 

## IAM Identity Center Start URL
<a name="odbc-v2-driver-browser-sso-oidc-sso-start-url"></a>

The URL for the AWS access portal. The IAM Identity Center [RegisterClient](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_RegisterClient.html) API action uses this value for the `issuerUrl` parameter.

**To copy the AWS access portal URL**

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. In the navigation pane, choose **Settings**.

1. On the **Settings** page, under **Identity source**, choose the clipboard icon for **AWS access portal URL**.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_start\_url | Required | none | sso\_oidc\_start\_url=https://app\_id.awsapps.com/start; | 

## IAM Identity Center Region
<a name="odbc-v2-driver-browser-sso-oidc-sso-region"></a>

The AWS Region where your SSO is configured. The `SSOOIDCClient` and `SSOClient` AWS SDK clients use this value for the `region` parameter.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_region | Required | none | sso\_oidc\_region=us-east-1; | 

## Scopes
<a name="odbc-v2-driver-browser-sso-oidc-scopes"></a>

The list of scopes that are defined by the client. Upon authorization, this list restricts permissions when an access token is granted. The IAM Identity Center [RegisterClient](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_RegisterClient.html) API action uses this value for the `scopes` parameter.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_scopes | Optional | sso:account:access | sso\_oidc\_scopes=sso:account:access; | 

## Account ID
<a name="odbc-v2-driver-browser-sso-oidc-account-id"></a>

The identifier for the AWS account that is assigned to the user. The IAM Identity Center [GetRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html) API uses this value for the `accountId` parameter.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_account\_id | Required | none | sso\_oidc\_account\_id=123456789123; | 

## Role name
<a name="odbc-v2-driver-browser-sso-oidc-role-name"></a>

The friendly name of the role that is assigned to the user. The name that you specify for this permission set appears in the AWS access portal as an available role. The IAM Identity Center [GetRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html) API action uses this value for the `roleName` parameter.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_role\_name | Required | none | sso\_oidc\_role\_name=AthenaReadAccess; | 

## Timeout
<a name="odbc-v2-driver-browser-sso-oidc-timeout"></a>

The number of seconds the polling SSO API should check for the access token.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_timeout | Optional | 120 | sso\_oidc\_timeout=60; | 

## Listen port
<a name="odbc-v2-driver-browser-sso-oidc-listen-port"></a>

The local port number to use for the OAuth 2.0 callback server. This is used as the redirect URI and you may need to allowlist this port on your network. The default generated redirect URI is: `http://127.0.0.1:7890/oauth/callback`. This parameter was added in v2.1.0.0 as part of the migration from Device Code to Authorization Code with PKCE.

**Warning**  
In shared environments like Windows Terminal Servers or Remote Desktop Services, the loopback port (default: 7890) is shared among all users on the same machine. System administrators can mitigate potential port hijacking risks by:  
Configuring different port numbers for different user groups
Using Windows security policies to restrict port access
Implementing network isolation between user sessions



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| listen\_port | Optional | 7890 | listen\_port=8080; | 

## Enable file cache
<a name="odbc-v2-driver-browser-sso-oidc-file-cache"></a>

Enables a temporary credentials cache. This connection parameter enables temporary credentials to be cached and reused between multiple processes. Use this option to reduce the number of opened browser windows when you use BI tools such as Microsoft Power BI.

**Note**  
Starting in v2.1.0.0, cached credentials are stored as plaintext JSON in the `user-profile/.athena-odbc/` directory with file permissions restricted to the owning user, consistent with how the AWS CLI protects locally stored credentials.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| sso\_oidc\_cache | Optional | 1 | sso\_oidc\_cache=0; | 