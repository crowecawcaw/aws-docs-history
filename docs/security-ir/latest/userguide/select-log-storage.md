# Select log storage

The choice of log storage is generally related to which querying tool you use,
retention capabilities, familiarity, and cost. When you enable AWS service logs,
provide a storage facility; usually an Amazon S3 bucket or CloudWatch log group.

An Amazon S3 bucket provides cost-effective durable storage with an optional
lifecycle policy. Logs stored in Amazon S3 buckets can be natively queried using
services such as Amazon Athena. A CloudWatch log group provides durable storage and a built-in query facility through CloudWatch Logs Insights.
