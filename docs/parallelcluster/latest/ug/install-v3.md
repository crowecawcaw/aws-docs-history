# Setting up AWS ParallelCluster

The following topics describe how to set up AWS ParallelCluster. You will learn how to install
the necessary tools and how to use them, how to implement and manage multiple user access to
clusters, and the best practices.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Installing the AWS ParallelCluster command line interface (CLI)](install-v3-parallelcluster.md "install-v3-parallelcluster.md")
- [Steps to take after installation](install-v3-after-install.md "install-v3-after-install.md")
- [Installing the PCUI](install-pcui-v3.md "install-pcui-v3.md")
- [Getting started with AWS ParallelCluster](getting-started-v3.md "getting-started-v3.md")
- [Multiple user access to clusters](multi-user-v3.md "multi-user-v3.md")
- [Best practices](best-practices-v3.md "best-practices-v3.md")
- [Moving from AWS ParallelCluster 2.x to 3.x](moving-from-v2-to-v3.md "moving-from-v2-to-v3.md")

## Prerequisites

Before you can start setting up and using AWS ParallelCluster, make sure that you've completed the following prerequisites.

### Setting up an AWS account

Set up an AWS account to use AWS ParallelCluster.

#### Sign up for an AWS account

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

#### Create a user with administrative access

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

### Create a key pair

To deploy clusters, AWS ParallelCluster launches Amazon EC2 instances to create the cluster head node and compute nodes. To perform cluster tasks,
such as running and monitoring jobs, or managing users, you must be able to access the cluster head node. To verify you can access the head node
instance using SSH, you must use an Amazon EC2 key pair. To learn how to create a key pair, see [Create a key pair](../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair "../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair") in the _Amazon Elastic Compute Cloud_
User Guide for Linux Instances.
