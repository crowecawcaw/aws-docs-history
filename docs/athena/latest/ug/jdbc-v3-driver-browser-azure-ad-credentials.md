

# Browser Azure AD credentials
<a name="jdbc-v3-driver-browser-azure-ad-credentials"></a>

Browser Azure AD is a SAML-based authentication mechanism that works with the Azure AD identity provider and supports multi-factor authentication. Unlike the standard Azure AD authentication mechanism, this mechanism does not require a user name, password, or client secret in the connection parameters. Like the standard Azure AD authentication mechanism, Browser Azure AD also assumes the user has already set up federation between Athena and Azure AD.

## Credentials provider
<a name="jdbc-v3-driver-browser-azure-ad-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `BrowserAzureAD`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | BrowserAzureAD | 

## Azure AD tenant ID
<a name="jdbc-v3-driver-browser-azure-ad-azure-ad-tenant-id"></a>

The tenant ID of your Azure AD application



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AzureAdTenantId | tenant\_id (deprecated) | Required | none | 

## Azure AD client ID
<a name="jdbc-v3-driver-browser-azure-ad-azure-ad-client-id"></a>

The client ID of your Azure AD application



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AzureAdClientId | client\_id (deprecated) | Required | none | 

## Identity provider response timeout
<a name="jdbc-v3-driver-identity-provider-response-timeout"></a>

The duration, in seconds, before the driver stops waiting for the SAML response from Azure AD.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| IdpResponseTimeout | idp\_response\_timeout (deprecated) | Optional | 120 | 

## Preferred role
<a name="jdbc-v3-driver-browser-azure-ad-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| PreferredRole | preferred\_role (deprecated) | Optional | none | 

## Role session duration
<a name="jdbc-v3-driver-browser-azure-ad-role-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 

## Lake Formation enabled
<a name="jdbc-v3-driver-browser-azure-ad-lake-formation-enabled"></a>

Specifies whether to use the [AssumeDecoratedRoleWithSAML](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.html) Lake Formation API action to retrieve temporary IAM credentials instead of the [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) AWS STS API action.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| LakeFormationEnabled | none | Optional | FALSE | 

## Enable token caching
<a name="jdbc-v3-driver-browser-azure-ad-enable-token-caching"></a>

When enabled, caches the SAML assertion in memory across driver connections. This prevents SQL tools that create multiple driver connections from launching multiple browser windows.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| EnableTokenCaching | none | Optional | FALSE | 