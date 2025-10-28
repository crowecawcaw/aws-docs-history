Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Determining whether you can access an Amazon S3 compatible storage on Snowball Edge

bucket on a Snowball Edge

The following example uses the `head-bucket` command to determine if an
Amazon S3 bucket exists and you have permissions to access it using the AWS CLI. To use
this command, replace each user input placeholder with your own information.

```
aws s3api head-bucket --bucket `sample-bucket` --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`
```
