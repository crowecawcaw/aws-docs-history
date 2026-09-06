

# Specifying an existing S3 bucket for your recommendations export
<a name="create-s3-bucket-policy-for-compute-optimizer"></a>

You can export your Compute Optimizer recommendations to an Amazon Simple Storage Service (Amazon S3) bucket. Your recommendations are exported as CSV file and the metadata is exported as a JSON file. This section provides you with instructions on how to specify an Amazon S3 bucket for your recommendation export by adding a policy to the bucket. The policy that you add allows Compute Optimizer to write recommendations export files to your Amazon S3 bucket.

## Prerequisites
<a name="s3-export-prerequisites"></a>

Make sure that you create a destination S3 bucket for your recommendations export. The S3 bucket that you specify for your recommendations export files must not be publicly accessible, and can't be configured as a [Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) bucket. As a security best practice, create a dedicated S3 bucket for Compute Optimizer export files. For more information, see [How Do I Create an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket.html) in the *Amazon S3 Console User Guide*.

## Procedure
<a name="specify-an-existing-bucket-for-cloudtrail-log-delivery"></a>

After you create your S3 bucket, follow these steps to add a policy to the S3 bucket that allows Compute Optimizer to write recommendations export files to your bucket.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the bucket where you want Compute Optimizer to deliver your export files.

1. Choose **Permissions**.

1. Choose **Bucket Policy**.

1. Copy one of the following policies, and paste it into the **Bucket Policy Editor** text box.

1. Replace the following placeholder text in the policy:
   + Replace {{amzn-s3-demo-bucket}} with the name of your bucket.
   + Replace {{optionalPrefix}} with the optional object prefix.
   + Replace {{myRegion}} with the source AWS Region.
   + Replace {{myAccountID}} with the account number of the requester of the export job.

     

1. Include all three of the following statements in the policy: 

   1. The first statement (for the `GetBucketAcl` action) allows Compute Optimizer to get the access control list (ACL) of your bucket.

   1. The second statement (for the `GetBucketPolicyStatus` action) allows Compute Optimizer to get the policy status of your bucket, indicating whether the bucket is public.

   1. The third statement (for the `PutObject` action) gives Compute Optimizer full control to put the export file in your bucket.

   Your export request fails if any of these statements are missing or if the bucket name and optional object prefix in the policy don't match what you specify in your export request. Your export also fails if the account number in the policy doesn't match the account number of the requester of the export job. 
**Note**  
If the existing bucket already has one or more policies attached, add the statements for Compute Optimizer access to that policy or policies. Evaluate the resulting set of permissions to ensure that they're appropriate for the users who access the bucket. 

**Policy option 1: Using an optional prefix** 

The object prefix is an optional addition to the S3 object key that organizes your export files in your S3 bucket. If you want to specify an object prefix when you create your recommendations export, use the following policy.

------
#### [ JSON ]

****  

```
{
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketAcl",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketPolicyStatus",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:PutObject",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{optionalPrefix}}/compute-optimizer/{{myAccountID}}/*",
                    "Condition": {"StringEquals": {
                            "s3:x-amz-acl": "bucket-owner-full-control",
                            "aws:SourceAccount": "{{myAccountID}}"
                        },
                        "ArnLike": {
                              "aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"
                         }
                    }
                 }
            ]
        }
```

------

**Note**  
The {{compute-optimizer/myAccountID/}} component isn’t part of the optional prefix. Compute Optimizer creates the {{optimizer/myAccountID/}} part of the bucket path for you that's added to the prefix that you specify.

**Policy option 2: No object prefix **

If you don't want to specify an object prefix, use the following policy.

------
#### [ JSON ]

****  

```
{
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketAcl",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketPolicyStatus",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:PutObject",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/compute-optimizer/{{myAccountID}}/*",
                    "Condition": {"StringEquals": {
                            "s3:x-amz-acl": "bucket-owner-full-control",
                            "aws:SourceAccount": "{{myAccountID}}"
                        },
                        "ArnLike": {
                             "aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"
                         }
                     }
                 }
            ]
        }
```

------

## Next steps
<a name="s3-export-next-steps"></a>

For instructions on how to export your AWS Compute Optimizer recommendations, see [Exporting your recommendations](exporting-your-recommendations.md).

Additionally, you can specify S3 buckets that are encrypted with either Amazon S3 customer managed keys or AWS Key Management Service (KMS) keys. For instructions on how to do this, see [Using encrypted S3 buckets for your recommendations export](using-encrypted-s3-buckets.md).

## Additional resources
<a name="cloudtrail-S3-bucket-policy-resources"></a>
+ Troubleshooting — [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports)
+ [Exported files](exported-files.md)
+ [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).