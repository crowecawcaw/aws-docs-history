# Use `UpdateJobPriority` with an AWS SDK or CLI

The following code examples show how to use `UpdateJobPriority`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Learn the basics](s3-control_example_s3-control_Basics_section.md "s3-control_example_s3-control_Basics_section.md")

CLI


**AWS CLI**

**To update the job priority of an Amazon S3 batch operations job**


The following `update-job-priority` example updates the specified job to a new priority.



```
`aws s3control update-job-priority \
 --account-id `123456789012` \
 --job-id `8d9a18fe-c303-4d39-8ccc-860d372da386` \
 --priority `52``

```

Output:



```
{
    "JobId": "8d9a18fe-c303-4d39-8ccc-860d372da386",
    "Priority": 52
}
```


* For API details, see
 [UpdateJobPriority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-priority.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-priority.html")
 in *AWS CLI Command Reference*.




Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/batch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/batch#code-examples").
 



```
    /**
     * Updates the priority of a job asynchronously.
     *
     * @param jobId     the ID of the job to update
     * @param accountId the ID of the account associated with the job
     * @return a {@link CompletableFuture} that represents the asynchronous operation, which completes when the job priority has been updated or an error has occurred
     */
    public CompletableFuture<Void> updateJobPriorityAsync(String jobId, String accountId) {
        UpdateJobPriorityRequest priorityRequest = UpdateJobPriorityRequest.builder()
            .accountId(accountId)
            .jobId(jobId)
            .priority(60)
            .build();

        CompletableFuture<Void> future = new CompletableFuture<>();
        getAsyncClient().updateJobPriority(priorityRequest)
            .thenAccept(response -> {
                System.out.println("The job priority was updated");
                future.complete(null); // Complete the CompletableFuture on successful execution
            })
            .exceptionally(ex -> {
                System.err.println("Failed to update job priority: " + ex.getMessage());
                future.completeExceptionally(ex); // Complete the CompletableFuture exceptionally on error
                return null; // Return null to handle the exception
            });

        return future;
    }


```


* For API details, see
 [UpdateJobPriority](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobPriority")
 in *AWS SDK for Java 2.x API Reference*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/batch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/batch#code-examples").
 



```
    def update_job_priority(self, job_id: str, account_id: str) -> None:
        """
        Update the priority of a batch job and start it.

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
            
            if current_status in ['Ready', 'Suspended']:
                self.s3control_client.update_job_priority(
                    AccountId=account_id,
                    JobId=job_id,
                    Priority=60
                )
                print("The job priority was updated")
                
                try:
                    self.s3control_client.update_job_status(
                        AccountId=account_id,
                        JobId=job_id,
                        RequestedJobStatus='Ready'
                    )
                    print("Job activated successfully")
                except ClientError as activation_error:
                    print(f"Note: Could not activate job automatically: {activation_error}")
                    print("Job priority was updated successfully. Job may need manual activation in the console.")
            elif current_status in ['Active', 'Completing', 'Complete']:
                print(f"Job is in '{current_status}' state - priority cannot be updated")
                if current_status == 'Completing':
                    print("Job is finishing up and will complete soon.")
                elif current_status == 'Complete':
                    print("Job has already completed successfully.")
                else:
                    print("Job is currently running.")
            else:
                print(f"Job is in '{current_status}' state - priority update not allowed")
                
        except ClientError as e:
            print(f"Error updating job priority: {e}")
            print("Continuing with the scenario...")
            return


```


* For API details, see
 [UpdateJobPriority](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobPriority "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobPriority")
 in *AWS SDK for Python (Boto3) API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
