# Copy an S3 prefix to job attachments on Deadline Cloud

The
[copy\_s3\_prefix\_to\_job\_attachments](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/copy_s3_prefix_to_job_attachments "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/copy_s3_prefix_to_job_attachments")
job bundle pre-populates a queue's job attachments S3 bucket by copying
files from where they are already stored in Amazon S3. If you are adding a
Deadline Cloud farm to a project that already has a large volume of data, or are
submitting a job that depends on a lot of new data such as a fluid
simulation output, the initial job attachments upload can be slow.

Because job attachments uses content-addressed storage and never
re-uploads files that are already in job attachments, you can use
alternative upload tools like
[AWS Snowball](https://aws.amazon.com/snowball/ "https://aws.amazon.com/snowball/") or
[AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") to copy data into Amazon S3 first, then use this
job to copy it into the job attachments bucket for your queue.

Submit the bundle and choose how many workers to parallelize across:

```
deadline bundle submit copy_s3_prefix_to_job_attachments \
    -p S3CopySource=s3://`SOURCE_BUCKET_NAME`/`prefix-to-copy` \
    -p Parallelism=20
```

Add the following IAM permissions to your queue IAM role. The role
already has permissions to read and write the job attachments bucket
prefix.

```
{
    "Effect": "Allow",
    "Sid": "DeadlineQueueReadOnly",
    "Action": [
        "deadline:GetQueue"
    ],
    "Resource": [
        "arn:aws:deadline:`REGION`:`ACCOUNT_ID`:farm/`FARM_ID`/queue/`QUEUE_ID`"
    ]
},
{
    "Effect": "Allow",
    "Sid": "SourceBucketAccess",
    "Action": [
        "s3:ListBucket",
        "s3:GetObjectTagging",
        "s3:PutObjectTagging",
        "s3:GetObject"
    ],
    "Resource": [
        "arn:aws:s3:::`SOURCE_BUCKET_NAME`",
        "arn:aws:s3:::`SOURCE_BUCKET_NAME`/*"
    ]
}
```

This job calls Amazon S3 APIs and copies data into your queue's job
attachments bucket, which incurs additional costs. Use the
[Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") page
and the [AWS Pricing Calculator](https://calculator.aws "https://calculator.aws")
to estimate costs.
