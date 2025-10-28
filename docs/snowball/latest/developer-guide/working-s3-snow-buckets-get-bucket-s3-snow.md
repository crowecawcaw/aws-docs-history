Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Getting a bucket with Amazon S3 compatible storage on Snowball Edge on a Snowball Edge

The following example gets an Amazon S3 compatible storage on Snowball Edge bucket using the AWS CLI. To use this
command, replace each user input placeholder with your own information.

```
aws s3control get-bucket --account-id `123456789012` --bucket amzn-s3-demo-bucket --endpoint-url https://`s3ctrlapi-endpoint-ip` --profile `your-profile`
```

For more information about this command, see [get-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket.html") in the AWS CLI Command Reference.

The following Amazon S3 compatible storage on Snowball Edge example gets a bucket using the SDK for Java. For more
information, see [GetBucket](../../../AmazonS3/latest/API/API_control_GetBucket.md "../../../AmazonS3/latest/API/API_control_GetBucket.md") in the [Amazon Simple Storage Service API Reference](../../../AmazonS3/latest/API.md "../../../AmazonS3/latest/API.md").

```

import com.amazonaws.services.s3control.model.*;

public void getBucket(String bucketName) {

    GetBucketRequest reqGetBucket = new GetBucketRequest()
            .withBucket(bucketName)
            .withAccountId(AccountId);

    GetBucketResult respGetBucket = s3ControlClient.getBucket(reqGetBucket);
    System.out.printf("GetBucket Response: %s%n", respGetBucket.toString());
}

```
