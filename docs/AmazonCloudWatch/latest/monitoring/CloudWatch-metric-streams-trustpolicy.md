# Trust between CloudWatch and Firehose

The Firehose delivery stream must trust CloudWatch through an IAM role that has write permissions
to Firehose. These permissions can be limited to the single Firehose delivery stream that the CloudWatch metric
stream uses. The IAM role must trust the `streams.metrics.cloudwatch.amazonaws.com`
service principal.

If you use the CloudWatch console to create a metric stream, you can have CloudWatch create the role
with the correct permissions. If you use another method to create a metric stream, or you want to
create the IAM role itself, it must contain the following permissions policy
and trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "streams.metrics.cloudwatch.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Metric data is streamed by CloudWatch to the destination Firehose delivery stream on
behalf of the source
that owns the metric stream resource.
