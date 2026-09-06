

# Dataset export job permissions requirements
<a name="export-permissions"></a>

To export a dataset, Amazon Personalize needs permission to add files to your Amazon S3 bucket. To grant permissions, attach a new AWS Identity and Access Management (IAM) policy to your Amazon Personalize service role that grants the role permission to use the `PutObject` and `ListBucket` Actions on your bucket, and attach a bucket policy to your output Amazon S3 bucket that grants the Amazon Personalize principle permission to use the `PutObject` and `ListBucket` Actions.

 If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md).

## Service role policy for exporting a dataset
<a name="role-policy-for-dataset-export-job"></a>

The following example policy grants your Amazon Personalize service role permission to use the `PutObject` and `ListBucket` Actions. Replace `amzn-s3-demo-bucket` with the name of your output bucket. For information about attaching policies to a IAM service role, see [Attaching an Amazon S3 policy to your Amazon Personalize service role](granting-personalize-s3-access.md#attaching-s3-policy-to-role). 

```
{
    "Version": "2012-10-17",		 	 	 
    "Id": "PersonalizeS3BucketAccessPolicy",
    "Statement": [
        {
            "Sid": "PersonalizeS3BucketAccessPolicy",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        }
    ]
}
```

## Amazon S3 bucket policy for exporting a dataset
<a name="bucket-policy-for-dataset-export-job"></a>

The following example policy grants Amazon Personalize permission to use the `PutObject` and `ListBucket` Actions on an Amazon S3 bucket. Replace `amzn-s3-demo-bucket` with the name of your bucket. For information on adding an Amazon S3 bucket policy to a bucket, see [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) in the *Amazon Simple Storage Service User Guide.* 

```
{
    "Version": "2012-10-17",		 	 	 
    "Id": "PersonalizeS3BucketAccessPolicy",
    "Statement": [
        {
            "Sid": "PersonalizeS3BucketAccessPolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "personalize.amazonaws.com"
            },
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        }
    ]
}
```