# Use `UpdateJobStatus` with an AWS SDK or CLI

The following code examples show how to use `UpdateJobStatus`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Learn the basics](s3-control_example_s3-control_Basics_section.md "s3-control_example_s3-control_Basics_section.md")

CLI


**AWS CLI**

**To update the status of an Amazon S3 batch operations job**


The following `update-job-status` example cancels the specified job which is awaiting approval.



```
`aws s3control update-job-status \
 --account-id `123456789012` \
 --job-id `8d9a18fe-c303-4d39-8ccc-860d372da386` \
 --requested-job-status `Cancelled``

```

Output:



```
{
    "Status": "Cancelled",
    "JobId": "8d9a18fe-c303-4d39-8ccc-860d372da386"
}
```

The following `update-job-status` example confirms and runs the specified which is awaiting approval.



```
`aws s3control update-job-status \
 --account-id `123456789012` \
 --job-id `5782949f-3301-4fb3-be34-8d5bab54dbca` \
 --requested-job-status `Ready`

`Output::`

`{`
 "Status": "Ready",
 "JobId": `"5782949f-3301-4fb3-be34-8d5bab54dbca"`
`}``

```

The following `update-job-status` example cancels the specified job which is running.



```
 aws s3control update-job-status \
    --account-id 123456789012 \
    --job-id 5782949f-3301-4fb3-be34-8d5bab54dbca \
    --requested-job-status Cancelled

Output::
{
         "Status": "Cancelling",
         "JobId": "5782949f-3301-4fb3-be34-8d5bab54dbca"
}
```


* For API details, see
 [UpdateJobStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-status.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/batch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/batch#code-examples").
 



```
    /**
     * Cancels a job asynchronously.
     *
     * @param jobId The ID of the job to be canceled.
     * @param accountId The ID of the account associated with the job.
     * @return A {@link CompletableFuture} that completes when the job status has been updated to "CANCELLED".
     *         If an error occurs during the update, the returned future will complete exceptionally.
     */
    public CompletableFuture<Void> cancelJobAsync(String jobId, String accountId) {
        UpdateJobStatusRequest updateJobStatusRequest = UpdateJobStatusRequest.builder()
            .accountId(accountId)
            .jobId(jobId)
            .requestedJobStatus(String.valueOf(JobStatus.CANCELLED))
            .build();

        return asyncClient.updateJobStatus(updateJobStatusRequest)
            .thenAccept(updateJobStatusResponse -> {
                System.out.println("Job status updated to: " + updateJobStatusResponse.status());
            })
            .exceptionally(ex -> {
                System.err.println("Failed to cancel job: " + ex.getMessage());
                throw new RuntimeException(ex); // Propagate the exception
            });
    }


```


* For API details, see
 [UpdateJobStatus](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobStatus")
 in *AWS SDK for Java 2.x API Reference*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/batch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/batch#code-examples").
 



```
    def cancel_job(self, job_id: str, account_id: str) -> None:
        """
        Cancel an S3 batch job.

        Args:
            job_id (str): ID of the batch job
            account_id (str): AWS account ID
        """
        try:
            response = self.s3control_client.describe_job(
                AccountId=account_id,
                JobId=job_id
            )
            current_status = response['Job']['Status']
            print(f"Current job status: {current_status}")

            if current_status in ['Ready', 'Suspended', 'Active']:
                self.s3control_client.update_job_status(
                    AccountId=account_id,
                    JobId=job_id,
                    RequestedJobStatus='Cancelled'
                )
                print(f"Job {job_id} was successfully canceled.")
            elif current_status in ['Completing', 'Complete']:
                print(f"Job is in '{current_status}' state - cannot be cancelled")
                if current_status == 'Completing':
                    print("Job is finishing up and will complete soon.")
                elif current_status == 'Complete':
                    print("Job has already completed successfully.")
            else:
                print(f"Job is in '{current_status}' state - cancel not allowed")
        except ClientError as e:
            print(f"Error canceling job: {e}")
            raise


```


* For API details, see
 [UpdateJobStatus](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobStatus "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobStatus")
 in *AWS SDK for Python (Boto3) API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
