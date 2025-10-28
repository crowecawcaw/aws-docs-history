# Monitoring Spark jobs

So that you can monitor and troubleshoot failures, configure your interactive endpoints
so that the jobs initiated with the endpoint can send log information to Amazon S3, Amazon CloudWatch Logs, or
both. The following sections describe how to send Spark application logs to Amazon S3 for the
Spark jobs that you launch with Amazon EMR on EKS interactive endpoints.

**Configure IAM policy for Amazon S3 logs**

Before your kernels can send log data to Amazon S3, the permissions policy for the job
execution role must include the following permissions. Replace
`amzn-s3-demo-destination-bucket` with the name of your logging
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Sid": "AllowS3Putobject"
 }
 ]
}`

```

###### Note

Amazon EMR on EKS can also create an S3 bucket. If an S3 bucket is not available, include the
`s3:CreateBucket` permission in the IAM policy.

After you've given your execution role the permissions it needs to send logs to the S3
bucket, your log data is sent to the following Amazon S3 locations. This happens when
`s3MonitoringConfiguration` is passed in the
`monitoringConfiguration` section of a `create-managed-endpoint`
request.

- **Driver logs** –
  `logUri/virtual-cluster-id/endpoints/endpoint-id/containers/spark-application-id/spark-application-id-driver/(stderr.gz/stdout.gz)`
- **Executor logs** –
  `logUri/virtual-cluster-id/endpoints/endpoint-id/containers/spark-application-id/executor-pod-name-exec-<Number>/(stderr.gz/stdout.gz)`

###### Note

Amazon EMR on EKS doesn't upload the endpoint logs to your S3 bucket.
