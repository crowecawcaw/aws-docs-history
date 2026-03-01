# DynamoDB global tables security

Global tables replicas are DynamoDB tables, so you use the same methods for controlling
access to replicas that you do for single-Region tables, including AWS Identity and Access Management (IAM)
identity policies and resource-based policies.

This topic covers how to secure DynamoDB global tables using IAM permissions and AWS Key Management Service
(AWS KMS) encryption. You learn about the service-linked roles (SLR) that allow cross-Region
replication and auto-scaling, the IAM permissions needed to create, update, and delete
global tables , and the differences between multi-Region eventual consistency (MREC) and
multi-Region strong consistency (MRSC) tables. You also learn about AWS KMS encryption keys to
manage cross-Region replication securely.

## Service-linked roles for global tables

DynamoDB global tables rely on service-linked roles (SLRs) to manage cross-Region
replication and auto-scaling capabilities.

You only need to set up these roles once per AWS account. Once created, the same
roles serve all global tables in your account. For more information about service-linked
roles, see [Using service-linked
roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the _IAM User Guide_.

### Replication service-linked role

Amazon DynamoDB automatically creates the
`AWSServiceRoleForDynamoDBReplication` service-linked role (SLR) when
you create your first global table. This role manages cross-Region replication for
you.

When applying resource-based policies to replicas, ensure that you don't deny any
of the permissions defined in the
`AWSServiceRoleForDynamoDBReplicationPolicy` to the SLR principal, as
this will interrupt replication. If you deny required SLR permissions, replication
to and from affected replicas will stop, and the replica table status will change to
`REPLICATION_NOT_AUTHORIZED`.

- For multi-Region eventual consistency (MREC) global tables, if a replica
  remains in the `REPLICATION_NOT_AUTHORIZED` state for more than
  20 hours, the replica is irreversibly converted to a single-Region DynamoDB
  table.
- For multi-Region strong consistency (MRSC) global tables, denying required
  permissions results in `AccessDeniedException` for write and
  strongly consistent read operations. If a replica remains in the
  `REPLICATION_NOT_AUTHORIZED` state for more than seven days,
  the replica becomes permanently inaccessible, and write and strongly
  consistent read operations will continue to fail with an error. Some
  management operations like replica deletion will succeed.

### Auto scaling service-linked role

When configuring a global table for provisioned capacity mode, auto scaling must
be configured for the global table. DynamoDB auto scaling uses the AWS Application
Auto Scaling service to dynamically adjust provisioned throughput capacity on your
global table replicas. The Application Auto Scaling service creates a service-linked
role (SLR) named [`AWSServiceRoleForApplicationAutoScaling_DynamoDBTable`](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md").
This service-linked role is automatically created in your AWS account when you
first configure auto scaling for a DynamoDB table. It allows Application Auto Scaling
to managed provisioned table capacity and create CloudWatch alarms.

When applying resource-based policies to replicas, ensure that you don't deny any
permissions defined in the [`AWSApplicationAutoscalingDynamoDBTablePolicy`](../../../aws-managed-policy/latest/reference/AWSApplicationAutoscalingDynamoDBTablePolicy.md "../../../aws-managed-policy/latest/reference/AWSApplicationAutoscalingDynamoDBTablePolicy.md") to the
Application Auto Scaling SLR principal, as this will interrupt auto scaling
functionality.

### Example IAM policies for service-linked roles

An IAM policy with the following condition does not impact required permissions
to the DynamoDB replication SLR and AWS Auto Scaling SLR. This condition can be added
to otherwise broadly restrictive policies to avoid unintentionally interrupting
replication or auto scaling.

The following example shows how to exclude service-linked role principals
from deny statements:

```
"Condition": {
    "StringNotEquals": {
        "aws:PrincipalArn": [
            "arn:aws::iam::`111122223333`:role/aws-service-role/replication.dynamodb.amazonaws.com/`AWSServiceRoleForDynamoDBReplication`",
            "arn:aws::iam::`111122223333`:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/`AWSServiceRoleForApplicationAutoScaling_DynamoDBTable`"
        ]
    }
}
```

## How global tables use AWS IAM

The following sections describe the required permissions for different global table
operations and provide policy examples to help you configure the appropriate access for
your users and applications.

###### Note

All permissions described must be applied to the specific table resource ARN in
the affected Region(s). The table resource ARN follows the format
`arn:aws:dynamodb:region:account-id:table/table-name`, where you need
to specify your actual Region, account ID, and table name values.

###### Topics

- [Creating global tables and adding replicas](#globaltables-creation-iam "#globaltables-creation-iam")
- [Updating global tables](#globaltables-update-iam "#globaltables-update-iam")
- [Deleting global tables and removing replicas](#globaltables-delete-iam "#globaltables-delete-iam")

### Creating global tables and adding replicas

DynamoDB global tables support two consistency modes: multi-Region eventual
consistency (MREC) and multi-Region strong consistency (MRSC). MREC global tables
can have multiple replicas across any number of Regions and provide eventual
consistency. MRSC global tables require exactly three Regions (three replicas or two
replicas and one witness) and provide strong consistency with zero recovery point
objective (RPO).

The permissions required to create global tables depend on whether you're creating
a global table with or without a witness.

#### Permissions for creating global tables

The following permissions are required both for initial global table creation
and for adding replicas later. These permissions apply to both Multi-Region
Eventual Consistency (MREC) and Multi-Region Strong Consistency (MRSC) global
tables.

- Global tables require cross-Region replication, which DynamoDB manages
  through the [AWSServiceRoleForDynamoDBReplication](#globaltables-replication-slr "#globaltables-replication-slr")
  service-linked role (SLR). The following permission allows DynamoDB to
  create this role automatically when you create a global table for the
  first time:
  - `iam:CreateServiceLinkedRole`

- To create a global table or add a replica using the [`UpdateTable`](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") API, you must have the
  following permission on the source table resource:
  - `dynamodb:UpdateTable`

- You must have the following permissions on the table resource in the
  Regions for the replicas to be added:
  - `dynamodb:CreateTable`
  - `dynamodb:CreateTableReplica`
  - `dynamodb:Query`
  - `dynamodb:Scan`
  - `dynamodb:UpdateItem`
  - `dynamodb:PutItem`
  - `dynamodb:GetItem`
  - `dynamodb:DeleteItem`
  - `dynamodb:BatchWriteItem`

#### Additional permissions for MRSC global tables using a witness

When creating a Multi-Region Strong Consistency (MRSC) global table with a
witness Region, you must have the following permission on the table resource in
all participating Regions (including both replica Regions and the witness
Region):

- `dynamodb:CreateGlobalTableWitness`

#### Example IAM policies for creating global tables

The following identity-based policy allows you to create an MREC or
MRSC global table named "users" across three Regions, including creating
the required DynamoDB replication service-linked role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreatingUsersGlobalTable",
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:CreateTableReplica",
 "dynamodb:UpdateTable",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem",
 "dynamodb:PutItem",
 "dynamodb:GetItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1:123456789012`:table/`users`",
 "arn:aws:dynamodb:`us-east-2:123456789012`:table/`users`",
 "arn:aws:dynamodb:`us-west-2:123456789012`:table/`users`"
 ]
 },
 {
 "Sid": "AllowCreatingSLR",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::`123456789012`:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
 ]
 }
 ]
}`

```

The following identity-based policy allows you to create DynamoDB global
tables replicas across specific Regions using the [aws:RequestedRegion](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion") condition key, including creating the
required DynamoDB replication service-linked role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAddingReplicasToSourceTable",
 "Effect": "Allow",
 "Action": [
 "dynamodb:UpdateTable"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": [
 "`us-east-1`"
 ]
 }
 }
 },
 {
 "Sid": "AllowCreatingReplicas",
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:CreateTableReplica",
 "dynamodb:UpdateTable",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem",
 "dynamodb:PutItem",
 "dynamodb:GetItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": [
 "`us-east-2`",
 "`us-west-2`"
 ]
 }
 }
 },
 {
 "Sid": "AllowCreatingSLR",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::`123456789012`:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
 ]
 }
 ]
}`

```

The following identity-based policy allows you to a create a DynamoDB
MRSC global table named "users" with replicas in us-east-1 and us-east-2
and a witness in us-west-2, including creating the required DynamoDB
replication service-linked role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreatingUsersGlobalTableWithWitness",
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:CreateTableReplica",
 "dynamodb:CreateGlobalTableWitness",
 "dynamodb:UpdateTable",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem",
 "dynamodb:PutItem",
 "dynamodb:GetItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1:123456789012`:table/`users`",
 "arn:aws:dynamodb:`us-east-2:123456789012`:table/`users`"
 ]
 },
 {
 "Sid": "AllowCreatingSLR",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::`123456789012`:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
 ]
 }
 ]
}`

```

This identity-based policy allows you to create a MRSC global table
with replicas restricted to specific Regions using the [aws:RequestedRegion](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion") condition key and unrestricted witness
creation across all Regions, including creating the required DynamoDB
replication service-linked role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreatingReplicas",
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:CreateTableReplica",
 "dynamodb:UpdateTable",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem",
 "dynamodb:PutItem",
 "dynamodb:GetItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": [
 "`us-east-1`",
 "`us-east-2`"
 ]
 }
 }
 },
 {
 "Sid": "AllowCreatingWitness",
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateGlobalTableWitness"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowCreatingSLR",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::`123456789012`:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
 ]
 }
 ]
}`

```

### Updating global tables

To modify replica settings for an existing global table using the [`UpdateTable`](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") API, you need the following permission on
the table resource in the Region where you're making the API call:

- `dynamodb:UpdateTable`

You can additionally update other global table configurations, such as auto
scaling policies and Time to Live settings. The following permissions are required
for these additional update operations:

- To update a replica auto scaling policy with the [`UpdateTableReplicaAutoScaling`](../APIReference/API_UpdateTableReplicaAutoScaling.md "../APIReference/API_UpdateTableReplicaAutoScaling.md") API, you must
  have the following permissions on the table resource in all Regions
  containing replicas:
  - `application-autoscaling:DeleteScalingPolicy`
  - `application-autoscaling:DeleteScheduledAction`
  - `application-autoscaling:DeregisterScalableTarget`
  - `application-autoscaling:DescribeScalableTargets`
  - `application-autoscaling:DescribeScalingActivities`
  - `application-autoscaling:DescribeScalingPolicies`
  - `application-autoscaling:DescribeScheduledActions`
  - `application-autoscaling:PutScalingPolicy`
  - `application-autoscaling:PutScheduledAction`
  - `application-autoscaling:RegisterScalableTarget`

- To update Time to Live settings with the [`UpdateTimeToLive`](../APIReference/API_UpdateTimeToLive.md "../APIReference/API_UpdateTimeToLive.md") API, you must have the
  following permission on the table resource in all Regions containing
  replicas:

      + `dynamodb:UpdateTimeToLive`

  Note that Time to Live (TTL) is only supported for global tables
  configured with Multi-Region Eventual Consistency (MREC). For more
  information about how global tables work with TTL, see [How DynamoDB global tables work](V2globaltables_HowItWorks.md "V2globaltables_HowItWorks.md").

### Deleting global tables and removing replicas

To delete a global table, you must remove all replicas. The permissions required
for this operation differ depending on whether you're deleting a global table with
or without a witness Region.

#### Permissions for deleting global tables and removing replicas

The following permissions are required both for removing individual replicas
and for completely deleting global tables. Deleting a global table configuration
only removes the replication relationship between tables in different Regions.
It does not delete the underlying DynamoDB table in the last remaining Region. The
table in the last Region continues to exist as a standard DynamoDB table with the
same data and settings. These permissions apply to both Multi-Region Eventual
Consistency (MREC) and Multi-Region Strong Consistency (MRSC) global tables.

- To remove replicas from a global table using the [`UpdateTable`](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") API, you need the following
  permission on the table resource in the Region from which you're making
  the API call:
  - `dynamodb:UpdateTable`

- You need the following permissions on the table resource in each
  Region where you're removing a replica:
  - `dynamodb:DeleteTable`
  - `dynamodb:DeleteTableReplica`

#### Additional permissions for MRSC global tables using a witness

To delete a multi-Region strong consistency (MRSC) global table with a
witness, you must have the following permission on the table resource in all
participating Regions (including both replica Regions and the witness
Region):

- `dynamodb:DeleteGlobalTableWitness`

#### Examples IAM policies to delete a global table replicas

This identity-based policy allows you to delete a DynamoDB global table
named "users" and its replicas across three Regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:UpdateTable",
 "dynamodb:DeleteTable",
 "dynamodb:DeleteTableReplica"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1:123456789012`:table/`users`",
 "arn:aws:dynamodb:`us-east-2:123456789012`:table/`users`",
 "arn:aws:dynamodb:`us-west-2:123456789012`:table/`users`"
 ]
 }
 ]
}`

```

This identity-based policy allows you to delete the replica and the
witness of a MRSC global table named "users":

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:UpdateTable",
 "dynamodb:DeleteTable",
 "dynamodb:DeleteTableReplica",
 "dynamodb:DeleteGlobalTableWitness"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1:123456789012`:table/`users`",
 "arn:aws:dynamodb:`us-east-2:123456789012`:table/`users`"
 ]
 }
 ]
}`

```

## How global tables use AWS KMS

Like all DynamoDB tables, global tables replicas always encrypt data at rest using
encryption keys stored in AWS Key Management Service (AWS KMS).

All replicas in a global table must be configured with the same type of KMS key (AWS
owned key, AWS managed key, or Customer managed key).

###### Important

DynamoDB requires access to the replica's encryption key to delete a replica. If you
want to disable or delete a customer managed key used to encrypt a replica because
you are deleting the replica, you should first delete the replica, wait for the
table status on one of the remaining replicas to change to `ACTIVE`, then
disable or delete the key.

For a global table configured for multi-Region eventual consistency (MREC), if you
disable or revoke DynamoDB's access to a customer managed key used to encrypt a replica,
replication to and from the replica will stop and the replica status will change to
`INACCESSIBLE_ENCRYPTION_CREDENTIALS`. If a replica in a MREC global
table remains in the `INACCESSIBLE_ENCRYPTION_CREDENTIALS` state for more
than 20 hours, the replica is irreversibly converted to a single-Region DynamoDB
table.

For a global table configured for multi-Region strong consistency (MRSC), if you
disable or revoke DynamoDB's access to a customer managed key used to encrypt a replica,
replication to and from the replica will stop, attempts to perform write or strongly
consistent reads to the replica will return an error, and the replica status will change
to `INACCESSIBLE_ENCRYPTION_CREDENTIALS`. If a replica in a MRSC global table
remains in the `INACCESSIBLE_ENCRYPTION_CREDENTIALS` state for more than
seven days, depending on the specific permissions revoked the replica will be archived
or become permanently inaccessible.
