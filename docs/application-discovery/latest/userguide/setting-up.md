

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Setting up Application Discovery Service
<a name="setting-up"></a>

Before you use AWS Application Discovery Service for the first time, complete the following tasks:
+ [Create IAM users](#setting-up-iam)
+ [Sign in to the Migration Hub console and choose a home Region](#setting-up-choose-home-region)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create IAM users
<a name="setting-up-iam"></a>

**Topics**
+ [Creating an IAM Non-Administrative User](#setting-up-iam-non-admin)

### Creating an IAM Non-Administrative User
<a name="setting-up-iam-non-admin"></a>

When creating non-administrative IAM users, follow the security best practice [ Grant Least Privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), granting users minimum permissions. 

Use IAM managed policies to define the level of access to Application Discovery Service by non-administrative IAM users. For information about Application Discovery Service managed policies, see [AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md).

**To create a non-administrator IAM user**

1. In AWS Management Console, navigate to the IAM console.

1. Create a non-administrator IAM user by following the instructions for creating a user with the console as described in [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in the *IAM User Guide*. 

   While following the instructions in the *IAM User Guide*:
   + When on the step about the **Set permissions** page, choose the option to **Attach existing policies to user directly**. Then select a managed IAM policy for Application Discovery Service from the list of policies. For information about Application Discovery Service managed policies, see [AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md).
   + When on the step about viewing the user's access keys (access key IDs and secret access keys), follow the guidance in the **Important** note about saving the user's new access key ID and secret access key in a safe and secure place. 

1. After you create the user provide them with programmatic access as described in [Support programmatic user access](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html?icmpid=docs_iam_console#gs-get-keys).

## Sign in to the Migration Hub console and choose a home Region
<a name="setting-up-choose-home-region"></a>

You need to choose an AWS Migration Hub home Region in the AWS account that you're using for the AWS Application Discovery Service.

**To choose a home Region**

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane, choose **Settings** and the choose a home Region. 

   Your Migration Hub data is stored in your home Region for purposes of discovery, planning, and migration tracking. For more information, see [The Migration Hub Home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/home-region.html). 