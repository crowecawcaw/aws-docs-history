# Describe an AWS IoT SiteWise bulk import job (AWS CLI)

Use the [DescribeBulkImportJob](../APIReference/API_DescribeBulkImportJob.md "../APIReference/API_DescribeBulkImportJob.md") API operation to retrieve information about a specific bulk
import job in AWS IoT SiteWise. This operation returns details such as the job's status, creation time,
and error information if the job failed. You can use this operation to monitor job progress
and troubleshoot issues. To use `DescribeBulkImportJob`, you need the job ID from
the `CreateBulkImportJob` operation. The API returns the following
information:

- List of files being imported, including their Amazon S3 bucket locations and keys
- Error report location (if applicable)
- Job configuration details, such as file format and CSV column names
- Job creation and last update timestamps
- Current job status (for example, whether the job is in progress, completed, or
  failed)
- IAM role ARN used for the import job
  For completed jobs, review the results to confirm successful data integration. If a job
  fails, examine the error details to diagnose and resolve issues.

Replace `job-ID` with the ID of the bulk import job that you want
to retrieve.

```
aws iotsitewise describe-bulk-import-job --job-id `job-ID`
```

###### Example response

```
{
   "files":[
      {
         "bucket":"amzn-s3-demo-bucket1",
         "key":"100Tags12Hours.csv"
      },
      {
         "bucket":"amzn-s3-demo-bucket2",
         "key":"BulkImportData1MB.csv"
      },
      {
         "bucket":"	amzn-s3-demo-bucket3",
         "key":"UnmodeledBulkImportData1MB.csv"
      }
   ],
   "errorReportLocation":{
      "prefix":"errors/",
      "bucket":"amzn-s3-demo-bucket`-for-errors`"
   },
   "jobConfiguration":{
      "fileFormat":{
         "csv":{
            "columnNames":[
               "ALIAS",
               "DATA_TYPE",
               "TIMESTAMP_SECONDS",
               "TIMESTAMP_NANO_OFFSET",
               "QUALITY",
               "VALUE"
            ]
         }
      }
   },
   "jobCreationDate":1645745176.498,
   "jobStatus":"COMPLETED",
   "jobName":"myBulkImportJob",
   "jobLastUpdateDate":1645745279.968,
   "jobRoleArn":"arn:aws:iam::123456789012:role/DemoRole",
   "jobId":"f8c031d0-01d1-4b94-90b1-afe8bb93b7e5"
}
```
