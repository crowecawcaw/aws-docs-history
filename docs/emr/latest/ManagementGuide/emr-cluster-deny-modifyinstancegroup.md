# Denying the

ModifyInstanceGroup action in Amazon EMR

The [ModifyInstanceGroups](../APIReference/API_ModifyInstanceGroups.md "../APIReference/API_ModifyInstanceGroups.md") action in Amazon EMR does not require that you provide
a cluster ID with the action. Instead, you can specify only an instance group ID.
For this reason, an apparently simple deny policy for this action based on cluster
ID or a cluster tag may not have the intended effect. Consider the following example
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Sid": "AllowELASTICMAPREDUCEModifyinstancegroups"
 },
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Deny",
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:cluster/j-12345ABCDEFG67"
 ],
 "Sid": "DenyELASTICMAPREDUCEModifyinstancegroups"
 }
 ]
}`

```

If a user with this policy attached performs a `ModifyInstanceGroup`
action and specifies only the instance group ID, the policy does not apply. Because
the action is allowed on all other resources, the action is successful.

A solution to this issue is to attach a policy statement to the identity that uses
a [NotResource](../../../IAM/latest/UserGuide/reference_policies_elements_notresource.md "../../../IAM/latest/UserGuide/reference_policies_elements_notresource.md") element to deny any `ModifyInstanceGroup` action
issued without a cluster ID. The following example policy adds such a deny statement
so that any `ModifyInstanceGroups` request fails unless a cluster ID is
specified. Because an identity must specify a cluster ID with the action, deny
statements based on cluster ID are therefore effective.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Sid": "AllowELASTICMAPREDUCEModifyinstancegroups"
 },
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Deny",
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:cluster/j-12345ABCDEFG67"
 ],
 "Sid": "DenyELASTICMAPREDUCEModifyinstancegroupsSpecificCluster"
 },
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Deny",
 "NotResource": "arn:*:elasticmapreduce:*:*:cluster/*",
 "Sid": "DenyELASTICMAPREDUCEModifyinstancegroupsNonCluster"
 }
 ]
}`

```

A similar issue exists when you want to deny the `ModifyInstanceGroups`
action based on the value associated with a cluster tag. The solution is similar. In
addition to a deny statement that specifies the tag value, you can add a policy
statement that denies the `ModifyInstanceGroup` action if the tag that
you specify is not present, regardless of value.

The following example demonstrates a policy that, when attached to an identity,
denies the identity the `ModifyInstanceGroups` action any cluster with
the tag `department` set to `dev`. This statement is only
effective because of the deny statement that uses the `StringNotLike`
condition to deny the action unless the `department` tag is
present.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Sid": "AllowELASTICMAPREDUCEModifyinstancegroups"
 },
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "dev"
 }
 },
 "Effect": "Deny",
 "Resource": [
 "*"
 ],
 "Sid": "DenyELASTICMAPREDUCEModifyinstancegroupsDevDepartment"
 },
 {
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups"
 ],
 "Condition": {
 "StringNotLike": {
 "aws:ResourceTag/department": "?*"
 }
 },
 "Effect": "Deny",
 "Resource": [
 "*"
 ],
 "Sid": "DenyELASTICMAPREDUCEModifyinstancegroupsNoDepartmentTag"
 }
 ]
}`

```
