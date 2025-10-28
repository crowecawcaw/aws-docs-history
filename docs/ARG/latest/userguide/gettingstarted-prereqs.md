# Prerequisites for working with AWS Resource Groups

Before you get started working with resource groups, be sure you have an active AWS
account with existing resources and appropriate rights to tag resources and create
groups.

###### Topics

- [Sign up for AWS](#gettingstarted-prereqs-signup "#gettingstarted-prereqs-signup")
- [Create resources](#gettingstarted-prereqs-create "#gettingstarted-prereqs-create")
- [Set up permissions](gettingstarted-prereqs-permissions.md "gettingstarted-prereqs-permissions.md")

## Sign up for AWS

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create resources

You can create an empty resource group, but won't be able to perform any tasks on
resource group members until there are resources in the group. For more information
about the supported resource types, see [Resource types you can use with AWS Resource Groups and
Tag Editor](supported-resources.md "supported-resources.md").
