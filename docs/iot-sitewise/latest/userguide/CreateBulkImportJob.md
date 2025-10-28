# Create an AWS IoT SiteWise bulk import job (AWS CLI)

Use the [CreateBulkImportJob](../APIReference/API_CreateBulkImportJob.md "../APIReference/API_CreateBulkImportJob.md") API operation to transfer data from Amazon S3 to AWS IoT SiteWise. The [CreateBulkImportJob](../APIReference/API_CreateBulkImportJob.md "../APIReference/API_CreateBulkImportJob.md") API enables
ingestion of large volumes of historical data, and buffered ingestion of analytical data
streams in small batches. It provides a cost-effective primitive for data ingestion. The
following example uses the AWS CLI.

###### Important

Before creating a bulk import job, you must enable AWS IoT SiteWise warm tier or AWS IoT SiteWise cold tier.
For more information, see [Configure storage settings in AWS IoT SiteWise](configure-storage.md "configure-storage.md").

The [CreateBulkImportJob](../APIReference/API_CreateBulkImportJob.md "../APIReference/API_CreateBulkImportJob.md") API supports ingestion of historical data into AWS IoT SiteWise with
the option to set the adaptive-ingestion-flag parameter.

- When set to `false`, the API ingests historical data without triggering
  computations or notifications.
- When set to `true`, the API ingests new data, calculating metrics and
  transforming the data to optimize ongoing analytics and notifications within seven
  days.
  Run the following command. Replace `file-name` with the name of
  the file that contains the bulk import job configuration.

```
aws iotsitewise create-bulk-import-job --cli-input-json file://`file-name`.json
```

###### Example Bulk import job configuration

The following are examples of configuration settings:

- Replace `adaptive-ingestion-flag` with `true` or
  `false`.
  - If set to `false`, the bulk import job ingests historical data into
    AWS IoT SiteWise.
  - If set to `true`, the bulk import job does the following:
    - Ingests new data into AWS IoT SiteWise.
    - Calculates metrics and transforms, and supports notifications for data with
      a time stamp that's within seven days.

- Replace `delete-files-after-import-flag` with
  `true` to delete the data from the Amazon S3 data bucket after ingesting into
  AWS IoT SiteWise warm tier storage.
- Replace amzn-s3-demo-bucket`-for-errors` with the name of
  the Amazon S3 bucket to which errors associated with this bulk import job are sent.
- Replace amzn-s3-demo-bucket`-for-errors-prefix` with the
  prefix of the Amazon S3 bucket to which errors associated with this bulk import job are sent.

Amazon S3 uses the prefix as a folder name to organize data in the bucket. Each Amazon S3
object has a key that is its unique identifier in the bucket. Each object in a bucket
has exactly one key. The prefix must end with a forward slash (/). For more information,
see [Organizing objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the _Amazon Simple Storage Service User
Guide_.

- Replace amzn-s3-demo-bucket`-data` with the name of the
  Amazon S3 bucket from which data is imported.
- Replace `data-bucket-key` with the key of the Amazon S3 object
  that contains your data. Each object has a key that is a unique identifier. Each object
  has exactly one key.
- Replace `data-bucket-version-id` with the version ID to
  identify a specific version of the Amazon S3 object that contains your data. This parameter
  is optional.
- Replace `column-name` with the column name specified in the
  .csv file.
- Replace `job-name` with a unique name that identifies the
  bulk import job.
- Replace `job-role-arn` with the IAM role that allows
  AWS IoT SiteWise to read Amazon S3 data.

###### Note

Make sure that your role has the permissions shown in the following example. Replace
amzn-s3-demo-bucket`-data` with the name of the Amazon S3 bucket
that contains
your
data. Also, replace
`amzn-s3-demo-bucket-for-errors` with the name of the Amazon S3
bucket to which errors associated with this bulk import job are sent.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket`-data`",
 "arn:aws:s3:::amzn-s3-demo-bucket`-data`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket`-for-errors`",
 "arn:aws:s3:::amzn-s3-demo-bucket`-for-errors`/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

```
{
   "adaptiveIngestion": adaptive-ingestion-flag,
   "deleteFilesAfterImport": delete-files-after-import-flag,
   "errorReportLocation": {
      "bucket": "amzn-s3-demo-bucket`-for-errors`",
      "prefix": "amzn-s3-demo-bucket`-for-errors-prefix`"
   },
   "files": [
      {
         "bucket": "`amzn-s3-demo-bucket-data`",
         "key": "`data-bucket-key`",
         "versionId": "`data-bucket-version-id`"
      }
   ],
   "jobConfiguration": {
      "fileFormat": {
         "csv": {
            "columnNames": [ "`column-name`" ]
         }
      }
   },
   "jobName": "`job-name`",
   "jobRoleArn": "`job-role-arn`"
}
```

###### Example response

```
{
   "jobId":"f8c031d0-01d1-4b94-90b1-afe8bb93b7e5",
   "jobStatus":"PENDING",
   "jobName":"myBulkImportJob"
}
```
