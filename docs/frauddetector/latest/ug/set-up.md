Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Set up for Amazon Fraud Detector

To use Amazon Fraud Detector, you first need an Amazon Web Services (AWS) account and then you must set up permissions that give your AWS account access to all interfaces.
Later when you start to create your Amazon Fraud Detector resources, you need to grant permissions that allow Amazon Fraud Detector to access your account to perform tasks on your behalf and to access resources that you own.

Complete the following tasks in this section to get set up for using Amazon Fraud Detector:

- Sign up for AWS.
- Set up permissions that allows your AWS account to access Amazon Fraud Detector interfaces.
- Set up interfaces you want to use to access Amazon Fraud Detector.
  After you complete these steps, see [Get started with Amazon Fraud Detector](get-started.md "get-started.md") to continue getting started with Amazon Fraud Detector.

## Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up for all
services on AWS, including Amazon Fraud Detector. You're charged only for the services that you use. If you already have an AWS account, skip
to the next task.

### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Set up permissions to access Amazon Fraud Detector interfaces

To use Amazon Fraud Detector, set up permissions to access the Amazon Fraud Detector console and API operations.

Following security best practice create an AWS Identity and Access Management (IAM) user with access restricted to Amazon Fraud Detector operations
and with required permissions. You can add other permissions as needed.

The following policies provide the required permission to use Amazon Fraud Detector:

- `AmazonFraudDetectorFullAccessPolicy`

Allows you to perform the following actions:

    + Access all Amazon Fraud Detector resources
    + List and describe all model endpoints in SageMaker AI
    + List all IAM roles in the account
    + List all Amazon S3 buckets
    + Allow IAM Pass Role to pass a role to Amazon Fraud Detector

- `AmazonS3FullAccess`

Allows full access to Amazon Simple Storage Service. This is required if you need to upload training datasets to Amazon S3.

The following describes how to create an IAM user and assign the needed permissions.

###### To create a user and assign required permissions

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** and then choose
   **Add user**.
3. For **User name**, enter `AmazonFraudDetectorUser`.
4. Select the **AWS Management Console access** check box, and then
   configure the user password.
5. (Optional) By default, AWS requires the new user to create a new password when
   they ﬁrst sign in. You can clear the check box next to **User must create a new
   password at next sign-in** to allow the new user to reset their
   password after they sign in.
6. Choose **Next: Permissions**.
7. Choose **Create group**.
8. For **Group name** enter `AmazonFraudDetectorGroup`.
9. In the policy list, select the check box for **AmazonFraudDetectorFullAccessPolicy** and **AmazonS3FullAccess**. Choose **Create group**.
10. In the list of groups, select the check box for your new group. Choose
    **Refresh** if you don't see the group in the list.
11. Choose **Next: Tags**.
12. (Optional) Add metadata to the user by attaching tags as key-value pairs. For
    instructions on how to use tags in IAM, see [Tagging IAM Users and Roles](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md").
13. Choose **Next: Review** to see the **User details** and
    **Permissions summary** for the new user. When
    you're ready to proceed, choose **Create user**.

## Set up interfaces to access Amazon Fraud Detector with

You can access Amazon Fraud Detector using the Amazon Fraud Detector console, AWS CLI, or AWS SDK.
Before you can use them, first set up the AWS CLI and AWS SDK.

### Access Amazon Fraud Detector console

You can access the Amazon Fraud Detector console and other AWS services through the AWS Management Console.
Your AWS account, grants you access to the AWS Management Console.

###### To access Amazon Fraud Detector console,

1. Go to [https://console.aws.amazon.com](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your AWS account.
2. Navigate to Amazon Fraud Detector.

With Amazon Fraud Detector console, you can create and manage your models and your fraud detection
resources such as Detectors, Variables, Events, Entities,
Labels, and Outcomes. You can generate predictions and evaluate
the performance and predictions of your model.

### Set up AWS CLI

You can use AWS Command Line Interface (AWS CLI) to interact with Amazon Fraud Detector by running commands in your command line shell. With minimal configuration,
you can use the AWS CLI to run commands for similar functionality to that provided by the Amazon Fraud Detector console from the command prompt in your
terminal.

**To set up the AWS CLI**

Download and configure the AWS CLI. For instructions, see the following topics in the AWS Command Line Interface User Guide:

- [Getting Set Up with the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md")
- [Configuring the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")

For information about Amazon Fraud Detector commands, see [Available Commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html")

### Set up AWS SDK

You can use the AWS SDKs to write code for creating and managing your fraud detection resources and for getting fraud predictions.
The AWS SDKs support Amazon Fraud Detector in [JavaScript](../../../AWSJavaScriptSDK/latest/AWS/FraudDetector.md "../../../AWSJavaScriptSDK/latest/AWS/FraudDetector.md") and [Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html").

**To set up AWS SDK for Python (Boto3)**

You can use AWS SDK for Python (Boto3) to create, configure, and manage AWS services. For instructions
on how to install Boto, see [AWS
SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html"). Make sure that you're using Boto3 SDK version 1.14.29 or higher.

After you install AWS SDK for Python (Boto3), run the following Python example to confirm that your environment is configured correctly. If
it's configured correctly, the response contains a list of detectors. If no detectors
were created, the list is empty.

```

import boto3
fraudDetector = boto3.client('frauddetector')

response = fraudDetector.get_detectors()
print(response)

```

**To set up AWS SDKs for Java**

For instructions on how to install and load the
AWS SDK for JavaScript, see [Setting up the SDK for JavaScript](../../../sdk-for-javascript/v3/developer-guide/setting-up.md "../../../sdk-for-javascript/v3/developer-guide/setting-up.md").
