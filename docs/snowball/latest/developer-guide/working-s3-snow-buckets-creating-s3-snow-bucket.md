Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Creating an S3 bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge

You can create Amazon S3 buckets on your Snowball Edge device to store and retrieve
objects at the edge for applications that require local data access, local data
processing, and data residency. Amazon S3 compatible storage on Snowball Edge provides a new storage class,
`SNOW`, which uses Amazon S3 and is designed to store data durably and
redundantly across multiple devices . You can use the same APIs and features as you
do on Amazon S3 buckets, including bucket lifecycle policies, encryption, and
tagging.

The following example creates an Amazon S3 bucket for a Snowball Edge device using the
AWS CLI. To run this command, replace the user input placeholders with your own
information.

###### Example of creating an S3 bucket

s3api syntax

```

aws s3api create-bucket --bucket `your-snow-bucket` --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`

```

s3control syntax

```

aws s3control create-bucket --bucket `your-snow-bucket` --endpoint-url https://`s3ctrlapi-endpoint-ip` --profile `your-profile`
```
