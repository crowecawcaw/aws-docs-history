

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS Backup reports
<a name="reporting-backup"></a>

**Topics**
+ [Backup Job Success / Failure report](#reporting-backup-success-failure)
+ [Backup Summary report](#reporting-backup-summary)
+ [Backup Summary/Coverage report](#backup-summary-coverage)

## Backup Job Success / Failure report
<a name="reporting-backup-success-failure"></a>

The Backup Job Success/Failure report provides information about backups run in the last few weeks. To customize the report, specify the number of weeks that you want to retrieve data for. The default number of weeks is 12. The following table lists the data included in the report:


| **Field Name** | **Definition** | 
| --- | --- | 
| AWS Account ID | AWS Account ID to which the resource belongs | 
| Account Name | AWS account name | 
| Backup Job ID | The ID of the Backup job | 
| Resource ID | The ID of the backed-up resource  | 
| Resource Type | The type of resource that is being backed up | 
| Resource Region | The AWS Region of the backed up resource | 
| Backup State | The state of the backup. For more information, see [Backup job statuses ](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html#backup-job-statuses) | 
| Recovery Point ID | The unique identifier of the recovery point | 
| Status message | Description of errors or warnings that occurred during the backup job | 
| Backup Size | Size of the backup in GB | 
| Recovery Point ARN | The ARN of the created backup | 
| Recovery point age in days | Number of days that have passed since the recovery point was created | 
| Less than 30 days old | Indicator of backups that are less than 30 days old | 

## Backup Summary report
<a name="reporting-backup-summary"></a>


| **Field Name** | **Definition** | 
| --- | --- | 
| Customer Name | Customer name for situations where multiple sub-customers are | 
| Backup Month | Month of the backup | 
| Backup Year | Year of the backup | 
| Resource Type | The type of resource that is being backed up | 
| \# of Resources | The number of resources that were backed up | 
| \# of Recovery points | Number of distinct snapshots | 
| Backups less than 30 Days Old | The count of backups that are less than 30 days old | 
| Max Recovery point age | The oldest recovery point age in days | 
| Min Recovery point age | The most recent recovery point age in days  | 

## Backup Summary/Coverage report
<a name="backup-summary-coverage"></a>

The Backup Summary/Coverage report lists how many resources are not currently protected by any AWS Backup plan. Discuss with your CDSM an appropriate plan to increase coverage, where possible, and to reduce the risk of data loss.


| **Field Name** | **Definition** | 
| --- | --- | 
| Customer Name | Customer name for situations where multiple sub-customers are | 
| Region | AWS region where the resource is located | 
| Account name | The name of the account | 
| AWS Account ID | The ID of the AWS account | 
| Resource Type | Type of the resource. Resources are supported by AWS Backup (Aurora, DocumentDB, DynamoDB, EBS, EC2, EFS, FSx, RDS, and S3)  | 
| Resource ARN | ARN of the resource  | 
| Resource ID | ID of the resource | 
| Coverage | Indicates if the resource is covered or not ("COVERED" or "NOT\_COVERED") | 
| \# of resources | Number of supported resources in the account | 
| perc\_coverage | Percentage of supported resources with a backup executed in the last 30 days. | 