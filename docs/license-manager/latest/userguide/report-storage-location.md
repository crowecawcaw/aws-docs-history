# Report storage

Usage reports begin publishing within 60 minutes. If you do not already have an Amazon S3 bucket associated with your account, License Manager will create a new Amazon S3 bucket when you create a usage report. Reports are stored with the following Amazon S3 URI pattern:

```
s3://aws-license-manager-service-*/Reports/usage-report-name/year/month/day/report-id.csv
```

For more information about the CLI command, see [create-license-manager-report-generator](../../../cli/latest/reference/license-manager/create-license-manager-report-generator.md "../../../cli/latest/reference/license-manager/create-license-manager-report-generator.md") (AWS CLI).

###### Note

AWS License Manager does not store your reports. Reports are published directly to your Amazon S3 bucket. Once you delete a usage report, reports are no longer published to your Amazon S3 bucket.
