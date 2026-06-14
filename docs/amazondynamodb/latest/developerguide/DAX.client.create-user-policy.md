# Step 2: Create a user and policy

In this step, you create a user with a policy that grants access to your Amazon
DynamoDB Accelerator (DAX) cluster and to DynamoDB using AWS Identity and Access Management. You can then run applications
that interact with your DAX cluster.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter or paste a JSON policy document. For details about the IAM policy language, see
[IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md"). 6. Resolve any security warnings, errors, or general warnings generated during [policy validation](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md"), and then choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON
or YAML policy template that you can use in CloudFormation templates.

To do this, in the **Policy editor** choose
**Actions**, and then choose **Generate CloudFormation
template**. To learn more about CloudFormation, see [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_. 8. When you are finished adding permissions to the policy, choose
**Next**. 9. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 10. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 11. Choose **Create policy** to save your new policy.

**Policy document** – Copy and paste the following document to
create the JSON policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "dax:*"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 },
 {
 "Action": [
 "dynamodb:*"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
