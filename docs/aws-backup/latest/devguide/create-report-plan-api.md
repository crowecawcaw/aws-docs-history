

# Creating report plans using the AWS Backup API
<a name="create-report-plan-api"></a>

You can also work with report plans programmatically.

There are two types of reports. One type is a **jobs report**, which shows jobs finished in the last 24 hours and all active jobs. The second type of report is a **compliance report**. Compliance reports can monitor resource levels or the different controls that are in effect. When you create a report, you choose which type of report to create.

Similar to a *backup plan*, you create a *report plan* to automate the creation of your reports and define their destination Amazon S3 bucket. A report plan requires that you have an S3 bucket to receive your reports. For instructions on setting up a new S3 bucket, see [Step 1: Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket) in the *Amazon Simple Storage Service User Guide*.

If you encrypt your bucket using a custom KMS key, the KMS key policy must meet the following requirements:
+ The `Principal` attribute must include the Backup Audit Manager service-linked role [`AWSServiceRoleForBackupReports`](https://console.aws.amazon.com/iam/home#/roles/AWSServiceRoleForBackupReports) ARN.
+ The `Action` attribute must include `kms:GenerateDataKey` at minimum.

 The policy [AWSServiceRolePolicyForBackupReports](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSServiceRolePolicyForBackupReports) has these permissions.

For single-account, single-Region reports, use the following syntax to call [CreateReportPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateReportPlan.html). 

```
{
   "ReportPlanName": "string",
   "ReportPlanDescription": "string",
   "ReportSetting": {
        "ReportTemplate": enum, // Can be RESOURCE_COMPLIANCE_REPORT, CONTROL_COMPLIANCE_REPORT, BACKUP_JOB_REPORT, COPY_JOB_REPORT, or RESTORE_JOB_REPORT. Only include "ReportCoverageList" if your report is a COMPLIANCE_REPORT.
   "ReportDeliveryChannel": {
       "S3BucketName": "string",
       "S3KeyPrefix": "string",
       "Formats": [ enum ] // Optional. Can be either CSV, JSON, or both. Default is CSV if left blank.
   },
   "ReportPlanTags": { 
       "string" : "string" // Optional.
   },
   "IdempotencyToken": "string"
}
```

When you call [DescribeReportPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeReportPlan.html) with the unique name of a report plan, the AWS Backup API responds with the following information.

```
{
    "ReportPlanArn": "string",
    "ReportPlanName": "string",
    "ReportPlanDescription": "string",
    "ReportSetting": {
        "ReportTemplate": enum,
    },
    "ReportDeliveryChannel": {
        "S3BucketName": "string",
        "S3KeyPrefix": "string",
        "Formats": [ enum ]
    },
    "DeploymentStatus": enum
    "CreationTime": timestamp,
    "LastAttemptExecutionTime": timestamp,
    "LastSuccessfulExecutionTime": timestamp
}
```

For multi-account, multi-Region reports, use the following syntax to call [CreateReportPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateReportPlan.html).

```
{
   "IdempotencyToken": "string",
   "ReportDeliveryChannel": { 
      "Formats": [ "string" ], *//Organization report only support CSV file*
      "S3BucketName": "string",
      "S3KeyPrefix": "string"
   },
   "ReportPlanDescription": "string",
   "ReportPlanName": "string",
   "ReportPlanTags": { 
      "string" : "string" 
   },
   "ReportSetting": { 
      "Accounts": [ "string" ], // Use string value of "ROOT" to include all organizational units
      "OrganizationUnits": [ "string" ],
      "Regions": ["string"], // Use wildcard value in string to include all Regions
      "FrameworkArns": [ "string" ],
      "NumberOfFrameworks": number,
      "ReportTemplate": "string"
   }
}
```

When you call [DescribeReportPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeReportPlan.html) with the unique name of a report plan, the AWS Backup API responds with the following information for multi-account, multi-Region plans:

```
{
   "ReportPlan": { 
      "CreationTime": number,
      "DeploymentStatus": "string",
      "LastAttemptedExecutionTime": number,
      "LastSuccessfulExecutionTime": number,
      "ReportDeliveryChannel": { 
         "Formats": [ "string" ],
         "S3BucketName": "string",
         "S3KeyPrefix": "string"
      },
      "ReportPlanArn": "string",
      "ReportPlanDescription": "string",
      "ReportPlanName": "string",
      "ReportSetting": { 
         "Accounts":[ "string" ],
         "OrganizationUnits":[ "string" ],
         "Regions": [ "string" ], 
         "FrameworkArns": [ "string" ],
         "NumberOfFrameworks": number,
         "ReportTemplate": "string"
      }
   }
}
```