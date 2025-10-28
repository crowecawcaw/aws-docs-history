# IAM policies for tag-based

access to clusters and EMR notebooks

You can use conditions in your identity-based policy to control access to clusters
and EMR notebooks based on tags.

For more information about adding tags to clusters, see [Tagging EMR clusters](emr-plan-tags.md "emr-plan-tags.md").

The following examples demonstrate different scenarios and ways to use condition
operators with Amazon EMR condition keys. These IAM policy statements are intended for
demonstration purposes only and should not be used in production environments. There
are multiple ways to combine policy statements to grant and deny permissions
according to your requirements. For more information about planning and testing
IAM policies, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

###### Important

Explicitly denying permission for tagging actions is an important
consideration. This prevents users from tagging a resource and thereby granting
themselves permissions that you did not intend to grant. If you don't deny
tagging actions for a resource, a user can modify tags and circumvent the
intention of the tag-based policies.

## Example identity-based policy

statements for clusters

The following examples demonstrate identity-based permissions policies that
are used to control the actions that are allowed with EMR clusters.

###### Important

The `ModifyInstanceGroup` action in Amazon EMR does not require that
you specify a cluster ID. For that reason, denying this action based on
cluster tags requires additional consideration. For more information, see
[Denying the
ModifyInstanceGroup action in Amazon EMR](emr-cluster-deny-modifyinstancegroup.md "emr-cluster-deny-modifyinstancegroup.md").

###### Topics

- [Allow actions only on
  clusters with specific tag values](#emr-cluster-access-example-tagvalue "#emr-cluster-access-example-tagvalue")
- [Require cluster
  tagging when a cluster is created](#emr-cluster-access-example-require-tagging "#emr-cluster-access-example-require-tagging")
- [Allow actions on clusters
  with a specific tag, regardless of tag value](#emr-cluster-access-example-tag "#emr-cluster-access-example-tag")

### Allow actions only on

clusters with specific tag values

The following examples demonstrate a policy that allows a user to perform
actions based on the cluster tag `department` with the value `dev` and also allows
a user to tag clusters with that same tag. The final policy example
demonstrates how to deny privileges to tag EMR clusters with anything but
that same tag.

In the following policy example, the `StringEquals` condition operator tries to match `dev` with the value
for the tag `department`. If the tag `department` hasn't
been added to the cluster, or doesn't contain the value `dev`, the policy
doesn't apply, and the actions aren't allowed by this policy. If no other
policy statements allow the actions, the user can only work with clusters
that have this tag with this value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt12345678901234",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListSteps",
 "elasticmapreduce:TerminateJobFlows",
 "elasticmapreduce:SetTerminationProtection",
 "elasticmapreduce:ListInstances",
 "elasticmapreduce:ListInstanceGroups",
 "elasticmapreduce:ListBootstrapActions",
 "elasticmapreduce:DescribeStep"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/department": "dev"
 }
 }
 }
 ]
}`

```

You can also specify multiple tag values using a condition operator. For
example, to allow all actions on clusters where the `department` tag contains the value
`dev` or `test`, you could
replace the condition block in the earlier example with the following.

```
            "Condition": {
              "StringEquals": {
                "elasticmapreduce:ResourceTag/department":["dev", "test"]
              }
            }

```

### Require cluster

tagging when a cluster is created

As in the prior example, the following policy example looks for the same
matching tag: the value `dev` for the `department` tag. But
in this example, the `RequestTag` condition
key specifies that the policy applies during tag creation. So you must
create a cluster with a tag that matches the specified value.

To create a cluster with a tag, you must also have permission for the
`elasticmapredue:AddTags` action. For this
statement, the `elasticmapreduce:ResourceTag`
condition key ensures that IAM only grants access to tag resources with
the value `dev` on
the `department`
tag. The `Resource` element is used to limit
this permission to cluster resources.

For the `PassRole` resources, you must
provide the AWS account ID or alias, the service role name in the `PassRoleForEMR` statement, and the instance
profile name in the `PassRoleForEC2`
statement. For more information about the IAM ARN format, see [IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") in the _IAM User Guide_.

For more information about matching tag-key values, see [`aws:RequestTag/tag-key`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RunJobFlowExplicitlyWithTag",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:RunJobFlow"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/department": "dev"
 }
 }
 },
 {
 "Sid": "AddTagsForDevClusters",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:AddTags"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:*:*:cluster/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/department": "dev"
 }
 }
 },
 {
 "Sid": "PassRoleForEMR",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/Role-Name-With-Path"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "elasticmapreduce.amazonaws.com*"
 }
 }
 },
 {
 "Sid": "PassRoleForEC2",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/Role-Name-With-Path"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "ec2.amazonaws.com*"
 }
 }
 }
 ]
}`

```

### Allow actions on clusters

with a specific tag, regardless of tag value

You can also allow actions only on clusters that have a particular tag,
regardless of the tag value. To do this, you can use the `Null` operator. For more information, see
[Condition operator to check existence of condition keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_Null "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_Null") in the
_IAM User Guide_. For example, to allow actions
only on EMR clusters that have the `department` tag, regardless of the
value it contains, you could replace the Condition blocks in the earlier
example with the following one. The `Null`
operator looks for the presence of the tag `department` on an EMR cluster. If
the tag exists, the `Null` statement evaluates
to false, matching the condition specified in this policy statement, and the
appropriate actions are allowed.

```

"Condition": {
  "Null": {
    "elasticmapreduce:ResourceTag/department":"false"
  }
}

```

The following policy statement allows a user to create an EMR cluster only
if the cluster will have a `department` tag, which can contain
any value. For the `PassRole` resource, you
need to provide the AWS account ID or alias, and the service role name.
For more information about the IAM ARN format, see [IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") in the _IAM User Guide_.

For more information specifying the null ("false") condition operator, see
[Condition operator to check existence of condition keys](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateClusterTagNullCondition",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:RunJobFlow"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Null": {
 "aws:RequestTag/department": "false"
 }
 }
 },
 {
 "Sid": "AddTagsNullCondition",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:AddTags"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:*:*:cluster/*"
 ],
 "Condition": {
 "Null": {
 "elasticmapreduce:ResourceTag/department": "false"
 }
 }
 },
 {
 "Sid": "PassRoleForElasticMapReduce",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/Role-Name-With-Path"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "elasticmapreduce.amazonaws.com*"
 }
 }
 },
 {
 "Sid": "PassRoleForEC2",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/Role-Name-With-Path"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "ec2.amazonaws.com*"
 }
 }
 }
 ]
}`

```

## Example identity-based

policy statements for EMR Notebooks

The example IAM policy statements in this section demonstrate common
scenarios for using keys to limit allowed actions using EMR Notebooks. As long as
no other policy associated with the principal (user) allows the actions, the
condition context keys limit allowed actions as indicated.

###### Example – Allow access only to EMR Notebooks that a user creates based on

tagging

The following example policy statement, when attached to a role or user,
allows the a user to work only with notebooks that they have created. This
policy statement uses the default tag applied when a notebook is
created.

In the example, the `StringEquals` condition operator tries to
match a variable representing the current users a user ID
(`{aws:userId}`) with the value of the tag
`creatorUserID`. If the tag `creatorUserID` hasn't
been added to the notebook, or doesn't contain the value of the current
user's ID, the policy doesn't apply, and the actions aren't allowed by this
policy. If no other policy statements allow the actions, the user can only
work with notebooks that have this tag with this value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:DescribeEditor",
 "elasticmapreduce:StartEditor",
 "elasticmapreduce:StopEditor",
 "elasticmapreduce:DeleteEditor",
 "elasticmapreduce:OpenEditorInConsole"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/creatorUserId": "${aws:userId}"
 }
 },
 "Sid": "AllowELASTICMAPREDUCEDescribeeditor"
 }
 ]
}`

```

###### Example –Require notebook tagging when a notebook is created

In this example, the `RequestTag` context key is used. The
`CreateEditor` action is allowed only if the user does not
change or delete the `creatorUserID` tag is added by default. The
variable ${aws:userId}, specifies the currently active user's User ID, which
is the default value of the tag.

The policy statement can be used to help ensure that users do not remove
the `createUserId` tag or change its value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:CreateEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:RequestTag/creatorUserId": "${aws:userid}"
 }
 },
 "Sid": "AllowELASTICMAPREDUCECreateeditor"
 }
 ]
}`

```

This example requires that the user create the cluster with a tag having
the key string `dept` and a value set to one of the following:
`datascience`, `analytics`,
`operations`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:CreateEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:RequestTag/dept": [
 "datascience",
 "analytics",
 "operations"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCECreateeditor"
 }
 ]
}`

```

###### Example –Limit notebook creation to tagged clusters, and require notebook

tags

This example allows notebook creation only if the notebook is created with
a tag that has the key string `owner` set to one of the specified
values. In addition, the notebook can be created only if the cluster has a
tag with the key string `department` set to one of the specified
values.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:CreateEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:RequestTag/owner": [
 "owner1",
 "owner2",
 "owner3"
 ],
 "elasticmapreduce:ResourceTag/department": [
 "dep1",
 "dep3"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCECreateeditor"
 }
 ]
}`

```

###### Example –Limit the ability to start a notebook based on tags

This example limits the ability to start notebooks only to those notebooks
that have a tag with the key string `owner` set to one of the
specified values. Because the `Resource` element is used to
specify only the `editor`, the condition does not apply to the
cluster, and it does not need to be tagged.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:StartEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:editor/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/owner": [
 "owner1",
 "owner2"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEStarteditor"
 }
 ]
}`

```

This example is similar to one above. However, the limit only applies to
tagged clusters, not notebooks.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:StartEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:cluster/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/department": [
 "dep1",
 "dep3"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEStarteditor"
 }
 ]
}`

```

This example uses a different set of notebook and cluster tags. It allows
a notebook to be started only if:

- The notebook has a tag with the key string `owner` set
  to any of the specified values

—and—

- The cluster has a tag with the key string `department`
  set to any of the specified values

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:StartEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:editor/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/owner": [
 "user1",
 "user2"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEStarteditorByOwner"
 },
 {
 "Action": [
 "elasticmapreduce:StartEditor"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:cluster/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/department": [
 "datascience",
 "analytics"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEStarteditorByDepartment"
 }
 ]
}`

```

###### Example –Limit the ability to open the notebook editor based on

tags

This example allows the notebook editor to be opened only if:

- The notebook has a tag with the key string `owner` set
  to any of the specified values.

—and—

- The cluster has a tag with the key string `department`
  set to any of the specified values.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticmapreduce:OpenEditorInConsole"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:editor/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/owner": [
 "user1",
 "user2"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEOpeneditorconsoleByOwner"
 },
 {
 "Action": [
 "elasticmapreduce:OpenEditorInConsole"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:cluster/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/department": [
 "datascience",
 "analytics"
 ]
 }
 },
 "Sid": "AllowELASTICMAPREDUCEOpeneditorconsoleByDepartment"
 }
 ]
}`

```
