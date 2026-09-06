

# Browser Azure AD
<a name="odbc-v2-driver-browser-azure-ad"></a>

Browser Azure AD is a SAML based authentication plugin that works with Azure AD identity provider and supports multi-factor authentication. Unlike the standard Azure AD plugin, this plugin does not require a user name, password, or client secret in the connection parameters.

**Note**  
**v2.1.0.0 security update:** Starting in v2.1.0.0, the BrowserAzureAD plugin includes PKCE (Proof Key for Code Exchange) in the OAuth 2.0 authorization flow. This prevents authorization code interception attacks on shared systems. No configuration changes are required.

## Authentication Type
<a name="odbc-v2-driver-browser-azure-ad-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=BrowserAzureAD; | 

## Preferred role
<a name="odbc-v2-driver-browser-azure-ad-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has multiple roles, you can specify this parameter to choose the role to be assumed. The role specified should be present in the SAML assertion. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.

 



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:IAM::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-browser-azure-ad-session-duration"></a>

The duration, in seconds, of the role session. For more information about session duration, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## Tenant ID
<a name="odbc-v2-driver-browser-azure-ad-tenant-id"></a>

Specifies your application tenant ID.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_tenant | Required | none | idp\_tenant=123zz112z-z12d-1z1f-11zz-f111aa111234; | 

## Client ID
<a name="odbc-v2-driver-browser-azure-ad-client-id"></a>

Specifies your application client ID.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| client\_id | Required | none | client\_id=9178ac27-a1bc-1a2b-1a2b-a123abcd1234; | 

## Timeout
<a name="odbc-v2-driver-browser-azure-ad-timeout"></a>

The duration, in seconds, before the plugin stops waiting for the SAML response from Azure AD.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| timeout | Optional | 120 | timeout=90; | 

## Enable Azure file cache
<a name="odbc-v2-driver-browser-azure-ad-file-cache"></a>

Enables a temporary credentials cache. This connection parameter enables temporary credentials to be cached and reused between multiple processes. Use this option to reduce the number of opened browser windows when you use BI tools such as Microsoft Power BI.

**Note**  
Starting in v2.1.0.0, cached credentials are stored as plaintext JSON in the `user-profile/.athena-odbc/` directory with file permissions restricted to the owning user, consistent with how the AWS CLI protects locally stored credentials.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| browser\_azure\_cache | Optional | 1 | browser\_azure\_cache=0; | 