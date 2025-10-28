# Managing custom Amazon SNS IAM policies

Custom IAM policies allow you to specify permissions for individual IAM users, groups,
or roles, granting or restricting access to specific AWS resources and actions.
When managing Amazon SNS resources, custom IAM policies allow you to tailor access permissions
according to your organization's security and operational requirements.

Use the following steps to manage custom IAM policies for Amazon SNS:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. From the navigation pane, choose **Policies**.
3. To create a new custom IAM policy, choose **Create policy** and
   choose **SNS**. To edit an existing policy, select the
   policy from the list and choose **Edit policy**.
4. In the policy editor, define the **permissions** for accessing Amazon SNS
   resources. You can specify **actions**, **resources**,
   and **conditions** based on your specific requirements.
5. To grant permissions for Amazon SNS actions, include relevant Amazon SNS actions such as
   `sns:Publish`, `sns:Subscribe`, and `sns:DeleteTopic`
   in your IAM policy. Define the ARN (Amazon Resource Name) of the Amazon SNS topics to which
   the permissions apply.
6. Specify the IAM **users**, **groups**, or
   **roles** to which the policy should be attached. You can attach the
   policy directly to IAM users or groups, or associate it with IAM roles used by
   AWS services or applications.
7. Review the IAM policy configuration to ensure it aligns with your access control
   requirements. Once verified, **save** the policy changes.
8. Attach the **custom IAM policy** to the relevant IAM users,
   groups, or roles within your AWS account. This grants them the permissions defined in
   the policy for managing Amazon SNS resources.
