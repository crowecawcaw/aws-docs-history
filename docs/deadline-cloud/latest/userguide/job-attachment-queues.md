# Secure job attachment and software buckets

Each queue stores its job attachments in an Amazon S3 bucket that you own. Three pieces
configure the connection between a queue and its bucket:

- Job attachments write to and read from a root prefix in the Amazon S3 bucket. You
  specify this root prefix in the `CreateQueue` API call.
- The bucket has a corresponding `Queue Role`, which specifies the role
  that grants queue users access to the bucket and root prefix. When creating a queue,
  you specify the `Queue Role` Amazon Resource Name (ARN) alongside the job
  attachments bucket and root prefix.
- Authorized calls to the `AssumeQueueRoleForRead`,
  `AssumeQueueRoleForUser`, and `AssumeQueueRoleForWorker` API
  operations return a set of temporary security credentials for the `Queue
 Role`.
  Queues that share an Amazon S3 bucket and root prefix also share access to the job
  attachments stored there. Give each queue its own bucket and root prefix so that queue
  permission boundaries also apply to job attachments. For example, when QueueA and QueueB
  have separate buckets, an artist with access to only QueueA can't read QueueB's job
  attachments. If several queues belong to the same security boundary, such as the queues
  for one show, sharing a bucket between them is a reasonable simplification. The console
  sets up each queue with its own bucket and root prefix by default.

To isolate your queues, you must configure the `Queue Role` to only allow
queue access to the bucket and root prefix. In the following example, replace each
`placeholder` with your resource-specific information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::`JOB_ATTACHMENTS_BUCKET_NAME`",
 "arn:aws:s3:::`JOB_ATTACHMENTS_BUCKET_NAME`/`JOB_ATTACHMENTS_ROOT_PREFIX`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Action": [
 "logs:GetLogEvents"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/deadline/`FARM_ID`/*"
 }
 ]
}`

```

You must also set a trust policy on the role. In the following example, replace the
`placeholder` text with your resource-specific
information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": "deadline.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:deadline:`us-east-1`:`111122223333`:farm/`FARM_ID`"
 }
 }
 },
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.deadline.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:deadline:`us-east-1`:`111122223333`:farm/`FARM_ID`"
 }
 }
 }
 ]
}`

```

## Custom software Amazon S3 buckets

You can add the following statement to your `Queue Role` to access custom
software in your Amazon S3 bucket. In the following example, replace
`SOFTWARE_BUCKET_NAME` with the name of your S3 bucket and `BUCKET_ACCOUNT_OWNER` with the AWS account ID that owns the bucket.

```
"Statement": [
    {
        "Action": [
            "s3:GetObject",
            "s3:ListBucket"
        ],
        "Effect": "Allow",
        "Resource": [
            "arn:aws:s3:::`SOFTWARE_BUCKET_NAME`",
            "arn:aws:s3:::`SOFTWARE_BUCKET_NAME`/*"
        ],
        "Condition": {
         "StringEquals": {
            "aws:ResourceAccount": "`BUCKET_ACCOUNT_OWNER`"
         }
      }
    }
]
```

For more information about Amazon S3 security best practices, see [Security best practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") in the _Amazon Simple Storage Service User Guide_.
