**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up your account to use the services

This topic describes preliminary steps, such as creating an account, to prepare you to
use AWS WAF, AWS Firewall Manager, and AWS Shield Advanced. You aren't charged for these preliminary
items. You are charged only for AWS services that you use.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Download tools](#setting-up-waf-tools "#setting-up-waf-tools")

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

## Download tools

The AWS Management Console includes a console for AWS WAF, AWS Shield Advanced, and AWS Firewall Manager, but if you want to access the services
programmatically, see the following:

- The API guides document the operations that the services support and provide links to the related SDK and CLI documentation:
  - [AWS WAF API Reference](../APIReference.md "../APIReference.md")
  - [AWS Shield Advanced API Reference](../DDOSAPIReference.md "../DDOSAPIReference.md")
  - [AWS Firewall Manager API Reference](../../../fms/2018-01-01/APIReference/Welcome.md "../../../fms/2018-01-01/APIReference/Welcome.md")

- To call an API without having to handle low-level details like
  assembling raw HTTP requests, you can use an AWS SDK. The AWS SDKs provide
  functions and data types that encapsulate the functionality of AWS services.
  To download an AWS SDK and access installation instructions, see the applicable page:

      + [Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")
      + [JavaScript](http://aws.amazon.com/sdkforbrowser/ "http://aws.amazon.com/sdkforbrowser/")
      + [.NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/")
      + [Node.js](https://aws.amazon.com/sdk-for-node-js/ "https://aws.amazon.com/sdk-for-node-js/")
      + [PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/")
      + [Python](https://github.com/boto/boto "https://github.com/boto/boto")
      + [Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/")

  For a complete list of AWS SDKs, see [Tools for
  Amazon Web Services](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/").

- You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services
  from the command line. You can also automate your commands using scripts. For more information,
  see [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").
- AWS Tools for Windows PowerShell supports these AWS services. For more information, see [AWS Tools for PowerShell Cmdlet Reference](http://aws.amazon.com/documentation/powershell/ "http://aws.amazon.com/documentation/powershell/").
