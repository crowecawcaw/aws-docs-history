

# Inspect errors for AWS IoT SiteWise
<a name="inspect-errors"></a>

## Inspect error details (console)
<a name="inspect-errors-console"></a>

**Error details in the AWS IoT SiteWise console:**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. See the **Jobs progress** table in AWS IoT SiteWise console for a list of bulk operation jobs.

1. Select a job to view the job details.

1. If a job's status is `COMPLETED` or `ERROR`, the `Total resources` count equals the sum of the detailed counts (`Succeeded`, `Failed`, and `Skipped`).

1.  If a job's status is `ERROR`, check the **Job failures** table for details about the specific errors and failures.

1. The **Job failures** table displays the content from the job report. The `Resource type` field indicates the location of the error or failures, such as the following:
   + For example, a validation error in the `Bulk operations template` in the `Resource type` field indicates that the import template and metadata schema file format don't match. See [AWS IoT SiteWise metadata transfer job schema](bulk-operations-schema.md) for more information. 
   + A failed `Asset` in the `Resource type` field indicates that the asset is not created because of a conflict with another asset. See [Common errors](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/CommonErrors.html) for information on AWS IoT SiteWise resource errors and conflicts. 

## Inspect error details (AWS CLI)
<a name="inspect-errors-cli"></a>

To handle and diagnose errors produced during a transfer job, see the following procedure about using the `GetMetadataTransferJob` API action:

1. After creating and running a transfer job, call [GetMetadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetMetadataTransferJob.html):

   ```
   aws iottwinmaker get-metadata-transfer-job \
           --metadata-transfer-job-id {{your_metadata_transfer_job_id}} \
           --region us-east-1
   ```

1. Once you see the state of the job turn to `COMPLETED`, you can start verifying the results of the job.

1. When you call `GetMetadataTransferJob`, it returns an object called [`MetadataTransferJobProgress`](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_MetadataTransferJobProgress.html).

   The MetadataTransferJobProgress object contains the following parameters:
   + **failedCount:** Indicates the count of assets that failed during the transfer process.
   + **skippedCount:** Indicates the count of assets that were skipped during the transfer process.
   + **succeededCount:** Indicates the count of assets that succeeded during the transfer process.
   + **totalCount:** Indicates the total count of assets involved in the transfer process.

1. Additionally, the API call returns an element `reportUrl`, which contains a presigned URL. If your transfer job has any issues that you need to investigate further, visit this url. 