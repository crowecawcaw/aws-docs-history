

# Azure AD
<a name="odbc-v2-driver-azure-ad"></a>

Azure AD is a SAML-based authentication plugin that works with Azure AD identity provider. This plugin does not support multifactor authentication (MFA). If you require MFA support, consider using the `BrowserAzureAD` plugin instead.

## Authentication Type
<a name="odbc-v2-driver-azure-ad-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=AzureAD; | 

## User ID
<a name="odbc-v2-driver-azure-ad-username"></a>

Your user name for connecting to Azure AD.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UID | Required | none | UID=jane.doe@example.com; | 

## Password
<a name="odbc-v2-driver-azure-ad-password"></a>

Your password for connecting to Azure AD.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| PWD | Required | none | PWD=password\_3EXAMPLE; | 

## Preferred role
<a name="odbc-v2-driver-azure-ad-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:iam::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-azure-ad-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## Tenant ID
<a name="odbc-v2-driver-azure-ad-tenent-id"></a>

Specifies your application tenant ID.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_tenant | Required | none | idp\_tenant=123zz112z-z12d-1z1f-11zz-f111aa111234; | 

## Client ID
<a name="odbc-v2-driver-azure-ad-client-id"></a>

Specifies your application client ID.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| client\_id | Required | none | client\_id=9178ac27-a1bc-1a2b-1a2b-a123abcd1234; | 

## Client secret
<a name="odbc-v2-driver-azure-ad-client-secret"></a>

Specifies your client secret.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| client\_secret | Required | none | client\_secret=zG12q\~.xzG1xxxZ1wX1.\~ZzXXX1XxkHZizeT1zzZ; | 