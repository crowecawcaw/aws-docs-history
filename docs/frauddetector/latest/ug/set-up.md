

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Set up for Amazon Fraud Detector
<a name="set-up"></a>

To use Amazon Fraud Detector, you first need an Amazon Web Services (AWS) account and then you must set up permissions that give your AWS account access to all interfaces. Later when you start to create your Amazon Fraud Detector resources, you need to grant permissions that allow Amazon Fraud Detector to access your account to perform tasks on your behalf and to access resources that you own. 

Complete the following tasks in this section to get set up for using Amazon Fraud Detector:
+ Sign up for AWS.
+ Set up permissions that allows your AWS account to access Amazon Fraud Detector interfaces.
+ Set up interfaces you want to use to access Amazon Fraud Detector.

After you complete these steps, see [Get started with Amazon Fraud Detector](get-started.md) to continue getting started with Amazon Fraud Detector.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Set up permissions to access Amazon Fraud Detector interfaces
<a name="set-up-iam-admin"></a>

To use Amazon Fraud Detector, set up permissions to access the Amazon Fraud Detector console and API operations. 

Following security best practice create an AWS Identity and Access Management (IAM) user with access restricted to Amazon Fraud Detector operations and with required permissions. You can add other permissions as needed.

The following policies provide the required permission to use Amazon Fraud Detector:
+ `AmazonFraudDetectorFullAccessPolicy`

  Allows you to perform the following actions:
  + Access all Amazon Fraud Detector resources
  + List and describe all model endpoints in SageMaker AI
  + List all IAM roles in the account
  + List all Amazon S3 buckets
  + Allow IAM Pass Role to pass a role to Amazon Fraud Detector 
+ `AmazonS3FullAccess`

  Allows full access to Amazon Simple Storage Service. This is required if you need to upload training datasets to Amazon S3.

The following describes how to create an IAM user and assign the needed permissions.

**To create a user and assign required permissions**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users** and then choose **Add user**.

1. For **User name**, enter **AmazonFraudDetectorUser**.

1. Select the **AWS Management Console access** check box, and then configure the user password.

1. (Optional) By default, AWS requires the new user to create a new password when they ﬁrst sign in. You can clear the check box next to **User must create a new password at next sign-in** to allow the new user to reset their password after they sign in.

1. Choose **Next: Permissions**.

1. Choose **Create group**.

1. For **Group name** enter **AmazonFraudDetectorGroup**.

1. In the policy list, select the check box for **AmazonFraudDetectorFullAccessPolicy** and **AmazonS3FullAccess**. Choose **Create group**.

1. In the list of groups, select the check box for your new group. Choose **Refresh** if you don't see the group in the list.

1. Choose **Next: Tags**.

1. (Optional) Add metadata to the user by attaching tags as key-value pairs. For instructions on how to use tags in IAM, see [Tagging IAM Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html).

1. Choose **Next: Review** to see the **User details** and **Permissions summary** for the new user. When you're ready to proceed, choose **Create user**.

## Set up interfaces to access Amazon Fraud Detector with
<a name="set-up-interfaces"></a>

You can access Amazon Fraud Detector using the Amazon Fraud Detector console, AWS CLI, or AWS SDK. Before you can use them, first set up the AWS CLI and AWS SDK.

### Access Amazon Fraud Detector console
<a name="access-console"></a>

You can access the Amazon Fraud Detector console and other AWS services through the AWS Management Console. Your AWS account, grants you access to the AWS Management Console. 

**To access Amazon Fraud Detector console,**

1. Go to [https://console.aws.amazon.com](https://console.aws.amazon.com) and sign in to your AWS account.

1. Navigate to Amazon Fraud Detector.

With Amazon Fraud Detector console, you can create and manage your models and your fraud detection resources such as Detectors, Variables, Events, Entities, Labels, and Outcomes. You can generate predictions and evaluate the performance and predictions of your model.

### Set up AWS CLI
<a name="set-up-cli"></a>

You can use AWS Command Line Interface (AWS CLI) to interact with Amazon Fraud Detector by running commands in your command line shell. With minimal configuration, you can use the AWS CLI to run commands for similar functionality to that provided by the Amazon Fraud Detector console from the command prompt in your terminal.

**To set up the AWS CLI**

Download and configure the AWS CLI. For instructions, see the following topics in the AWS Command Line Interface User Guide:
+ [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)
+ [Configuring the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

For information about Amazon Fraud Detector commands, see [Available Commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html)

### Set up AWS SDK
<a name="set-up-sdk"></a>

You can use the AWS SDKs to write code for creating and managing your fraud detection resources and for getting fraud predictions. The AWS SDKs support Amazon Fraud Detector in [JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/FraudDetector.html) and [Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html).

**To set up AWS SDK for Python (Boto3)**

You can use AWS SDK for Python (Boto3) to create, configure, and manage AWS services. For instructions on how to install Boto, see [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). Make sure that you're using Boto3 SDK version 1.14.29 or higher.

After you install AWS SDK for Python (Boto3), run the following Python example to confirm that your environment is configured correctly. If it's configured correctly, the response contains a list of detectors. If no detectors were created, the list is empty.

```
import boto3
fraudDetector = boto3.client('frauddetector')
            
response = fraudDetector.get_detectors()
print(response)
```

**To set up AWS SDKs for Java**

For instructions on how to install and load the AWS SDK for JavaScript, see [Setting up the SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-up.html).