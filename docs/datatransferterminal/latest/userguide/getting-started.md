# Getting started

Get started with making remote data transfers to your AWS Cloud services by making a reservation at one of the Data Transfer Terminal facilities. To begin, you’ll need equipment that is supported by the Data Transfer Terminal facility and an AWS Enterprise account.

Review the [Technical requirements for using Data Transfer Terminal](tech-requirements.md "tech-requirements.md") section of this guide before scheduling a Data Transfer Terminal reservation to ensure you have equipment with the optimal configurations for the data transfer. Not all data storage devices and network connection equipment is compatible with the fiber optic network connections available in the suites.

When you sign up for AWS, your AWS account is automatically signed up for all services in AWS, including Data Transfer Terminal. You are charged only for the services that you use.

To set up Data Transfer Terminal, use the steps in the following sections.

When you sign up for AWS and set up Data Transfer Terminal, you can optionally change the display language in the AWS Management Console. For more information, see [Changing the language of the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md#change-language "../../../awsconsolehelpdocs/latest/gsg/getting-started.md#change-language") in the _AWS Management Console Getting Started Guide_.

Once you have an AWS account you can access Data Transfer Terminal. For more information about setting up and using AWS Data Transfer Terminal, see [Schedule a Data Transfer Terminal reservation](setting-up.md "setting-up.md").

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

1. Open https://portal.aws.amazon.com/billing/signup.
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is complete. At any time, you can view your current account activity and manage your account by going to https://aws.amazon.com/ and choosing **My Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you don’t use the root user for everyday tasks.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_. 3. Enable IAM Identity Center.

For instructions, see [Enabling AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the _AWS IAM Identity Center User Guide_. 4. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the _AWS IAM Identity Center User Guide_. 5. To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_. 6. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 7. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.
