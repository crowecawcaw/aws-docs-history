# Setting up account access for Route 53 Global Resolver

Before you start using Route 53 Global Resolver, you need an AWS account and the appropriate permissions to
access Route 53 Global Resolver resources. This includes creating IAM users and roles with the necessary
permissions.

This section guides you through the steps required to configure users and roles to access
Route 53 Global Resolver.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Creating policies and roles](#gr-setting-up-permissions "#gr-setting-up-permissions")
- [Network considerations](#gr-setting-up-network "#gr-setting-up-network")

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

## Creating policies and roles

Configure AWS Identity and Access Management (IAM) permissions so your team can deploy and
manage Route 53 Global Resolver resources. You can use administrative permissions for full access or read-only
permissions for monitoring and viewing configurations.

All Route 53 Global Resolver API operations require appropriate IAM permissions. If you don't have the
required permissions, API calls will return `AccessDeniedException` (401) or
`UnauthorizedException` (401) errors.

### Administrative permissions

If you're setting up Route 53 Global Resolver for the first time or managing all aspects of the service,
you need administrative permissions. You can use these AWS managed policies:

- `AmazonRoute53GlobalResolverFullAccess` - Provides full access to Route 53 Global Resolver
  resources, including creating, updating, and deleting global resolvers, DNS views, firewall
  rules, and domain lists
- `AmazonRoute53FullAccess` - Required if you plan to use private hosted zone
  forwarding
- `CloudWatchLogsFullAccess` - Required if you plan to send logs to
  Amazon CloudWatch
- `AmazonS3FullAccess` - Required if you plan to import firewall domain lists
  from Amazon S3 or send logs to Amazon S3

### Read-only permissions

If you only need to view Route 53 Global Resolver configurations and logs, you can use these AWS managed
policies:

- `AmazonRoute53GlobalResolverReadOnlyAccess` - Provides read-only access to
  Route 53 Global Resolver resources, including viewing global resolvers, DNS views, firewall rules, domain
  lists, and access sources
- `AmazonRoute53ReadOnlyAccess` - Required to view private hosted zone
  associations
- `CloudWatchReadOnlyAccess` - Required to view logs in Amazon CloudWatch
- `AmazonS3ReadOnlyAccess` - Required to view firewall domain list files stored
  in Amazon S3

## Network considerations

Before implementing Route 53 Global Resolver, consider the following network requirements:

Client IP ranges

This is only required when using access source-based authentication. Identify the IP address ranges (CIDR blocks) for all clients that will use Route 53 Global Resolver.
You'll need these for configuring rules for your access source.

DNS protocols

Determine which DNS protocols your clients will use:

- **Do53** - Standard DNS over port 53 (UDP/TCP)
- **DoH** - DNS-over-HTTPS for encrypted queries
- **DoT** - DNS-over-TLS for encrypted queries

Firewall and security groups

Ensure your network firewalls and security groups allow outbound traffic to Route 53 Global Resolver
anycast IP addresses on the appropriate ports (53 for Do53, 443 for DoH, 853 for DoT).
