

# Submitting feedback on medical codes

After a coder or clinician reviews the suggested codes for a job, you can submit the final codes as feedback. You call `SubmitFeedback` with the job ID and the S3 location of the final codes. The service compares the final codes with the codes that the job generated.

For the full request and response syntax, see [SubmitFeedback](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_SubmitFeedback.html) in the *Amazon Connect Health API Reference*. In the AWS SDKs, the operation is on the `ConnectHealth` client. In the AWS CLI, it’s `aws connecthealth submit-feedback`.

**Topics**
+ [Requirements](#mc-fb-requirements)
+ [Request parameters](#mc-fb-request)
+ [Final codes file](#mc-fb-final-codes)
+ [Response](#mc-fb-response)
+ [Retries](#mc-fb-idempotency)
+ [Feedback and the AI services opt-out policy](#mc-fb-opt-out)
+ [Errors](#mc-fb-errors)

## Requirements
<a name="mc-fb-requirements"></a>

You can submit feedback on a medical coding job when the following conditions are true:
+ The job belongs to your account and to the domain in the request.
+ The job’s `jobStatus` is `SUCCEEDED`.
+ No more than 29 days have passed since the job was created. After that, `SubmitFeedback` returns `ResourceNotFoundException`.
+ The final codes are in an S3 object that the caller can read. The caller needs `s3:GetObject` on the object and, if the object is encrypted with a customer managed AWS KMS key, `kms:Decrypt` on that key. The bucket can be in another AWS account, but it must be in an AWS Region that is enabled by default. Buckets in opt-in Regions aren’t supported.
+ The caller has IAM permission to call `SubmitFeedback` in the domain, and to call `GetMedicalCodingJob` on the job. If the job’s domain uses a customer managed AWS KMS key, the caller also needs `kms:Decrypt` on that key. See [Example 8: Allow users to manage medical coding datasets and submit feedback](security-iam.md#iam-example-medical-coding-datasets).

The service reads the job and the final codes with the caller’s credentials. Each `SubmitFeedback` request makes one `GetMedicalCodingJob` call as the caller. That call counts toward your `GetMedicalCodingJob` quota and appears in your AWS CloudTrail log.

## Request parameters
<a name="mc-fb-request"></a>

The `SubmitFeedback` request takes the following parameters for medical codes.


| Parameter | Required | Description | 
| --- | --- | --- | 
|  `domainId` (request path) | Yes | The domain that the coding job ran in. | 
|  `artifactType`  | Yes |  `MEDICAL_CODES`. | 
|  `artifactSourceId`  | Yes | The `jobId` of the medical coding job, a 36-character UUID. | 
|  `signedArtifactS3Uri`  | Yes | The S3 URI of the final codes in your bucket. The URI must be a full object key, not a bucket or a prefix. | 
|  `comments`  | No | Free-text comments about the codes, 1 to 4,096 characters. | 
|  `clientToken`  | No | A token for idempotent retries, 1 to 128 characters. The SDKs generate one if you don’t provide it. | 

For medical codes, you don’t need `subscriptionId` or `generatedArtifactS3Uri`. The service compares your final codes with its own copy of the codes that the job generated.

## Final codes file
<a name="mc-fb-final-codes"></a>

The object at `signedArtifactS3Uri` uses the same format as the job’s results file, `medical-codes.json`. You can edit the results file to reflect the coder’s decisions and submit it as is. For the format, see [Results file structure](mc-outputs.md#mc-output-structure).

The service reads only the following fields. It ignores all other fields, such as `evidence`, `description`, and `confidence`.


| Field | Required | Notes | 
| --- | --- | --- | 
|  `medicalCodes`  | Yes | An array of 1 to 1,000 codes. | 
|  `system`  | Yes, for each code |  `ICD10` or `CPT`. | 
|  `name`  | Yes, for each code | The code. A CPT code can include an inline modifier, such as `99214-25`. | 
|  `modifiers[].code`  | No | CPT codes only. | 
|  `linkedCodes[]`  | No | CPT codes only. Each entry needs a `system` of `ICD10` and a `name`. | 

The file can be up to 5 MiB. If the file is too large, isn’t valid JSON, has no `medicalCodes` array, or has no valid codes, the service discards the feedback. If an individual code is invalid, for example because its `system` is missing or its `name` isn’t a valid code, the service skips that code and compares the rest.

The following example shows a `SubmitFeedback` request body:

```json
{
  "artifactType": "MEDICAL_CODES",
  "artifactSourceId": "4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d",
  "signedArtifactS3Uri": "s3://amzn-s3-demo-bucket/final-codes/4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d.json",
  "comments": "Coder changed the E/M level after review."
}
```

## Response
<a name="mc-fb-response"></a>

 `SubmitFeedback` returns HTTP status 202 with an empty body. The response doesn’t include a feedback ID, and there is no operation to read feedback back. When you contact AWS about a request, provide the request ID from the `x-amzn-RequestId` response header.

The service processes the feedback asynchronously. It reads the final codes and runs the comparison after it returns the 202 response.

**Important**  
 `SubmitFeedback` checks only that `signedArtifactS3Uri` names an object, not that the object exists or that the caller can read it. If the object is missing, the caller can’t read it, or the file is invalid, the service discards the feedback after it returns 202, and it can’t report the failure to you. Before you submit, confirm that the object exists, that the caller has `s3:GetObject` (and `kms:Decrypt`, if applicable), and that the file matches [Final codes file](#mc-fb-final-codes).

## Retries
<a name="mc-fb-idempotency"></a>

If you retry a request with the same `clientToken` and the same parameters, the service accepts it again and doesn’t record the feedback twice. If you reuse a `clientToken` with different parameters, `SubmitFeedback` returns `ValidationException`.

## Feedback and the AI services opt-out policy
<a name="mc-fb-opt-out"></a>

If your account is opted out of the `connecthealth::operations` opt-out type in your AWS Organizations AI services opt-out policy, `SubmitFeedback` still returns a success response (HTTP status 202), but the service doesn’t process the feedback. It doesn’t read your final codes, and it doesn’t store your comments or the location of your final codes. For more information about the opt-out types, see [Service improvement and how to opt out](data-protection.md#service-improvement).

An account with no AI services opt-out policy is treated as opted in. Changes to your opt-out policy can take up to 10 minutes to apply to feedback.

## Errors
<a name="mc-fb-errors"></a>

 `SubmitFeedback` can return the following errors.


| Error | Likely cause | What to do | 
| --- | --- | --- | 
|  `ValidationException`  | A parameter failed validation, such as an `artifactSourceId` that isn’t a UUID or a `signedArtifactS3Uri` that names a bucket or prefix. Or a `clientToken` was reused with a different request. Or the job hasn’t succeeded: the message is `The medical coding job has not completed.` for a job that is still running, and `The medical coding job did not succeed, so feedback cannot be recorded.` for a job that failed. | Check each parameter against [Request parameters](#mc-fb-request). Use a new `clientToken` for a different request. Submit feedback only after the job reaches `SUCCEEDED`. | 
|  `AccessDeniedException`  | The caller can’t read the job. The caller needs `health-agent:GetMedicalCodingJob` on the job and, if the domain uses a customer managed AWS KMS key, `kms:Decrypt` on that key. | Grant the missing permissions. See [Requirements](#mc-fb-requirements). | 
|  `ResourceNotFoundException`  | The job doesn’t exist in your account and domain, more than 29 days have passed since the job was created, or the request was sent to a Region where medical coding isn’t available. The message is the same in each case. | Verify the domain ID, the `jobId`, and the Region. Submit feedback within 29 days of creating the job. | 
|  `ThrottlingException`  | The request rate exceeded the `SubmitFeedback` quota of 5 requests per second, or the caller’s `GetMedicalCodingJob` quota. | Retry with exponential backoff. Polling `GetMedicalCodingJob` and submitting feedback draw on the same `GetMedicalCodingJob` quota. | 
|  `InternalServerException`  | A transient service-side error. | Retry the request. | 