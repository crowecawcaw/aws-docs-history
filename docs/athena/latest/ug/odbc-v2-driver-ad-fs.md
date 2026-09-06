

# AD FS
<a name="odbc-v2-driver-ad-fs"></a>

AD FS is a SAML based authentication plugin that works with the Active Directory Federation Service (AD FS) identity provider. The plugin supports [Integrated Windows authentication](https://learn.microsoft.com/en-us/aspnet/web-api/overview/security/integrated-windows-authentication) and form-based authentication. If you use Integrated Windows Authentication, you can omit the user name and password. For information about configuring AD FS and Athena, see [Configure federated access to Amazon Athena for Microsoft AD FS users using an ODBC client](odbc-adfs-saml.md).

## Authentication type
<a name="odbc-v2-driver-authentication-type-8"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=ADFS; | 

## User ID
<a name="odbc-v2-driver-ad-fs-username"></a>

Your user name for connecting to the AD FS server. For Integrated Windows Authentication, you can omit the user name. If your AD FS setup requires a user name, you must provide it in the connection parameter.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UID | Optional for windows integrated authentication | none | UID=domain\\username; | 

## Password
<a name="odbc-v2-driver-ad-fs-password"></a>

Your password for connecting to the AD FS server. Like the user name field, you can omit the user name if you use Integrated Windows Authentication. If your AD FS setup requires a password, you must provide it in the connection parameter.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| PWD | Optional for windows integrated authentication | none | PWD=password\_3EXAMPLE; | 

## Preferred role
<a name="odbc-v2-driver-ad-fs-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has multiple roles, you can specify this parameter to choose the role to be assumed. This role should present in the SAML assertion. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*. 



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:IAM::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-ad-fs-session-duration"></a>

The duration, in seconds, of the role session. For more information about session duration, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## IdP host
<a name="odbc-v2-driver-ad-fs-idp-host"></a>

The name of the AD FS service host.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_host | Require | none | idp\_host=<server-name>.<company.com>; | 

## IdP port
<a name="odbc-v2-driver-ad-fs-idp-port"></a>

The port to use to connect to the AD FS host.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_port | Required | none | idp\_port=443; | 

## LoginToRP
<a name="odbc-v2-driver-ad-fs-logintorp"></a>

The trusted relying party. Use this parameter to override the AD FS relying party endpoint URL.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| LoginToRP | Optional | urn:amazon:webservices | LoginToRP=trustedparty; | 