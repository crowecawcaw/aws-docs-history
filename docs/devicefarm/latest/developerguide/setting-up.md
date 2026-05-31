# Setting up AWS Device Farm

Before you use Device Farm for the first time, you must complete the following tasks:

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Step 3: Give the IAM user permission to access Device Farm](#setting-up-permissions "#setting-up-permissions")
- [Next step](#setting-up-next-step "#setting-up-next-step")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

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
