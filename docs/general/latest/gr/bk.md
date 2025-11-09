# AWS Backup endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                      | Protocol       |
| -------------------------- | -------------- | ----------------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | backup.us-east-2.amazonaws.com<br>backup-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | backup.us-east-1.amazonaws.com<br>backup-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | backup.us-west-1.amazonaws.com<br>backup-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | backup.us-west-2.amazonaws.com<br>backup-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | backup.af-south-1.amazonaws.com                                               | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | backup.ap-east-1.amazonaws.com                                                | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | backup.ap-south-2.amazonaws.com                                               | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | backup.ap-southeast-3.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | backup.ap-southeast-5.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | backup.ap-southeast-4.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | backup.ap-south-1.amazonaws.com                                               | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | backup.ap-southeast-6.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | backup.ap-northeast-3.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | backup.ap-northeast-2.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | backup.ap-southeast-1.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | backup.ap-southeast-2.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | backup.ap-east-2.amazonaws.com                                                | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | backup.ap-southeast-7.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | backup.ap-northeast-1.amazonaws.com                                           | HTTPS          |
| Canada (Central)           | ca-central-1   | backup.ca-central-1.amazonaws.com<br>backup-fips.ca-central-1.amazonaws.com   | HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | backup.ca-west-1.amazonaws.com<br>backup-fips.ca-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | backup.eu-central-1.amazonaws.com                                             | HTTPS          |
| Europe (Ireland)           | eu-west-1      | backup.eu-west-1.amazonaws.com                                                | HTTPS          |
| Europe (London)            | eu-west-2      | backup.eu-west-2.amazonaws.com                                                | HTTPS          |
| Europe (Milan)             | eu-south-1     | backup.eu-south-1.amazonaws.com                                               | HTTPS          |
| Europe (Paris)             | eu-west-3      | backup.eu-west-3.amazonaws.com                                                | HTTPS          |
| Europe (Spain)             | eu-south-2     | backup.eu-south-2.amazonaws.com                                               | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | backup.eu-north-1.amazonaws.com                                               | HTTPS          |
| Europe (Zurich)            | eu-central-2   | backup.eu-central-2.amazonaws.com                                             | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | backup.il-central-1.amazonaws.com                                             | HTTPS          |
| Mexico (Central)           | mx-central-1   | backup.mx-central-1.amazonaws.com                                             | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | backup.me-south-1.amazonaws.com                                               | HTTPS          |
| Middle East (UAE)          | me-central-1   | backup.me-central-1.amazonaws.com                                             | HTTPS          |
| South America (São Paulo)  | sa-east-1      | backup.sa-east-1.amazonaws.com                                                | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | backup.us-gov-east-1.amazonaws.com<br>backup-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | backup.us-gov-west-1.amazonaws.com<br>backup-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                                       | Default                          | Adjustable                                                                                                                                                                       | Description                                                          |
| ---------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Backup plans per Region per account                        | Each supported Region: 300       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-BD69F607 "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-BD69F607") | Number of backup plans in this account in the current Region         |
| Backup vaults per Region per account                       | Each supported Region: 300       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-7705D2CB "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-7705D2CB") | Number of backup vaults in this account in the current Region        |
| Concurrent backup copies per supported service per account | Each supported Region: 5         | No                                                                                                                                                                               | Number of concurrent backup copies per supported service per account |
| Concurrent backup jobs per resource                        | Each supported Region: 1         | No                                                                                                                                                                               | Number of concurrent backup jobs per resource                        |
| Framework controls per Region per account                  | Each supported Region: 50        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-B4021FB0 "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-B4021FB0") | Number of framework controls in this account in the current Region   |
| Frameworks per Region per account                          | Each supported Region: 10        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-E43E0ED6 "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-E43E0ED6") | Number of frameworks in this account in the current Region           |
| Frameworks per report plan                                 | Each supported Region: 1,000     | No                                                                                                                                                                               | Number of frameworks per report plan                                 |
| Maximum backup nest level                                  | Each supported Region: 10        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-C0A8C14B "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-C0A8C14B") | Maximum number of nested levels allowed for backups                  |
| Metadata tags per backup                                   | Each supported Region: 50        | No                                                                                                                                                                               | Number of metadata tags per backup                                   |
| Recovery points per backup vault                           | Each supported Region: 1,000,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-514878B6 "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-514878B6") | Number of recovery points per backup vault                           |
| Report plans per Region per account                        | Each supported Region: 20        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-C296F1F5 "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-C296F1F5") | Number of report plans in this account in the current Region         |
| Versions per backup plan                                   | Each supported Region: 2,000     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-9122A82F "https://console.aws.amazon.com/servicequotas/home/services/backup/quotas/L-9122A82F") | Number of versions per backup plan                                   |

If you regularly receive throttling exceptions, consider using a rate limiter.

| API name             | Default calls/sec         |
| -------------------- | ------------------------- | ----------------------- | -------------------------- | --------------------- | ------------------------------ | ---------------------------------- | ----------------------------------- | ----------------------------------- | ---------------------------- | ----------------------------- | --------------------------- | ------------------ | --------------- | ------------- | --------------- | ------------- | ---------------- | -------------------------------- | --- |
| CreateBackupPlan     | CreateBackupSelection     | <br>DeleteBackupPlan    | DeleteBackupSelection      | <br>DeleteBackupVault | DeleteBackupVaultAccessPolicy  | <br>DeleteBackupVaultNotifications | DescribeBackupVault                 | <br>ExportBackupPlanTemplate        | GetBackupPlanFromJSON        | <br>GetBackupPlanFromTemplate | PutBackupVaultNotifications | <br>StartBackupJob | StartRestoreJob | StopBackupJob | <br>TagResource | UntagResource | UpdateBackupPlan | <br>UpdateRecoveryPointLifecycle | 5   |
| DeleteRecoveryPoint  | DescribeProtectedResource | 10                      |
| DescribeBackupJob    | DescribeRecoveryPoint     | <br>DescribeRestoreJob  | GetBackupPlan              | GetBackupSelection    | <br>GetBackupVaultAccessPolicy | GetBackupVaultNotifications        | <br>GetRecoveryPointRestoreMetadata | GetSupportedResourceTypes           | 15                           |
| ListBackupJobs       | ListBackupPlans           | ListBackupPlanTemplates | <br>ListBackupPlanVersions | ListBackupSelections  | ListBackupVaults               | <br>ListProtectedResources         | ListRecoveryPointByResource         | <br>ListRecoveryPointsByBackupVault | ListRecoveryPointsByResource | <br>ListRestoreJobs           | ListTags                    | 20                 |
| Sum of All API Calls | 50                        |

For additional information, see [Quotas](../../../aws-backup/latest/devguide/aws-backup-limits.md "../../../aws-backup/latest/devguide/aws-backup-limits.md") in the _AWS Backup Developer Guide_.
