

# Deleting the tags from an S3 Batch Operations job
<a name="delete-job-tags"></a>

You can use these examples to delete the tags from an Amazon S3 Batch Operations job.

## Using the AWS CLI
<a name="batch-ops-example-cli-job-tags-delete-job-tagging"></a>

The following example deletes the tags from a Batch Operations job using the AWS CLI.

```
aws \
    s3control delete-job-tagging \
    --account-id {{123456789012}} \
    --job-id {{Example-e25a-4ed2-8bee-7f8ed7fc2f1c}} \
    --region {{us-east-1}}
```

## Delete the job tags of a Batch Operations job
<a name="batch-ops-examples-java-job-with-tags-delete"></a>

To delete the tags of an S3 Batch Operations job using the AWS SDK for Java, you can use the S3Control client with the job ID to remove all tags associated with the batch operations job.

For examples of how to delete job tags with the AWS SDK for Java, see [Delete tags from a batch job](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_DeleteJobTagging_section.html) in the *Amazon S3 API Reference*.