# Create a signing job for IoT in AWS Signer

To start a signing job, you need to specify the following:

- The source S3 bucket of the IoT binary to be signed
- A signing profile
- The destination S3 bucket for the signed file
  A signing job has a status of `InProgress` while it is being processed,
  and after completion, the status changes to `Succeeded`. If Signer is
  unable to generate a signature, the signing job updates to `Failed`.
  Signing fails for a zip file if the file is empty, already has a signature, or is
  malformed.

**To perform a signing job (CLI)**

Use the following CLI commands to run and manage signing jobs.

- [**start-signing-job**](../../../cli/latest/reference/signer/start-signing-job.md "../../../cli/latest/reference/signer/start-signing-job.md")
  To get the status of a particular signing job, use the following action or
  command:

- [**describe-signing-job**](../../../cli/latest/reference/signer/describe-signing-job.md "../../../cli/latest/reference/signer/describe-signing-job.md")
  For a list of all available signing jobs, including those in the Failed state, use
  the following action or command:

- [**list-signing-jobs**](../../../cli/latest/reference/signer/list-signing-jobs.md "../../../cli/latest/reference/signer/list-signing-jobs.md")
  **To perform a signing job (API)**

Use the following API actions to run and manage signing jobs.

- [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md")
- [`DescribeSigningJob`](../api/API_DescribeSigningJob.md "../api/API_DescribeSigningJob.md")
- [`ListSigningJobs`](../api/API_ListSigningJobs.md "../api/API_ListSigningJobs.md")
  For more information about configurations and parameters related to signing jobs,
  see [`SigningJob`](../api/API_SigningJob.md "../api/API_SigningJob.md")
  in the _AWS Signer API Reference._
