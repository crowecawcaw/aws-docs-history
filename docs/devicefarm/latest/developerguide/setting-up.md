# Setting up AWS Device Farm

Before you use Device Farm for the first time, you must complete the following tasks:

###### Topics

- [Step 1: Sign up for AWS](#setting-up-sign-up "#setting-up-sign-up")
- [Step 2: Create or use an IAM user in your AWS account](#setting-up-iam "#setting-up-iam")
- [Step 3: Give the IAM user permission to access Device Farm](#setting-up-permissions "#setting-up-permissions")
- [Next step](#setting-up-next-step "#setting-up-next-step")

## Step 1: Sign up for AWS

Sign up for Amazon Web Services (AWS).

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Step 2: Create or use an IAM user in your AWS account

We recommend that you do not use your AWS root account to access Device Farm. Instead, create an AWS Identity and Access Management
(IAM) user (or use an existing one) in your AWS account, and then access Device Farm with that IAM
user.

For more information, see [Creating an IAM User (AWS Management Console)](../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console "../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console").

## Step 3: Give the IAM user permission to access Device Farm

Give the IAM user permission to access Device Farm. To do this, create an access policy in IAM, and then
assign the access policy to the IAM user, as follows.

###### Note

The AWS root account or IAM user that you use to complete the following steps must have permission
to create the following IAM policy and attach it to the IAM user. For more information, see [Working with Policies](../../../IAM/latest/UserGuide/policies_manage.md "../../../IAM/latest/UserGuide/policies_manage.md").

1. Create a policy with the following JSON body. Give it a descriptive title, such as
   `DeviceFarmAdmin`.

For more information on creating IAM policies, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
IAM User Guide. 2. Attach the IAM policy you created to your new user. For more information on attaching IAM
policies to users, see [Adding and Removing IAM
Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the IAM User Guide.

Attaching the policy provides the IAM user with access to all Device Farm actions and resources associated
with that IAM user. For information about how to restrict IAM users to a limited set of Device Farm actions
and resources, see [Identity and access management in AWS Device Farm](security-iam.md "security-iam.md").

## Next step

You are now ready to start using Device Farm. See [Getting started with Device Farm](getting-started.md "getting-started.md").
