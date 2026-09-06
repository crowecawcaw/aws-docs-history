

# Setting up DynamoDB (web service)
<a name="SettingUp.DynamoWebService"></a>

 To use the Amazon DynamoDB web service: 

1.  [Sign up for an AWS account](#sign-up-for-aws) 

1.  [Configure your credentials](#SettingUp.DynamoWebService.ConfigureCredentials) (used to access DynamoDB programmatically). 
**Note**  
 If you plan to interact with DynamoDB only through the AWS Management Console, you don't need an AWS access key, and you can skip ahead to [Using the console](AccessingDynamoDB.md#ConsoleDynamoDB). 

## Signing up for AWS
<a name="SettingUp.DynamoWebService.SignUpForAWS"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Configuring your credentials
<a name="SettingUp.DynamoWebService.ConfigureCredentials"></a>

 Before you can access DynamoDB programmatically or through the AWS CLI, you must configure your credentials to enable authorization for your applications. 

 There are several ways to do this. For example, you can manually create the credentials file to store your access key ID and secret access key. You also can use the AWS CLI command `aws configure` to automatically create the file. Alternatively, you can use environment variables. For more information about configuring your credentials, see the programming-specific AWS SDK developer guide.

 To install and configure the AWS CLI, see [Using the AWS CLI](AccessingDynamoDB.md#Tools.CLI). 

## Integrating with other DynamoDB services
<a name="w2aab9c17b9c11"></a>

You can integrate DynamoDB with many other AWS services. For more information, see the following: 
+ [Using DynamoDB with other AWS services](OtherServices.md)
+ [CloudFormation for DynamoDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html)
+ [Using AWS Backup with DynamoDB](backuprestore_HowItWorksAWS.md)
+ [AWS Identity and Access Management (IAM) and DynamoDB](identity-and-access-mgmt.md)
+ [Using AWS Lambda with Amazon DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html)