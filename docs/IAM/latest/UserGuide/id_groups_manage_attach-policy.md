# Attach a policy to an IAM user group

You can attach an [AWS managed
policy](access_policies_managed-vs-inline.md#aws-managed-policies "access_policies_managed-vs-inline.md#aws-managed-policies")—that is, a prewritten policy provided by AWS—to a user group, as
explained in the following steps. To attach a customer managed policy—that is, a policy
with custom permissions that you create—you must first create the policy. For information
about creating customer managed policies, see [Define custom IAM permissions with customer managed
policies](access_policies_create.md "access_policies_create.md").

For more information about permissions and policies, see [Access management for AWS resources](access.md "access.md").

## To attach a policy to an IAM group

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups** and then choose
   the name of the group.
3. Choose the **Permissions** tab.
4. Choose **Add permissions** and then choose **Attach
   policies**.
5. The current policies attached to the user group are displayed in the
   **Current permissions policies** list. In the list of
   **Other permissions policies**, select the check box next to the
   names of the policies to attach. You can use the search box to filter the list of
   policies by type and policy name.
6. Select the policy you want to attach to your IAM group and choose
   **Attach policies**.

AWS CLI
Run the following command:

- `aws iam
attach-group-policy`

API
Call the following operation:

- `AttachGroupPolicy`
