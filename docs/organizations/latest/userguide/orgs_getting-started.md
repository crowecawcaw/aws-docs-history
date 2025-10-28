# Getting started with AWS Organizations

The following topics provide information to help you start using
AWS Organizations. You can also use the following tutorials to begin performing tasks using AWS Organizations.

[Tutorial: Creating and configuring an
organization](orgs_tutorials_basic.md "orgs_tutorials_basic.md")

Get up and running with step-by-step instructions to create your organization,
invite your first member accounts, create an OU hierarchy that contains your
accounts, and apply some service control policies (SCPs).

[Tutorial: Monitor important changes to your
organization with Amazon EventBridge](orgs_tutorials_cwe.md "orgs_tutorials_cwe.md")

Monitor key changes in your organization by configuring Amazon EventBridge to trigger
an alarm in the form of an email, SMS text message, or log entry when actions
that you designate occur in your organization. For example, many organizations
want to know when a new account is created or when an account attempts to leave
the organization.

###### Topics

- [Signing up for AWS](#getting-started-signing-up "#getting-started-signing-up")
- [Accessing AWS Organizations](#how-to-access "#how-to-access")
- [Tutorial: Creating and configuring an
  organization](orgs_tutorials_basic.md "orgs_tutorials_basic.md")
- [Tutorial: Monitor an organization with Amazon EventBridge](orgs_tutorials_cwe.md "orgs_tutorials_cwe.md")
- [Working with AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md")

## Signing up for AWS

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")

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

## Accessing AWS Organizations

You can work with AWS Organizations in any of the following ways:

**AWS Management Console**

The [AWS Organizations console](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/") is a
browser-based interface that you can use to manage your organization and
your AWS resources. You can perform any task in your organization by using
the console.

**AWS Command Line Tools**

With the AWS command line tools, you can issue commands at your system's
command line to perform AWS Organizations and AWS tasks. Working with the command
line can be faster and more convenient than using the console. The command
line tools also are useful if you want to build scripts that perform AWS
tasks.

AWS provides two sets of command line tools:

- [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")

The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.
With just one tool to download and configure,
you can control multiple AWS services from the command line and automate them through scripts.

For
information about installing and using the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

- [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/ "https://aws.amazon.com/powershell/")

The Tools for Windows PowerShell let developers and administrators manage their AWS services
and resources in the PowerShell scripting environment.
You can manage your AWS resources with the same PowerShell tools you use to manage your Windows, Linux, and MacOS environments.

For
information about installing and using the Tools for Windows PowerShell, see the [AWS Tools for PowerShell User Guide](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md").

**AWS SDKs**

The AWS SDKs consist of libraries and sample code for various
programming languages and platforms (for example, Java, Python, Ruby, .NET,
iOS, and Android). The SDKs take care of tasks such as cryptographically
signing requests, managing errors, and retrying requests automatically. For
more information about the AWS SDKs, including how to download and install
them, see [Tools for Amazon Web
Services](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk").

**AWS Organizations HTTPS Query API**

The AWS Organizations HTTPS Query API gives you programmatic access to AWS Organizations and
AWS. The HTTPS Query API lets you issue HTTPS requests directly to the
service. When you use the HTTPS API, you must include code to digitally sign
requests using your credentials. For more information, see [Calling the API by Making
HTTP Query Requests](orgs_query-requests.md "orgs_query-requests.md") and the [AWS Organizations API Reference](../APIReference.md "../APIReference.md").
