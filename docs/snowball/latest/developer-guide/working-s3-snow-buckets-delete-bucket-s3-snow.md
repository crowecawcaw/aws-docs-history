Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Deleting a bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge

You can use the s3api SDK or s3control SDK to delete a bucket in Amazon S3 compatible storage on Snowball Edge.

###### Important

- The AWS account that creates the bucket owns it and is the only one
  that can delete it.
- Snowball Edge buckets must be empty before they can be deleted.
- You cannot recover a bucket after it has been deleted.
  The following examples delete an Amazon S3 compatible storage on Snowball Edge bucket using the AWS CLI. To use this
  command, replace each user input placeholder with your own information.

###### Example of deleting a bucket

s3api syntax

```

aws s3api delete-bucket --bucket `amzn-s3-demo-bucket` --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`

```

For more information about this command, see [delete-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html") in the AWS CLI Command Reference.

s3control syntax

```

aws s3control delete-bucket --account-id `123456789012` --bucket amzn-s3-demo-bucket --endpoint-url https://`s3ctrlapi-endpoint-ip` --profile `your-profile`
```

For more information about this command, see [delete-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket.html") in the AWS CLI Command
Reference.
