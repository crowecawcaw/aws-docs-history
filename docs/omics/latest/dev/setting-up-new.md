AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Setting up HealthOmics

To set up AWS HealthOmics, sign up for an AWS account,
create an administrative user, and securely manage access for additional users.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Create IAM permissions for HealthOmics](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [Connect with external code repositories](#setting-up-omics-repository "#setting-up-omics-repository")
- [Using Amazon Q CLI with HealthOmics](#setting-up-omics-q-cli "#setting-up-omics-q-cli")

## Sign up for an AWS account

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

## Create a user with administrative access

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

## Create IAM permissions for HealthOmics

To use HealthOmics, configure the following IAM permissions:

- IAM identity-based policies for users in your account to access HealthOmics.
- An IAM service role for HealthOmics to access resources on your behalf.
- Permissions in other services (such as Lake Formation and Amazon ECR) for your users and the HealthOmics service to access
  resources.

For more information about configuring IAM permissions for HealthOmics, see [IAM permissions for HealthOmics](omics-permissions.md "omics-permissions.md").

## Connect with external code repositories

With AWS HealthOmics, you can manage your workflows using Git-based repositories through AWS CodeConnections. HealthOmics
uses this connection to access your source code repositories.

Before working with external code repositories, follow the
[Setting up connections](../../../dtconsole/latest/userguide/setting-up-connections.md "../../../dtconsole/latest/userguide/setting-up-connections.md")
guide to start working with AWS CodeConnections. Verify that you have created the proper IAM policies and
permissions for your AWS account. For a list of supported Git providers and more information, see
[What third-party providers can I create connections for?](../../../dtconsole/latest/userguide/welcome-connections-supported-providers.md "../../../dtconsole/latest/userguide/welcome-connections-supported-providers.md").

**Create a connection**

To create a connection with your preferred repository provider, follow the
[Create a connection](../../../dtconsole/latest/userguide/connections-create.md "../../../dtconsole/latest/userguide/connections-create.md") tutorial.

## Using Amazon Q CLI with HealthOmics

Amazon Q CLI provides natural language interactions with AWS HealthOmics, allowing you to perform complex
genomic workflows and analysis tasks using conversational commands. To use Amazon Q CLI, be sure to
configure IAM permissions for HealthOmics and other services (such as CloudWatch, Amazon ECR, or Amazon S3) for Amazon Q to
access their resources.

The [HealthOmics Agentic
generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai") provides a step-by-step guidance for configuring context files and enabling
Amazon Q CLI to create, run, and optimize your AWS HealthOmics workflows.
