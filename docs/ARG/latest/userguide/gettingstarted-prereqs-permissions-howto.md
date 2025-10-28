# Granting permissions for

using AWS Resource Groups and Tag Editor

To add a policy for using AWS Resource Groups and Tag Editor to a user, do the
following.

1. Open the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. In the navigation pane, choose **Users**.
3. Find the user to whom you want to grant AWS Resource Groups and Tag Editor permissions.
   Choose the user's name to open the user properties page.
4. Choose **Add permissions**.
5. Choose **Attach existing policies directly**.
6. Choose **Create policy**.
7. On the **JSON** tab, paste the following policy
   statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:*",
 "cloudformation:DescribeStacks",
 "cloudformation:ListStackResources",
 "tag:GetResources",
 "tag:TagResources",
 "tag:UntagResources",
 "tag:getTagKeys",
 "tag:getTagValues",
 "resource-explorer:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

This example policy statement grants permissions only for AWS Resource Groups
and Tag Editor actions. It does not allow access to AWS Systems Manager tasks in the
AWS Resource Groups console. For example, this policy does not grant permissions
for you to use Systems Manager Automation commands. To perform Systems Manager tasks on
resource groups, you must have Systems Manager permissions attached to your policy
(such as `ssm:*`). For more information about granting access
to Systems Manager, see [Configuring access
to Systems Manager](../../../systems-manager/latest/userguide/systems-manager-access.md "../../../systems-manager/latest/userguide/systems-manager-access.md") in the _AWS Systems Manager User
Guide_. 8. Choose **Review policy**. 9. Give the new policy a name and description. (for example,
`AWSResourceGroupsQueryAPIAccess`). 10. Choose **Create policy**. 11. Now that the policy is saved in IAM, you can attach it to other users.
For more information about how to add a policy to a user, see [Adding permissions by attaching policies directly to the user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#by-direct-attach-policy "../../../IAM/latest/UserGuide/id_users_change-permissions.md#by-direct-attach-policy")
in the _IAM User Guide_.
