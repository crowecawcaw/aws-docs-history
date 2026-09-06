

# DynamoDB API operations supported by resource-based policies
<a name="rbac-iam-actions"></a>

This topic lists the API operations that are supported by resource-based policies. However, for cross-account access, you can only use a certain set of DynamoDB APIs through resource-based policies. You can't attach resource-based policies to resource types, such as backups and imports. The IAM actions, which correspond with the APIs operating on these resource types, are excluded from the supported IAM actions in resource-based policies. Because table administrators configure internal table settings within the same account, APIs, such as [UpdateTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTimeToLive.html) and [DisableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DisableKinesisStreamingDestination.html), don't support cross-account access through resource-based policies.

The DynamoDB data plane and control plane APIs that support cross-account access also support table name overloading, which lets you specify the table ARN instead of the table name. You can specify table ARN in the `TableName` parameter of these APIs. However, not all of these APIs support cross-account access.

**Topics**
+ [Data plane API operations](#rbac-data-plane-actions)
+ [PartiQL API operations](#rbac-partiql-actions)
+ [Control plane API operations](#rbac-control-plane-actions)
+ [Version 2019.11.21 (Current) global tables API operations](#rbac-current-global-table-actions)
+ [Version 2017.11.29 (Legacy) global tables API operations](#rbac-legacy-global-table-actions)
+ [Tags API operations](#rbac-tags-actions)
+ [Backup and Restore API operations](#rbac-backup-restore-actions)
+ [Continuous Backup/Restore (PITR) API operations](#rbac-continuous-backup-restore-actions)
+ [Contributor Insights API operations](#rbac-contributor-insights-actions)
+ [Export API operations](#rbac-export-actions)
+ [Import API operations](#rbac-import-actions)
+ [Amazon Kinesis Data Streams API operations](#rbac-kinesis-actions)
+ [Resource-based policy API operations](#rbac-rbp-actions)
+ [Time-to-Live API operations](#rbac-ttl-actions)
+ [Other API operations](#rbac-other-actions)
+ [DynamoDB Streams API operations](#rbac-ds-actions)

## Data plane API operations
<a name="rbac-data-plane-actions"></a>

The following table lists the API-level support provided by [data plane](HowItWorks.API.md#HowItWorks.API.DataPlane) API operations for resource-based policies and cross-account access.


| Data Plane - Tables/indexes APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html)  | Yes | Yes | 
|  [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html)  | Yes | Yes | 
|  [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html)  | Yes | Yes | 
|  [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html)  | Yes | Yes | 
|  [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html)  | Yes | Yes | 
|  [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html)  | Yes | Yes | 
|  [TransactGetItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html)  | Yes | Yes | 
|  [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html)  | Yes | Yes | 
|  [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html)  | Yes | Yes | 
|  [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html)  | Yes | Yes | 

## PartiQL API operations
<a name="rbac-partiql-actions"></a>

The following table lists the API-level support provided by [PartiQL](HowItWorks.API.md#HowItWorks.API.DataPlane.partiql) API operations for resource-based policies and cross-account access.


| PartiQL APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [BatchExecuteStatement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchExecuteStatement.html)  | Yes | No | 
|  [ExecuteStatement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)  | Yes | No | 
|  [ExecuteTransaction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteTransaction.html)  | Yes | No | 

## Control plane API operations
<a name="rbac-control-plane-actions"></a>

The following table lists the API-level support provided by [control plane](HowItWorks.API.md#HowItWorks.API.ControlPlane) API operations for resource-based policies and cross-account access.


| Control Plane - Tables APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html)  | No | No | 
|  [DeleteTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html)  | Yes | Yes | 
|  [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html)  | Yes | Yes | 
|  [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html)  | Yes | Yes | 

## Version 2019.11.21 (Current) global tables API operations
<a name="rbac-current-global-table-actions"></a>

The following table lists the API-level support provided by [Version 2019.11.21 (Current) global tables](GlobalTables.md) API operations for resource-based policies and cross-account access.


| Version 2019.11.21 (Current) global tables APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTableReplicaAutoScaling.html)  | Yes | No | 
|  [UpdateTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTableReplicaAutoScaling.html)  | Yes | No | 

## Version 2017.11.29 (Legacy) global tables API operations
<a name="rbac-legacy-global-table-actions"></a>

The following table lists the API-level support provided by [Version 2017.11.29 (Legacy) global tables](globaltables.V1.md) API operations for resource-based policies and cross-account access.


| Version 2017.11.29 (Legacy) global tables APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [CreateGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalTable.html)  | No | No | 
|  [DescribeGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTable.html)  | No | No | 
|  [DescribeGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTableSettings.html)  | No | No | 
|  [ListGlobalTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListGlobalTables.html)  | No | No | 
|  [UpdateGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTable.html)  | No | No | 
|  [UpdateGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTableSettings.html)  | No | No | 

## Tags API operations
<a name="rbac-tags-actions"></a>

The following table lists the API-level support provided by API operations related to [tags](Tagging.Operations.md) for resource-based policies and cross-account access.


| Tags APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [ListTagsOfResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTagsOfResource.html)  | Yes | Yes | 
|  [TagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TagResource.html)  | Yes | Yes | 
|  [UntagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UntagResource.html)  | Yes | Yes | 

## Backup and Restore API operations
<a name="rbac-backup-restore-actions"></a>

The following table lists the API-level support provided by API operations related to [backup and restore](Backup-and-Restore.md) for resource-based policies and cross-account access.


| Backup and Restore APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [CreateBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateBackup.html)  | Yes | No | 
|  [DescribeBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBackup.html)  | No | No | 
|  [DeleteBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteBackup.html)  | No | No | 
|  [RestoreTableFromBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableFromBackup.html)  | No | No | 

## Continuous Backup/Restore (PITR) API operations
<a name="rbac-continuous-backup-restore-actions"></a>

The following table lists the API-level support provided by API operations related to [Continuous Backup/Restore (PITR)](Point-in-time-recovery.md) for resource-based policies and cross-account access.


| Continuous Backup/Restore (PITR) APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContinuousBackups.html)  | Yes | No | 
|  [RestoreTableToPointInTime](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableToPointInTime.html)  | Yes | No | 
|  [UpdateContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContinuousBackups.html)  | Yes | No | 

## Contributor Insights API operations
<a name="rbac-contributor-insights-actions"></a>

The following table lists the API-level support provided by API operations related to [Continuous Backup/Restore (PITR)](Point-in-time-recovery.md) for resource-based policies and cross-account access.


| Contributor Insights APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContributorInsights.html)  | Yes | No | 
|  [ListContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListContributorInsights.html)  | No | No | 
|  [UpdateContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContributorInsights.html)  | Yes | No | 

## Export API operations
<a name="rbac-export-actions"></a>

The following table lists the API-level support provided by Export API operations for resource-based policies and cross-account access.


| Export APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeExport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeExport.html)  | No | No | 
|  [ExportTableToPointInTime](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportTableToPointInTime.html)  | Yes | No | 
|  [ListExports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListExports.html)  | No | No | 

## Import API operations
<a name="rbac-import-actions"></a>

The following table lists the API-level support provided by Import API operations for resource-based policies and cross-account access.


| Import APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeImport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeImport.html)  | No | No | 
|  [ImportTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportTable.html)  | No | No | 
|  [ListImports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListImports.html)  | No | No | 

## Amazon Kinesis Data Streams API operations
<a name="rbac-kinesis-actions"></a>

The following table lists the API-level support provided by Kinesis Data Streams API operations for resource-based policies and cross-account access.


| Kinesis APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeKinesisStreamingDestination.html)  | Yes | No | 
|  [DisableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DisableKinesisStreamingDestination.html)  | Yes | No | 
|  [EnableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_EnableKinesisStreamingDestination.html)  | Yes | No | 
|  [UpdateKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateKinesisStreamingDestination.html)  | Yes | No | 

## Resource-based policy API operations
<a name="rbac-rbp-actions"></a>

The following table lists the API-level support provided by resource-based policy API operations for resource-based policies and cross-account access.


| Resource-based policy APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [GetResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetResourcePolicy.html)  | Yes | No | 
|  [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html)  | Yes | No | 
|  [DeleteResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteResourcePolicy.html)  | Yes | No | 

## Time-to-Live API operations
<a name="rbac-ttl-actions"></a>

The following table lists the API-level support provided by [time to live](TTL.md) (TTL) API operations for resource-based policies and cross-account access.


| TTL APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTimeToLive.html)  | Yes | No | 
|  [UpdateTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTimeToLive.html)  | Yes | No | 

## Other API operations
<a name="rbac-other-actions"></a>

The following table lists the API-level support provided by other miscellaneous API operations for resource-based policies and cross-account access.


| Other APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeLimits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeLimits.html)  | No | No | 
|  [DescribeEndpoints](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeEndpoints.html)  | No | No | 
|  [ListBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html)  | No | No | 
|  [ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html)  | No | No | 

## DynamoDB Streams API operations
<a name="rbac-ds-actions"></a>

The following table lists the API-level support of DynamoDB Streams APIs for resource-based policies and cross-account access.


| DynamoDB Streams APIs | Resource-based policy support | Cross-account support | 
| --- | --- | --- | 
|  [DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html)  | Yes | Yes | 
|  [GetRecords](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html)  | Yes | Yes | 
|  [GetShardIterator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html)  | Yes | Yes | 
|  [ListStreams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ListStreams.html)  | No | No | 