#

Grant permission to tag Amazon RDS
resources during creation

Some RDS API operations allow you to specify tags when you create the resource. You can use resource tags
to implement attribute-based control (ABAC). For more information, see [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
and [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

To enable users to tag resources on creation, they must have permissions to use the action that
creates the resource, such as `rds:CreateDBInstance`.
If tags are specified in the create action, RDS performs additional authorization on the
`rds:AddTagsToResource` action to verify if users have permissions to create tags.
Therefore, users must also have explicit permissions to use the `rds:AddTagsToResource` action.

In the IAM policy definition for the `rds:AddTagsToResource` action,
you can use the `aws:RequestTag` condition key to require tags in a request to tag a resource.

For example, the following policy allows users to create DB instances and apply tags during DB instance creation,
but only with specific tag keys (`environment` or `project`):

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds:CreateDBInstance"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "rds:AddTagsToResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": ["production", "development"],
 "aws:RequestTag/project": ["dataanalytics", "webapp"]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["environment", "project"]
 }
 }
 }
 ]
}`

```

This policy denies any create DB instance request that includes tags other than the
`environment` or `project` tags, or that doesn't
specify either of these tags. Additionally, users must specify values for the
tags that match the allowed values in the policy.

The following policy allows users to create DB clusters and apply any tags during creation except the `environment=prod` tag:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds:CreateDBCluster"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "rds:AddTagsToResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:RequestTag/environment": "prod"
 }
 }
 }
 ]
}`

```

## Supported RDS API actions for tagging on creation

The following RDS API actions support tagging when you create a resource.
For these actions, you can specify tags when you create the resource:

- `CreateBlueGreenDeployment`
- `CreateCustomDBEngineVersion`
- `CreateDBCluster`
- `CreateDBClusterEndpoint`
- `CreateDBClusterParameterGroup`
- `CreateDBClusterSnapshot`
- `CreateDBInstance`
- `CreateDBInstanceReadReplica`
- `CreateDBParameterGroup`
- `CreateDBProxy`
- `CreateDBProxyEndpoint`
- `CreateDBSecurityGroup`
- `CreateDBShardGroup`
- `CreateDBSnapshot`
- `CreateDBSubnetGroup`
- `CreateEventSubscription`
- `CreateGlobalCluster`
- `CreateIntegration`
- `CreateOptionGroup`
- `CreateTenantDatabase`
- `CopyDBClusterParameterGroup`
- `CopyDBClusterSnapshot`
- `CopyDBParameterGroup`
- `CopyDBSnapshot`
- `CopyOptionGroup`
- `RestoreDBClusterFromS3`
- `RestoreDBClusterFromSnapshot`
- `RestoreDBClusterToPointInTime`
- `RestoreDBInstanceFromDBSnapshot`
- `RestoreDBInstanceFromS3`
- `RestoreDBInstanceToPointInTime`
- `PurchaseReservedDBInstancesOffering`

If you use the AWS CLI or API to create a resource with tags, the `Tags`
parameter is used to apply tags to resources during creation.

For these API actions, if tagging fails, the resource is not created, and the
request fails with an error. This ensures that resources are either created with
tags or not created at all, preventing resources from being created without the intended tags.
