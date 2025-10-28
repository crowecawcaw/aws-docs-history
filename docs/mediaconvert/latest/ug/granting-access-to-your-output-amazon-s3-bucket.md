# Granting access to

your output Amazon S3 bucket

Suppose that you want the outputs of your MediaConvert jobs to reside in an Amazon S3
bucket that you own, but you want users that belong to another AWS account to have
access to them. To grant access, you can add an Amazon S3 bucket policy to your output
bucket.

For a tutorial about how to grant this access, see [Example 2:
Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in the _Amazon Simple Storage Service User Guide_.

The following example bucket policy grants access to your output bucket:

```

{
    "Id": "Policy1572454561447",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1572454547712",
            "Action": [
                "s3:GetObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Principal": {
                "AWS": [
                    "111122223333"
                ]
            }
        }
    ]
}

```
