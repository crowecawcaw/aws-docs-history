

# SageMaker IAM
<a name="odbc-v2-driver-sagemaker-iam"></a>

An authentication plugin that uses IAM credentials to connect to Amazon Athena through SageMaker Unified Studio. This plugin authenticates using IAM credentials (static access key/secret key or the AWS default credential chain) and retrieves Athena environment credentials via the SageMaker connection service.

## Authentication Type
<a name="odbc-v2-driver-sagemaker-iam-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | none | AuthenticationType=SageMakerIam; | 

## SageMaker domain ID
<a name="odbc-v2-driver-sagemaker-iam-domain-id"></a>

The identifier of the SageMaker domain to use.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| SageMakerDomainId | Required | none | SageMakerDomainId=d-abcdef1234; | 

## SageMaker project ID
<a name="odbc-v2-driver-sagemaker-iam-project-id"></a>

The identifier of the SageMaker project to use.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| SageMakerProjectId | Required | none | SageMakerProjectId=p-abcdef1234; | 

## SageMaker domain region
<a name="odbc-v2-driver-sagemaker-iam-domain-region"></a>

The AWS Region where your SageMaker domain is provisioned.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| SageMakerDomainRegion | Required | none | SageMakerDomainRegion=us-east-1; | 

## User ID
<a name="odbc-v2-driver-sagemaker-iam-user-id"></a>

Your AWS access key ID. If not specified, the driver uses the AWS default credential chain. For more information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UID | Optional | none | UID=AKIAIOSFODNN7EXAMPLE; | 

## Password
<a name="odbc-v2-driver-sagemaker-iam-password"></a>

Your AWS secret access key. Required if `UID` is specified.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| PWD | Optional | none | PWD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY; | 