

# Troubleshooting medical coding
<a name="mc-troubleshooting"></a>

**Topics**
+ [API errors](#mc-ts-api-errors)
+ [Job-status issues](#mc-ts-job-status)

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
| Job stays `IN_PROGRESS` longer than expected | Processing is still under way. A primary care note typically completes in about 35 seconds. | Continue polling with backoff, up to a 30-second interval. Compare `updatedTime` with `creationTime` to see elapsed time. | 
| Job goes from `SUBMITTED` to `FAILED`  | Rare. A service issue kept the job from starting. | Submit the job again with a new `clientToken`. If it happens repeatedly, contact your AWS account team. | 
| Can’t find the results file | The file is in a subfolder named after the job. | Read the URI in `medicalCodingOutput.uri`. The file is at `{s3OutputPath}/{jobId}/medical-codes.json`. | 
| Duplicate jobs from retries | Retrying `StartMedicalCodingJob` without a `clientToken`. | Include a `clientToken` on every submission. See [Idempotent submissions](mc-how-it-works.md#mc-idempotency). | 