

# Jobs progress tracking
<a name="review-job-progress"></a>

## Review job progress and details (console)
<a name="review-job-progress-console"></a>

See [Import metadata (console)](running-bulk-operations-import.md#import-metadata-console) or [Export metadata (console)](running-bulk-operations-export.md#export-metadata-console) to start a bulk job.

**Job progress overview in the AWS IoT SiteWise console:**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. Choose **Bulk operations New** from the navigation pane.

1. The **Jobs progress** table in the AWS IoT SiteWise console, displays the list of bulk operation jobs.

1. The **Job type** column describes if it's an export or import job. The **Date imported** columns display the date that the job started.

1. The **Status** column displays the status of the job. You can select a job to see details about the job.

1. The selected job shows **Success** upon being successful, or a list of failure if the job failed. An error description is also displayed with each resource type.

**Job details overview in the AWS IoT SiteWise console:**

The **Jobs progress** table in the AWS IoT SiteWise console, displays the list of bulk operation jobs.

1. Choose a job to see more details.

1. For an **import** job, the `Data source ARN` represents the Amazon S3 location of the import file.

1. For an **export** job, the `Data destination ARN` represents the Amazon S3 location of the file after the export.

1. The `Status` and `Status reason`, provide additional details on the current job. See [Jobs progress tracking and error handling](jobs-progress-error-handling.md) for more details.

1. The `Queued position` represents the position of the job in the process queue. The jobs are processed one at a time. A queued position of 1, indicates that the job will be processed next.

1.  The jobs details page also displays the job progress counts.

   1. The job progress count types are:

     1. `Total resources` – Indicates the total count of assets in the transfer process.

     1. `Succeeded` – Indicates the count of assets successfully transferred during the process.

     1. `Failed` – Indicates the count assets that failed during the process.

     1. `Skipped` – Indicates the count of assets that were skipped during the process.

1. A job status of `PENDING` or `VALIDATING`, displays all the jobs progress counts as `–`. This indicates that the jobs progress counts are being evaluated.

1. A job status of `RUNNING` displays the `Total resources` count, the job submitted for processing. The detailed counts (`Succeeded`, `Failed`, and `Skipped`), apply to the processed resources. The sum of the detailed counts is lesser than the `Total resources` count, until the job's status is `COMPLETED` or `ERROR`.

1.  If a job's status is `COMPLETED` or `ERROR`, the `Total resources` count equals the sum of the detailed counts (`Succeeded`, `Failed`, and `Skipped`). 

1.  If a job's status is `ERROR`, check the **Job failures** table for details about the specific errors and failures. See [Inspect error details (console)](inspect-errors.md#inspect-errors-console) for more details. 

## Review job progress and details (AWS CLI)
<a name="review-job-progress-cli"></a>

After starting a bulk operation, you can check or update its status using the following API actions:
+ To retrieve information on a specific job, use the [ GetMetadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetMetadataTransferJob.html) API action.

**Retrieve information with the `GetMetadataTransferJob` API:**

  1. Create and run a transfer job. Call the `GetMetadataTransferJob` API.  
**Example AWS CLI command:**  

     ```
     aws iottwinmaker get-metadata-transfer-job \ 
             --metadata-transfer-job-id {{your_metadata_transfer_job_id}} \
             --region {{your_region}}
     ```

  1.  The `GetMetadataTransferJob` API returns a `MetadataTransferJobProgress` object with the following parameters: 
     + **succeededCount** – Indicates the count of assets successfully transferred in the process.
     + **failedCount** – Indicates the count of assets that failed during the process.
     + **skippedCount** – Indicates the count of assets that were skipped during the process.
     + **totalCount** – Indicates the total count of assets in the transfer process.

     These parameters indicate the job progress status. If the status is `RUNNING`, they help track the number of resources still to be processed.

     If you encounter schema validation errors, or if **failedCount** is greater than or equal to 1, the job progress state turns to `ERROR`. A full error report for the job is placed in your Amazon S3 bucket. See [Inspect errors for AWS IoT SiteWise](inspect-errors.md) for more details.
+ To list current jobs, use the [ListMetadataTransferJobs](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListMetadataTransferJobs.html) API action.

  Use a JSON file to filter the returned jobs based on their current state. See the following procedure:

  1. To specify the filters you want to use, create an AWS CLI input JSON file. want to use:

     ```
     {
         "sourceType": "s3",
         "destinationType": "iottwinmaker",
         "filters": [{
             "state": "COMPLETED"
         }]
     }
     ```

     For a list of valid `state` values, see [ListMetadataTransferJobsFilter](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListMetadataTransferJobsFilter.html) in the *AWS IoT TwinMaker API Reference Guide*.

  1.  Use the JSON file as an argument in the following AWS CLI example command:

     ```
     aws iottwinmaker list-metadata-transfer-job --region {{your_region}} \
             --cli-input-json file://ListMetadataTransferJobsExample.json
     ```
+ To cancel a job, use the [CancelMetadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CancelMetadataTransferJob.html) API action. This API cancels the specific metadata transfer job, without affecting any resources already exported or imported:

  ```
  aws iottwinmaker cancel-metadata-transfer-job \ 
          --region {{your_region}} \ 
          --metadata-transfer-job-id {{job-to-cancel-id}}
  ```