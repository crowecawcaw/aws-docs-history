

# Disassociating a global table replica
<a name="globaltables-disassociate"></a>

You can disassociate a replica from a global table to stop replication to and from that replica without deleting its table or data. The replica becomes a single-Region table in the same AWS account and Region and keeps its table name and Amazon Resource Name (ARN). You can use this operation after a Region or account migration, or when you no longer need a table to participate in replication.

You can disassociate replicas from same-account and multi-account global tables configured for multi-Region eventual consistency (MREC), using Global Tables version 2019.11.21 (Current). This operation is not supported for multi-Region strong consistency (MRSC) or Global Tables version 2017.11.29 (Legacy).

The result depends on the number of replicas in the global table:
+ If the global table has three or more replicas, the replica you disassociate becomes a single-Region table. The remaining replicas continue as a global table.
+ If the global table has two replicas, both tables become single-Region tables. Neither table nor its data is deleted.

The resulting table retains its table settings, including indexes, DynamoDB Streams, Time to Live (TTL), backups, encryption, billing mode, and table class. Replication-specific settings and metrics no longer apply. The table is billed as a single-Region table.

**Topics**
+ [Replication behavior](#globaltables-disassociate-replication)
+ [Disassociation protection and requirements](#globaltables-disassociate-protection)
+ [Required permissions](#globaltables-disassociate-permissions)
+ [Disassociating a replica using the AWS CLI](#globaltables-disassociate-cli)
+ [Disassociating a replica using CloudFormation](#globaltables-disassociate-cloudformation)
+ [Handling failures](#globaltables-disassociate-failures)

## Replication behavior
<a name="globaltables-disassociate-replication"></a>

When you request disassociation, DynamoDB establishes a replication stop boundary, a point in time it chooses after accepting the request, and waits until every remaining replica has received all writes made directly to the departing replica up to that boundary. If DynamoDB cannot deliver those writes to every remaining replica, disassociation does not complete and all original replicas remain in the global table.

The table continues serving reads and writes during and after disassociation. It retains its data, but because MREC replicates changes asynchronously, it might not contain the latest writes from other Regions. When disassociation completes, the table no longer sends or receives replicated writes.

## Disassociation protection and requirements
<a name="globaltables-disassociate-protection"></a>

Disassociation protection is enabled by default for each global table replica. Disable disassociation protection and wait for the update to finish before requesting disassociation. Disabling protection does not stop replication. Disassociation protection is independent of deletion protection. Disabling deletion protection does not disable disassociation protection.

Make both requests from the replica's Region and owning account. The replica must be `ACTIVE`, all replicas must be reachable, and the permissions and encryption-key access required for replication must remain available. Only one replica-lifecycle operation can run for a global table at a time, so wait for other operations, including replica creation and another disassociation, to finish before you submit the request.

Disassociation is blocked if any replica has a status of `INACCESSIBLE_ENCRYPTION_CREDENTIALS`, `REPLICATION_NOT_AUTHORIZED`, `ARCHIVING`, or `ARCHIVED`. Restore access and resolve replication issues before retrying.

For a multi-account global table, an account can disassociate only its own replica. You also cannot disassociate a replica that has acted as the source for a new replica added in the last 24 hours. Wait until 24 hours have elapsed since the new replica was added.

**Important**  
You cannot undo disassociation or reattach the same table to the global table it left. Before creating a replacement replica in that Region, apply any changes you need to keep from the standalone table to the remaining global table, resolving differences using your application's rules. Then delete the standalone table and add a new replica. The new replica copies data from the remaining global table.

## Required permissions
<a name="globaltables-disassociate-permissions"></a>

Disassociation uses the `Disassociate` action in the `ReplicaUpdates` array of `UpdateTable`. You need both `dynamodb:UpdateTable` and `dynamodb:DisassociateTableReplica` on the local replica's table ARN. `dynamodb:DisassociateTableReplica` is an IAM permission, not a separate API operation. Changing disassociation protection requires `dynamodb:UpdateTable`, and checking protection and monitoring completion require `dynamodb:DescribeTable`. The following identity policy grants these permissions for one table. Replace the Region, account ID, and table name with your values.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:UpdateTable",
                "dynamodb:DisassociateTableReplica",
                "dynamodb:DescribeTable"
            ],
            "Resource": "arn:aws:dynamodb:{{us-west-2}}:{{111122223333}}:table/{{Music}}"
        }
    ]
}
```

## Disassociating a replica using the AWS CLI
<a name="globaltables-disassociate-cli"></a>

The following procedure disassociates the `Music` replica in `us-west-2`. Use credentials for the account that owns this replica. Replace `Music` and `us-west-2` with your table and its local Region. The `--table-name` parameter accepts the table name or table ARN. If you use an ARN, specify the ARN of the replica in that account and Region.

1. Disable disassociation protection on the local replica.

   ```
   aws dynamodb update-table \
       --table-name {{Music}} \
       --region {{us-west-2}} \
       --no-disassociation-protection-enabled
   ```

1. Check the local table. Repeat this command until the table is `ACTIVE` and `DisassociationProtectionEnabled` is `false`. Do not proceed if the protection field is absent or `true`.

   ```
   aws dynamodb describe-table \
       --table-name {{Music}} \
       --region {{us-west-2}} \
       --query 'Table.{TableStatus:TableStatus,DisassociationProtectionEnabled:DisassociationProtectionEnabled,Replicas:Replicas}'
   ```

1. Submit a separate request with one `Disassociate` action. Specify the local Region and explicitly set `DisassociationMode` to `WAIT_FOR_REPLICATION`.

   ```
   aws dynamodb update-table \
       --table-name {{Music}} \
       --region {{us-west-2}} \
       --replica-updates '[{"Disassociate":{"RegionName":"{{us-west-2}}","DisassociationMode":"WAIT_FOR_REPLICATION"}}]'
   ```

   A successful response means that DynamoDB accepted the request. The operation continues asynchronously. An `UPDATING` status indicates that the update is still in progress.

1. Monitor the local table with `DescribeTable`.

   ```
   aws dynamodb describe-table \
       --table-name {{Music}} \
       --region {{us-west-2}} \
       --query 'Table.{TableStatus:TableStatus,Replicas:Replicas}'
   ```

   Confirm both that `TableStatus` is `ACTIVE` and that `Replicas` no longer lists any peer replicas. The list can be absent, empty, or contain only the local table. Also verify the updated membership from a remaining replica, using credentials authorized to describe that table.
**Important**  
`ACTIVE` alone does not confirm success. A table might return to `ACTIVE` after disassociation rolls back and still be a member of the global table. Always check replica membership.

For API details, see [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html) and [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) in the *Amazon DynamoDB API Reference*.

## Disassociating a replica using CloudFormation
<a name="globaltables-disassociate-cloudformation"></a>

If an `AWS::DynamoDB::GlobalTable` resource manages the replica, use its [`TableType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-tabletype) property to disassociate the replica. CloudFormation disassociates only the replica in the stack's account and Region. For a multi-account global table, each account disassociates its own replica from its own stack. To disassociate a replica in another Region of a same-account global table, first import that replica into a stack in its own Region with `TableType` set to `GlobalTableReplica`, and then run the updates there. For more information, see [Import AWS resources into a CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources.html) in the *AWS CloudFormation User Guide*.

The same stack keeps managing the table after it becomes regional. No table or data is deleted. The IAM principal that CloudFormation uses for the stack update needs the permissions described in [Required permissions](#globaltables-disassociate-permissions). Run both of the following stack updates in the replica's own account and Region.

1. Set [`DisassociationProtectionEnabled`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-disassociationprotectionenabled) to `false` in the `Replicas` entry for the stack's Region, and set `TableType` to `GlobalTableReplica`. Wait for the stack update to complete. Replication continues unchanged.

1. Set `TableType` to `Regional`. Keep only the stack's Region in `Replicas`, and remove `DisassociationProtectionEnabled` from that entry. Remove `GlobalTableSourceArn` and `MultiRegionConsistency` if present. If you remove `GlobalTableSourceArn`, declare the settings that the replica inherited from the source table, such as `KeySchema`, `AttributeDefinitions`, `BillingMode`, and `StreamSpecification`, with their current values. Make any other property change in a separate stack update. The stack update completes after DynamoDB finishes the disassociation.

**Important**  
The `TableType` change tells CloudFormation to disassociate the replica instead of deleting it. Removing the other Region entries in this update doesn't delete those tables. Removing a replica entry without changing `TableType` to `Regional` deletes that replica, as in any other stack update.

If DynamoDB rejects the disassociation or rolls it back, the table remains a replica and the stack update rolls back. Resolve the cause and run the second update again. CloudFormation can't undo a completed disassociation. If the disassociation completes and the stack update then rolls back, for example because another resource fails, the stack enters the `UPDATE_ROLLBACK_FAILED` state. Continue the rollback and skip the table resource. Then check whether the table is still a replica. If the table is now regional, apply the second update again. For more information, see [Continue rolling back an update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html) in the *AWS CloudFormation User Guide*. Recovering the stack doesn't require deleting the table or its data. To avoid this state, don't change other resources in the same stack update.

A table can also become regional outside the stack. For example, you disassociate it with the AWS CLI, or another account disassociates the other replica of a two-replica global table. In either case, apply the second update. CloudFormation recognizes that the table is already regional and doesn't delete the former replicas. Run [drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) afterward to confirm that the stack matches the table.

The following examples show the two stack updates for a same-account global table and for a multi-account global table, in YAML and JSON. The examples use fictitious values: the table name `GT-CFN-Table` and the account ID `111122223333`. Replace them, and the table settings, with your own values. `DeletionPolicy: Retain` keeps the table if you later delete the stack; it isn't required for disassociation.

### Same-account global table
<a name="globaltables-disassociate-cloudformation-same-account"></a>

This example uses a stack in `us-east-1` to disassociate the `us-east-1` replica of a same-account global table with replicas in `us-east-1`, `us-east-2`, and `us-west-2`. After the second update, the stack manages the `us-east-1` table as a regional table, and the `us-east-2` and `us-west-2` replicas continue as a global table. The stack no longer manages those tables. To manage the remaining global table with CloudFormation, import it into a stack in `us-east-2` or `us-west-2`.

#### Update 1: Disable disassociation protection
<a name="globaltables-disassociate-cloudformation-same-account-update-1"></a>

This template sets `DisassociationProtectionEnabled` to `false` on the `us-east-1` replica and sets `TableType` to `GlobalTableReplica`. The other properties are unchanged.

------
#### [ YAML ]

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  GlobalTable:
    Type: AWS::DynamoDB::GlobalTable
    DeletionPolicy: Retain
    Properties:
      TableName: GT-CFN-Table
      TableType: GlobalTableReplica
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      Replicas:
        - Region: us-east-1
          DisassociationProtectionEnabled: false
        - Region: us-east-2
        - Region: us-west-2
```

------
#### [ JSON ]

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "GlobalTable": {
            "Type": "AWS::DynamoDB::GlobalTable",
            "DeletionPolicy": "Retain",
            "Properties": {
                "TableName": "GT-CFN-Table",
                "TableType": "GlobalTableReplica",
                "BillingMode": "PAY_PER_REQUEST",
                "AttributeDefinitions": [
                    {
                        "AttributeName": "id",
                        "AttributeType": "S"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "id",
                        "KeyType": "HASH"
                    }
                ],
                "StreamSpecification": {
                    "StreamViewType": "NEW_AND_OLD_IMAGES"
                },
                "Replicas": [
                    {
                        "Region": "us-east-1",
                        "DisassociationProtectionEnabled": false
                    },
                    {
                        "Region": "us-east-2"
                    },
                    {
                        "Region": "us-west-2"
                    }
                ]
            }
        }
    }
}
```

------

#### Update 2: Disassociate the replica
<a name="globaltables-disassociate-cloudformation-same-account-update-2"></a>

This template sets `TableType` to `Regional`, keeps only `us-east-1` in `Replicas`, and removes `DisassociationProtectionEnabled` from that entry.

------
#### [ YAML ]

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  GlobalTable:
    Type: AWS::DynamoDB::GlobalTable
    DeletionPolicy: Retain
    Properties:
      TableName: GT-CFN-Table
      TableType: Regional
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      Replicas:
        - Region: us-east-1
```

------
#### [ JSON ]

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "GlobalTable": {
            "Type": "AWS::DynamoDB::GlobalTable",
            "DeletionPolicy": "Retain",
            "Properties": {
                "TableName": "GT-CFN-Table",
                "TableType": "Regional",
                "BillingMode": "PAY_PER_REQUEST",
                "AttributeDefinitions": [
                    {
                        "AttributeName": "id",
                        "AttributeType": "S"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "id",
                        "KeyType": "HASH"
                    }
                ],
                "StreamSpecification": {
                    "StreamViewType": "NEW_AND_OLD_IMAGES"
                },
                "Replicas": [
                    {
                        "Region": "us-east-1"
                    }
                ]
            }
        }
    }
}
```

------

### Multi-account global table
<a name="globaltables-disassociate-cloudformation-multi-account"></a>

This example disassociates the `us-east-2` replica of a multi-account global table. Account A (`111122223333`) owns the source table in `us-east-1`. Account B owns the `us-east-2` replica and runs both updates from its own stack in `us-east-2`. Because the global table has only two replicas, Account A's table also becomes regional. Account A can then set `TableType` to `Regional` in its own template. This update isn't required for Account B's disassociation to complete.

#### Update 1: Disable disassociation protection
<a name="globaltables-disassociate-cloudformation-multi-account-update-1"></a>

This template sets `DisassociationProtectionEnabled` to `false` on the `us-east-2` replica and sets `TableType` to `GlobalTableReplica`. The other properties are unchanged. The replica inherits its table settings from the source table identified by `GlobalTableSourceArn`.

------
#### [ YAML ]

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  ReplicaTable:
    Type: AWS::DynamoDB::GlobalTable
    DeletionPolicy: Retain
    Properties:
      TableName: GT-CFN-Table
      TableType: GlobalTableReplica
      GlobalTableSourceArn: arn:aws:dynamodb:us-east-1:111122223333:table/GT-CFN-Table
      Replicas:
        - Region: us-east-2
          DisassociationProtectionEnabled: false
```

------
#### [ JSON ]

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ReplicaTable": {
            "Type": "AWS::DynamoDB::GlobalTable",
            "DeletionPolicy": "Retain",
            "Properties": {
                "TableName": "GT-CFN-Table",
                "TableType": "GlobalTableReplica",
                "GlobalTableSourceArn": "arn:aws:dynamodb:us-east-1:111122223333:table/GT-CFN-Table",
                "Replicas": [
                    {
                        "Region": "us-east-2",
                        "DisassociationProtectionEnabled": false
                    }
                ]
            }
        }
    }
}
```

------

#### Update 2: Disassociate the replica
<a name="globaltables-disassociate-cloudformation-multi-account-update-2"></a>

This template sets `TableType` to `Regional`, removes `GlobalTableSourceArn` and `DisassociationProtectionEnabled`, and declares the inherited table settings with their current values.

------
#### [ YAML ]

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  ReplicaTable:
    Type: AWS::DynamoDB::GlobalTable
    DeletionPolicy: Retain
    Properties:
      TableName: GT-CFN-Table
      TableType: Regional
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      Replicas:
        - Region: us-east-2
```

------
#### [ JSON ]

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ReplicaTable": {
            "Type": "AWS::DynamoDB::GlobalTable",
            "DeletionPolicy": "Retain",
            "Properties": {
                "TableName": "GT-CFN-Table",
                "TableType": "Regional",
                "BillingMode": "PAY_PER_REQUEST",
                "AttributeDefinitions": [
                    {
                        "AttributeName": "id",
                        "AttributeType": "S"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "id",
                        "KeyType": "HASH"
                    }
                ],
                "StreamSpecification": {
                    "StreamViewType": "NEW_AND_OLD_IMAGES"
                },
                "Replicas": [
                    {
                        "Region": "us-east-2"
                    }
                ]
            }
        }
    }
}
```

------

## Handling failures
<a name="globaltables-disassociate-failures"></a>

A request rejected during validation or authorization does not start disassociation. Read the error response, correct the reported problem, and retry. For example, disable disassociation protection, wait for a concurrent operation to finish, or restore access to an inaccessible replica. If a request times out or its response is lost, check the table's status and membership before retrying because the request might have been accepted.

An accepted operation can fail later. For example, losing access to a replica's encryption key or required replication permissions can cause disassociation to roll back. After rollback, the replica remains part of the global table. Inspect `ReplicaStatus` and `ReplicaStatusDescription`, restore access where needed, and wait for the replicas to become active before retrying. Continued inaccessibility is still subject to the global table's existing recovery behavior. For more information, see [DynamoDB global tables security](globaltables-security.md).