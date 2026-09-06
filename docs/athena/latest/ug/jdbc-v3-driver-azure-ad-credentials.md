

# Azure AD credentials
<a name="jdbc-v3-driver-azure-ad-credentials"></a>

A SAML-based authentication mechanism that enables authentication to Athena using the Azure AD identity provider. This method assumes that a federation has already been set up between Athena and Azure AD.

**Note**  
Some of the parameter names in this section have aliases. The aliases are functional equivalents of the parameter names and have been provided for backward compatibility with the JDBC 2.x driver. Because the parameter names have been improved to follow a clearer, more consistent naming convention, we recommend that you use them instead of the aliases, which have been deprecated. 

## Credentials provider
<a name="jdbc-v3-driver-azure-ad-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `AzureAD`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | AzureAD | 

## User
<a name="jdbc-v3-driver-azure-ad-user"></a>

The email address of the Azure AD user to use for authentication with Azure AD.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| User | UID (deprecated) | Required | none | 

## Password
<a name="jdbc-v3-driver-azure-ad-password"></a>

The password for the Azure AD user.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Password | PWD (deprecated) | Required | none | 

## Azure AD tenant ID
<a name="jdbc-v3-driver-azure-ad-tenant-id"></a>

The tenant ID of your Azure AD application.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AzureAdTenantId | tenant\_id (deprecated) | Required | none | 

## Azure AD client ID
<a name="jdbc-v3-driver-azure-ad-client-id"></a>

The client ID of your Azure AD application.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AzureAdClientId | client\_id (deprecated) | Required | none | 

## Azure AD client secret
<a name="jdbc-v3-driver-azure-ad-client-secret"></a>

The client secret of your Azure AD application.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AzureAdClientSecret | client\_secret (deprecated) | Required | none | 

## Preferred role
<a name="jdbc-v3-driver-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PreferredRole | preferred\_role (deprecated) | Optional | none | 

## Role session duration
<a name="jdbc-v3-driver-role-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 

## Lake Formation enabled
<a name="jdbc-v3-driver-lake-formation-enabled"></a>

Specifies whether to use the [AssumeDecoratedRoleWithSAML](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.html) Lake Formation API action to retrieve temporary IAM credentials instead of the [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) AWS STS API action.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| LakeFormationEnabled | none | Optional | FALSE | 