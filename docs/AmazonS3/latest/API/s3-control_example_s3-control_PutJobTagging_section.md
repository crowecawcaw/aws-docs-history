# Use `PutJobTagging` with an AWS SDK

The following code examples show how to use `PutJobTagging`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Learn the basics](s3-control_example_s3-control_Basics_section.md "s3-control_example_s3-control_Basics_section.md")

Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/batch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3/src/main/java/com/example/s3/batch#code-examples").
 



```
    /**
     * Asynchronously adds tags to a job in the system.
     *
     * @param jobId     the ID of the job to add tags to
     * @param accountId the account ID associated with the job
     * @return a CompletableFuture that completes when the tagging operation is finished
     */
    public CompletableFuture<Void> putJobTaggingAsync(String jobId, String accountId) {
        S3Tag departmentTag = S3Tag.builder()
            .key("department")
            .value("Marketing")
            .build();

        S3Tag fiscalYearTag = S3Tag.builder()
            .key("FiscalYear")
            .value("2020")
            .build();

        PutJobTaggingRequest putJobTaggingRequest = PutJobTaggingRequest.builder()
            .jobId(jobId)
            .accountId(accountId)
            .tags(departmentTag, fiscalYearTag)
            .build();

        return asyncClient.putJobTagging(putJobTaggingRequest)
            .thenRun(() -> {
                System.out.println("Additional Tags were added to job " + jobId);
            })
            .exceptionally(ex -> {
                System.err.println("Failed to add tags to job: " + ex.getMessage());
                throw new RuntimeException(ex); // Propagate the exception
            });
    }


```


* For API details, see
 [PutJobTagging](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutJobTagging")
 in *AWS SDK for Java 2.x API Reference*.




Python


**SDK for Python (Boto3)**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/batch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/batch#code-examples").
 



```
    def put_job_tags(self, job_id: str, account_id: str) -> None:
        """
        Add tags to a batch job.

        Args:
            job_id (str): ID of the batch job
            account_id (str): AWS account ID
        """
        try:
            self.s3control_client.put_job_tagging(
                AccountId=account_id,
                JobId=job_id,
                Tags=[
                    {'Key': 'Environment', 'Value': 'Development'},
                    {'Key': 'Team', 'Value': 'DataProcessing'}
                ]
            )
            print(f"Additional tags were added to job {job_id}")
        except ClientError as e:
            print(f"Error adding job tags: {e}")
            raise


```


* For API details, see
 [PutJobTagging](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutJobTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutJobTagging")
 in *AWS SDK for Python (Boto3) API Reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
