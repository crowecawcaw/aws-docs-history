# Troubleshooting S3 access point issues

This section describes symptoms, causes, and resolutions for when you encounter issues accessing your FSx data from S3 access points.

## The file system is unable to handle S3 requests

If the S3 request volume for a particular workload exceeds the file system’s capacity to handle the traffic, you may experience
S3 request errors (for example, `Internal Server Error`, `503 Slow Down`, and `Service Unavailable`).
You can proactively monitor and alarm on the performance of your file system using Amazon CloudWatch metrics (for example, `Network throughput
 utilization` and `CPU utilization`). If you observe degraded performance, you can resolve this issue by increasing the file system's
throughput capacity.

## Client ETag mismatch error with AWS Java SDK v1

When using the AWS Java SDK v1 to access data via the S3 API, you may encounter an SDK client exception
with the following message:

```
`Unable to verify integrity of data download. Client calculated content hash didn’t match hash calculated by Amazon S3`
```

This error occurs specifically when attempting to retrieve a file that was initially written or has been modified
using file-protocols. To resolve this issue, you can either configure your AWS Java SDK to disable MD5 checksum
validation on `GetObject` or update to the AWS Java SDK v2.

## Access Denied with default S3 access point permissions for automatically created service roles

Some S3-integrated AWS services will create a custom service role and customize the attached permissions to your
specific usecase. When specifying your S3 access point alias as the S3 resource, those attached permissions may include your access point
using a bucket ARN format (for example, `arn:aws:s3:::my-fsx-ap-foo7detztxouyjpwtu8krroppxytruse1a-ext-s3alias`)
rather than the access point ARN format (for example, `arn:aws:s3:us-east-1:1234567890:accesspoint/my-fsx-ap`).
To resolve this, modify the policy to use the ARN of the access point.
