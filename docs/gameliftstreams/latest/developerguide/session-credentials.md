# Provide AWS credentials to your streaming application

By default, applications running on Amazon GameLift Streams do not have access to AWS resources in
your account. If your application needs to call AWS APIs — for example, to read from your
Amazon S3 buckets, write to your DynamoDB tables, or publish metrics to CloudWatch — you can provide an
IAM role when starting a stream session. Amazon GameLift Streams assumes the role on your behalf and makes
credentials available to your application. You do not need to change your application code.
