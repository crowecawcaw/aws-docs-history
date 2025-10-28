# Setting up AutoUpdate

permissions

Rekognition supports the AutoUpdate feature for custom adapters. This means automated retraining is given a
best effort attempt when AutoUpdate flag is ENABLED on a project. These automatic updateds requires permission to access your
Training/Testing datasets and the AWS KMS key that you train your customer adapter with. You can provide these
permissions by following below steps.

## Amazon S3 Bucket Permissions

By default, all Amazon S3 buckets and objects are private. Only the
resource owner, the AWS account that created the bucket, can access the bucket
and any objects that it contains. However, the resource owner can choose to
grant access permissions to other resources and users by writing a bucket
policy.

If you want to create or modify an Amazon S3 bucket to be used
as a source of input datasets and destination of training results in a
custom adapter training, you must further modify the bucket policy. To
read from or write to an Amazon S3 bucket, Rekognition must have
the the following permissions.

**Rekognition Required Amazon S3 Policy**

Rekognition requires a permission policy with the following attributes:

- The statement SID
- The bucket name
- The service principal name for Rekognition.
- The resources required for Rekognition the bucket and all of its contents
- The required actions that Rekognition needs to take.

The following policy allows Rekognition to access an Amazon S3 bucket during automated retraining.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Sid": "AllowRekognitionAutoUpdateActions",
            "Principal": {
                "Service": "rekognition.amazonaws.com"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:HeadObject",
                "s3:HeadBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ]
        }
    ]
}
```

You can follow [this guide](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") to add above bucket policy to your S3 bucket.

See more information on bucket policies [here](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md").

## AWS KMS Key Permissions

Rekognition allows you to provide an optional KmsKeyId while training a custom adapter. When provided,
Rekognition uses this key to encrypt training and test images copied into the service for model training.
The key is also used to encrypt training results and manifest files written to the output Amazon S3 bucket (OutputConfig).

If you choose to provide a KMS key as input to your custom adapter
training (i.e.
`Rekognition:CreateProjectVersion`),
you must further modify the KMS Key policy to allow the Rekognition Service
Principal to use this key for automated retraining in the future.Rekognition must have the the following
permissions.

**Rekognition Required AWS KMS Key Policy**

Amazon Rekognition requires a permission policy with the following attributes:

- The statement SID
- The service principal name for Amazon Rekognition.
- The required actions that Amazon Rekognition needs to take.

The following key policy allows Amazon Rekognition to access an Amazon KMS key during automated retraining:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "KeyPermissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "rekognition.amazonaws.com"
 },
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can follow [this guide](../../../kms/latest/APIReference/API_PutKeyPolicy.md "../../../kms/latest/APIReference/API_PutKeyPolicy.md") to add above AWS KMS policy to your AWS KMS key.

See more information on AWS KMS policies [here](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md").
