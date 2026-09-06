

# SageMaker Browser IDC Credentials Provider
<a name="jdbc-v3-driver-datazone-idc"></a>

An authentication plugin that connects to Amazon Athena through SageMaker Unified Studio. It opens a browser for AWS Identity and Access Management Identity Center sign-in using the OAuth 2.0 Authorization Code flow with PKCE, then exchanges the resulting token for temporary credentials scoped to your SageMaker Unified Studio domain and Athena project environment.

For information on enabling and using IAM Identity Center, see [Step 1: Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-enable-identity-center.html) in the *AWS IAM Identity Center User Guide*.

**Note**  
This plugin is designed for single-user desktop environments. In shared environments like Windows Terminal Servers or Remote Desktop Services, system administrators are responsible for establishing and maintaining security boundaries between users.

## Credentials provider
<a name="jdbc-v3-driver-datazone-idc-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `SageMakerBrowserIdc`. Note that the `AWSCredentialsProviderClass` alias is deprecated; use the `CredentialsProvider` parameter name instead.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated), DataZoneIdc | Required | none | SageMakerBrowserIdc | 

## DataZone domain identifier
<a name="jdbc-v3-driver-datazone-idc-datazone-domain-identifier"></a>

Identifier of the DataZone domain to use.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneDomainId | none | Required | none | 

## DataZone project identifier
<a name="jdbc-v3-driver-datazone-idc-datazone-project-identifier"></a>

Identifier of the DataZone project to use.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneProjectId | none | Optional | none | 

## DataZone environment identifier
<a name="jdbc-v3-driver-datazone-idc-datazone-environment-identifier"></a>

Identifier of the DataZone environment to use. Required if `DataZoneProjectId` is not specified.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneEnvironmentId | none | Optional | none | 

## DataZone domain region
<a name="jdbc-v3-driver-datazone-idc-datazone-domain-region"></a>

The AWS Region where your DataZone domain is provisioned.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneDomainRegion | none | Required | none | 

## Region
<a name="jdbc-v3-driver-datazone-idc-region"></a>

The AWS Region where your DataZone environment and Athena workgroup are provisioned.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Region | none | Required | none | 

## IAM Identity Center issuer URL
<a name="jdbc-v3-driver-datazone-idc-iam-identity-center-issuer-url"></a>

The issuer URL of the IAM Identity Center instance that the DataZone domain uses.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| IdentityCenterIssuerUrl | none | Required | none | 

## DataZone endpoint override
<a name="jdbc-v3-driver-datazone-idc-datazone-endpoint-override"></a>

The DataZone API endpoint to be used instead of the default for the provided AWS Region.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneEndpointOverride | none | Optional | none | 

## Enable token caching
<a name="jdbc-v3-driver-datazone-idc-enable-token-caching"></a>

When enabled, allows the same IAM Identity Center access token to be used across driver connections. This prevents SQL tools that create multiple driver connections from launching multiple browser windows. If you enable this parameter, we recommend that you close the SQL tool immediately after using it to clear the token cache and require re-authentication.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| EnableTokenCaching | none | Optional | FALSE | 

## Listen port
<a name="jdbc-v3-driver-datazone-idc-listen-port"></a>

The port number that listens for the IAM Identity Center response.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| ListenPort | none | Optional | 8000 | 

## Identity provider response time out
<a name="jdbc-v3-driver-datazone-idc-identity-provider-response-time-out"></a>

The duration, in seconds, before the driver stops waiting for the response from IAM Identity Center.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| IdpResponseTimeout | none | Optional | 120 | 