# Adding job tags to an existing Batch Operations job

You can use the [PutJobTagging](../API/API_control_PutJobTagging.md "../API/API_control_PutJobTagging.md") API operation to add job tags to your existing
 Amazon S3 Batch Operations jobs. For more information, see the following examples.

The following is an example of using `s3control put-job-tagging` to add job
 tags to your S3 Batch Operations job by using the AWS CLI. To use the examples, replace the
 ``user input placeholders`` with your
 own information.

###### Note

If you send this request with an empty tag set, Batch Operations deletes the existing tag set on the
 object. However, if you use this approach, you are charged for a Tier 1 Request
 (`PUT`). For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

Instead, to delete existing tags for your Batch Operations job, we recommend using the
 `DeleteJobTagging` operation because it achieves the same result
 without incurring charges.

1. Identify the job `TAGS` that you want for the job. In this case,
 you apply two tags, ``department`` and
 ``FiscalYear``, with the values
 ``Marketing`` and
 ``2020`` respectively.



```
read -d '' TAGS <<EOF
[
  {
    "Key": "`department`",
    "Value": "`Marketing`"
  },
  {
    "Key": "`FiscalYear`",
    "Value": "`2020`"
  }
]
EOF
```
2. Run the following `put-job-tagging` command with the required
 parameters:



```
aws \
    s3control put-job-tagging \
    --account-id `123456789012` \
    --tags "${TAGS//$'\n'/}" \
    --job-id `Example-e25a-4ed2-8bee-7f8ed7fc2f1c` \
    --region `us-east-1`  
```
To put tags on an S3 Batch Operations job using the AWS SDK for Java, you can use the S3Control client to add or update tags with key-value pairs for organization and tracking purposes.

For examples of how to put job tags with the AWS SDK for Java, see [Add tags to a batch job](../API/s3-control_example_s3-control_PutJobTagging_section.md "../API/s3-control_example_s3-control_PutJobTagging_section.md") in the *Amazon S3 API Reference*.
