# Troubleshooting bulk import and export operations

To handle and diagnose errors produced during a transfer job, see the AWS IoT TwinMaker **GetMetadataTransferJob** API:

1. After creating and running a transfer job, call the **GetMetadataTransferJob** API:

```

aws iottwinmaker get-metadata-transfer-job \
--metadata-transfer-job-id your_metadata_transfer_job_id \
--region us-east-1

```

2. The state of the job changes to one of the below states:
   - COMPLETED
   - CANCELLED
   - ERROR

3. The **GetMetadataTransferJob** API returns a
   [MetadataTransferJobProgress](../../../iot-twinmaker/latest/apireference/API_MetadataTransferJobProgress.md "../../../iot-twinmaker/latest/apireference/API_MetadataTransferJobProgress.md") object.
4. The **MetadataTransferJobProgress** object contains the following parameters:
   - **failedCount** : Indicates the count of assets that failed during
     the transfer process.
   - **skippedCount** : Indicates the count of assets that were skipped during
     the transfer process.
   - **succeededCount** : Indicates the count of assets that succeeded during
     the transfer process.
   - **totalCount** : Indicates the total count of assets involved in
     the transfer process.

5. Additionally a **reportUrl** element is returned by the API call,
   which contains a pre-signed URL.
   If your transfer job has errors that needs investigation, you can download a full error
   report at this URL.
