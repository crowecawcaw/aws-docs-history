

# Getting started with medical coding
<a name="mc-getting-started"></a>

This tutorial walks you through a single medical coding job from end to end. Each step links to a topic with full detail. Use this page to understand the flow, and the linked topics as reference when you build.

![Request flow: start a medical coding job, poll its status, then read the results file from Amazon S3.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-request-sequence.png)


**Important**  
Medical coding is a gated preview feature. Complete the access request with your AWS account team before you begin.

**Topics**
+ [Prerequisites](#mc-gs-prerequisites)
+ [Step 1: Submit a coding job](#mc-gs-step1)
+ [Step 2: Wait for the job to complete](#mc-gs-step2)
+ [Step 3: Retrieve the suggested codes](#mc-gs-step3)
+ [End-to-end example](#mc-gs-end-to-end)
+ [Next steps](#mc-gs-next-steps)

## Prerequisites
<a name="mc-gs-prerequisites"></a>

Before you start, make sure you have:
+ Gated preview access to medical coding, granted through your AWS account team.
+ An Amazon Connect Health domain in a supported Region (`us-east-1` or `us-west-2`).
+ An Amazon S3 bucket to receive job output.
+ A submission rate within the default quotas: 5 `StartMedicalCodingJob` and 10 `GetMedicalCodingJob` requests per second per account and Region. See [Quotas for Amazon Connect Health](connecthealth-quotas.md).
+ IAM permissions to call the medical coding APIs and to write to your output bucket. If your domain uses a customer managed AWS KMS key, the caller also needs permission to use that key. See [Example IAM policy](#mc-gs-permissions).
+ The authorizations your organization requires to send protected health information (PHI) to AWS. Clinical documentation contains PHI. If you are subject to HIPAA, you must have a Business Associate Addendum (BAA) with AWS in place before you send PHI. See [Compliance validation for Amazon Connect Health](compliance-validation.md).

**Note**  
During the gated preview, SDK and CLI support for the medical coding APIs is provided by your AWS account team as part of onboarding. These operations are not yet available in the generally available AWS SDKs. In the preview SDKs, the operations are on the `HealthAgent` client. In the AWS CLI, they are `aws health-agent start-medical-coding-job` and `aws health-agent get-medical-coding-job`.

**Tip**  
The model is currently optimized for primary care. For your first jobs, use primary care documentation so that you evaluate the model where it performs best. If your use case is another specialty, see [Specialty scope and model performance](medical-coding.md#mc-specialty-scope).

### Example IAM policy
<a name="mc-gs-permissions"></a>

The following policy allows a caller to start and get medical coding jobs in one domain. The actions support resource-level permissions on the domain and on its medical coding jobs. Medical coding supports only the AWS global condition keys.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health-agent:StartMedicalCodingJob",
        "health-agent:GetMedicalCodingJob"
      ],
      "Resource": [
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>",
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>/medical-coding-job/*"
      ]
    }
  ]
}
```

The caller also needs `s3:PutObject` on the output location. `StartMedicalCodingJob` checks the S3 and AWS KMS permissions before it creates the job, and returns `AccessDeniedException` if any are missing.

## Step 1: Submit a coding job
<a name="mc-gs-step1"></a>

Call `StartMedicalCodingJob` with your clinical documentation in the `text` field and an S3 output location in `outputDataConfig.s3OutputPath`. Also include the `encounterContext` and `patientContext` fields. They are optional, but they are important for optimal coding accuracy, because the visit and patient details change which codes apply. For a complete example request and every allowed value, see [Medical coding inputs](mc-inputs.md).

```
POST /domain/{domainId}/medical-coding-job
```

The response returns a `jobId` that identifies the job:

```
{
  "creationTime": "2026-10-03T14:05:12Z",
  "jobArn": "arn:aws:health-agent:us-east-1:111122223333:domain/dom-a1b2c3d4e5f6g7h8/medical-coding-job/4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d",
  "jobId": "4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d"
}
```

## Step 2: Wait for the job to complete
<a name="mc-gs-step2"></a>

Medical coding runs asynchronously. Poll `GetMedicalCodingJob` with your domain ID and the `jobId` (1 to 36 characters) returned in Step 1. The request has no body.

```
GET /domain/{domainId}/medical-coding-job/{jobId}
```

Check `jobStatus`, which moves from `SUBMITTED` to `IN_PROGRESS` and then to `SUCCEEDED` or `FAILED`. For details, see [How medical coding works](mc-how-it-works.md).

## Step 3: Retrieve the suggested codes
<a name="mc-gs-step3"></a>

When `jobStatus` is `SUCCEEDED`, the response includes `medicalCodingOutput.uri`, the S3 location of the results file. Read that file. It contains a `medicalCodes` array. Each code gives its code system, a description, the linked diagnoses, the supporting evidence passages, any modifiers, and a confidence score. For an example response, the full structure of the results file, and rendering guidance, see [Medical coding outputs](mc-outputs.md).

## End-to-end example
<a name="mc-gs-end-to-end"></a>

The following language-neutral sketch shows the full flow for one encounter. Map each call to the equivalent method on the `HealthAgent` client in your SDK.

```
# One clientToken per encounter, so a retry never creates a duplicate job
token = "encounter-" + encounter_id

job = StartMedicalCodingJob(
    domainId = domain_id,
    clientToken = token,
    text = finalized_note,
    encounterContext = { encounterType: "IN_PERSON", encounterReason: reason, afterHours: false },
    patientContext   = { sex: sex, status: "ESTABLISHED", dateOfBirth: dob, insurance: payer },
    outputDataConfig = { s3OutputPath: "s3://amzn-s3-demo-bucket/medical-coding/" })

# Poll with exponential backoff until the job reaches a terminal state.
# A primary care note typically completes in about 35 seconds.
delay = 10 seconds   # initial delay
max_delay = 30 seconds
loop:
    result = GetMedicalCodingJob(domainId = domain_id, jobId = job.jobId)
    if result.jobStatus == "SUCCEEDED": break
    if result.jobStatus == "FAILED":    raise error(result.statusDetails)
    sleep(delay)
    delay = min(delay * 2, max_delay)

# The codes are in the results file, not in the API response
codes = read_json_from_s3(result.medicalCodingOutput.uri)["medicalCodes"]
```

## Next steps
<a name="mc-gs-next-steps"></a>
+ Choose where medical coding fits in your revenue cycle: at the point of care, in a coding workbench, or in an autonomous coding pipeline. See [Integrating medical coding into your workflows](mc-integration.md).
+ Build a review experience that lets coders accept, reject, or modify each suggestion. See [Medical coding outputs](mc-outputs.md).
+ If a job fails or an API call is rejected, see [Troubleshooting medical coding](mc-troubleshooting.md).