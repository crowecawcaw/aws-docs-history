

# Troubleshooting medical coding

**Topics**
+ [API errors](#mc-ts-api-errors)
+ [Job-status issues](#mc-ts-job-status)
+ [Dataset issues](#mc-ts-datasets)
+ [Feedback issues](#mc-ts-feedback)

## API errors
<a name="mc-ts-api-errors"></a>

The following errors can be returned by `StartMedicalCodingJob` and `GetMedicalCodingJob`.


| Error | HTTP | Applies to | Likely cause | What to do | 
| --- | --- | --- | --- | --- | 
|  `ValidationException`  | 400 | Start, Get | An input failed validation. For example, empty `text`, `text` over 100,000 characters (the message reads `Text field exceeds maximum length of 100000 characters`), an `encounterReason` over 256 characters or containing unsupported characters, a malformed `dateOfBirth`, an invalid enumeration value, or a malformed S3 path. | Check each field against the allowed values in [Medical coding inputs](mc-inputs.md). | 
|  `AccessDeniedException`  | 401 | Start, Get | Missing or invalid credentials, or the caller lacks a required permission. On `StartMedicalCodingJob`, this includes permission to write to the S3 output location and, if the domain uses a customer managed AWS KMS key, to use that key. No job is created. | Verify credentials and grant the missing permissions. See [Example IAM policy](mc-getting-started.md#mc-gs-permissions). | 
|  `ResourceNotFoundException`  | 404 | Get | The `domainId` or `jobId` doesn’t exist. | Verify the domain ID and confirm the `jobId` came from a successful `StartMedicalCodingJob` response. | 
|  `ConflictException`  | 409 | Start | The request conflicts with the current state, commonly a `clientToken` reused with different parameters. | Use a new `clientToken`, or reuse the token only with an identical request. | 
|  `ThrottlingException`  | 429 | Start, Get | The request rate exceeded the quota. By default, `StartMedicalCodingJob` allows 5 and `GetMedicalCodingJob` allows 10 requests per second per account and Region. | Back off and retry with exponential backoff, and poll `GetMedicalCodingJob` less frequently. To request a higher quota, contact your AWS account team. See [Quotas for Amazon Connect Health](connecthealth-quotas.md). | 
|  `InternalServerException`  | 500 | Start, Get | A transient service-side error. | Retry the request. | 

## Job-status issues
<a name="mc-ts-job-status"></a>


| Symptom | Likely cause | What to do | 
| --- | --- | --- | 
|  `jobStatus` is `FAILED`  | The job could not be completed. | Read `statusDetails` in the `GetMedicalCodingJob` response for the specific reason, correct the input, and submit a new job. | 
|  `jobStatus` is `FAILED`, and `statusDetails` is `{"error":{"code":"CONTENT_FILTERED","message":"The input was flagged by content safety filters."}}`  | Content safety filters flagged the input. No results file is written. | Check that `text` contains only the clinical documentation for the encounter. If the documentation is valid, contact your AWS account team with the `jobId`. | 
| Job stays `IN_PROGRESS` longer than expected | Processing is still under way. A primary care note typically completes in about 35 seconds. | Continue polling with backoff, up to a 30-second interval. Compare `updatedTime` with `creationTime` to see elapsed time. | 
| Job goes from `SUBMITTED` to `FAILED`  | Rare. A service issue kept the job from starting. | Submit the job again with a new `clientToken`. If it happens repeatedly, contact your AWS account team. | 
| Can’t find the results file | The file is in a subfolder named after the job. | Read the URI in `medicalCodingOutput.uri`. The file is at `{s3OutputPath}/{jobId}/medical-codes.json`. | 
| Duplicate jobs from retries | Retrying `StartMedicalCodingJob` without a `clientToken`. | Include a `clientToken` on every submission. See [Idempotent submissions](mc-how-it-works.md#mc-idempotency). | 

## Dataset issues
<a name="mc-ts-datasets"></a>

The following issues can occur when you create, use, or delete a site-specific dataset.


| Symptom | Likely cause | What to do | 
| --- | --- | --- | 
| Dataset status is `CREATE_FAILED`  | The build failed, and nothing usable was built. | Read `statusDetails` in the `GetDataset` response. Delete the dataset, correct the input, and create a new dataset. The dataset’s quota slot is freed once it reaches `DELETED`. | 
|  `CreateDataset` returns `ServiceQuotaExceededException`  | The dataset quota is reached. Every dataset that isn’t `DELETED` counts toward the quota, including datasets in `CREATE_FAILED`, `DELETING`, and `DELETE_FAILED`. | Delete datasets that you no longer need, including any in `CREATE_FAILED`, and wait until they reach `DELETED`. See [Dataset lifecycle](mc-datasets.md#mc-ds-lifecycle). | 
|  `CreateDataset` fails validation with a message about the number of encounters, the input size, or the file count | The encounters at `s3InputPath` don’t meet the dataset input limits, or a file under that path isn’t a `.json` or `.jsonl` file. | Check your input against [How much data to provide](mc-ss-prepare.md#mc-ss-prepare-volume) and [Input file format](mc-ss-prepare.md#mc-ss-prepare-format). `statusDetails` reports a count for each problem, not the individual records. | 
|  `statusDetails` is `Access denied to s3InputPath: …​` or `Access denied to s3OutputPath: …​`  | The bucket isn’t owned by the dataset’s account, or the caller can’t read the input, write the output, or use the objects' AWS KMS key. | Use buckets in the same account, and grant the permissions in [Required permissions](mc-datasets.md#mc-ds-permissions). | 
|  `statusDetails` is `The domain’s KMS key can’t be used: …​`  | The domain’s customer managed key is disabled, or the caller lacks `kms:DescribeKey`, `kms:CreateGrant`, `kms:Decrypt`, or `kms:GenerateDataKey` on it. The message names the missing permission. | Enable the key and grant the caller `kms:DescribeKey`, `kms:CreateGrant`, `kms:Decrypt`, and `kms:GenerateDataKey`. | 
|  `statusDetails` says the `s3InputPath` bucket or an object doesn’t exist, is in another Region, or is in an archive storage class, or that `s3InputPath` and `s3OutputPath` overlap | The input location doesn’t meet the dataset requirements. | Fix the input location. The bucket must be in the same Region as the domain, objects must be restored from archive storage, and the input and output paths must not overlap. | 
|  `statusDetails` is `Dataset creation failed because of an internal error. Delete the dataset and create it again.`  | A service-side failure. | Delete the dataset and create it again. | 
|  `DeleteDataset` returns `ConflictException`  | The dataset is still `CREATING`. | Wait until the dataset is `ACTIVE` or `CREATE_FAILED`, and then delete it. | 
| Dataset status is `DELETE_FAILED`  | Deletion failed partway, and some provisioned resources might remain. | Read `statusDetails`, and then call `DeleteDataset` again. | 
|  `GetDataset` returns `ResourceNotFoundException`  | The dataset was deleted, or the `domainId` or `datasetId` is wrong. | Verify the IDs. Call `ListDatasets` to see the datasets in the domain. | 
|  `AccessDeniedException` from a dataset operation | The caller lacks an IAM permission, or an S3 or AWS KMS permission on the input or output location. | Grant the permissions listed in [Required permissions](mc-datasets.md#mc-ds-permissions). | 

### Errors when a job names a dataset
<a name="mc-ts-dataset-in-job"></a>


| Error | Likely cause | What to do | 
| --- | --- | --- | 
|  `ResourceNotFoundException`: `Dataset <datasetId> was not found in this domain.`  | The dataset doesn’t exist, was deleted, or is in another account or domain. | Call `ListDatasets` in the job’s domain and use an `ACTIVE` dataset ID. | 
|  `ConflictException`: `Dataset <datasetId> is still being created.`  | The dataset is still `CREATING`. | Retry when `GetDataset` returns `ACTIVE`. | 
|  `ValidationException`: `Dataset <datasetId> cannot be used for medical coding because its status is <status>.`  | The dataset is `CREATE_FAILED`, `DELETING`, or `DELETE_FAILED`. | Use a different dataset, or omit `datasetId` to use the generalized knowledge base. | 
|  `AccessDeniedException`  | The domain uses a customer managed AWS KMS key, and the caller can’t decrypt the dataset or lacks `kms:ListGrants` on the key. Or the dataset’s `-read` grant was revoked. | Grant the caller `kms:Decrypt` on the key for the dataset’s storage and `kms:ListGrants` on the key. If the grant was revoked, create a new dataset. See [Required permissions](mc-datasets.md#mc-ds-permissions). | 

## Feedback issues
<a name="mc-ts-feedback"></a>

For `SubmitFeedback` errors, see [Errors](mc-feedback.md#mc-fb-errors) in [Submitting feedback on medical codes](mc-feedback.md). A 202 response means that the service accepted the request. If your account is opted out of the `connecthealth::operations` opt-out type, `SubmitFeedback` still returns a success response (202), but the service doesn’t process or store the feedback.