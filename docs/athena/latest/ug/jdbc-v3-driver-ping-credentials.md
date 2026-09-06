

# Ping credentials
<a name="jdbc-v3-driver-ping-credentials"></a>

A SAML-based authentication mechanism that enables authentication to Athena using the Ping Federate identity provider. This method assumes that a federation has already been set up between Athena and Ping Federate.

## Credentials provider
<a name="jdbc-v3-driver-ping-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `Ping`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | Ping | 

## User
<a name="jdbc-v3-driver-ping-user"></a>

The email address of the Ping Federate user to use for authentication with Ping Federate.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| User | UID (deprecated) | Required | none | 

## Password
<a name="jdbc-v3-driver-ping-password"></a>

The password for the Ping Federate user.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Password | PWD (deprecated) | Required | none | 

## PingHostName
<a name="jdbc-v3-driver-ping-host-name"></a>

The address for your Ping server. To find your address, visit the following URL and view the **SSO Application Endpoint** field.

```
https://your-pf-host-#:9999/pingfederate/your-pf-app#/spConnections
```



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PingHostName | IdP\_Host (deprecated) | Required | none | 

## PingPortNumber
<a name="jdbc-v3-driver-ping-port-number"></a>

The port number to use to connect to your IdP host.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PingPortNumber | IdP\_Port (deprecated) | Required | none | 

## PingPartnerSpId
<a name="jdbc-v3-driver-ping-partner-spid"></a>

The service provider address. To find the service provider address, visit the following URL and view the **SSO Application Endpoint** field.

```
https://your-pf-host-#:9999/pingfederate/your-pf-app#/spConnections
```



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PingPartnerSpId | Partner\_SPID (deprecated) | Required | none | 

## Preferred role
<a name="jdbc-v3-driver-ping-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PreferredRole | preferred\_role (deprecated) | Optional | none | 

## Role session duration
<a name="jdbc-v3-driver-role-ping-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 

## Lake Formation enabled
<a name="jdbc-v3-driver-ping-lake-formation-enabled"></a>

Specifies whether to use the [AssumeDecoratedRoleWithSAML](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.html) Lake Formation API action to retrieve temporary IAM credentials instead of the [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) AWS STS API action.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| LakeFormationEnabled | none | Optional | FALSE | 