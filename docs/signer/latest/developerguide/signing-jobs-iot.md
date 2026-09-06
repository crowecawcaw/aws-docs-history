

# Create a signing job for IoT in AWS Signer
<a name="signing-jobs-iot"></a>

To start a signing job, you need to specify the following:
+ The source S3 bucket of the IoT binary to be signed
+ A signing profile
+ The destination S3 bucket for the signed file

A signing job has a status of `InProgress` while it is being processed, and after completion, the status changes to `Succeeded`. If Signer is unable to generate a signature, the signing job updates to `Failed`. Signing fails for a zip file if the file is empty, already has a signature, or is malformed. 



**To perform a signing job (CLI)**

Use the following CLI commands to run and manage signing jobs. 
+ [**start-signing-job**](https://docs.aws.amazon.com/cli/latest/reference/signer/start-signing-job.html)

To get the status of a particular signing job, use the following action or command: 
+ [**describe-signing-job**](https://docs.aws.amazon.com/cli/latest/reference/signer/describe-signing-job.html)

For a list of all available signing jobs, including those in the Failed state, use the following action or command: 
+ [**list-signing-jobs**](https://docs.aws.amazon.com/cli/latest/reference/signer/list-signing-jobs.html) 

**To perform a signing job (API)**

Use the following API actions to run and manage signing jobs. 
+ [`StartSigningJob`](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html)
+ [`DescribeSigningJob`](https://docs.aws.amazon.com/signer/latest/api/API_DescribeSigningJob.html)
+ [`ListSigningJobs`](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningJobs.html)

For more information about configurations and parameters related to signing jobs, see [`SigningJob`](https://docs.aws.amazon.com/signer/latest/api/API_SigningJob.html) in the *AWS Signer API Reference.*