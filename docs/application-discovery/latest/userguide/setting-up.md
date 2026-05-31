AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Setting up Application Discovery Service

Before you use AWS Application Discovery Service for the first time, complete the following tasks:

- [Create IAM users](#setting-up-iam "#setting-up-iam")
- [Sign in to the Migration Hub console and choose a home Region](#setting-up-choose-home-region "#setting-up-choose-home-region")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Create IAM users

###### Topics

- [Creating an IAM Non-Administrative User](#setting-up-iam-non-admin "#setting-up-iam-non-admin")

### Creating an IAM Non-Administrative User

When creating non-administrative IAM users, follow the security best practice
[Grant
Least Privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"), granting users minimum permissions.

Use IAM managed policies to define the level of access to Application Discovery Service by
non-administrative IAM users. For information about Application Discovery Service managed policies, see
[AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### To create a non-administrator IAM user

1. In AWS Management Console, navigate to the IAM console.
2. Create a non-administrator IAM user by following the instructions for
   creating a user with the console as described in [Creating an IAM user
   in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the
   _IAM User Guide_.

While following the instructions in the
_IAM User Guide_:

    * When on the step about the **Set permissions**
     page, choose the option to **Attach existing policies to
     user directly**. Then select a managed IAM policy for
     Application Discovery Service from the list of policies. For information about Application Discovery Service
     managed policies, see [AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
    * When on the step about viewing the user's access keys (access key
     IDs and secret access keys), follow the guidance in the
     **Important** note about saving the user's new
     access key ID and secret access key in a safe and secure place.

3. After you create the user provide them with programmatic access as described in
   [Support programmatic user access](../../../IAM/latest/UserGuide/introduction_identity-management.md#gs-get-keys "../../../IAM/latest/UserGuide/introduction_identity-management.md#gs-get-keys").

## Sign in to the Migration Hub console and choose a home Region

You need to choose an AWS Migration Hub home Region in the AWS account that you're using
for the AWS Application Discovery Service.

###### To choose a home Region

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub
   console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane, choose **Settings**
   and the choose a home Region.

Your Migration Hub data is stored in your home Region for purposes of discovery,
planning, and migration tracking. For more information, see [The
Migration Hub Home Region](../../../migrationhub/latest/ug/home-region.md "../../../migrationhub/latest/ug/home-region.md").
