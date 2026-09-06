

# Data retrieval APIs for AWS Backup
<a name="awsbackup"></a>

AWS Backup provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="backup-DescribeBackupAccessPoint"></a>[DescribeBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupAccessPoint.html) | Return information about the specified backup access point | Read | 
| <a name="backup-DescribeBackupJob"></a>[DescribeBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupJob.html) | Describe a backup job | Read | 
| <a name="backup-DescribeBackupVault"></a>[DescribeBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupVault.html) | Describe a new backup vault with the specified name | Read | 
| <a name="backup-DescribeCopyJob"></a>[DescribeCopyJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeCopyJob.html) | Describe a copy job | Read | 
| <a name="backup-DescribeFramework"></a>[DescribeFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeFramework.html) | Describe a framework with the specified name | Read | 
| <a name="backup-DescribeGlobalSettings"></a>[DescribeGlobalSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeGlobalSettings.html) | Describe global settings | Read | 
| <a name="backup-DescribeProtectedResource"></a>[DescribeProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeProtectedResource.html) | Describe a protected resource | Read | 
| <a name="backup-DescribeRecoveryPoint"></a>[DescribeRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRecoveryPoint.html) | Describe a recovery point | Read | 
| <a name="backup-DescribeRegionSettings"></a>[DescribeRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRegionSettings.html) | Describe region settings | Read | 
| <a name="backup-DescribeReportJob"></a>[DescribeReportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeReportJob.html) | Describe a report job | Read | 
| <a name="backup-DescribeReportPlan"></a>[DescribeReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeReportPlan.html) | Describe a report plan with the specified name | Read | 
| <a name="backup-DescribeRestoreJob"></a>[DescribeRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRestoreJob.html) | Describe a restore job | Read | 
| <a name="backup-DescribeScanJob"></a>[DescribeScanJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeScanJob.html) | Describe a scan job | Read | 
| <a name="backup-ExportBackupPlanTemplate"></a>[ExportBackupPlanTemplate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ExportBackupPlanTemplate.html) | Export a backup plan as a JSON | Read | 
| <a name="backup-GetBackupPlan"></a>[GetBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlan.html) | Get a backup plan | Read | 
| <a name="backup-GetBackupPlanFromJSON"></a>[GetBackupPlanFromJSON](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlanFromJSON.html) | Transform a JSON to a backup plan | Read | 
| <a name="backup-GetBackupPlanFromTemplate"></a>[GetBackupPlanFromTemplate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlanFromTemplate.html) | Transform a template to a backup plan | Read | 
| <a name="backup-GetBackupSelection"></a>[GetBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupSelection.html) | Get a backup plan resource assignment | Read | 
| <a name="backup-GetBackupVaultAccessPolicy"></a>[GetBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupVaultAccessPolicy.html) | Get backup vault access policy | Read | 
| <a name="backup-GetBackupVaultNotifications"></a>[GetBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupVaultNotifications.html) | Get backup vault notifications | Read | 
| <a name="backup-GetBackupVaultSharingPolicy"></a>[GetBackupVaultSharingPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html) | Get backup vault sharing policy | Read | 
| <a name="backup-GetLegalHold"></a>[GetLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetLegalHold.html) | Get a legal hold | Read | 
| <a name="backup-GetPITRMalwareScanResults"></a>[GetPITRMalwareScanResults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetPITRMalwareScanResults.html) | Get point-in-time recovery (PITR) malware scan results | Read | 
| <a name="backup-GetRecoveryPointIndexDetails"></a>[GetRecoveryPointIndexDetails](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRecoveryPointIndexDetails.html) | Get indexing details for a recovery point | Read | 
| <a name="backup-GetRecoveryPointRestoreMetadata"></a>[GetRecoveryPointRestoreMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRecoveryPointRestoreMetadata.html) | Get recovery point restore metadata | Read | 
| <a name="backup-GetRestoreJobMetadata"></a>[GetRestoreJobMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreJobMetadata.html) | Get the restore metadata associated with a restore job | Read | 
| <a name="backup-GetRestoreTestingInferredMetadata"></a>[GetRestoreTestingInferredMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingInferredMetadata.html) | Get inferred metadata generated by restore testing | Read | 
| <a name="backup-GetRestoreTestingPlan"></a>[GetRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingPlan.html) | Get a restore testing plan | Read | 
| <a name="backup-GetRestoreTestingSelection"></a>[GetRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingSelection.html) | Get a restore testing plan resource assignment | Read | 
| <a name="backup-GetSupportedResourceTypes"></a>[GetSupportedResourceTypes](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetSupportedResourceTypes.html) | Get supported resource types | Read | 
| <a name="backup-GetTieringConfiguration"></a>[GetTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetTieringConfiguration.html) | Describe a tiering configuration | Read | 
| <a name="backup-ListBackupAccessPoints"></a>[ListBackupAccessPoints](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupAccessPoints.html) | List backup access points in the caller's account | List | 
| <a name="backup-ListBackupAccessPointsByRecoveryPoint"></a>[ListBackupAccessPointsByRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupAccessPointsByRecoveryPoint.html) | List backup access points associated with a recovery point | List | 
| <a name="backup-ListBackupAccessPointsByResource"></a>[ListBackupAccessPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupAccessPointsByResource.html) | List backup access points associated with a resource | List | 
| <a name="backup-ListBackupJobSummaries"></a>[ListBackupJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobSummaries.html) | List backup job summaries | List | 
| <a name="backup-ListBackupJobs"></a>[ListBackupJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobs.html) | List backup jobs | List | 
| <a name="backup-ListBackupPlanTemplates"></a>[ListBackupPlanTemplates](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlanTemplates.html) | List backup plan templates provided by AWS Backup | List | 
| <a name="backup-ListBackupPlanVersions"></a>[ListBackupPlanVersions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlanVersions.html) | List backup plan versions | List | 
| <a name="backup-ListBackupPlans"></a>[ListBackupPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlans.html) | List backup plans | List | 
| <a name="backup-ListBackupSelections"></a>[ListBackupSelections](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupSelections.html) | List resource assignments for a specific backup plan | List | 
| <a name="backup-ListBackupVaults"></a>[ListBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupVaults.html) | List backup vaults | List | 
| <a name="backup-ListCopyJobSummaries"></a>[ListCopyJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListCopyJobSummaries.html) | List copy job summaries | List | 
| <a name="backup-ListCopyJobs"></a>[ListCopyJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListCopyJobs.html) | List copy jobs | List | 
| <a name="backup-ListFrameworks"></a>[ListFrameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListFrameworks.html) | List frameworks | List | 
| <a name="backup-ListIndexedRecoveryPoints"></a>[ListIndexedRecoveryPoints](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListIndexedRecoveryPoints.html) | Get list indexed recovery points | List | 
| <a name="backup-ListLegalHolds"></a>[ListLegalHolds](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListLegalHolds.html) | List legal holds | List | 
| <a name="backup-ListProtectedResources"></a>[ListProtectedResources](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListProtectedResources.html) | List protected resources by AWS Backup | List | 
| <a name="backup-ListProtectedResourcesByBackupVault"></a>[ListProtectedResourcesByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListProtectedResourcesByBackupVault.html) | List protected resources inside a backup vault | List | 
| <a name="backup-ListRecoveryPointsByBackupVault"></a>[ListRecoveryPointsByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByBackupVault.html) | List recovery points inside a backup vault | List | 
| <a name="backup-ListRecoveryPointsByLegalHold"></a>[ListRecoveryPointsByLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByLegalHold.html) | List recovery points by legal hold | List | 
| <a name="backup-ListRecoveryPointsByResource"></a>[ListRecoveryPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByResource.html) | List recovery points for a resource | List | 
| <a name="backup-ListReportJobs"></a>[ListReportJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListReportJobs.html) | List report jobs | List | 
| <a name="backup-ListReportPlans"></a>[ListReportPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListReportPlans.html) | List report plans | List | 
| <a name="backup-ListRestoreAccessBackupVaults"></a>[ListRestoreAccessBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreAccessBackupVaults.html) | List a restore access backup vaults associated with a backup vault | List | 
| <a name="backup-ListRestoreJobSummaries"></a>[ListRestoreJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobSummaries.html) | List restore job summaries | List | 
| <a name="backup-ListRestoreJobs"></a>[ListRestoreJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobs.html) | List restore jobs | List | 
| <a name="backup-ListRestoreJobsByProtectedResource"></a>[ListRestoreJobsByProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobsByProtectedResource.html) | List restore jobs for a protected resource | List | 
| <a name="backup-ListRestoreTestingPlans"></a>[ListRestoreTestingPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreTestingPlans.html) | List restore testing plans | List | 
| <a name="backup-ListRestoreTestingSelections"></a>[ListRestoreTestingSelections](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreTestingSelections.html) | List resource assignments for a specific restore testing plan | List | 
| <a name="backup-ListScanJobSummaries"></a>[ListScanJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListScanJobSummaries.html) | List scan job summaries | List | 
| <a name="backup-ListScanJobs"></a>[ListScanJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListScanJobs.html) | List scan jobs | List | 
| <a name="backup-ListTags"></a>[ListTags](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTags.html) | List tags for a resource | Read | 
| <a name="backup-ListTieringConfigurations"></a>[ListTieringConfigurations](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTieringConfigurations.html) | List tiering configurations | List | 