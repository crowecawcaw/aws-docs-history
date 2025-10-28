# Get started with Amazon Bedrock

Before you can use Amazon Bedrock, you must carry out the following steps:

- Sign up for an AWS account (if you don't already have one).
- Create an AWS Identity and Access Management role with the necessary permissions for Amazon Bedrock.

###### Note

Beginning June 15, 2025 access to all Amazon Bedrock foundation models is enabled by default. For Anthropic models, first-time users may need to submit use case details before they can access the model. For more information, see [Access Amazon Bedrock foundation models](model-access.md "model-access.md").

If you're new to AWS and need to sign up for an AWS account, expand [I'm new to AWS](#new-to-aws "#new-to-aws"). Otherwise, skip that step and instead expand [I already have an AWS account](#getting-started-bedrock-role "#getting-started-bedrock-role").

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").
AWS sends you a confirmation email after the sign-up process isn
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

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
To learn more about IAM, see [Identity and access management for Amazon Bedrock](security-iam.md "security-iam.md") and the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

After you have created an administrative user, proceed to [I already have an AWS account](#getting-started-bedrock-role "#getting-started-bedrock-role") to set up permissions for Amazon Bedrock.

Use IAM to create a role for with the necessary permissions to use Amazon Bedrock. You can then add users to this role to grant the permissions.

###### To create an Amazon Bedrock role

1. Create a role with a name of your choice by following the steps at [Creating a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the IAM User Guide. When you reach the step to attach a policy to the role, attach the [AmazonBedrockFullAccess](security-iam-awsmanpol.md "security-iam-awsmanpol.md") AWS managed policy.
2. Create a new policy to allow your role to manage access to Amazon Bedrock models. From the following list, select the link that corresponds to your method of choice and follow the steps. Use the following JSON object as the policy.
   - [Creating IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md")
   - [Creating IAM policies (AWS CLI)](../../../IAM/latest/UserGuide/access_policies_create-cli.md "../../../IAM/latest/UserGuide/access_policies_create-cli.md")
   - [Creating IAM policies (AWS API)](../../../IAM/latest/UserGuide/access_policies_create-api.md "../../../IAM/latest/UserGuide/access_policies_create-api.md")

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MarketplaceBedrock",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:ViewSubscriptions",
 "aws-marketplace:Unsubscribe",
 "aws-marketplace:Subscribe"
 ],
 "Resource": "*"
 }
 ]
}`

```

3. Attach the policy that you created in the last step to your Amazon Bedrock role by following the steps at [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

###### To add users to the Amazon Bedrock role

1. For users to access an IAM role, you must add them to the role. You can add both users in your account or from other accounts. To grant users permissions to switch to the Amazon Bedrock role that you created, follow the steps at [Granting a user permissions to switch roles](../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md "../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md") and specify the Amazon Bedrock role as the `Resource`.

###### Note

If you need to create more users in your account so that you can give them access to the Amazon Bedrock role, follow the steps in [Creating an IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md"). 2. After you've granted a user permissions to use the Amazon Bedrock role, provide the user with role name and ID or alias of the account to which the role belongs. Then, guide the user through how to switch to the role by following the instructions at [Providing information to the user](../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md#roles-usingrole-giveuser "../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md#roles-usingrole-giveuser").

## Explore Amazon Bedrock features through the console or API

After requesting access to the foundation models that you want to use, you'll be ready to explore the different capabilities offered by Amazon Bedrock.

If you want to familiarize yourself more with Amazon Bedrock first, you can continue to the following pages:

- To learn how to run basic prompts and generate model responses using the **Playgrounds** in the Amazon Bedrock console, continue to [Get started in the Amazon Bedrock console](getting-started-console.md "getting-started-console.md").
- To learn how to set up access to Amazon Bedrock operations through the Amazon Bedrock API and test out some API calls, continue to [Get started with the API](getting-started-api.md "getting-started-api.md").
- To learn about the software development kits (SDKs) supported by Amazon Bedrock, continue to [Using Amazon Bedrock with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
