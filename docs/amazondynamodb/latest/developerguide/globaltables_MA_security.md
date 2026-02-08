# DynamoDB global tables security

Global tables replicas are DynamoDB tables, so you use the same methods for controlling access to replicas that you do
for single-Region tables, including AWS Identity and Access Management (IAM) identity policies and resource-based policies. This topic covers how to
secure DynamoDB multi-account global tables using IAM permissions and AWS Key Management Service (AWS KMS) encryption. You learn about the resource
based policies and service-linked roles (SLR) that allow cross-Region cross-account replication and auto-scaling, the IAM permissions
needed to create, update, and delete global tables, for a multi-Region eventual consistency (MREC) tables. You also learn about AWS KMS encryption
keys to manage cross-Region replication securely.

It provides detailed information about the resource-based policies and permissions required to establish cross-account and cross-region
table replication. Understanding this security model is crucial for customers who need to implement secure, cross-account data replication solutions.

## Service principal authorization for replication

DynamoDB's multi-account global tables use a distinct authorization approach because replication is performed across
account boundaries. This is done using DynamoDB's replication service principal: `replication.dynamodb.amazonaws.com`.
Each participating account must explicitly allow that principal in the replica table's resource policy, giving it permissions that can be
constrained to specific replicas by source context conditions on keys like `aws:SourceAccount`, `aws:SourceArn`, etc.
— see [AWS global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") for more details.
Permissions are bi-directional, which means that all replicas must explicitly grant permissions to each other before replication can be established
across any particular pair of replicas.

The following service principal permissions are essential for cross-account replication:

- `dynamodb:ReadDataForReplication` grants the ability to read data for replication purposes.
  This permission allows changes in one replica to be read and propagated to other replicas.
- `dynamodb:WriteDataForReplication` permits the writing of replicated data to destination tables.
  This permission allows changes to be synchronized across all replicas in the global table.
- `dynamodb:ReplicateSettings` enables the synchronization of table settings across replicas, providing
  consistent configuration across all participating tables.

Each replica must give the above permissions to all other replicas and to itself — i.e. the source context conditions must include
the full set of replicas that comprises the global table. These permission are verified for each new replica when it is added to a multi-account
global table. This verifies that replication operations are performed only by the authorized DynamoDB service and only between the intended tables.

## Service-linked roles for multi-account global tables

DynamoDB multi-account global tables replicate settings across all replicas so that each replica is set up identically with consistent throughput
and provides a seamless fail-over experience. Replication of settings is controlled through the `ReplicateSettings` permission on the service
principal, but we also rely on service-linked roles (SLRs) to manage certain cross-account cross-Region replication and auto-scaling capabilities. These roles
are set up only once per AWS account. Once created, the same roles serve all global tables in your account. For more information about service-linked roles,
see [Using service-linked roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the IAM User Guide.

### Settings management service-linked role

Amazon DynamoDB automatically creates the AWSServiceRoleForDynamoDBGlobalTableSettingsManagement service-linked role (SLR) when you create your first multi-account
global table replica in the account. This role manages cross-account cross-Region replication of settings for you.

When applying resource-based policies to replicas, confirm that you do not deny any of the permissions defined in the `AWSServiceRoleForDynamoDBGlobalTableSettingsManagement`
to the SLR principal, as this could interfere with settings management and may impair replication if throughput does not match across replicas or GSIs. If you deny required SLR
permissions, replication to and from affected replicas may stop, and the replica table status will change to `REPLICATION_NOT_AUTHORIZED`. For multi-account global tables,
if a replica remains in the `REPLICATION_NOT_AUTHORIZED` state for more than 20 hours, the replica is irreversibly converted to a single-Region DynamoDB table. The SLR
has the following permissions:

- `application-autoscaling:DeleteScalingPolicy`
- `application-autoscaling:DescribeScalableTargets`
- `application-autoscaling:DescribeScalingPolicies`
- `application-autoscaling:DeregisterScalableTarget`
- `application-autoscaling:PutScalingPolicy`
- `application-autoscaling:RegisterScalableTarget`

### Auto scaling service-linked role

When configuring a global table for provisioned capacity mode, auto scaling must be configured for the global table. DynamoDB auto scaling
uses the AWS Application Auto Scaling service to dynamically adjust provisioned throughput capacity on your global table replicas. The Application Auto Scaling
service creates a service-linked role (SLR) named [AWSServiceRoleForApplicationAutoScaling_DynamoDBTable](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md").
This service-linked role is automatically created in your AWS account when you first configure auto scaling for a DynamoDB table. It allows Application Auto Scaling to manage provisioned
table capacity and create CloudWatch alarms.

When applying resource-based policies to replicas, verify that you do not deny any permissions defined in the
[AWSApplicationAutoscalingDynamoDBTablePolicy](../../../aws-managed-policy/latest/reference/AWSApplicationAutoscalingDynamoDBTablePolicy.md "../../../aws-managed-policy/latest/reference/AWSApplicationAutoscalingDynamoDBTablePolicy.md") to
the Application Auto Scaling SLR principal, as this will interrupt auto-scaling functionality.

## How global tables use AWS IAM

The following sections describe the required permissions for different global table operations and provide policy examples to help you configure the appropriate access for your users and applications.

###### Note

All permissions described must be applied to the specific table resource ARN in the affected Region(s). The table resource ARN follows the format `arn:aws:dynamodb:region:account-id:table/table-name`, where you need to specify your actual Region, account ID, and table name values.

The following are the step-by-step topics we cover in the sections below:

- Creating multi-account global tables and adding replicas
- Updating a multi-account global table
- Deleting global tables and removing replicas

### Creating global tables and adding replicas

#### Permissions for creating global tables

When a new replica is added to a regional table to form a multi-account global table or to an existing multi-account global table, the IAM principal performing the action must be authorized by all existing members. All existing members needs to give the following permission in their table policy for the replica addition to succeed:

- `dynamodb:AssociateTableReplica` - This permission allows tables to be joined into a global table setup. This is the foundational permission that enables the initial establishment of the replication relationship.

This precise control allows only authorized accounts to participate in the global table setup.

#### Example IAM policies for creating global tables

The setup of multi-account global tables follows a specific authorization flow that provides secure replication. Let's examine how this works in practice by walking through a practical scenario where a customer wants to establish a global table with two replicas. The first replica (ReplicaA) resides in Account A in the ap-east-1 region, while the second replica (ReplicaB) is in Account B in the eu-south-1 region.

- In the source account (Account A), the process begins with creating the primary replica table. The account administrator must attach a resource-based policy to this table that explicitly grants necessary permissions to the destination account (Account B) to perform the association. This policy also authorizes the DynamoDB replication service to perform essential replication actions.
- The destination account (Account B) follows a similar process by attaching a corresponding resource-based policy while creating the replica and referencing the source table ARN to be used to create the replica. This policy mirrors the permissions granted by Account A, creating a trusted bi-directional relationship. Before establishing replication, DynamoDB validates these cross-account permissions to verify proper authorization is in place.
  To establish this setup:

- The administrator of Account A must first attach the resource-based policy to ReplicaA. This policy explicitly grants the necessary permissions to Account B and the DynamoDB replication service.
- Similarly, the administrator of Account B must attach a matching policy to ReplicaB, with account references reversed to grant corresponding permissions to Account A, in the create table call to create replica B referencing replica A as source table.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": [ "A", "B" ],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
                        "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB"
                    ]
                }
            }
        },
        {
            "Sid": "AllowTrustedAccountsToJoinThisGlobalTable",
            "Effect": "Allow",
            "Action": [
                "dynamodb:AssociateTableReplica"
            ],
            "Resource": "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
            "Principal": {"AWS": ["B"]}
        }
    ]
}

```

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": [ "A", "B" ],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
                        "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB"
                    ]
                }
            }
        }
    ]
}
```

In this setup, we have 3 replicas ReplicaA, ReplicaB, and ReplicaC in Account A, Account B, and Account C, respectively. Replica A is the first replica, which starts as a regional table, and then ReplicaB and ReplicaC are added to it.

- The administrator of Account A must first attach the resource-based policy to ReplicaA allowing replication with all members, and allowing the IAM principals of Account B and Account C to add replicas.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": [ "A", "B", "C" ],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
                        "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB",
                        "arn:aws:dynamodb:us-east-1:C:table/ReplicaC"
                    ]
                }
            }
        },
        {
            "Sid": "AllowTrustedAccountsToJoinThisGlobalTable",
            "Effect": "Allow",
            "Action": [
                "dynamodb:AssociateTableReplica"
            ],
            "Resource": "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
            "Principal": { "AWS": [ "B", "C" ] }
        }
    ]
}

```

- The administrator of Account B must add a replica (Replica B) pointing to ReplicaA as a source. Replica B has the following policy allowing replication between all members, and allowing Account C to add a replica:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": [ "A", "B", "C" ],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
                        "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB",
                        "arn:aws:dynamodb:us-east-1:C:table/ReplicaC"
                    ]
                }
            }
        },
        {
            "Sid": "AllowTrustedAccountsToJoinThisGlobalTable",
            "Effect": "Allow",
            "Action": [
                "dynamodb:AssociateTableReplica"
            ],
            "Resource": "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB",
            "Principal": { "AWS": [ "C" ] }
        }
    ]
}

```

- Finally, the administrator of Account C create a replica with the following policy allowing replication permissions between all members. The policy doesn't allow any further replicas to be added.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:C:table/ReplicaC",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": [ "A", "B" ],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
                        "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB"
                    ]
                }
            }
        }
    ]
}

```

### Updating a multi-account global table

To modify replica settings for an existing global table using the UpdateTable API, you need the following permission on the table resource in the Region where you're making the API call: `dynamodb:UpdateTable`

You can additionally update other global table configurations, such as auto scaling policies and Time to Live settings. The following permissions are required for these additional update operations:

To update Time to Live settings with the `UpdateTimeToLive` API, you must have the following permission on the table resource in all Regions containing replicas: `dynamodb:UpdateTimeToLive`

To update a replica auto scaling policy with the `UpdateTableReplicaAutoScaling` API, you must have the following permissions on the table resource in all Regions containing replicas:

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

###### Note

You need to provide `dynamodb:ReplicateSettings` permissions across all replica regions and accounts
for the update table to succeed. If any replica does not provide permissions to replicate settings to any replica in
the multi-account global table, all Update operations across all replicas will fail with `AccessDeniedException`
till the permissions are fixed.

### Deleting global tables and removing replicas

To delete a global table, you must remove all replicas. Unlike same-account Global Table, you cannot use `UpdateTable` to delete a replica table in a remote region and each replica must be deleted through the `DeleteTable` API from the account that controls it.

#### Permissions for deleting global tables and removing replicas

The following permissions are required both for removing individual replicas and for completely deleting global tables. Deleting a global table configuration only removes the replication relationship between tables in different Regions. It does not delete the underlying DynamoDB table in the last remaining Region. The table in the last Region continues to exist as a standard DynamoDB table with the same data and settings.

You need the following permissions on the table resource in each Region where you're removing a replica:

- `dynamodb:DeleteTable`
- `dynamodb:DeleteTableReplica`

## How global tables use AWS KMS

Like all DynamoDB tables, global table replicas always encrypt data at rest using encryption keys stored in AWS Key Management Service (AWS KMS).

###### Note

Unlike same-account global table, different replicas in a multi-account global table can be configured with the different type of AWS KMS key (AWS owned key, or Customer managed key). Multi-account global tables do not support AWS Managed Keys.

Multi-account global tables that use CMKs requires each replica's keys policy to give permissions to the DynamoDB replication service principal (`replication.dynamodb.amazonaws.com`) to access the key for replication and settings management. The following permissions are required:

- `kms:Decrypt`
- `kms:ReEncrypt*`
- `kms:GenerateDataKey*`
- `kms:DescribeKey`

**Important**

DynamoDB requires access to the replica's encryption key to delete a replica. If you want to disable or delete a customer managed key used to encrypt a replica because you are deleting the replica, you should first delete the replica, wait for the table to be removed from the replication group by calling describe in one of the other replicas, then disable or delete the key.

If you disable or revoke DynamoDB's access to a customer managed key used to encrypt a replica, replication to and from the replica will stop and the replica status will change to `INACCESSIBLE_ENCRYPTION_CREDENTIALS`. If a replica remains in the `INACCESSIBLE_ENCRYPTION_CREDENTIALS` state for more than 20 hours, the replica is irreversibly converted to a single-Region DynamoDB table.

### Example AWS KMS policy

The AWS KMS policy allows DynamoDB to access both AWS KMS keys for replication between replicas A an B.
The AWS KMS keys attached to the DynamoDB replica in each account needs to be updated with the following policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": { "Service": "replication.dynamodb.amazonaws.com" },
        "Action": [
            "kms:Decrypt",
            "kms:ReEncrypt*",
            "kms:GenerateDataKey*",
            "kms:DescribeKey"
        ],
        "Condition": {
            "StringEquals": {
                "aws:SourceAccount": [ "A", "B" ],
                "aws:SourceArn": [
                    "arn:aws:dynamodb:ap-east-1:A:table/ReplicaA",
                    "arn:aws:dynamodb:eu-south-1:B:table/ReplicaB"
                ]
            }
        }
      }
   ]
 }

```
