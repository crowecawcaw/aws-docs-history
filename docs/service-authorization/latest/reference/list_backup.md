

# Actions, resources, and condition keys for AWS Backup
<a name="list_backup"></a>

AWS Backup (service prefix: `backup`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-considerations.html#authentication) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/backup/backup.json) for this service.

**Topics**
+ [API operations defined by AWS Backup](#list_backup-operations)
+ [Actions defined by AWS Backup](#list_backup-actions-as-permissions)
+ [Permission-only actions for AWS Backup](#list_backup-permission-only-actions)
+ [Resource types defined by AWS Backup](#list_backup-resources-for-iam-policies)
+ [Condition keys for AWS Backup](#list_backup-policy-keys)

## API operations defined by AWS Backup
<a name="list_backup-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_backup-actions-as-permissions).




- **   AssociateBackupVaultMpaApprovalTeam  **
  - **IAM action:**  [backup:AssociateBackupVaultMpaApprovalTeam](#list_backup-action-AssociateBackupVaultMpaApprovalTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelLegalHold  **
  - **IAM action:**  [backup:CancelLegalHold](#list_backup-action-CancelLegalHold) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBackupAccessPoint  **
  - **IAM action:**  [backup:CreateBackupAccessPoint](#list_backup-action-CreateBackupAccessPoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateBackupPlan  **
  - **IAM action:**  [backup:CreateBackupPlan](#list_backup-action-CreateBackupPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** malware-protection.guardduty.amazonaws.com / **Access level:** Write

- **   CreateBackupSelection  **
  - **IAM action:**  [backup:CreateBackupSelection](#list_backup-action-CreateBackupSelection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup.amazonaws.com / **Access level:** Write

- **   CreateBackupVault  **
  - **IAM action:**  [backup:CreateBackupVault](#list_backup-action-CreateBackupVault)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFramework  **
  - **IAM action:**  [backup:CreateFramework](#list_backup-action-CreateFramework)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLegalHold  **
  - **IAM action:**  [backup:CreateLegalHold](#list_backup-action-CreateLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLogicallyAirGappedBackupVault  **
  - **IAM action:**  [backup:CreateLogicallyAirGappedBackupVault](#list_backup-action-CreateLogicallyAirGappedBackupVault)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateReportPlan  **
  - **IAM action:**  [backup:CreateReportPlan](#list_backup-action-CreateReportPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRestoreAccessBackupVault  **
  - **IAM action:**  [backup:CreateRestoreAccessBackupVault](#list_backup-action-CreateRestoreAccessBackupVault)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRestoreTestingPlan  **
  - **IAM action:**  [backup:CreateRestoreTestingPlan](#list_backup-action-CreateRestoreTestingPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRestoreTestingSelection  **
  - **IAM action:**  [backup:CreateRestoreTestingSelection](#list_backup-action-CreateRestoreTestingSelection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** restore-testing.backup.amazonaws.com / **Access level:** Write

- **   CreateTieringConfiguration  **
  - **IAM action:**  [backup:CreateTieringConfiguration](#list_backup-action-CreateTieringConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBackupAccessPoint  **
  - **IAM action:**  [backup:DeleteBackupAccessPoint](#list_backup-action-DeleteBackupAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBackupPlan  **
  - **IAM action:**  [backup:DeleteBackupPlan](#list_backup-action-DeleteBackupPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBackupSelection  **
  - **IAM action:**  [backup:DeleteBackupSelection](#list_backup-action-DeleteBackupSelection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBackupVault  **
  - **IAM action:**  [backup:DeleteBackupVault](#list_backup-action-DeleteBackupVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBackupVaultAccessPolicy  **
  - **IAM action:**  [backup:DeleteBackupVaultAccessPolicy](#list_backup-action-DeleteBackupVaultAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteBackupVaultLockConfiguration  **
  - **IAM action:**  [backup:DeleteBackupVaultLockConfiguration](#list_backup-action-DeleteBackupVaultLockConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBackupVaultNotifications  **
  - **IAM action:**  [backup:DeleteBackupVaultNotifications](#list_backup-action-DeleteBackupVaultNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFramework  **
  - **IAM action:**  [backup:DeleteFramework](#list_backup-action-DeleteFramework) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecoveryPoint  **
  - **IAM action:**  [backup:DeleteRecoveryPoint](#list_backup-action-DeleteRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReportPlan  **
  - **IAM action:**  [backup:DeleteReportPlan](#list_backup-action-DeleteReportPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRestoreTestingPlan  **
  - **IAM action:**  [backup:DeleteRestoreTestingPlan](#list_backup-action-DeleteRestoreTestingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRestoreTestingSelection  **
  - **IAM action:**  [backup:DeleteRestoreTestingSelection](#list_backup-action-DeleteRestoreTestingSelection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTieringConfiguration  **
  - **IAM action:**  [backup:DeleteTieringConfiguration](#list_backup-action-DeleteTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBackupAccessPoint  **
  - **IAM action:**  [backup:DescribeBackupAccessPoint](#list_backup-action-DescribeBackupAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBackupJob  **
  - **IAM action:**  [backup:DescribeBackupJob](#list_backup-action-DescribeBackupJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBackupVault  **
  - **IAM action:**  [backup:DescribeBackupVault](#list_backup-action-DescribeBackupVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCopyJob  **
  - **IAM action:**  [backup:DescribeCopyJob](#list_backup-action-DescribeCopyJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFramework  **
  - **IAM action:**  [backup:DescribeFramework](#list_backup-action-DescribeFramework) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGlobalSettings  **
  - **IAM action:**  [backup:DescribeGlobalSettings](#list_backup-action-DescribeGlobalSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProtectedResource  **
  - **IAM action:**  [backup:DescribeProtectedResource](#list_backup-action-DescribeProtectedResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecoveryPoint  **
  - **IAM action:**  [backup:DescribeRecoveryPoint](#list_backup-action-DescribeRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegionSettings  **
  - **IAM action:**  [backup:DescribeRegionSettings](#list_backup-action-DescribeRegionSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReportJob  **
  - **IAM action:**  [backup:DescribeReportJob](#list_backup-action-DescribeReportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReportPlan  **
  - **IAM action:**  [backup:DescribeReportPlan](#list_backup-action-DescribeReportPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRestoreJob  **
  - **IAM action:**  [backup:DescribeRestoreJob](#list_backup-action-DescribeRestoreJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScanJob  **
  - **IAM action:**  [backup:DescribeScanJob](#list_backup-action-DescribeScanJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateBackupVaultMpaApprovalTeam  **
  - **IAM action:**  [backup:DisassociateBackupVaultMpaApprovalTeam](#list_backup-action-DisassociateBackupVaultMpaApprovalTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateRecoveryPoint  **
  - **IAM action:**  [backup:DisassociateRecoveryPoint](#list_backup-action-DisassociateRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateRecoveryPointFromParent  **
  - **IAM action:**  [backup:DisassociateRecoveryPointFromParent](#list_backup-action-DisassociateRecoveryPointFromParent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportBackupPlanTemplate  **
  - **IAM action:**  [backup:ExportBackupPlanTemplate](#list_backup-action-ExportBackupPlanTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackupPlan  **
  - **IAM action:**  [backup:GetBackupPlan](#list_backup-action-GetBackupPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackupPlanFromJSON  **
  - **IAM action:**  [backup:GetBackupPlanFromJSON](#list_backup-action-GetBackupPlanFromJSON) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackupPlanFromTemplate  **
  - **IAM action:**  [backup:GetBackupPlanFromTemplate](#list_backup-action-GetBackupPlanFromTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackupSelection  **
  - **IAM action:**  [backup:GetBackupSelection](#list_backup-action-GetBackupSelection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackupVaultAccessPolicy  **
  - **IAM action:**  [backup:GetBackupVaultAccessPolicy](#list_backup-action-GetBackupVaultAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackupVaultNotifications  **
  - **IAM action:**  [backup:GetBackupVaultNotifications](#list_backup-action-GetBackupVaultNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLegalHold  **
  - **IAM action:**  [backup:GetLegalHold](#list_backup-action-GetLegalHold) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPITRMalwareScanResults  **
  - **IAM action:**  [backup:GetPITRMalwareScanResults](#list_backup-action-GetPITRMalwareScanResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryPointIndexDetails  **
  - **IAM action:**  [backup:GetRecoveryPointIndexDetails](#list_backup-action-GetRecoveryPointIndexDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryPointRestoreMetadata  **
  - **IAM action:**  [backup:GetRecoveryPointRestoreMetadata](#list_backup-action-GetRecoveryPointRestoreMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRestoreJobMetadata  **
  - **IAM action:**  [backup:GetRestoreJobMetadata](#list_backup-action-GetRestoreJobMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRestoreTestingInferredMetadata  **
  - **IAM action:**  [backup:GetRestoreTestingInferredMetadata](#list_backup-action-GetRestoreTestingInferredMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRestoreTestingPlan  **
  - **IAM action:**  [backup:GetRestoreTestingPlan](#list_backup-action-GetRestoreTestingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRestoreTestingSelection  **
  - **IAM action:**  [backup:GetRestoreTestingSelection](#list_backup-action-GetRestoreTestingSelection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSupportedResourceTypes  **
  - **IAM action:**  [backup:GetSupportedResourceTypes](#list_backup-action-GetSupportedResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTieringConfiguration  **
  - **IAM action:**  [backup:GetTieringConfiguration](#list_backup-action-GetTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBackupAccessPoints  **
  - **IAM action:**  [backup:ListBackupAccessPoints](#list_backup-action-ListBackupAccessPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupAccessPointsByRecoveryPoint  **
  - **IAM action:**  [backup:ListBackupAccessPointsByRecoveryPoint](#list_backup-action-ListBackupAccessPointsByRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupAccessPointsByResource  **
  - **IAM action:**  [backup:ListBackupAccessPointsByResource](#list_backup-action-ListBackupAccessPointsByResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupJobSummaries  **
  - **IAM action:**  [backup:ListBackupJobSummaries](#list_backup-action-ListBackupJobSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupJobs  **
  - **IAM action:**  [backup:ListBackupJobs](#list_backup-action-ListBackupJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupPlanTemplates  **
  - **IAM action:**  [backup:ListBackupPlanTemplates](#list_backup-action-ListBackupPlanTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupPlanVersions  **
  - **IAM action:**  [backup:ListBackupPlanVersions](#list_backup-action-ListBackupPlanVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupPlans  **
  - **IAM action:**  [backup:ListBackupPlans](#list_backup-action-ListBackupPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupSelections  **
  - **IAM action:**  [backup:ListBackupSelections](#list_backup-action-ListBackupSelections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackupVaults  **
  - **IAM action:**  [backup:ListBackupVaults](#list_backup-action-ListBackupVaults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCopyJobSummaries  **
  - **IAM action:**  [backup:ListCopyJobSummaries](#list_backup-action-ListCopyJobSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCopyJobs  **
  - **IAM action:**  [backup:ListCopyJobs](#list_backup-action-ListCopyJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFrameworks  **
  - **IAM action:**  [backup:ListFrameworks](#list_backup-action-ListFrameworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIndexedRecoveryPoints  **
  - **IAM action:**  [backup:ListIndexedRecoveryPoints](#list_backup-action-ListIndexedRecoveryPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLegalHolds  **
  - **IAM action:**  [backup:ListLegalHolds](#list_backup-action-ListLegalHolds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtectedResources  **
  - **IAM action:**  [backup:ListProtectedResources](#list_backup-action-ListProtectedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtectedResourcesByBackupVault  **
  - **IAM action:**  [backup:ListProtectedResourcesByBackupVault](#list_backup-action-ListProtectedResourcesByBackupVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecoveryPointsByBackupVault  **
  - **IAM action:**  [backup:ListRecoveryPointsByBackupVault](#list_backup-action-ListRecoveryPointsByBackupVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecoveryPointsByLegalHold  **
  - **IAM action:**  [backup:ListRecoveryPointsByLegalHold](#list_backup-action-ListRecoveryPointsByLegalHold) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecoveryPointsByResource  **
  - **IAM action:**  [backup:ListRecoveryPointsByResource](#list_backup-action-ListRecoveryPointsByResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReportJobs  **
  - **IAM action:**  [backup:ListReportJobs](#list_backup-action-ListReportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReportPlans  **
  - **IAM action:**  [backup:ListReportPlans](#list_backup-action-ListReportPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRestoreAccessBackupVaults  **
  - **IAM action:**  [backup:ListRestoreAccessBackupVaults](#list_backup-action-ListRestoreAccessBackupVaults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRestoreJobSummaries  **
  - **IAM action:**  [backup:ListRestoreJobSummaries](#list_backup-action-ListRestoreJobSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRestoreJobs  **
  - **IAM action:**  [backup:ListRestoreJobs](#list_backup-action-ListRestoreJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRestoreJobsByProtectedResource  **
  - **IAM action:**  [backup:ListRestoreJobsByProtectedResource](#list_backup-action-ListRestoreJobsByProtectedResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRestoreTestingPlans  **
  - **IAM action:**  [backup:ListRestoreTestingPlans](#list_backup-action-ListRestoreTestingPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRestoreTestingSelections  **
  - **IAM action:**  [backup:ListRestoreTestingSelections](#list_backup-action-ListRestoreTestingSelections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScanJobSummaries  **
  - **IAM action:**  [backup:ListScanJobSummaries](#list_backup-action-ListScanJobSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScanJobs  **
  - **IAM action:**  [backup:ListScanJobs](#list_backup-action-ListScanJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **IAM action:**  [backup:ListTags](#list_backup-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTieringConfigurations  **
  - **IAM action:**  [backup:ListTieringConfigurations](#list_backup-action-ListTieringConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutBackupVaultAccessPolicy  **
  - **IAM action:**  [backup:PutBackupVaultAccessPolicy](#list_backup-action-PutBackupVaultAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutBackupVaultLockConfiguration  **
  - **IAM action:**  [backup:PutBackupVaultLockConfiguration](#list_backup-action-PutBackupVaultLockConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBackupVaultNotifications  **
  - **IAM action:**  [backup:PutBackupVaultNotifications](#list_backup-action-PutBackupVaultNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRestoreValidationResult  **
  - **IAM action:**  [backup:PutRestoreValidationResult](#list_backup-action-PutRestoreValidationResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeRestoreAccessBackupVault  **
  - **IAM action:**  [backup:RevokeRestoreAccessBackupVault](#list_backup-action-RevokeRestoreAccessBackupVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBackupJob  **
  - **IAM action:**  [backup:StartBackupJob](#list_backup-action-StartBackupJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup.amazonaws.com / **Access level:** Write

- **   StartCopyJob  **
  - **IAM action:**  [backup:StartCopyJob](#list_backup-action-StartCopyJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup.amazonaws.com / **Access level:** Write

- **   StartReportJob  **
  - **IAM action:**  [backup:StartReportJob](#list_backup-action-StartReportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRestoreJob  **
  - **IAM action:**  [backup:StartRestoreJob](#list_backup-action-StartRestoreJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup.amazonaws.com / **Access level:** Write

- **   StartScanJob  **
  - **IAM action:**  [backup:StartScanJob](#list_backup-action-StartScanJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup.amazonaws.com, malware-protection.guardduty.amazonaws.com / **Access level:** Write

- **   StopBackupJob  **
  - **IAM action:**  [backup:StopBackupJob](#list_backup-action-StopBackupJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [backup:TagResource](#list_backup-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [backup:UntagResource](#list_backup-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBackupPlan  **
  - **IAM action:**  [backup:UpdateBackupPlan](#list_backup-action-UpdateBackupPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** malware-protection.guardduty.amazonaws.com / **Access level:** Write

- **   UpdateFramework  **
  - **IAM action:**  [backup:UpdateFramework](#list_backup-action-UpdateFramework) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlobalSettings  **
  - **IAM action:**  [backup:UpdateGlobalSettings](#list_backup-action-UpdateGlobalSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecoveryPointIndexSettings  **
  - **IAM action:**  [backup:UpdateRecoveryPointIndexSettings](#list_backup-action-UpdateRecoveryPointIndexSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup.amazonaws.com / **Access level:** Write

- **   UpdateRecoveryPointLifecycle  **
  - **IAM action:**  [backup:UpdateRecoveryPointLifecycle](#list_backup-action-UpdateRecoveryPointLifecycle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegionSettings  **
  - **IAM action:**  [backup:UpdateRegionSettings](#list_backup-action-UpdateRegionSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReportPlan  **
  - **IAM action:**  [backup:UpdateReportPlan](#list_backup-action-UpdateReportPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRestoreTestingPlan  **
  - **IAM action:**  [backup:UpdateRestoreTestingPlan](#list_backup-action-UpdateRestoreTestingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRestoreTestingSelection  **
  - **IAM action:**  [backup:UpdateRestoreTestingSelection](#list_backup-action-UpdateRestoreTestingSelection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** restore-testing.backup.amazonaws.com / **Access level:** Write

- **   UpdateTieringConfiguration  **
  - **IAM action:**  [backup:UpdateTieringConfiguration](#list_backup-action-UpdateTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Backup
<a name="list_backup-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateBackupVaultMpaApprovalTeam](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_AssociateBackupVaultMpaApprovalTeam.html)  **
  - **Description:** Grants permission to associate an MPA approval team with a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[backup:MpaApprovalTeamArn](#list_backup-backup_MpaApprovalTeamArn)
  - **Access level:** Write

- **   [CancelLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CancelLegalHold.html)  **
  - **Description:** Grants permission to cancel a legal hold
  - **Resource types (\*required):** [legalHold\*](#list_backup-resource-legalHold)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupAccessPoint.html)  **
  - **Description:** Grants permission to create a new backup access point
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupPlan.html)  **
  - **Description:** Grants permission to create a new backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupSelection.html)  **
  - **Description:** Grants permission to create a new resource assignment in a backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupVault.html)  **
  - **Description:** Grants permission to create a new backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateFramework.html)  **
  - **Description:** Grants permission to create a new framework
  - **Resource types (\*required):** [framework\*](#list_backup-resource-framework)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateLegalHold.html)  **
  - **Description:** Grants permission to create a new legal hold
  - **Resource types (\*required):** [legalHold\*](#list_backup-resource-legalHold)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLogicallyAirGappedBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateLogicallyAirGappedBackupVault.html)  **
  - **Description:** Grants permission to create a new logically air-gapped backup vault, a logical container where backups are stored
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)<br />[backup:MaxRetentionDays](#list_backup-backup_MaxRetentionDays)<br />[backup:MinRetentionDays](#list_backup-backup_MinRetentionDays)
  - **Access level:** Write

- **   [CreateReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateReportPlan.html)  **
  - **Description:** Grants permission to create a new report plan
  - **Resource types (\*required):** [reportPlan\*](#list_backup-resource-reportPlan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)<br />[backup:FrameworkArns](#list_backup-backup_FrameworkArns)
  - **Access level:** Write

- **   [CreateRestoreAccessBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateRestoreAccessBackupVault.html)  **
  - **Description:** Grants permission to create a restore access backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateRestoreTestingPlan.html)  **
  - **Description:** Grants permission to create a new restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateRestoreTestingSelection.html)  **
  - **Description:** Grants permission to create a new resource assignment in a restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateTieringConfiguration.html)  **
  - **Description:** Grants permission to create a new tiering configuration
  - **Resource types (\*required):** [tieringConfiguration\*](#list_backup-resource-tieringConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupAccessPoint.html)  **
  - **Description:** Grants permission to delete the backup access point
  - **Resource types (\*required):** [backupAccessPoint\*](#list_backup-resource-backupAccessPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupPlan.html)  **
  - **Description:** Grants permission to delete a backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupSelection.html)  **
  - **Description:** Grants permission to delete a resource assignment from a backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVault.html)  **
  - **Description:** Grants permission to delete a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVaultAccessPolicy.html)  **
  - **Description:** Grants permission to delete backup vault access policy
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteBackupVaultLockConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVaultLockConfiguration.html)  **
  - **Description:** Grants permission to remove the lock configuration from a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVaultNotifications.html)  **
  - **Description:** Grants permission to remove the notifications from a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteFramework.html)  **
  - **Description:** Grants permission to delete a framework
  - **Resource types (\*required):** [framework\*](#list_backup-resource-framework)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteRecoveryPoint.html)  **
  - **Description:** Grants permission to delete a recovery point from a backup vault
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteReportPlan.html)  **
  - **Description:** Grants permission to delete a report plan
  - **Resource types (\*required):** [reportPlan\*](#list_backup-resource-reportPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteRestoreTestingPlan.html)  **
  - **Description:** Grants permission to delete a restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteRestoreTestingSelection.html)  **
  - **Description:** Grants permission to delete a resource assignment from a restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteTieringConfiguration.html)  **
  - **Description:** Grants permission to delete a tiering configuration
  - **Resource types (\*required):** [tieringConfiguration\*](#list_backup-resource-tieringConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupAccessPoint.html)  **
  - **Description:** Grants permission to return information about the specified backup access point
  - **Resource types (\*required):** [backupAccessPoint\*](#list_backup-resource-backupAccessPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupJob.html)  **
  - **Description:** Grants permission to describe a backup job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupVault.html)  **
  - **Description:** Grants permission to describe a new backup vault with the specified name
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCopyJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeCopyJob.html)  **
  - **Description:** Grants permission to describe a copy job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeFramework.html)  **
  - **Description:** Grants permission to describe a framework with the specified name
  - **Resource types (\*required):** [framework\*](#list_backup-resource-framework)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGlobalSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeGlobalSettings.html)  **
  - **Description:** Grants permission to describe global settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeProtectedResource.html)  **
  - **Description:** Grants permission to describe a protected resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRecoveryPoint.html)  **
  - **Description:** Grants permission to describe a recovery point
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRegionSettings.html)  **
  - **Description:** Grants permission to describe region settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeReportJob.html)  **
  - **Description:** Grants permission to describe a report job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeReportPlan.html)  **
  - **Description:** Grants permission to describe a report plan with the specified name
  - **Resource types (\*required):** [reportPlan\*](#list_backup-resource-reportPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRestoreJob.html)  **
  - **Description:** Grants permission to describe a restore job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeScanJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeScanJob.html)  **
  - **Description:** Grants permission to describe a scan job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateBackupVaultMpaApprovalTeam](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DisassociateBackupVaultMpaApprovalTeam.html)  **
  - **Description:** Grants permission to disassociate an MPA approval team from a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DisassociateRecoveryPoint.html)  **
  - **Description:** Grants permission to disassociate a recovery point from a backup vault
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateRecoveryPointFromParent](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DisassociateRecoveryPointFromParent.html)  **
  - **Description:** Grants permission to disassociate a recovery point from its parent
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportBackupPlanTemplate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ExportBackupPlanTemplate.html)  **
  - **Description:** Grants permission to export a backup plan as a JSON
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlan.html)  **
  - **Description:** Grants permission to get a backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBackupPlanFromJSON](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlanFromJSON.html)  **
  - **Description:** Grants permission to transform a JSON to a backup plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBackupPlanFromTemplate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlanFromTemplate.html)  **
  - **Description:** Grants permission to transform a template to a backup plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupSelection.html)  **
  - **Description:** Grants permission to get a backup plan resource assignment
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupVaultAccessPolicy.html)  **
  - **Description:** Grants permission to get backup vault access policy
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupVaultNotifications.html)  **
  - **Description:** Grants permission to get backup vault notifications
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetLegalHold.html)  **
  - **Description:** Grants permission to get a legal hold
  - **Resource types (\*required):** [legalHold\*](#list_backup-resource-legalHold)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPITRMalwareScanResults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetPITRMalwareScanResults.html)  **
  - **Description:** Grants permission to get point-in-time recovery (PITR) malware scan results
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPointIndexDetails](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRecoveryPointIndexDetails.html)  **
  - **Description:** Grants permission to get indexing details for a recovery point
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPointRestoreMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRecoveryPointRestoreMetadata.html)  **
  - **Description:** Grants permission to get recovery point restore metadata
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRestoreJobMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreJobMetadata.html)  **
  - **Description:** Grants permission to get the restore metadata associated with a restore job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRestoreTestingInferredMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingInferredMetadata.html)  **
  - **Description:** Grants permission to get inferred metadata generated by restore testing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingPlan.html)  **
  - **Description:** Grants permission to get a restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingSelection.html)  **
  - **Description:** Grants permission to get a restore testing plan resource assignment
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSupportedResourceTypes](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetSupportedResourceTypes.html)  **
  - **Description:** Grants permission to get supported resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetTieringConfiguration.html)  **
  - **Description:** Grants permission to describe a tiering configuration
  - **Resource types (\*required):** [tieringConfiguration\*](#list_backup-resource-tieringConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBackupAccessPoints](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupAccessPoints.html)  **
  - **Description:** Grants permission to list backup access points in the caller's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupAccessPointsByRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupAccessPointsByRecoveryPoint.html)  **
  - **Description:** Grants permission to list backup access points associated with a recovery point
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupAccessPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupAccessPointsByResource.html)  **
  - **Description:** Grants permission to list backup access points associated with a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobSummaries.html)  **
  - **Description:** Grants permission to list backup job summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobs.html)  **
  - **Description:** Grants permission to list backup jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupPlanTemplates](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlanTemplates.html)  **
  - **Description:** Grants permission to list backup plan templates provided by AWS Backup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupPlanVersions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlanVersions.html)  **
  - **Description:** Grants permission to list backup plan versions
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBackupPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlans.html)  **
  - **Description:** Grants permission to list backup plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBackupSelections](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupSelections.html)  **
  - **Description:** Grants permission to list resource assignments for a specific backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupVaults.html)  **
  - **Description:** Grants permission to list backup vaults
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCopyJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListCopyJobSummaries.html)  **
  - **Description:** Grants permission to list copy job summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCopyJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListCopyJobs.html)  **
  - **Description:** Grants permission to list copy jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFrameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListFrameworks.html)  **
  - **Description:** Grants permission to list frameworks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIndexedRecoveryPoints](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListIndexedRecoveryPoints.html)  **
  - **Description:** Grants permission to get list indexed recovery points
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLegalHolds](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListLegalHolds.html)  **
  - **Description:** Grants permission to list legal holds
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProtectedResources](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListProtectedResources.html)  **
  - **Description:** Grants permission to list protected resources by AWS Backup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProtectedResourcesByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListProtectedResourcesByBackupVault.html)  **
  - **Description:** Grants permission to list protected resources inside a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecoveryPointsByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByBackupVault.html)  **
  - **Description:** Grants permission to list recovery points inside a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecoveryPointsByLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByLegalHold.html)  **
  - **Description:** Grants permission to list recovery points by legal hold
  - **Resource types (\*required):** [legalHold\*](#list_backup-resource-legalHold)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecoveryPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByResource.html)  **
  - **Description:** Grants permission to list recovery points for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReportJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListReportJobs.html)  **
  - **Description:** Grants permission to list report jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReportPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListReportPlans.html)  **
  - **Description:** Grants permission to list report plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRestoreAccessBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreAccessBackupVaults.html)  **
  - **Description:** Grants permission to list a restore access backup vaults associated with a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRestoreJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobSummaries.html)  **
  - **Description:** Grants permission to list restore job summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRestoreJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobs.html)  **
  - **Description:** Grants permission to list restore jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRestoreJobsByProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobsByProtectedResource.html)  **
  - **Description:** Grants permission to list restore jobs for a protected resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRestoreTestingPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreTestingPlans.html)  **
  - **Description:** Grants permission to list restore testing plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRestoreTestingSelections](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreTestingSelections.html)  **
  - **Description:** Grants permission to list resource assignments for a specific restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListScanJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListScanJobSummaries.html)  **
  - **Description:** Grants permission to list scan job summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScanJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListScanJobs.html)  **
  - **Description:** Grants permission to list scan jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTags.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [backupAccessPoint](#list_backup-resource-backupAccessPoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [backupPlan](#list_backup-resource-backupPlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [backupVault](#list_backup-resource-backupVault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [framework](#list_backup-resource-framework) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [legalHold](#list_backup-resource-legalHold) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recoveryPoint](#list_backup-resource-recoveryPoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [reportPlan](#list_backup-resource-reportPlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [restoreTestingPlan](#list_backup-resource-restoreTestingPlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tieringConfiguration](#list_backup-resource-tieringConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTieringConfigurations](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTieringConfigurations.html)  **
  - **Description:** Grants permission to list tiering configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultAccessPolicy.html)  **
  - **Description:** Grants permission to add an access policy to the backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutBackupVaultLockConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultLockConfiguration.html)  **
  - **Description:** Grants permission to add a lock configuration to the backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[backup:ChangeableForDays](#list_backup-backup_ChangeableForDays)<br />[backup:MaxRetentionDays](#list_backup-backup_MaxRetentionDays)<br />[backup:MinRetentionDays](#list_backup-backup_MinRetentionDays)
  - **Access level:** Write

- **   [PutBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html)  **
  - **Description:** Grants permission to add an SNS topic to the backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRestoreValidationResult](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutRestoreValidationResult.html)  **
  - **Description:** Grants permission to put a restore validation result
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RevokeRestoreAccessBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RevokeRestoreAccessBackupVault.html)  **
  - **Description:** Grants permission to revoke a restore access backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartBackupJob.html)  **
  - **Description:** Grants permission to start a new backup job
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCopyJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartCopyJob.html)  **
  - **Description:** Grants permission to copy a backup from a source backup vault to a destination backup vault
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartReportJob.html)  **
  - **Description:** Grants permission to start a new report job
  - **Resource types (\*required):** [reportPlan\*](#list_backup-resource-reportPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartRestoreJob.html)  **
  - **Description:** Grants permission to start a new restore job
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartScanJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartScanJob.html)  **
  - **Description:** Grants permission to start a new scan job
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StopBackupJob.html)  **
  - **Description:** Grants permission to stop a backup job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [backupAccessPoint](#list_backup-resource-backupAccessPoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [backupPlan](#list_backup-resource-backupPlan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [backupVault](#list_backup-resource-backupVault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [framework](#list_backup-resource-framework) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [legalHold](#list_backup-resource-legalHold) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [recoveryPoint](#list_backup-resource-recoveryPoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [reportPlan](#list_backup-resource-reportPlan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [restoreTestingPlan](#list_backup-resource-restoreTestingPlan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [tieringConfiguration](#list_backup-resource-tieringConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [backupAccessPoint](#list_backup-resource-backupAccessPoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [backupPlan](#list_backup-resource-backupPlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [backupVault](#list_backup-resource-backupVault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [framework](#list_backup-resource-framework) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [legalHold](#list_backup-resource-legalHold) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [recoveryPoint](#list_backup-resource-recoveryPoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [reportPlan](#list_backup-resource-reportPlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [restoreTestingPlan](#list_backup-resource-restoreTestingPlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Resource types (\*required):** [tieringConfiguration](#list_backup-resource-tieringConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateBackupPlan.html)  **
  - **Description:** Grants permission to update a backup plan
  - **Resource types (\*required):** [backupPlan\*](#list_backup-resource-backupPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateFramework.html)  **
  - **Description:** Grants permission to update a framework
  - **Resource types (\*required):** [framework\*](#list_backup-resource-framework)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGlobalSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateGlobalSettings.html)  **
  - **Description:** Grants permission to update the current global settings for the AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRecoveryPointIndexSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRecoveryPointIndexSettings.html)  **
  - **Description:** Grants permission to update recovery point index settings
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[backup:Index](#list_backup-backup_Index)
  - **Access level:** Write

- **   [UpdateRecoveryPointLifecycle](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRecoveryPointLifecycle.html)  **
  - **Description:** Grants permission to update the lifecycle of the recovery point
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRegionSettings.html)  **
  - **Description:** Grants permission to update the current service opt-in settings for the Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateReportPlan.html)  **
  - **Description:** Grants permission to update a report plan
  - **Resource types (\*required):** [reportPlan\*](#list_backup-resource-reportPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[backup:FrameworkArns](#list_backup-backup_FrameworkArns)
  - **Access level:** Write

- **   [UpdateRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRestoreTestingPlan.html)  **
  - **Description:** Grants permission to update a restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRestoreTestingSelection.html)  **
  - **Description:** Grants permission to update a resource assignment in a restore testing plan
  - **Resource types (\*required):** [restoreTestingPlan\*](#list_backup-resource-restoreTestingPlan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateTieringConfiguration.html)  **
  - **Description:** Grants permission to update a tiering configuration
  - **Resource types (\*required):** [tieringConfiguration\*](#list_backup-resource-tieringConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Backup
<a name="list_backup-permission-only-actions"></a>

The following actions are defined by AWS Backup but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CopyFromBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html.html)  **
  - **Description:** Grants permission to copy from a backup vault
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)<br />[backup:CopyTargetOrgPaths](#list_backup-backup_CopyTargetOrgPaths)<br />[backup:CopyTargets](#list_backup-backup_CopyTargets)
  - **Access level:** Write

- **   [CopyIntoBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html)  **
  - **Description:** Grants permission to copy into a backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackupVaultSharingPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html)  **
  - **Description:** Grants permission to delete backup vault sharing policy
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [GetBackupVaultSharingPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html)  **
  - **Description:** Grants permission to get backup vault sharing policy
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIndexedRecoveryPointsForSearch](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListIndexedRecoveryPointsForSearch.html)  **
  - **Description:** Grants permission to list indexed recovery points to search
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutBackupVaultSharingPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html)  **
  - **Description:** Grants permission to add a sharing policy to the backup vault
  - **Resource types (\*required):** [backupVault\*](#list_backup-resource-backupVault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SearchRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_SearchRecoveryPoint.html)  **
  - **Description:** Grants permission to search a recovery point
  - **Resource types (\*required):** [recoveryPoint\*](#list_backup-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Backup
<a name="list_backup-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [backupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-access-points.html)  | arn:${Partition}:backup:${Region}:${Account}:accesspoint/${AccessPointName} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [backupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html)  | arn:${Partition}:backup:${Region}:${Account}:backup-plan:${BackupPlanId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [backupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html)  | arn:${Partition}:backup:${Region}:${Account}:backup-vault:${BackupVaultName} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [framework](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-frameworks.html)  | arn:${Partition}:backup:${Region}:${Account}:framework:${FrameworkName}-${FrameworkId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [legalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/legalhold.html)  | arn:${Partition}:backup:${Region}:${Account}:legal-hold:${LegalHoldId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [recoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html)  | arn:${Partition}:${Vendor}:${Region}:\*:${ResourceType}:${RecoveryPointId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [reportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-api.html)  | arn:${Partition}:backup:${Region}:${Account}:report-plan:${ReportPlanName}-${ReportPlanId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [restoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html)  | arn:${Partition}:backup:${Region}:${Account}:restore-testing-plan:${RestoreTestingPlanName}-${RestoreTestingPlanId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 
|  [tieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/tiering-configuration.html)  | arn:${Partition}:backup:${Region}:${Account}:tiering-configuration:${TieringConfigurationName}-${TieringConfigurationId} | [aws:ResourceTag/${TagKey}](#list_backup-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Backup
<a name="list_backup-policy-keys"></a>

AWS Backup defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 
|   [backup:ChangeableForDays](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the value of the ChangeableForDays parameter | Numeric | 
|   [backup:CopyTargetOrgPaths](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the organization unit | ArrayOfString | 
|   [backup:CopyTargets](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the ARN of a backup vault | ArrayOfARN | 
|   [backup:FrameworkArns](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the Framework ARNs | ArrayOfARN | 
|   [backup:Index](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the value of Index parameter | String | 
|   [backup:MaxRetentionDays](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the value of the MaxRetentionDays parameter | Numeric | 
|   [backup:MinRetentionDays](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the value of the MinRetentionDays parameter | Numeric | 
|   [backup:MpaApprovalTeamArn](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#amazon-backup-keys)  | Filters access by the MPA Approval Team ARN of a backup vault | ARN | 