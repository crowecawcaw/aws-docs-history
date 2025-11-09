**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Step 1: Before You Begin with Amazon Glacier

Before you can start with this exercise, you must sign up for an AWS account (if you don't already have one), and then download one of the AWS SDKs. See the following sections for instructions.

###### Topics

- [Set Up an AWS account and an Administrator User](#setup "#setup")
- [Download the Appropriate AWS SDK](#getting-started-download-sdk "#getting-started-download-sdk")

## Set Up an AWS account and an Administrator User

If you have not already done so, you must sign up for an AWS account and create an
administrator user in the account.

To complete the setup, follow the instructions in the following topics.

### Set Up an AWS account and Create an Administrator

User

#### Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up for all services in AWS, including Amazon Glacier. You are charged only for the services that you use. For more information about Amazon Glacier usage rates, see the [Amazon Glacier pricing page](https://aws.amazon.com/s3/glacier/pricing/ "https://aws.amazon.com/s3/glacier/pricing/").

If you already have an AWS account, skip to [Download the Appropriate AWS SDK](#getting-started-download-sdk "#getting-started-download-sdk"). If you don't have an AWS account, use the following procedure to create one.

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                      | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM<br>users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |

## Download the Appropriate AWS SDK

To try the getting started exercise, you must decide which programming language you want to
use, and then download the appropriate AWS SDK for your development
platform.

The getting started exercise provides examples in Java and C#.

### Downloading the

AWS SDK for Java

To test the Java examples in this developer guide, you need the AWS SDK for Java.
You have the following download options:

- If you are using Eclipse, you can download and install the AWS Toolkit for Eclipse by using the update
  site [http://aws.amazon.com/eclipse/](http://aws.amazon.com/eclipse/ "http://aws.amazon.com/eclipse/"). For more information, see
  [AWS Toolkit for Eclipse](http://aws.amazon.com/eclipse/ "http://aws.amazon.com/eclipse/").
- If you are using any other IDE to create your application, download
  the [AWS SDK for Java](http://aws.amazon.com/sdkforjava "http://aws.amazon.com/sdkforjava").

### Downloading the

AWS SDK for .NET

To test the C# examples in this developer guide, you need the AWS SDK for .NET. You
have the following download options:

- If you are using Visual Studio, you can install both the AWS SDK for .NET and the AWS Toolkit for Visual Studio.
  The toolkit provides AWS Explorer for Visual Studio and project
  templates that you can use for development. To download the AWS SDK for .NET,
  go to [http://aws.amazon.com/sdkfornet](http://aws.amazon.com/sdkfornet/ "http://aws.amazon.com/sdkfornet/"). By default, the installation
  script installs both the AWS SDK and the AWS Toolkit for Visual Studio. To learn more
  about the toolkit, see the [AWS Toolkit for Visual Studio User Guide](../../../AWSToolkitVS/latest/UserGuide.md "../../../AWSToolkitVS/latest/UserGuide.md").
- If you are using any other IDE to create your application, you can use the same link
  provided in the preceding step and install only the AWS SDK for .NET.
