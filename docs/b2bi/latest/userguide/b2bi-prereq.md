

# Prerequisites for using AWS B2B Data Interchange
<a name="b2bi-prereq"></a>

This topic describes how to sign up for an AWS account, create an admin user, and configure an Amazon S3 bucket to use with B2B Data Interchange. 

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Configure an Amazon S3 bucket
<a name="configure-s3-bucket"></a>

You need to have an Amazon S3 bucket set up and ready to use. B2B Data Interchange requires buckets for storing input, output, and instruction documents. For details, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html).
+ The Amazon S3 bucket must be in the same AWS account as the B2B Data Interchange user.
+ The Amazon S3 bucket must be in the same region as the B2B Data Interchange user. 

## Setting up S3 bucket policies and permissions
<a name="buckets-and-permissions"></a>

Before you can transform and generate Electronic Data Interchange (EDI) documents, you must configure S3 bucket policies for your trading capabilities. This topic provides step-by-step instructions and example policies to help you get started.

### Configuring S3 bucket policies
<a name="bucket-policy-configuration"></a>

Follow these steps to configure policies for both your input and output buckets. If your buckets use SSE-KMS encryption, you must also update your AWS KMS key policy. For policy examples, see [Example policies](#bucket-policy-examples).

**To configure a bucket policy**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Navigate to your bucket and choose the **Permissions** tab.

1. In the **Bucket policy** section, choose **Edit**.

1. Do one of the following:
   + Copy an example policy from [Example policies](#bucket-policy-examples) and paste it into the policy editor.
   + Choose **Copy policy** when creating a trading capability, and paste the copied policy.

1. Choose **Save changes**.

**Note**  
For information about temporary files and related permissions, see [Managing temporary files and permissions](#temp-files-permissions).

### Enabling EventBridge notifications
<a name="bucket-policy-eventbridge"></a>

You must enable Amazon EventBridge notifications for your input S3 bucket.

**To enable EventBridge notifications**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Navigate to your bucket and choose the **Properties** tab.

1. Scroll to the **EventBridge** section.

1. If notifications are already enabled, you're done. Otherwise, continue to the next step.

1. Choose **Edit**.

1. Select **On** and choose **Save changes**.

**Important**  
After enabling EventBridge, wait at least 5 minutes before placing files in your S3 bucket. This allows time for the changes to take effect.

### Managing temporary files and permissions
<a name="temp-files-permissions"></a>

Your output bucket policies require the following permissions:
+ `s3:GetObject` - Allows the service to read temporary files
+ `s3:DeleteObject` - Enables cleanup of temporary files

**Important**  
Without the `s3:DeleteObject` permission:  
Temporary files remain in your S3 bucket and incur storage charges.
These files can be up to ten times larger than the input X12 file.

The service uses the following locations for temporary files:
+ `customerOutputDirectory/parsed` - For service use
+ `customerOutputDirectory/{{tradingPartnerId}}/parsed` - For S3 use (when using partnerships)

### Example policies
<a name="bucket-policy-examples"></a>

Use these example policies to configure permissions for your S3 buckets and AWS KMS keys.

**Important**  
Replace all {{user input placeholder}} values with your own information.

------
#### [ Input bucket policy ]

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "B2BIEdiCapabilityInputPolicy",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "b2bi.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:GetObjectAttributes"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/{{input-folder}}*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                }
            }
        }
    ]
}
```

------

------
#### [ Output bucket policy ]

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "B2BIEdiCapabilityOutputPolicy",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "b2bi.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:AbortMultipartUpload"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/{{output-folder}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                }
            }
        }
    ]
}
```

------

------

If you use SSE-KMS or DSSE-KMS encryption, you must also configure AWS KMS key policies:

**Important**  
Don't use AWS managed key policies - they can't be edited. Create a customer managed key instead.

------
#### [ Input KMS key policy ]

Use this policy for encrypted input buckets to allow decryption of files:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "B2BIEdiCapabilityInputKeyPolicy",
    "Statement": [
        {
            "Sid": "Allow administration of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow B2Bi access",
            "Effect": "Allow",
            "Principal": {
                "Service": "b2bi.amazonaws.com"
            },
            "Action": "kms:Decrypt",
            "Resource": "*"
        }
    ]
}
```

------

------
#### [ Output KMS key policy ]

Use this policy for encrypted output buckets to allow encryption of files:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "B2BIEdiCapabilityOutputKeyPolicy",
    "Statement": [
        {
            "Sid": "Allow administration of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow B2Bi access",
            "Effect": "Allow",
            "Principal": {
                "Service": "b2bi.amazonaws.com"
            },
            "Action": "kms:GenerateDataKey",
            "Resource": "*"
        }
    ]
}
```

------

------

If you use the same bucket for both input and output, use either policy and add the other permission, as shown in this example:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "B2BIEdiCapabilityOutputKeyPolicy",
    "Statement": [
        {
            "Sid": "Allow administration of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow B2Bi access",
            "Effect": "Allow",
            "Principal": {
                "Service": "b2bi.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*"
        }
    ]
}
```

------