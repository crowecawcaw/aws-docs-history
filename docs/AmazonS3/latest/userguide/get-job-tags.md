# Getting the tags of a S3 Batch Operations job

To retrieve the tags of an Amazon S3 Batch Operations job, you can use the
`GetJobTagging` API operation. For more information, see the following
examples.

The following example gets the tags of a Batch Operations job using the AWS CLI. To use
this example, replace the `user input
 placeholders` with your own information.

```
aws \
    s3control get-job-tagging \
    --account-id `123456789012` \
    --job-id `Example-e25a-4ed2-8bee-7f8ed7fc2f1c` \
    --region `us-east-1`
```

To get the tags of an S3 Batch Operations job using the AWS SDK for Java, you can use the S3Control client with the job ID to retrieve all tags associated with the batch operations job and return them as a list.

For examples of how to get job tags with the AWS SDK for Java, see [Get tags from a batch job](../API/s3-control_example_s3-control_GetJobTagging_section.md "../API/s3-control_example_s3-control_GetJobTagging_section.md") in the _Amazon S3 API Reference_.
