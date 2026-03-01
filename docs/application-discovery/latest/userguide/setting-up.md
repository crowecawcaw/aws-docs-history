AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Setting up Application Discovery Service

Before you use AWS Application Discovery Service for the first time, complete the following tasks:

- [Sign up for Amazon Web Services](#setting-up-signup "#setting-up-signup")
- [Create IAM users](#setting-up-iam "#setting-up-iam")
- [Sign in to the Migration Hub console and choose a home Region](#setting-up-choose-home-region "#setting-up-choose-home-region")

## Sign up for Amazon Web Services

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create IAM users

When you create an AWS account, you get a single sign-in identity that has complete
access to all of the AWS services and resources in the account. This identity is
called the AWS account _root user_. Signing in to the
AWS Management Console using the email address and password that you used to create the account gives
you complete access to all of the AWS resources in your account.

We strongly recommend that you _not_ use the root
user for everyday tasks, even the administrative ones. Instead, follow the security best
practice [Create
Individual IAM Users](../../../IAM/latest/UserGuide/best-practices.md#create-iam-users "../../../IAM/latest/UserGuide/best-practices.md#create-iam-users") and create an AWS Identity and Access Management (IAM) administrator user.
Then securely lock away the root user credentials and use them to perform only a few
account and service management tasks.

In addition to creating an administrative user you'll also need to create
non-administrative IAM users. The following topics explain how to create both types of
IAM users.

###### Topics

- [Creating an IAM Administrative User](#setting-up-iam-admin "#setting-up-iam-admin")
- [Creating an IAM Non-Administrative User](#setting-up-iam-non-admin "#setting-up-iam-non-admin")

### Creating an IAM Administrative User

By default, an administrator account inherits all of the policies required for
accessing Application Discovery Service.

###### To create an administrator user

- Create an administrator user in your AWS account. For instructions, see
  [Creating Your First IAM User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
  _IAM User Guide_.

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
