# Processing images in bulk

You can start a new bulk analysis job by submitting a manifest file and calling the
StartMediaAnalysisJob operation. The input manifest file contains references to images
in an Amazon S3 bucket and it is formatted as follows:

```
{"source-ref": "s3://foo/bar/1.jpg"}
```

## To create a bulk analysis job (CLI)

1. If you haven't already:
   1. Create or update a user with
      `AmazonRekognitionFullAccess` and
      `AmazonS3ReadOnlyAccess` permissions. For more
      information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Upload images to your S3 bucket.

For instructions, see [Uploading Objects
into Amazon S3](../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md "../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md") in the
_Amazon Simple Storage Service User Guide_. 3. Use the following commands to create and retrieve bulk analysis
jobs.

CLI
Use the following command to call the [StartMediaAnalysisJob](../APIReference/API_StartMediaAnalysisJob.md "../APIReference/API_StartMediaAnalysisJob.md") operation for analysis with the
DetectModerationLabels operation:

```
# Requests
# Starting DetectModerationLabels job with default settings
aws rekognition start-media-analysis-job \
--operations-config "DetectModerationLabels={MinConfidence='1'}" \
--input "S3Object={Bucket=`amzn-s3-demo-source-bucket`,Name=`my-input.json`l}" \
--output-config "S3Bucket=`amzn-s3-demo-destination-bucket;`,S3KeyPrefix=`my-results`"
```

You can get information about a given job, such as the Amazon S3 path of
the bucket where results and summary files are stored, by using the
[GetMediaAnalysisJob](../APIReference/API_GetMediaAnalysisJob.md "../APIReference/API_GetMediaAnalysisJob.md") operation. You provide it with a job ID
returned by StartMediaAnalysisJob or ListMediaAnalysisJob. Details about
individual jobs are only retained for one year.

```
# Request
aws rekognition get-media-analysis-job \
--job-id `customer-job-id`

```

You can list all of your bulk analyses by using the [ListMediaAnalysisJobs](../APIReference/API_ListMediaAnalysisJobs.md "../APIReference/API_ListMediaAnalysisJobs.md") job operation, which returns pages of
jobs. With the `max-results` argument, you can specify the
maximum number of jobs to return per page, limited to the value of
`max-results`. A maximum of 100 results are returned per
page. Details about individual jobs are only retained for one
year.

```
# Request
# Specify number of jobs to return per page, limited to max-results.
aws rekognition list-media-analysis-jobs --max-results 1
```
