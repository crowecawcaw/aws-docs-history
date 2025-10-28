# Create a signing job for Lambda in AWS Signer

To start a signing job, you need to specify the following:

- The source S3 bucket of the IoT code or Lambda zip file to be signed
- A signing profile
- The destination S3 bucket for the signed file
  A signing job has a status of `InProgress` while it is being processed,
  and after completion, the status changes to `Succeeded`. If Signer is
  unable to generate a signature, the signing job updates to `Failed`.
  Signing fails for a zip file if the file is empty, already has a signature, or is
  malformed.

###### To perform a signing job (console)

1. Log into the AWS Signer console.
2. Choose **Start signing jobs**.
3. From the list of profiles, choose a signing profile to perform code
   signing for your Lambda application.
4. Do either of the following:
   - For **Code asset source location**, enter the URL
     for the Amazon S3 bucket that contains your code.
   - Choose **Browse**, and locate the S3 bucket that
     contains your code.

###### Note

Be sure your file is in zip format. The AWS Signer console does not
accept other file formats. 5. Do one of the following:

    * In the **Signature Destination path with
     Prefix**, enter the URL for the S3 bucket where you store
     your signed code.
    * Choose **Browse** and locate the S3 bucket that
     stores your signed code.

6. Choose **Start**.

AWS Signer updates the **Manage signing jobs** page
with your new profile, and displays the following information:

    * **Job ID** – The generated ID
     number
    * **Profile name** – The name of the
     profile
    * **Signing status** – The signing status of
     the job
    * **Revocation status** – The status of the
     revocation if any

7. If you receive a **Failed** under **Signing
   status**, return to the list of the signing jobs, and choose
   **Failed** to see the details of the signing
   job.
   The **Signing job details** page lists the following
   information:

- **Job ID** – The identifier of the signing
  job
- **Signing profile used** – The signing profile
  used for the job
- **Version of signing profiles used** – The version
  of the signing profile used for the job
- **Requested by** – Identity of the requester of
  the job
- **Signing platform** – The signing platform used
  for the job (Lambda only)
- **Signing status** – The status of the job as
  either **Successful** or **Failed**
- **Status reason** – Explanation for the failure if
  the signing job failed
- **Started at** – The time and date that the
  signing job started
- **Completed at** – The time and date that the job
  ended
  The **Code assets details** displays additional
  information:

- **Code asset source bucket** – The S3 source
  bucket of the code file used
- **Code asset source key** – The name of the code
  file used for signing code
- **Code asset source version** – The version of the
  code file
  **To perform a signing job (AWS CLI)**

Use the following command to start a signing job:

- [**start-signing-job**](../../../cli/latest/reference/signer/start-signing-job.md "../../../cli/latest/reference/signer/start-signing-job.md")
  To get the status of a particular signing job, use the following command:

- [**describe-signing-job**](../../../cli/latest/reference/signer/describe-signing-job.md "../../../cli/latest/reference/signer/describe-signing-job.md")
  For a list of all available signing jobs, including those in the Failed state, use
  the following command:

- [**list-signing-jobs**](../../../cli/latest/reference/signer/list-signing-jobs.md "../../../cli/latest/reference/signer/list-signing-jobs.md")
  **To perform a signing job (API)**

Following API actions can be used to run and track signing jobs.

- [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md")
- [`DescribeSigningJob`](../api/API_DescribeSigningJob.md "../api/API_DescribeSigningJob.md")
- [`ListSigningJobs`](../api/API_ListSigningJobs.md "../api/API_ListSigningJobs.md")
  For more information about configurations and parameters related to signing jobs,
  see [`SigningJob`](../api/API_SigningJob.md "../api/API_SigningJob.md")
  in the _AWS Signer API Reference._
