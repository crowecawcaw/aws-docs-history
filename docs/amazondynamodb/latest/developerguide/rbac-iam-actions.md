# DynamoDB API operations supported by resource-based

policies

This topic lists the API operations that are supported by resource-based policies.
However, for cross-account access, you can only use a certain set of DynamoDB APIs through
resource-based policies. You can't attach resource-based policies to resource types, such as
backups and imports. The IAM actions, which correspond with the APIs operating on these
resource types, are excluded from the supported IAM actions in resource-based policies.
Because table administrators configure internal table settings within the same account, APIs,
such as [UpdateTimeToLive](../APIReference/API_UpdateTimeToLive.md "../APIReference/API_UpdateTimeToLive.md")
and [DisableKinesisStreamingDestination](../APIReference/API_DisableKinesisStreamingDestination.md "../APIReference/API_DisableKinesisStreamingDestination.md"), don't support cross-account access through
resource-based policies.

The DynamoDB data plane and control plane APIs that support cross-account access also support
table name overloading, which lets you specify the table ARN instead of the table name. You
can specify table ARN in the `TableName` parameter of these APIs. However, not all
of these APIs support cross-account access.

###### Topics

- [Data plane API operations](#rbac-data-plane-actions "#rbac-data-plane-actions")
- [PartiQL API operations](#rbac-partiql-actions "#rbac-partiql-actions")
- [Control plane API operations](#rbac-control-plane-actions "#rbac-control-plane-actions")
- [Version 2019.11.21 (Current) global
  tables API operations](#rbac-current-global-table-actions "#rbac-current-global-table-actions")
- [Version 2017.11.29 (Legacy) global tables
  API operations](#rbac-legacy-global-table-actions "#rbac-legacy-global-table-actions")
- [Tags API operations](#rbac-tags-actions "#rbac-tags-actions")
- [Backup and Restore API operations](#rbac-backup-restore-actions "#rbac-backup-restore-actions")
- [Continuous Backup/Restore (PITR)
  API operations](#rbac-continuous-backup-restore-actions "#rbac-continuous-backup-restore-actions")
- [Contributor Insights API
  operations](#rbac-contributor-insights-actions "#rbac-contributor-insights-actions")
- [Export API operations](#rbac-export-actions "#rbac-export-actions")
- [Import API operations](#rbac-import-actions "#rbac-import-actions")
- [Amazon Kinesis Data Streams API operations](#rbac-kinesis-actions "#rbac-kinesis-actions")
- [Resource-based policy API operations](#rbac-rbp-actions "#rbac-rbp-actions")
- [Time-to-Live API operations](#rbac-ttl-actions "#rbac-ttl-actions")
- [Other API operations](#rbac-other-actions "#rbac-other-actions")
- [DynamoDB Streams API operations](#rbac-ds-actions "#rbac-ds-actions")

## Data plane API operations

The following table lists the API-level support provided by [data plane](HowItWorks.md#HowItWorks.API.DataPlane "HowItWorks.md#HowItWorks.API.DataPlane") API operations for resource-based
policies and cross-account access.

| Data Plane - Tables/indexes APIs                                                                                                                               | Resource-based policy support | Cross-account support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DeleteItem](../APIReference/API_DeleteItem.md "../APIReference/API_DeleteItem.md")                                                                            | Yes                           | Yes                   |
| [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md")                                                                                     | Yes                           | Yes                   |
| [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md")                                                                                     | Yes                           | Yes                   |
| [Query](../APIReference/API_Query.md "../APIReference/API_Query.md")                                                                                           | Yes                           | Yes                   |
| [Scan](../APIReference/API_Scan.md "../APIReference/API_Scan.md")                                                                                              | Yes                           | Yes                   |
| [UpdateItem](../APIReference/API_UpdateItem.md "../APIReference/API_UpdateItem.md")                                                                            | Yes                           | Yes                   |
| [TransactGetItems](../APIReference/API_TransactGetItems.md "../APIReference/API_TransactGetItems.md")                                                          | Yes                           | Yes                   |
| [TransactWriteItems](../APIReference/API_TransactWriteItems.md "../APIReference/API_TransactWriteItems.md")                                                    | Yes                           | Yes                   |
| [BatchGetItem](../APIReference/API_BatchGetItem.md "../APIReference/API_BatchGetItem.md")                                                                      | Yes                           | Yes                   |
| [BatchWriteItem](../APIReference/API_BatchWriteItem.md "../APIReference/API_BatchWriteItem.md")                                                                | Yes                           | Yes                   | ## PartiQL API operations The following table lists the API-level support provided by [PartiQL](HowItWorks.md#HowItWorks.API.DataPlane.partiql "HowItWorks.md#HowItWorks.API.DataPlane.partiql") API operations for resource-based policies and cross-account access.                    |
| PartiQL APIs                                                                                                                                                   | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [BatchExecuteStatement](../APIReference/API_BatchExecuteStatement.md "../APIReference/API_BatchExecuteStatement.md")                                           | Yes                           | No                    |
| [ExecuteStatement](../APIReference/API_ExecuteStatement.md "../APIReference/API_ExecuteStatement.md")                                                          | Yes                           | No                    |
| [ExecuteTransaction](../APIReference/API_ExecuteTransaction.md "../APIReference/API_ExecuteTransaction.md")                                                    | Yes                           | No                    | ## Control plane API operations The following table lists the API-level support provided by [control plane](HowItWorks.md#HowItWorks.API.ControlPlane "HowItWorks.md#HowItWorks.API.ControlPlane") API operations for resource-based policies and cross-account access.                  |
| Control Plane - Tables APIs                                                                                                                                    | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md")                                                                         | No                            | No                    |
| [DeleteTable](../APIReference/API_DeleteTable.md "../APIReference/API_DeleteTable.md")                                                                         | Yes                           | Yes                   |
| [DescribeTable](../APIReference/API_DescribeTable.md "../APIReference/API_DescribeTable.md")                                                                   | Yes                           | Yes                   |
| [UpdateTable](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md")                                                                         | Yes                           | Yes                   | ## Version 2019.11.21 (Current) global tables API operations The following table lists the API-level support provided by [Version 2019.11.21 (Current) global tables](GlobalTables.md "GlobalTables.md") API operations for resource-based policies and cross-account access.            |
| Version 2019.11.21 (Current) global tables APIs                                                                                                                | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeTableReplicaAutoScaling](../APIReference/API_DescribeTableReplicaAutoScaling.md "../APIReference/API_DescribeTableReplicaAutoScaling.md")             | Yes                           | No                    |
| [UpdateTableReplicaAutoScaling](../APIReference/API_UpdateTableReplicaAutoScaling.md "../APIReference/API_UpdateTableReplicaAutoScaling.md")                   | Yes                           | No                    | ## Version 2017.11.29 (Legacy) global tables API operations The following table lists the API-level support provided by [Version 2017.11.29 (Legacy) global tables](globaltables.md "globaltables.md") API operations for resource-based policies and cross-account access.              |
| Version 2017.11.29 (Legacy) global tables APIs                                                                                                                 | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [CreateGlobalTable](../APIReference/API_CreateGlobalTable.md "../APIReference/API_CreateGlobalTable.md")                                                       | No                            | No                    |
| [DescribeGlobalTable](../APIReference/API_DescribeGlobalTable.md "../APIReference/API_DescribeGlobalTable.md")                                                 | No                            | No                    |
| [DescribeGlobalTableSettings](../APIReference/API_DescribeGlobalTableSettings.md "../APIReference/API_DescribeGlobalTableSettings.md")                         | No                            | No                    |
| [ListGlobalTables](../APIReference/API_ListGlobalTables.md "../APIReference/API_ListGlobalTables.md")                                                          | No                            | No                    |
| [UpdateGlobalTable](../APIReference/API_UpdateGlobalTable.md "../APIReference/API_UpdateGlobalTable.md")                                                       | No                            | No                    |
| [UpdateGlobalTableSettings](../APIReference/API_UpdateGlobalTableSettings.md "../APIReference/API_UpdateGlobalTableSettings.md")                               | No                            | No                    | ## Tags API operations The following table lists the API-level support provided by API operations related to [tags](Tagging.md "Tagging.md") for resource-based policies and cross-account access.                                                                                       |
| Tags APIs                                                                                                                                                      | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [ListTagsOfResource](../APIReference/API_ListTagsOfResource.md "../APIReference/API_ListTagsOfResource.md")                                                    | Yes                           | Yes                   |
| [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")                                                                         | Yes                           | Yes                   |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")                                                                   | Yes                           | Yes                   | ## Backup and Restore API operations The following table lists the API-level support provided by API operations related to [backup and restore](Backup-and-Restore.md "Backup-and-Restore.md") for resource-based policies and cross-account access.                                     |
| Backup and Restore APIs                                                                                                                                        | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [CreateBackup](../APIReference/API_CreateBackup.md "../APIReference/API_CreateBackup.md")                                                                      | Yes                           | No                    |
| [DescribeBackup](../APIReference/API_DescribeBackup.md "../APIReference/API_DescribeBackup.md")                                                                | No                            | No                    |
| [DeleteBackup](../APIReference/API_DeleteBackup.md "../APIReference/API_DeleteBackup.md")                                                                      | No                            | No                    |
| [RestoreTableFromBackup](../APIReference/API_RestoreTableFromBackup.md "../APIReference/API_RestoreTableFromBackup.md")                                        | No                            | No                    | ## Continuous Backup/Restore (PITR) API operations The following table lists the API-level support provided by API operations related to [Continuous Backup/Restore (PITR)](Point-in-time-recovery.md "Point-in-time-recovery.md") for resource-based policies and cross-account access. |
| Continuous Backup/Restore (PITR) APIs                                                                                                                          | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeContinuousBackups](../APIReference/API_DescribeContinuousBackups.md "../APIReference/API_DescribeContinuousBackups.md")                               | Yes                           | No                    |
| [RestoreTableToPointInTime](../APIReference/API_RestoreTableToPointInTime.md "../APIReference/API_RestoreTableToPointInTime.md")                               | Yes                           | No                    |
| [UpdateContinuousBackups](../APIReference/API_UpdateContinuousBackups.md "../APIReference/API_UpdateContinuousBackups.md")                                     | Yes                           | No                    | ## Contributor Insights API operations The following table lists the API-level support provided by API operations related to [Continuous Backup/Restore (PITR)](Point-in-time-recovery.md "Point-in-time-recovery.md") for resource-based policies and cross-account access.             |
| Contributor Insights APIs                                                                                                                                      | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeContributorInsights](../APIReference/API_DescribeContributorInsights.md "../APIReference/API_DescribeContributorInsights.md")                         | Yes                           | No                    |
| [ListContributorInsights](../APIReference/API_ListContributorInsights.md "../APIReference/API_ListContributorInsights.md")                                     | No                            | No                    |
| [UpdateContributorInsights](../APIReference/API_UpdateContributorInsights.md "../APIReference/API_UpdateContributorInsights.md")                               | Yes                           | No                    | ## Export API operations The following table lists the API-level support provided by Export API operations for resource-based policies and cross-account access.                                                                                                                         |
| Export APIs                                                                                                                                                    | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeExport](../APIReference/API_DescribeExport.md "../APIReference/API_DescribeExport.md")                                                                | No                            | No                    |
| [ExportTableToPointInTime](../APIReference/API_ExportTableToPointInTime.md "../APIReference/API_ExportTableToPointInTime.md")                                  | Yes                           | No                    |
| [ListExports](../APIReference/API_ListExports.md "../APIReference/API_ListExports.md")                                                                         | No                            | No                    | ## Import API operations The following table lists the API-level support provided by Import API operations for resource-based policies and cross-account access.                                                                                                                         |
| Import APIs                                                                                                                                                    | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeImport](../APIReference/API_DescribeImport.md "../APIReference/API_DescribeImport.md")                                                                | No                            | No                    |
| [ImportTable](../APIReference/API_ImportTable.md "../APIReference/API_ImportTable.md")                                                                         | No                            | No                    |
| [ListImports](../APIReference/API_ListImports.md "../APIReference/API_ListImports.md")                                                                         | No                            | No                    | ## Amazon Kinesis Data Streams API operations The following table lists the API-level support provided by Kinesis Data Streams API operations for resource-based policies and cross-account access.                                                                                      |
| Kinesis APIs                                                                                                                                                   | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeKinesisStreamingDestination](../APIReference/API_DescribeKinesisStreamingDestination.md "../APIReference/API_DescribeKinesisStreamingDestination.md") | Yes                           | No                    |
| [DisableKinesisStreamingDestination](../APIReference/API_DisableKinesisStreamingDestination.md "../APIReference/API_DisableKinesisStreamingDestination.md")    | Yes                           | No                    |
| [EnableKinesisStreamingDestination](../APIReference/API_EnableKinesisStreamingDestination.md "../APIReference/API_EnableKinesisStreamingDestination.md")       | Yes                           | No                    |
| [UpdateKinesisStreamingDestination](../APIReference/API_UpdateKinesisStreamingDestination.md "../APIReference/API_UpdateKinesisStreamingDestination.md")       | Yes                           | No                    | ## Resource-based policy API operations The following table lists the API-level support provided by resource-based policy API operations for resource-based policies and cross-account access.                                                                                           |
| Resource-based policy APIs                                                                                                                                     | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [GetResourcePolicy](../APIReference/API_GetResourcePolicy.md "../APIReference/API_GetResourcePolicy.md")                                                       | Yes                           | No                    |
| [PutResourcePolicy](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md")                                                       | Yes                           | No                    |
| [DeleteResourcePolicy](../APIReference/API_DeleteResourcePolicy.md "../APIReference/API_DeleteResourcePolicy.md")                                              | Yes                           | No                    | ## Time-to-Live API operations The following table lists the API-level support provided by [time to live](TTL.md "TTL.md") (TTL) API operations for resource-based policies and cross-account access.                                                                                    |
| TTL APIs                                                                                                                                                       | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeTimeToLive](../APIReference/API_DescribeTimeToLive.md "../APIReference/API_DescribeTimeToLive.md")                                                    | Yes                           | No                    |
| [UpdateTimeToLive](../APIReference/API_UpdateTimeToLive.md "../APIReference/API_UpdateTimeToLive.md")                                                          | Yes                           | No                    | ## Other API operations The following table lists the API-level support provided by other miscellaneous API operations for resource-based policies and cross-account access.                                                                                                             |
| Other APIs                                                                                                                                                     | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeLimits](../APIReference/API_DescribeLimits.md "../APIReference/API_DescribeLimits.md")                                                                | No                            | No                    |
| [DescribeEndpoints](../APIReference/API_DescribeEndpoints.md "../APIReference/API_DescribeEndpoints.md")                                                       | No                            | No                    |
| [ListBackups](../APIReference/API_ListBackups.md "../APIReference/API_ListBackups.md")                                                                         | No                            | No                    |
| [ListTables](../APIReference/API_ListTables.md "../APIReference/API_ListTables.md")                                                                            | No                            | No                    | ## DynamoDB Streams API operations The following table lists the API-level support of DynamoDB Streams APIs for resource-based policies and cross-account access.                                                                                                                        |
| DynamoDB Streams APIs                                                                                                                                          | Resource-based policy support | Cross-account support |
| ---                                                                                                                                                            | ---                           | ---                   |
| [DescribeStream](../APIReference/API_streams_DescribeStream.md "../APIReference/API_streams_DescribeStream.md")                                                | Yes                           | Yes                   |
| [GetRecords](../APIReference/API_streams_GetRecords.md "../APIReference/API_streams_GetRecords.md")                                                            | Yes                           | Yes                   |
| [GetShardIterator](../APIReference/API_streams_GetShardIterator.md "../APIReference/API_streams_GetShardIterator.md")                                          | Yes                           | Yes                   |
| [ListStreams](../APIReference/API_streams_ListStreams.md "../APIReference/API_streams_ListStreams.md")                                                         | No                            | No                    |
