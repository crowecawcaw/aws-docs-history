

# AD FS credentials
<a name="jdbc-v3-driver-adfs-credentials"></a>

A SAML-based authentication mechanism that enables authentication to Athena using Microsoft Active Directory Federation Services (AD FS). This method assumes that the user has already set up a federation between Athena and AD FS.

## Credentials provider
<a name="jdbc-v3-driver-adfs-credentials-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `ADFS`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | ADFS | 

## User
<a name="jdbc-v3-driver-adfs-credentials-user"></a>

The email address of the AD FS user to use for authentication with AD FS.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| User | UID (deprecated) | Required for form-based authentication. Optional for Windows Integrated Authentication. | none | 

## Password
<a name="jdbc-v3-driver-adfs-credentials-password"></a>

The password for the AD FS user.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Password | PWD (deprecated) | Required for form-based authentication. Optional for Windows Integrated Authentication. | none | 

## ADFS host name
<a name="jdbc-v3-driver-adfs-credentials-adfshostname"></a>

The address for your AD FS server.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AdfsHostName | IdP\_Host (deprecated) | Required | none | 

## ADFS port number
<a name="jdbc-v3-driver-adfs-credentials-adfsportnumber"></a>

The port number to use to connect to your AD FS server.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AdfsPortNumber | IdP\_Port (deprecated) | Required | none | 

## ADFS relying party
<a name="jdbc-v3-driver-adfs-credentials-adfsrelyingparty"></a>

The trusted relying party. Use this parameter to override the AD FS relying party endpoint URL.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AdfsRelyingParty | LoginToRP (deprecated) | Optional | urn:amazon:webservices | 

## ADFS WIA enabled
<a name="jdbc-v3-driver-adfs-credentials-adfswiaenabled"></a>

Boolean. Use this parameter to enable Windows Integrated Authentication (WIA) with AD FS.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AdfsWiaEnabled | none | Optional | FALSE | 

## Preferred role
<a name="jdbc-v3-driver-adfs-credentials-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about ARN roles, see [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PreferredRole | preferred\_role (deprecated) | Optional | none | 

## Role session duration
<a name="jdbc-v3-driver-adfs-credentials-role-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 

## Lake Formation enabled
<a name="jdbc-v3-driver-adfs-credentials-lake-formation-enabled"></a>

Specifies whether to use the [`AssumeDecoratedRoleWithSAML`](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.html) Lake Formation API action to retrieve temporary IAM credentials instead of the [`AssumeRoleWithSAML`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) AWS STS API action.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| LakeFormationEnabled | none | Optional | FALSE | 