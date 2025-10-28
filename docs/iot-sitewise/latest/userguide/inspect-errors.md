# Inspect errors for AWS IoT SiteWise

## Inspect error details (console)

###### Error details in the AWS IoT SiteWise console:

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. See the **Jobs progress** table in AWS IoT SiteWise console for a list of bulk operation jobs.
3. Select a job to view the job details.
4. If a job's status is `COMPLETED` or `ERROR`, the `Total resources`
   count equals the sum of the detailed counts (`Succeeded`, `Failed`, and
   `Skipped`).
5. If a job's status is `ERROR`, check the **Job failures** table for
   details about the specific errors and failures.
6. The **Job failures** table displays the content from the job report. The
   `Resource type` field indicates the location of the error or failures, such as the
   following:
   - For example, a validation error in the `Bulk operations template` in the `Resource
type` field indicates that the import template and metadata schema file format don't match.
     See [AWS IoT SiteWise metadata transfer job schema](bulk-operations-schema.md "bulk-operations-schema.md") for more
     information.
   - A failed `Asset` in the `Resource type` field indicates that the asset is
     not created because of a conflict with another asset. See [Common errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md") for information on AWS IoT SiteWise resource
     errors and conflicts.

## Inspect error details (AWS CLI)

To handle and diagnose errors produced during a transfer job, see the following procedure about using the
`GetMetadataTransferJob` API action:

1. After creating and running a transfer job, call [GetMetadataTransferJob](../../../iot-twinmaker/latest/apireference/API_GetMetadataTransferJob.md "../../../iot-twinmaker/latest/apireference/API_GetMetadataTransferJob.md"):

```
aws iottwinmaker get-metadata-transfer-job \
        --metadata-transfer-job-id `your_metadata_transfer_job_id` \
        --region us-east-1
```

2. Once you see the state of the job turn to `COMPLETED`, you can start verifying the results
   of the job.
3. When you call `GetMetadataTransferJob`, it returns an object called [`MetadataTransferJobProgress`](../../../iot-twinmaker/latest/apireference/API_MetadataTransferJobProgress.md "../../../iot-twinmaker/latest/apireference/API_MetadataTransferJobProgress.md").

The MetadataTransferJobProgress object contains the following parameters:

    * **failedCount:** Indicates the count of assets that failed during the
     transfer process.
    * **skippedCount:** Indicates the count of assets that were skipped
     during the transfer process.
    * **succeededCount:** Indicates the count of assets that succeeded
     during the transfer process.
    * **totalCount:** Indicates the total count of assets involved in the
     transfer process.

4. Additionally, the API call returns an element `reportUrl`, which contains a presigned URL.
   If your transfer job has any issues that you need to investigate further, visit this url.
