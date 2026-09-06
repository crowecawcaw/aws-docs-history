

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Granting Amazon ML Permissions to Output Predictions to Amazon S3
<a name="granting-amazon-ml-permissions-to-output-predictions-to-amazon-s3"></a>

 To output the results of the batch prediction operation to Amazon S3, you must grant Amazon ML the following permissions to the output location, which is provided as input to the Create Batch Prediction operation: 
+  **GetObject** permission on your S3 bucket and prefix. 
+  **PutObject** permission on your S3 bucket and prefix. 
+  **PutObjectAcl** on your S3 bucket and prefix. 
  +  Amazon ML needs this permission to ensure that it can grant the canned [ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) bucket-owner-full-control permission to your AWS account, after objects are created. 
+  **ListBucket** permission on the S3 bucket. Unlike other actions, **ListBucket** must be granted bucket-wide permissions (rather than on the prefix). You can, however, scope the permission to a specific prefix by using a **Condition** clause. 

 If you use the Amazon ML console to create the batch prediction request, these permissions can be added to the bucket for you. You will be prompted to confirm whether you want to add them as you complete the steps in the wizard. 

 The following example policy shows how to grant permission for Amazon ML to write data to the sample location s3://examplebucket/exampleprefix, while scoping the **ListBucket** permission to only the exampleprefix input path, and granting the permission for Amazon ML to set put object ACLs on the output prefix: 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "machinelearning.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::{{examplebucket}}/{{exampleprefix}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:machinelearning:us-east-1:{{123456789012}}:*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "machinelearning.amazonaws.com"
            },
            "Action": "s3:PutObjectAcl",
            "Resource": "arn:aws:s3:::{{examplebucket}}/{{exampleprefix}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:machinelearning:us-east-1:{{123456789012}}:*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "machinelearning.amazonaws.com"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{{examplebucket}}",
            "Condition": {
                "StringLike": {
                    "s3:prefix": "{{exampleprefix}}/*"
                },
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:machinelearning:us-east-1:{{123456789012}}:*"
                }
            }
        }
    ]
}
```

------

To apply this policy to your data, you must edit the policy statement associated with the S3 bucket where your data is stored. 

**To edit the permissions policy for an S3 bucket (using the old console)**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Select the bucket name where your data resides.

1. Choose **Properties**.

1. Choose **Edit bucket policy**

1. Enter the policy shown above, customizing it to fit your needs, and then choose **Save**.

1. Choose **Save**.



**To edit the permissions policy for an S3 bucket (using the new console)**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the bucket name and then choose **Permissions**.

1. Choose **Bucket Policy**.

1. Enter the policy shown above, customizing it to fit your needs.

1. Choose **Save**.