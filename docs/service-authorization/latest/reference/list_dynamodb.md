

# Actions, resources, and condition keys for Amazon DynamoDB
<a name="list_dynamodb"></a>

Amazon DynamoDB (service prefix: `dynamodb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dynamodb/dynamodb.json) for this service.

**Topics**
+ [API operations defined by Amazon DynamoDB](#list_dynamodb-operations)
+ [Actions defined by Amazon DynamoDB](#list_dynamodb-actions-as-permissions)
+ [Permission-only actions for Amazon DynamoDB](#list_dynamodb-permission-only-actions)
+ [Resource types defined by Amazon DynamoDB](#list_dynamodb-resources-for-iam-policies)
+ [Condition keys for Amazon DynamoDB](#list_dynamodb-policy-keys)

## API operations defined by Amazon DynamoDB
<a name="list_dynamodb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_dynamodb-actions-as-permissions).




- **   BatchExecuteStatement  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:PartiQLDelete](#list_dynamodb-action-PartiQLDelete)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PartiQLInsert](#list_dynamodb-action-PartiQLInsert)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PartiQLSelect](#list_dynamodb-action-PartiQLSelect)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PartiQLUpdate](#list_dynamodb-action-PartiQLUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   BatchGetItem  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:BatchGetItem](#list_dynamodb-action-BatchGetItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchWriteItem  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:BatchWriteItem](#list_dynamodb-action-BatchWriteItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBackup  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:CreateBackup](#list_dynamodb-action-CreateBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGlobalTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:CreateGlobalTable](#list_dynamodb-action-CreateGlobalTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:AssociateTableReplica](#list_dynamodb-action-AssociateTableReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:BatchWriteItem](#list_dynamodb-action-BatchWriteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:CreateTable](#list_dynamodb-action-CreateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:CreateTableReplica](#list_dynamodb-action-CreateTableReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:DeleteItem](#list_dynamodb-action-DeleteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:GetItem](#list_dynamodb-action-GetItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PutItem](#list_dynamodb-action-PutItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PutResourcePolicy](#list_dynamodb-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [dynamodb:Query](#list_dynamodb-action-Query)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:Scan](#list_dynamodb-action-Scan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:TagResource](#list_dynamodb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dynamodb:UpdateItem](#list_dynamodb-action-UpdateItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBackup  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DeleteBackup](#list_dynamodb-action-DeleteBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteItem  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DeleteItem](#list_dynamodb-action-DeleteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:WriteDataForReplication](#list_dynamodb-action-WriteDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DeleteResourcePolicy](#list_dynamodb-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DeleteTable](#list_dynamodb-action-DeleteTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBackup  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeBackup](#list_dynamodb-action-DescribeBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContinuousBackups  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeContinuousBackups](#list_dynamodb-action-DescribeContinuousBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContributorInsights  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeContributorInsights](#list_dynamodb-action-DescribeContributorInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoints  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeEndpoints](#list_dynamodb-action-DescribeEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExport  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeExport](#list_dynamodb-action-DescribeExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGlobalTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeGlobalTable](#list_dynamodb-action-DescribeGlobalTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGlobalTableSettings  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeGlobalTableSettings](#list_dynamodb-action-DescribeGlobalTableSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImport  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeImport](#list_dynamodb-action-DescribeImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKinesisStreamingDestination  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeKinesisStreamingDestination](#list_dynamodb-action-DescribeKinesisStreamingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLimits  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeLimits](#list_dynamodb-action-DescribeLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeTable](#list_dynamodb-action-DescribeTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReadDataForReplication](#list_dynamodb-action-ReadDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReplicateSettings](#list_dynamodb-action-ReplicateSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DescribeTableReplicaAutoScaling  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeTableReplicaAutoScaling](#list_dynamodb-action-DescribeTableReplicaAutoScaling) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTimeToLive  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DescribeTimeToLive](#list_dynamodb-action-DescribeTimeToLive)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReadDataForReplication](#list_dynamodb-action-ReadDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DisableKinesisStreamingDestination  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:DisableKinesisStreamingDestination](#list_dynamodb-action-DisableKinesisStreamingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableKinesisStreamingDestination  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:EnableKinesisStreamingDestination](#list_dynamodb-action-EnableKinesisStreamingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteStatement  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:PartiQLDelete](#list_dynamodb-action-PartiQLDelete)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PartiQLInsert](#list_dynamodb-action-PartiQLInsert)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PartiQLSelect](#list_dynamodb-action-PartiQLSelect)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PartiQLUpdate](#list_dynamodb-action-PartiQLUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ExecuteTransaction  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:PartiQLDelete](#list_dynamodb-action-PartiQLDelete)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PartiQLInsert](#list_dynamodb-action-PartiQLInsert)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PartiQLSelect](#list_dynamodb-action-PartiQLSelect)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PartiQLUpdate](#list_dynamodb-action-PartiQLUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ExportTableToPointInTime  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ExportTableToPointInTime](#list_dynamodb-action-ExportTableToPointInTime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetItem  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:GetItem](#list_dynamodb-action-GetItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReadDataForReplication](#list_dynamodb-action-ReadDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:GetResourcePolicy](#list_dynamodb-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ImportTable](#list_dynamodb-action-ImportTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListBackups  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListBackups](#list_dynamodb-action-ListBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContributorInsights  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListContributorInsights](#list_dynamodb-action-ListContributorInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExports  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListExports](#list_dynamodb-action-ListExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGlobalTables  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListGlobalTables](#list_dynamodb-action-ListGlobalTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImports  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListImports](#list_dynamodb-action-ListImports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTables  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListTables](#list_dynamodb-action-ListTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsOfResource  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ListTagsOfResource](#list_dynamodb-action-ListTagsOfResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutItem  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:PutItem](#list_dynamodb-action-PutItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:WriteDataForReplication](#list_dynamodb-action-WriteDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutResourcePolicy  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:PutResourcePolicy](#list_dynamodb-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   Query  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:Query](#list_dynamodb-action-Query) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RestoreTableFromBackup  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:BatchWriteItem](#list_dynamodb-action-BatchWriteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:DeleteItem](#list_dynamodb-action-DeleteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:GetItem](#list_dynamodb-action-GetItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PutItem](#list_dynamodb-action-PutItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:Query](#list_dynamodb-action-Query)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:RestoreTableFromBackup](#list_dynamodb-action-RestoreTableFromBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:Scan](#list_dynamodb-action-Scan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:UpdateItem](#list_dynamodb-action-UpdateItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RestoreTableToPointInTime  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:AssociateTableReplica](#list_dynamodb-action-AssociateTableReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:BatchWriteItem](#list_dynamodb-action-BatchWriteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:CreateTableReplica](#list_dynamodb-action-CreateTableReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:DeleteItem](#list_dynamodb-action-DeleteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:GetItem](#list_dynamodb-action-GetItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PutItem](#list_dynamodb-action-PutItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:Query](#list_dynamodb-action-Query)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:Scan](#list_dynamodb-action-Scan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:UpdateItem](#list_dynamodb-action-UpdateItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   Scan  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:Scan](#list_dynamodb-action-Scan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:TagResource](#list_dynamodb-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TransactGetItems  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:GetItem](#list_dynamodb-action-GetItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TransactWriteItems  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ConditionCheckItem](#list_dynamodb-action-ConditionCheckItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:DeleteItem](#list_dynamodb-action-DeleteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:PutItem](#list_dynamodb-action-PutItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:UpdateItem](#list_dynamodb-action-UpdateItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UntagResource  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UntagResource](#list_dynamodb-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateContinuousBackups  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateContinuousBackups](#list_dynamodb-action-UpdateContinuousBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContributorInsights  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateContributorInsights](#list_dynamodb-action-UpdateContributorInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlobalTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateGlobalTable](#list_dynamodb-action-UpdateGlobalTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlobalTableSettings  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateGlobalTableSettings](#list_dynamodb-action-UpdateGlobalTableSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateItem  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateItem](#list_dynamodb-action-UpdateItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKinesisStreamingDestination  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateKinesisStreamingDestination](#list_dynamodb-action-UpdateKinesisStreamingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTable  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:BatchWriteItem](#list_dynamodb-action-BatchWriteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:CreateGlobalTableWitness](#list_dynamodb-action-CreateGlobalTableWitness)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:CreateTable](#list_dynamodb-action-CreateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:CreateTableReplica](#list_dynamodb-action-CreateTableReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:DeleteGlobalTableWitness](#list_dynamodb-action-DeleteGlobalTableWitness)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:DeleteItem](#list_dynamodb-action-DeleteItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:GetItem](#list_dynamodb-action-GetItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:PutItem](#list_dynamodb-action-PutItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:Query](#list_dynamodb-action-Query)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReplicateSettings](#list_dynamodb-action-ReplicateSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:Scan](#list_dynamodb-action-Scan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:TagResource](#list_dynamodb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dynamodb:UpdateItem](#list_dynamodb-action-UpdateItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:UpdateTable](#list_dynamodb-action-UpdateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:WriteDataForReplication](#list_dynamodb-action-WriteDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateTableReplicaAutoScaling  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:UpdateTableReplicaAutoScaling](#list_dynamodb-action-UpdateTableReplicaAutoScaling) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTimeToLive  **
  - **SDK client:** dynamodb
  - **IAM action:**  [dynamodb:ReplicateSettings](#list_dynamodb-action-ReplicateSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:UpdateTimeToLive](#list_dynamodb-action-UpdateTimeToLive)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dynamodb:WriteDataForReplication](#list_dynamodb-action-WriteDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DescribeStream  **
  - **SDK client:** dynamodbstreams
  - **IAM action:**  [dynamodb:DescribeStream](#list_dynamodb-action-DescribeStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReadDataForReplication](#list_dynamodb-action-ReadDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRecords  **
  - **SDK client:** dynamodbstreams
  - **IAM action:**  [dynamodb:GetRecords](#list_dynamodb-action-GetRecords)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReadDataForReplication](#list_dynamodb-action-ReadDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetShardIterator  **
  - **SDK client:** dynamodbstreams
  - **IAM action:**  [dynamodb:GetShardIterator](#list_dynamodb-action-GetShardIterator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dynamodb:ReadDataForReplication](#list_dynamodb-action-ReadDataForReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListStreams  **
  - **SDK client:** dynamodbstreams
  - **IAM action:**  [dynamodb:ListStreams](#list_dynamodb-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon DynamoDB
<a name="list_dynamodb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html)  **
  - **Description:** Grants permission to return the attributes of one or more items from one or more tables
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Access level:** Read

- **   [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html)  **
  - **Description:** Grants permission to put or delete multiple items in one or more tables
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)
  - **Access level:** Write

- **   [ConditionCheckItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConditionCheck.html)  **
  - **Description:** Grants permission to the ConditionCheckItem operation checks the existence of a set of attributes for the item with the given primary key
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)
  - **Access level:** Read

- **   [CreateBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateBackup.html)  **
  - **Description:** Grants permission to create a backup for an existing table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalTable.html)  **
  - **Description:** Grants permission to create a global table from an existing table
  - **Resource types (\*required):** [global-table\*](#list_dynamodb-resource-global-table) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html)  **
  - **Description:** Grants permission to the CreateTable operation adds a new table to your account
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dynamodb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dynamodb-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteBackup.html)  **
  - **Description:** Grants permission to delete an existing backup of a table
  - **Resource types (\*required):** [backup\*](#list_dynamodb-resource-backup)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html)  **
  - **Description:** Grants permission to deletes a single item in a table by primary key
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the resource-based policy attached to the resource
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html)  **
  - **Description:** Grants permission to the DeleteTable operation which deletes a table and all of its items
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBackup.html)  **
  - **Description:** Grants permission to describe an existing backup of a table
  - **Resource types (\*required):** [backup\*](#list_dynamodb-resource-backup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContinuousBackups.html)  **
  - **Description:** Grants permission to check the status of the backup restore settings on the specified table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContributorInsights.html)  **
  - **Description:** Grants permission to describe the contributor insights status and related details for a given table or global secondary index
  - **Resource types (\*required):** [index](#list_dynamodb-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpoints](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeEndpoints.html)  **
  - **Description:** Grants permission to return the regional endpoint information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeExport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeExport.html)  **
  - **Description:** Grants permission to describe an existing Export of a table
  - **Resource types (\*required):** [export\*](#list_dynamodb-resource-export)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTable.html)  **
  - **Description:** Grants permission to return information about the specified global table
  - **Resource types (\*required):** [global-table\*](#list_dynamodb-resource-global-table)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTableSettings.html)  **
  - **Description:** Grants permission to return settings information about the specified global table
  - **Resource types (\*required):** [global-table\*](#list_dynamodb-resource-global-table)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeImport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeImport.html)  **
  - **Description:** Grants permission to describe an existing import
  - **Resource types (\*required):** [import\*](#list_dynamodb-resource-import)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeKinesisStreamingDestination.html)  **
  - **Description:** Grants permission to grant permission to describe the status of Kinesis streaming and related details for a given table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLimits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeLimits.html)  **
  - **Description:** Grants permission to return the current provisioned-capacity limits for your AWS account in a region, both for the region as a whole and for any one DynamoDB table that you create there
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html)  **
  - **Description:** Grants permission to return information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html)  **
  - **Description:** Grants permission to return information about the table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTableReplicaAutoScaling.html)  **
  - **Description:** Grants permission to describe the auto scaling settings across all replicas of the global table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTimeToLive.html)  **
  - **Description:** Grants permission to give a description of the Time to Live (TTL) status on the specified table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DisableKinesisStreamingDestination.html)  **
  - **Description:** Grants permission to grant permission to stop replication from the DynamoDB table to the Kinesis data stream
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_EnableKinesisStreamingDestination.html)  **
  - **Description:** Grants permission to grant permission to start table data replication to the specified Kinesis data stream at a timestamp chosen during the enable workflow
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportTableToPointInTime](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportTableToPointInTime.html)  **
  - **Description:** Grants permission to initiate an Export of a DynamoDB table to S3
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html)  **
  - **Description:** Grants permission to the GetItem operation that returns a set of attributes for the item with the given primary key
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Access level:** Read

- **   [GetRecords](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html)  **
  - **Description:** Grants permission to retrieve the stream records from a given shard
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to view a resource-based policy for a resource
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetShardIterator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html)  **
  - **Description:** Grants permission to return a shard iterator
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportTable.html)  **
  - **Description:** Grants permission to initiate an import from S3 to a DynamoDB table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html)  **
  - **Description:** Grants permission to list backups associated with the account and endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListContributorInsights.html)  **
  - **Description:** Grants permission to list the ContributorInsightsSummary for all tables and global secondary indexes associated with the current account and endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListExports.html)  **
  - **Description:** Grants permission to list exports associated with the account and endpoint
  - **Resource types (\*required):** [table](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGlobalTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListGlobalTables.html)  **
  - **Description:** Grants permission to list all global tables that have a replica in the specified region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListImports.html)  **
  - **Description:** Grants permission to list imports associated with the account and endpoint
  - **Resource types (\*required):** [table](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStreams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ListStreams.html)  **
  - **Description:** Grants permission to return an array of stream ARNs associated with the current account and endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html)  **
  - **Description:** Grants permission to return an array of table names associated with the current account and endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsOfResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTagsOfResource.html)  **
  - **Description:** Grants permission to list all tags on an Amazon DynamoDB resource
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PartiQLDelete](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)  **
  - **Description:** Grants permission to delete a single item in a table by primary key
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)
  - **Access level:** Write

- **   [PartiQLInsert](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)  **
  - **Description:** Grants permission to create a new item, if an item with same primary key does not exist in the table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)
  - **Access level:** Write

- **   [PartiQLSelect](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)  **
  - **Description:** Grants permission to read a set of attributes for items from a table or index
  - **Resource types (\*required):** [index](#list_dynamodb-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:FullTableScan](#list_dynamodb-dynamodb_FullTableScan)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:FullTableScan](#list_dynamodb-dynamodb_FullTableScan)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Access level:** Read

- **   [PartiQLUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)  **
  - **Description:** Grants permission to edit an existing item's attributes
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)
  - **Access level:** Write

- **   [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html)  **
  - **Description:** Grants permission to create a new item, or replace an old item with a new item
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource-based policy to the resource
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html)  **
  - **Description:** Grants permission to use the primary key of a table or a secondary index to directly access items from that table or index
  - **Resource types (\*required):** [index](#list_dynamodb-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Access level:** Read

- **   [RestoreTableFromBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableFromBackup.html)  **
  - **Description:** Grants permission to create a new table from an existing backup
  - **Resource types (\*required):** [backup\*](#list_dynamodb-resource-backup) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreTableToPointInTime](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableToPointInTime.html)  **
  - **Description:** Grants permission to restore a table to a point in time
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html)  **
  - **Description:** Grants permission to return one or more items and item attributes by accessing every item in a table or a secondary index
  - **Resource types (\*required):** [index](#list_dynamodb-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)<br />[dynamodb:Select](#list_dynamodb-dynamodb_Select)
  - **Access level:** Read

- **   [SearchVectors](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SearchVectors.html)  **
  - **Description:** Grants permission to perform a vector similarity search on a vector index associated with an Amazon DynamoDB table
  - **Resource types (\*required):** [index\*](#list_dynamodb-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to associate a set of tags with an Amazon DynamoDB resource
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dynamodb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dynamodb-aws_TagKeys)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dynamodb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dynamodb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the association of tags from an Amazon DynamoDB resource
  - **Resource types (\*required):** [stream\*](#list_dynamodb-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dynamodb-aws_TagKeys)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dynamodb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContinuousBackups.html)  **
  - **Description:** Grants permission to enable or disable continuous backups
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContributorInsights.html)  **
  - **Description:** Grants permission to update the status for contributor insights for a specific table or global secondary index
  - **Resource types (\*required):** [index](#list_dynamodb-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTable.html)  **
  - **Description:** Grants permission to add or remove replicas in the specified global table
  - **Resource types (\*required):** [global-table\*](#list_dynamodb-resource-global-table) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTableSettings.html)  **
  - **Description:** Grants permission to update settings of the specified global table
  - **Resource types (\*required):** [global-table\*](#list_dynamodb-resource-global-table) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html)  **
  - **Description:** Grants permission to edit an existing item's attributes, or adds a new item to the table if it does not already exist
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)<br />[dynamodb:Attributes](#list_dynamodb-dynamodb_Attributes)<br />[dynamodb:EnclosingOperation](#list_dynamodb-dynamodb_EnclosingOperation)<br />[dynamodb:LeadingKeys](#list_dynamodb-dynamodb_LeadingKeys)<br />[dynamodb:ReturnConsumedCapacity](#list_dynamodb-dynamodb_ReturnConsumedCapacity)<br />[dynamodb:ReturnValues](#list_dynamodb-dynamodb_ReturnValues)
  - **Access level:** Write

- **   [UpdateKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateKinesisStreamingDestination.html)  **
  - **Description:** Grants permission to update data replication configurations for the specified Kinesis data stream
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html)  **
  - **Description:** Grants permission to modify the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTableReplicaAutoScaling.html)  **
  - **Description:** Grants permission to update auto scaling settings on your replica table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTimeToLive.html)  **
  - **Description:** Grants permission to enable or disable TTL for the specified table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon DynamoDB
<a name="list_dynamodb-permission-only-actions"></a>

The following actions are defined by Amazon DynamoDB but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateTableReplica](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_MA_security.html)  **
  - **Description:** Grants permission to create multi account global table replica
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGlobalTableWitness](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2gt_IAM.html)  **
  - **Description:** Grants permission to add a Witness to a Global Table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTableReplica](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2gt_IAM.html)  **
  - **Description:** Grants permission to add a new replica table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGlobalTableWitness](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2gt_IAM.html)  **
  - **Description:** Grants permission to remove a Witness from a Global Table
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTableReplica](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2gt_IAM.html)  **
  - **Description:** Grants permission to delete a replica table and all of its items
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeReservedCapacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-prevent-purchase-reserved-capacity.html)  **
  - **Description:** Grants permission to describe one or more of the Reserved Capacity purchased
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReservedCapacityOfferings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-prevent-purchase-reserved-capacity.html)  **
  - **Description:** Grants permission to describe Reserved Capacity offerings that are available for purchase
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAbacStatus](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-enable-ddb.html)  **
  - **Description:** Grants permission to view the status of Attribute Based Access Control for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InjectError](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2gt_IAM.html)  **
  - **Description:** Grants permission to start experiments on a Global Table
  - **Resource types (\*required):** 
  - **Condition keys:** [dynamodb:FisActionId](#list_dynamodb-dynamodb_FisActionId)<br />[dynamodb:FisTargetArns](#list_dynamodb-dynamodb_FisTargetArns)
  - **Access level:** Write

- **   [PurchaseReservedCapacityOfferings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-prevent-purchase-reserved-capacity.html)  **
  - **Description:** Grants permission to purchases reserved capacity for use with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ReadDataForReplication](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_MA_security.html)  **
  - **Description:** Grants permission to read data from a multi account global table replica
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ReplicateSettings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_MA_security.html)  **
  - **Description:** Grants permission to configure settings for a multi account global table replica
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreTableFromAwsBackup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/UsageNotesAWS.html)  **
  - **Description:** Grants permission to create a new table from recovery point on AWS Backup
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAwsBackupJob](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/UsageNotesAWS.html)  **
  - **Description:** Grants permission to create a backup on AWS Backup with advanced features enabled
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAbacStatus](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-enable-ddb.html)  **
  - **Description:** Grants permission to update the status of Attribute Based Access Control for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [UpdateGlobalTableVersion](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html)  **
  - **Description:** Grants permission to update version of the specified global table
  - **Resource types (\*required):** [global-table\*](#list_dynamodb-resource-global-table) / **Condition keys:**  
  - **Resource types (\*required):** [table](#list_dynamodb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [WriteDataForReplication](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_MA_security.html)  **
  - **Description:** Grants permission to write data to a multi account global table replica
  - **Resource types (\*required):** [table\*](#list_dynamodb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon DynamoDB
<a name="list_dynamodb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [backup](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html)  | arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName}/backup/${BackupName} |   | 
|  [export](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.HowItWorks.html)  | arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName}/export/${ExportName} |   | 
|  [global-table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html)  | arn:${Partition}:dynamodb::${Account}:global-table/${GlobalTableName} |   | 
|  [import](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.HowItWorks.html)  | arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName}/import/${ImportName} |   | 
|  [index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey)  | arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName}/index/${IndexName} | [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_) | 
|  [stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.Streams)  | arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName}/stream/${StreamLabel} | [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_) | 
|  [table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes)  | arn:${Partition}:dynamodb:${Region}:${Account}:table/${TableName} | [aws:ResourceTag/${TagKey}](#list_dynamodb-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon DynamoDB
<a name="list_dynamodb-policy-keys"></a>

Amazon DynamoDB defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [dynamodb:Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by attribute (field or column) names of the table | ArrayOfString | 
|   [dynamodb:EnclosingOperation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by blocking Transactions APIs calls and allow the non-Transaction APIs calls and vice-versa | String | 
|   [dynamodb:FirstPartitionKeyValues](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the first partition key of the table | ArrayOfString | 
|   [dynamodb:FisActionId](specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the ID of an AWS FIS action | String | 
|   [dynamodb:FisTargetArns](specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the ARN of an AWS FIS target | ArrayOfARN | 
|   [dynamodb:FourthPartitionKeyValues](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the forth partition key of the table | ArrayOfString | 
|   [dynamodb:FullTableScan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-iam.html)  | Filters access by blocking full table scan | Bool | 
|   [dynamodb:LeadingKeys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the first partition key of the table | ArrayOfString | 
|   [dynamodb:ReturnConsumedCapacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the ReturnConsumedCapacity parameter of a request. Contains either "TOTAL" or "NONE" | String | 
|   [dynamodb:ReturnValues](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the ReturnValues parameter of request. Contains one of the following: "ALL\_OLD", "UPDATED\_OLD","ALL\_NEW","UPDATED\_NEW", or "NONE" | String | 
|   [dynamodb:SecondPartitionKeyValues](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the second partition key of the table | ArrayOfString | 
|   [dynamodb:Select](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the Select parameter of a Query or Scan request | String | 
|   [dynamodb:ThirdPartitionKeyValues](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys)  | Filters access by the third partition key of the table | ArrayOfString | 