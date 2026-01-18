# Verifying AWS CloudTrail Is Enabled

As part of the automated AWS GovCloud (US) activation process, the CloudTrail service should be enabled for each account and an Amazon S3 bucket should be created to store CloudTrail logs. In the event of any interruptions in the automation process, you can manually enable CloudTrail.

###### To verify the S3 bucket was created for CloudTrail log storage

1. Sign in to the AWS GovCloud (US) console and open the Amazon S3 console at [link](https://console.amazonaws-us-gov.com/s3 "https://console.amazonaws-us-gov.com/s3").
2. If a bucket already exists, skip to the next procedure to ensure CloudTrail is enabled.
3. Choose **Create Bucket**.
4. Type a name for your bucket.

Bucket names must be unique. S3 buckets created during the automated process follow the naming convention "cloudtrail-<xxxxxxxxxxxx>" where <xxxxxxxxxxxx> is replaced by the AWS GovCloud (US) account number. If you want to use a different bucket name, you can delete this bucket, create a new bucket, and then follow the steps in the next section to enable CloudTrail.

###### To verify CloudTrail is enabled

1. Sign in to the AWS GovCloud (US) console and open the CloudTrail console at [link](https://console.amazonaws-us-gov.com/cloudtrail "https://console.amazonaws-us-gov.com/cloudtrail").
2. If CloudTrail is enabled, the **Dashboard** page opens, and the **Trails** section shows your trail.
3. If CloudTrail is not enabled, choose **Create a trail**. For more information about creating a trail using the console, see [Creating a trail in the console (advanced event selectors)](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console-adv "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console-adv") in the _AWS CloudTrail User Guide_.

###### Note

For the **Storage location**, choose **Use existing S3 bucket**, and specify the S3 bucket you created in the previous procedure.

This will set a bucket policy that allows the CloudTrail service to store logs in the S3 bucket. If the automated process created an S3 bucket and enabled CloudTrail, the following policy was applied:

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudtrail.amazonaws.com"
            },
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws-us-gov:s3:::s3_bucket_name",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws-us-gov:cloudtrail:region:account_id:trail/trail_name"
                }
            }
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudtrail.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws-us-gov:s3:::s3_bucket_name/AWSLogs/account_id/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control",
                    "aws:SourceArn": "arn:aws-us-gov:cloudtrail:region:account_id:trail/trail_name"
                }
            }
        }
    ]
}
```
