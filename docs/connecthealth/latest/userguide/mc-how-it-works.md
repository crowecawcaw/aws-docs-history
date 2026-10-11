

# How medical coding works
<a name="mc-how-it-works"></a>

Medical coding follows the same reasoning a professional coder uses. It runs as an asynchronous job: you start a job, the service processes it in the background, and you retrieve the results when the job completes. This model suits coding workflows where documentation is finalized first and coded afterward, and it lets you submit many jobs without holding a connection open.

**Topics**
+ [From documentation to codes](#mc-derivation)
+ [The job lifecycle](#mc-job-lifecycle)
+ [Job status](#mc-job-status)
+ [Idempotent submissions](#mc-idempotency)

## From documentation to codes
<a name="mc-derivation"></a>

After you call `StartMedicalCodingJob`, the medical coding service processes the job in the following steps. Your application doesn’t run or control these steps. It submits the job and reads the result.

1.  **Read the encounter.** The service reads the clinical documentation together with the encounter context and patient context you provide.

1.  **Extract the clinical facts.** It identifies the conditions addressed, the procedures performed, and the services rendered.

1.  **Determine the E/M level.** For visits, it assesses the problems addressed and the risk of patient management documented in the note, following MDM guidelines, and assigns the E/M level the documentation supports.

1.  **Assign codes.** It assigns ICD-10-CM codes to diagnoses and CPT codes to procedures and services, adding modifiers where the documentation requires them. It uses the most specific code the documentation supports.

1.  **Link and support.** It links each CPT code to the diagnoses that establish its medical necessity, attaches the note passages that support each code, and assigns each code a confidence score.

1.  **Deliver.** It writes the result as structured JSON to your S3 output location, and `GetMedicalCodingJob` returns the location of the file.

![How the medical coding agent turns a clinical note and context into linked ICD-10-CM and CPT codes.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-derivation.png)


## The job lifecycle
<a name="mc-job-lifecycle"></a>


| Step | What happens | Your role | 
| --- | --- | --- | 
| 1. Submit | You call `StartMedicalCodingJob` with clinical documentation and an Amazon S3 output location. The API returns a `jobId`. | Provide the text and output path, and include encounter and patient context whenever you have it. | 
| 2. Process | The service derives the code set from the documentation, as described in [From documentation to codes](#mc-derivation), and writes the results file to your S3 location. | None. Processing runs in the background. | 
| 3. Retrieve | You call `GetMedicalCodingJob` with the `jobId`. When the job has succeeded, the response gives the S3 location of the results file. | Poll for completion, then read the results file. | 

The quality of the suggested codes depends on what you provide at the submit step. The `encounterContext` and `patientContext` fields are optional, but they are important for optimal coding accuracy, because the visit type and the patient’s status and demographics change which codes apply. Include them whenever you have the data. See [Medical coding inputs](mc-inputs.md).

## Job status
<a name="mc-job-status"></a>

 `GetMedicalCodingJob` returns the job’s current state in `jobStatus`. A job normally moves from `SUBMITTED` to `IN_PROGRESS`, and then to `SUCCEEDED` or `FAILED`. In rare cases, such as a service infrastructure issue that keeps a job from starting, a job can move directly from `SUBMITTED` to `FAILED`.

![Medical coding job states: SUBMITTED, then IN_PROGRESS, then SUCCEEDED or FAILED.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-job-status.png)



|  `jobStatus`  | Meaning | What to do | 
| --- | --- | --- | 
|  `SUBMITTED`  | The job has been accepted and is queued. | Keep polling. | 
|  `IN_PROGRESS`  | The service is analyzing the documentation and generating codes. | Keep polling. | 
|  `SUCCEEDED`  | The job completed. The results file is in your S3 output location, and the response gives its URI. | Read the results. See [Medical coding outputs](mc-outputs.md). | 
|  `FAILED`  | The job did not complete. `statusDetails` describes the reason. | Check `statusDetails`. See [Troubleshooting medical coding](mc-troubleshooting.md). | 

**Tip**  
A primary care note typically completes in about 35 seconds. Wait about 10 seconds before the first `GetMedicalCodingJob` call, then back off exponentially to a maximum interval of 30 seconds. Each response also includes `creationTime` and `updatedTime`, so you can see how long a job has been running.

Some problems are caught before a job is created. `StartMedicalCodingJob` validates the input and checks the S3 and AWS KMS permissions first. If a check fails, the call returns an error, such as `ValidationException` or `AccessDeniedException`, and no job is created.

## Idempotent submissions
<a name="mc-idempotency"></a>

 `StartMedicalCodingJob` accepts an optional `clientToken`, a unique, case-sensitive identifier you provide. If a request is retried with the same `clientToken` (for example, after a network timeout), the service treats it as the same job instead of starting a duplicate. Use a `clientToken` whenever your application might retry a submission.