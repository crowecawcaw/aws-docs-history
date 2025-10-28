# Setting up Amazon Managed Blockchain (AMB) Access Bitcoin

Before you use Amazon Managed Blockchain (AMB) Access Bitcoin for the first time, follow the steps in this section to create an AWS account. The following chapter discusses how to start using AMB Access Bitcoin.

## Prerequisites and

considerations

Before you use AWS for the first time, you must have an AWS account.

### Sign up for AWS

When you sign up for AWS, your AWS account is automatically signed up for all AWS services, including Amazon Managed Blockchain (AMB) Access Bitcoin. You're charged only for the services that you use.

If you have an AWS account already, go to the next step. If you don't have an
AWS account, use the following procedure to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create an IAM user with appropriate permissions

To create and work with AMB Access Bitcoin, you must have an AWS Identity and Access Management (IAM) principal (user or group) with permissions that allow necessary Managed Blockchain actions.

Only IAM principals can make Bitcoin JSON-RPC calls. When making calls to the Bitcoin JSON-RPCs on Amazon Managed Blockchain, you
can do so over an HTTPS connection authenticated using the [Signature Version 4 signing
process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). This means that only authorized IAM principals in the AWS
account can make Bitcoin JSON-RPC calls. To do this, AWS credentials
(an access key ID and a secret access key) must be provided with the call.

For information about how to create an IAM user, see [Creating an IAM user in your AWS
account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md"). For more information about how to attach a permissions policy to a user, see
[Changing
permissions for an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md"). For an example of a permissions policy
that you can use to give a user permission to work with AMB Access Bitcoin, see [Identity-based policy
examples for Amazon Managed Blockchain (AMB) Access Bitcoin](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Install and configure the

AWS Command Line Interface

If you have not already done so, install the latest AWS Command-Line Interface (CLI) to
work with AWS resources from a terminal. For more information, see [Installing or updating the latest version
of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

For CLI access, you need an access key ID and a secret access key.
Use temporary credentials instead of long-term access keys when possible.
Temporary credentials include an access key ID, a secret access key, and a
security token that indicates when the credentials expire. For more information,
see [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.
