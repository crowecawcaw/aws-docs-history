

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Granting Amazon ML Permissions to Read Your Data from Amazon S3
<a name="granting-amazon-ml-permissions-to-read-your-data-from-amazon-s3"></a>

 To create a datasource object from your input data in Amazon S3, you must grant Amazon ML the following permissions to the S3 location where your input data is stored: 
+  **GetObject** permission on the S3 bucket and prefix. 
+  **ListBucket** permission on the S3 bucket. Unlike other actions, **ListBucket** must be granted bucket-wide permissions (rather than on the prefix). However, you can scope the permission to a specific prefix by using a **Condition** clause. 

 If you use the Amazon ML console to create the datasource, these permissions can be added to the bucket for you. You will be prompted to confirm whether you want to add them as you complete the steps in the wizard.The following example policy shows how to grant permission for Amazon ML to read data from the sample location s3://{{examplebucket}}/{{exampleprefix}}, while scoping the **ListBucket** permission to only the {{exampleprefix}} input path. 

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
            "Action": "s3:GetObject",
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