# Specifying conditions: Using custom tags

Amazon RDS
supports specifying conditions in an IAM policy using custom tags.

For example, suppose that you add a tag named `environment` to your DB
instances with values such as `beta`, `staging`,
`production`, and so on. If you do, you can create a policy that restricts
certain users to DB instances based on the `environment` tag value.

###### Note

Custom tag identifiers are case-sensitive.

The following table lists the RDS tag identifiers that you can use in a `Condition` element.

| **RDS tag identifier** | **Applies to**                        |
| ---------------------- | ------------------------------------- |
| `db-tag`               | DB instances, including read replicas |
| `snapshot-tag`         | DB snapshots                          |
| `ri-tag`               | Reserved DB instances                 |
| `og-tag`               | DB option groups                      |
| `pg-tag`               | DB parameter groups                   |
| `subgrp-tag`           | DB subnet groups                      |
| `es-tag`               | Event subscriptions                   |
| `cluster-tag`          | DB clusters                           |
| `cluster-pg-tag`       | DB cluster parameter groups           |
| `cluster-snapshot-tag` | DB cluster snapshots                  |

The syntax for a custom tag condition is as follows:

`"Condition":{"StringEquals":{"rds:`rds-tag-identifier`/`tag-name`":
 ["`value`"]} }`

For example, the following `Condition` element applies to DB instances with a
tag named `environment` and a tag value of `production`.

`"Condition":{"StringEquals":{"rds:db-tag/`environment`": ["`production`"]} }`

For information about creating tags, see [Tagging Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").

###### Important

If you manage access to your RDS resources using tagging, we recommend that you secure
access to the tags for your RDS resources. You can manage access to tags by creating policies for the
`AddTagsToResource` and `RemoveTagsFromResource` actions. For example, the following
policy denies users the ability to add or remove tags for all resources. You can then create policies
to allow specific users to add or remove tags.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"DenyTagUpdates",
 "Effect":"Deny",
 "Action":[
 "rds:AddTagsToResource",
 "rds:RemoveTagsFromResource"
 ],
 "Resource":"*"
 }
 ]
}`

```

To see a list of Amazon RDS actions, see [Actions Defined by Amazon RDS](../../../service-authorization/latest/reference/list_amazonrds.md#amazonrds-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonrds.md#amazonrds-actions-as-permissions") in the
_Service Authorization Reference_.

## Example policies:

Using custom tags

Following are examples of how you can use custom tags in Amazon RDS IAM permissions policies.
For more information about adding tags to an Amazon RDS resource, see [Amazon Resource Names (ARNs) in Amazon RDS](USER_Tagging.md "USER_Tagging.md").

###### Note

All examples use the us-west-2 region and contain fictitious account IDs.

### Example 1: Grant permission for actions on a resource with a specific tag with two

different values

The following policy allows permission to perform the
`CreateDBSnapshot` API operation on DB instances with either the `stage`
tag set to `development` or `test`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AllowAnySnapshotName",
 "Effect":"Allow",
 "Action":[
 "rds:CreateDBSnapshot"
 ],
 "Resource":"arn:aws:rds:*:123456789012:snapshot:*"
 },
 {
 "Sid":"AllowDevTestToCreateSnapshot",
 "Effect":"Allow",
 "Action":[
 "rds:CreateDBSnapshot"
 ],
 "Resource":"arn:aws:rds:*:123456789012:db:*",
 "Condition":{
 "StringEquals":{
 "rds:db-tag/stage":[
 "development",
 "test"
 ]
 }
 }
 }
 ]
}`

```

The following policy allows permission to perform the
`ModifyDBInstance` API operation on DB instances with either the `stage`
tag set to `development` or `test`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AllowChangingParameterOptionSecurityGroups",
 "Effect":"Allow",
 "Action":[
 "rds:ModifyDBInstance"
 ],
 "Resource": [
 "arn:aws:rds:*:123456789012:pg:*",
 "arn:aws:rds:*:123456789012:secgrp:*",
 "arn:aws:rds:*:123456789012:og:*"
 ]
 },
 {
 "Sid":"AllowDevTestToModifyInstance",
 "Effect":"Allow",
 "Action":[
 "rds:ModifyDBInstance"
 ],
 "Resource":"arn:aws:rds:*:123456789012:db:*",
 "Condition":{
 "StringEquals":{
 "rds:db-tag/stage":[
 "development",
 "test"
 ]
 }
 }
 }
 ]
}`

```

### Example 2: Explicitly deny permission to create a DB instance that uses specified DB parameter groups

The following policy explicitly denies permission to create a DB instance that uses DB
parameter groups with specific tag values. You might apply this policy if you
require that a specific customer-created DB parameter group always be used when
creating DB instances. Policies that use `Deny` are most often used to restrict access
that was granted by a broader policy.

Explicitly denying permission supersedes any other permissions granted.
This ensures that identities to not accidentally get permission that you
never want to grant.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"DenyProductionCreate",
 "Effect":"Deny",
 "Action":"rds:CreateDBInstance",
 "Resource":"arn:aws:rds:*:123456789012:pg:*",
 "Condition":{
 "StringEquals":{
 "rds:pg-tag/usage":"prod"
 }
 }
 }
 ]
}`

```

### Example 3: Grant permission for actions on a DB instance with an instance name that is prefixed with a

user name

The following policy allows permission to call any API (except to `AddTagsToResource` or
`RemoveTagsFromResource`) on a DB instance that has a DB instance name that is prefixed with the
user's name and that has a tag called `stage` equal to `devo` or that has no tag
called `stage`.

The `Resource` line in the policy identifies a resource by its Amazon Resource Name (ARN). For more
information about using ARNs with Amazon RDS resources, see [Amazon Resource Names (ARNs) in Amazon RDS](USER_Tagging.md "USER_Tagging.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AllowFullDevAccessNoTags",
 "Effect":"Allow",
 "NotAction":[
 "rds:AddTagsToResource",
 "rds:RemoveTagsFromResource"
 ],
 "Resource":"arn:aws:rds:*:123456789012:db:${aws:username}*",
 "Condition":{
 "StringEqualsIfExists":{
 "rds:db-tag/stage":"devo"
 }
 }
 }
 ]
}`

```
