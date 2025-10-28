# Set up prerequisite

permissions

Create a custom policy which includes the following required Resource Groups actions:

- `resource-groups:CreateGroup`
- `resource-groups:DeleteGroup`
- `resource-groups:GetGroupQuery`
- `resource-groups:ListGroupResources`
- `resource-groups:Tag`
- `tag:GetResources`
  For instructions on how to add an inline policy, see [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console"). When you choose the policy
  format, choose the JSON format and add the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:ListGroupResources"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:GetGroupQuery"
 ],
 "Resource": "arn:aws:resource-groups:*:*:group/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:CreateGroup",
 "resource-groups:Tag"
 ],
 "Resource": "arn:aws:resource-groups:*:*:group/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "sagemaker:collection"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "resource-groups:DeleteGroup",
 "Resource": "arn:aws:resource-groups:*:*:group/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:collection": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "tag:GetResources",
 "Resource": "*"
 }
 ]
}`

```
