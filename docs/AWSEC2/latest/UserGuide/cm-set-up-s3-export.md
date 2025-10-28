# Setting up an Amazon S3 bucket for Capacity Manager data exports

To receive Capacity Manager data exports, you must have an Amazon S3 bucket in your AWS account to receive and store your export files.
When creating a data export in the Capacity Manager console, you can select an existing Amazon S3 bucket that you own or create a new bucket.

In either case, you must apply the required bucket policy to allow Capacity Manager to deliver export files. Editing this policy in
the Amazon S3 console or changing the bucket owner after you've created a data export will prevent Capacity Manager from delivering your exports.

To create an Amazon S3 bucket, see [Creating an S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md")
in the _Amazon Simple Storage Service User Guide_.

The following policy must be applied to your S3 bucket to allow Capacity Manager to deliver data exports:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.capacitymanager.amazonaws.com"
            },
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`111122223333`"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:ec2:us-east-1:`111122223333`:capacity-manager-data-export/*"
                }
            }
        }
    ]
}

```

This bucket policy helps ensure that Capacity Manager data export files can be delivered securely to your bucket. Specifically:

- Every time a Capacity Manager data export is delivered, AWS first confirms whether the bucket is still owned by the account that
  set up the export. If the bucket ownership has changed, the export will not be delivered. This helps to ensure the security of Capacity
  Manager data. This bucket policy allows AWS (`"Effect": "Allow"`) to check which account owns the bucket (`"Action": ["s3:ListBucket"]`).
- The policy grants the Capacity Manager service (`"Service": "ec2.capacitymanager.amazonaws.com"`) permission to write export files
  (`"Action": "s3:PutObject"`) and read objects (`"Action": "s3:GetObject"`) to copy data to your bucket.
