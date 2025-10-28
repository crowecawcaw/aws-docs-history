# Setting up AWS TNB

Set up AWS TNB by completing the tasks described in this topic.

###### Tasks

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Choose an AWS Region](#choose-region "#choose-region")
- [Note the service endpoint](#endpoints "#endpoints")
- [(Optional) Install the AWS CLI](#install-aws-cli "#install-aws-cli")
- [Set up AWS TNB roles](#set-service-roles "#set-service-roles")

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

## Choose an AWS Region

To view the list of available Regions for AWS TNB, see the [AWS Regional Services
List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"). To view the list of endpoints for programmatic access, see [AWS TNB endpoints](../../../general/latest/gr/tnb.md "../../../general/latest/gr/tnb.md") in
the _AWS General Reference_.

## Note the service endpoint

To connect programmatically to an AWS service, you use an endpoint. In addition to the
standard AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. For
more information, see [AWS
service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

| Region Name               | Region         | Endpoint                         | Protocol |
| ------------------------- | -------------- | -------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | us-east-1      | tnb.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | tnb.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | tnb.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | tnb.ap-southeast-2.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | tnb.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | tnb.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Paris)            | eu-west-3      | tnb.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | tnb.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | tnb.eu-north-1.amazonaws.com     | HTTPS    |
| South America (São Paulo) | sa-east-1      | tnb.sa-east-1.amazonaws.com      | HTTPS    | ## (Optional) Install the AWS CLI The AWS Command Line Interface (AWS CLI) provides commands for a broad set of AWS products, and is supported on Windows, macOS, and Linux. You can access AWS TNB using the AWS CLI. To get started, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For more information about the commands for AWS TNB, see [tnb](../../../cli/latest/reference/tnb.md "../../../cli/latest/reference/tnb.md") in the _AWS CLI Command Reference_. ## Set up AWS TNB roles You must create a IAM service role to manage different parts of your AWS TNB solution. AWS TNB service roles can make API calls to other AWS services, such as AWS CloudFormation, AWS CodeBuild, and various compute and storage services, on your behalf, to instantiate and manage resources for your deployment. For more information about the AWS TNB service role, see [Identity and access management for AWS TNB](security-iam.md "security-iam.md"). |
