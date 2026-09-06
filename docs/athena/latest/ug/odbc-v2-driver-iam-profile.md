

# IAM profile
<a name="odbc-v2-driver-iam-profile"></a>

You can configure a named profile to connect to Amazon Athena using the ODBC driver. You can use a named profile with one of the following credential sources:
+ `Ec2InstanceMetadata` – Retrieves credentials from the Amazon EC2 Instance Metadata Service (IMDS). Use this when running on an Amazon EC2 instance.
+ `EcsContainer` – Retrieves credentials from the Amazon ECS Task Role endpoint. Use this when running in an Amazon ECS container.
+ `Environment` – Retrieves credentials from environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`).

Set the `credential_source` parameter in your AWS profile configuration to the appropriate value for your environment. If you want to use a custom credentials provider in a named profile, specify a value for the `plugin_name` parameter in your profile configuration.

## Authentication type
<a name="odbc-v2-driver-iam-profile-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=IAM Profile; | 

## AWS profile
<a name="odbc-v2-driver-iam-profile-aws-profile"></a>

The profile name to use for your ODBC connection. For more information about profiles, see [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) in the *AWS Command Line Interface User Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AWSProfile | Required | none | AWSProfile=default; | 

## Preferred role
<a name="odbc-v2-driver-iam-profile-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. The preferred role parameter is used when the custom credentials provider is specified by the `plugin_name` parameter in your profile configuration. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*. 



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:IAM::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-iam-profile-session-duration"></a>

The duration, in seconds, of the role session. For more information about session duration, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*. The session duration parameter is used when the custom credentials provider is specified by the `plugin_name` parameter in your profile configuration.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## Plugin name
<a name="odbc-v2-driver-iam-profile-plugin-name"></a>

Specifies the name of a custom credentials provider used in a named profile. This parameter can take the same values as those in the **Authentication Type** field of the ODBC Data Source Administrator, but is used only by `AWSProfile` configuration.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| plugin\_name | Optional | none | plugin\_name=AzureAD; | 