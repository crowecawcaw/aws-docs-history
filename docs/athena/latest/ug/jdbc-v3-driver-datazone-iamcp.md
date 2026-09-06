

# SageMaker IAM Credentials Provider
<a name="jdbc-v3-driver-datazone-iamcp"></a>

An authentication plugin that uses IAM credentials to connect to Amazon Athena through SageMaker Unified Studio. This plugin authenticates using IAM credentials (static access key/secret key or the AWS default credential chain) and retrieves Athena connection credentials via the SageMaker connection service.

## Credentials provider
<a name="jdbc-v3-driver-datazone-iamcp-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `SageMakerIam`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated), DataZoneIam | Required | none | SageMakerIam | 

## DataZone domain identifier
<a name="jdbc-v3-driver-datazone-iamcp-datazone-domain-identifier"></a>

Identifier of the DataZone domain to use.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneDomainId | none | Required | none | 

## DataZone project identifier
<a name="jdbc-v3-driver-datazone-iamcp-datazone-project-identifier"></a>

Identifier of the DataZone project to use.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneProjectId | none | Optional | none | 

## DataZone environment identifier
<a name="jdbc-v3-driver-datazone-iamcp-datazone-environment-identifier"></a>

Identifier of the DataZone environment to use. Required if `DataZoneProjectId` is not specified.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneEnvironmentId | none | Optional | none | 

## DataZone domain region
<a name="jdbc-v3-driver-datazone-iamcp-datazone-domain-region"></a>

The AWS Region where your DataZone domain is provisioned.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneDomainRegion | none | Required | none | 

## DataZone endpoint override
<a name="jdbc-v3-driver-datazone-iamcp-datazone-endpoint-override"></a>

The DataZone API endpoint to use instead of the endpoint default for the provided AWS Region.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| DataZoneEndpointOverride | none | Optional | none | 

## User
<a name="jdbc-v3-driver-datazone-iamcp-user"></a>

Your AWS access key ID. For more information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| User | AccessKeyId | Optional | none | 

## Password
<a name="jdbc-v3-driver-datazone-iamcp-password"></a>

Your AWS secret key ID. For more information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Password | SecretAccessKey | Optional | none | 