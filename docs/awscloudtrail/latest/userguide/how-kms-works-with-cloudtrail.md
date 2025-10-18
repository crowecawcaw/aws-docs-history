# How AWS CloudTrail uses AWS KMS

This section describes how AWS KMS works with a CloudTrail trail that is encrypted with an SSE-KMS key.

###### Important

AWS CloudTrail and Amazon S3 support only [symmetric
 AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html#symmetric-cmks "https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html#symmetric-cmks"). You cannot use an [asymmetric KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html "https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html") to encrypt your CloudTrail Logs. For help determining whether
 a KMS key is symmetric or asymmetric, see [Identify different key
 types](https://docs.aws.amazon.com/kms/latest/developerguide/identify-key-types.html "https://docs.aws.amazon.com/kms/latest/developerguide/identify-key-types.html") in the *AWS Key Management Service Developer Guide*.

You do not pay a key usage charge when CloudTrail reads or writes log files encrypted with an SSE-KMS key.
 However, you pay a key usage charge when you access CloudTrail log files encrypted with an SSE-KMS key. 
 For information about AWS KMS pricing, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/"). For information about
 CloudTrail pricing, see [AWS CloudTrail
 pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").


## Understanding when your KMS key is used for
 your trail


Encrypting CloudTrail log files with AWS KMS builds on the Amazon S3 feature called server-side
 encryption with an AWS KMS key (SSE-KMS). To learn more about SSE-KMS, see [Using
 server-side encryption with AWS KMS keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html") in the
 *Amazon Simple Storage Service User Guide*.


When you configure AWS CloudTrail to use SSE-KMS to encrypt your log files, CloudTrail and Amazon S3
 use your AWS KMS keys when you perform certain actions with those services. The
 following sections explain when and how those services can use your KMS key, and
 provide additional information that you can use to validate this explanation.


###### Actions that cause CloudTrail and Amazon S3 to use your KMS key

* [You configure CloudTrail to
 encrypt log files with your AWS KMS key](how-kms-works-with-cloudtrail.md#cloudtrail-details-update-configuration "how-kms-works-with-cloudtrail.md#cloudtrail-details-update-configuration")
* [CloudTrail puts a log file into your S3
 bucket](how-kms-works-with-cloudtrail.md#cloudtrail-details-put-log-file "how-kms-works-with-cloudtrail.md#cloudtrail-details-put-log-file")
* [You get an encrypted log file from
 your S3 bucket](how-kms-works-with-cloudtrail.md#cloudtrail-details-get-log-file "how-kms-works-with-cloudtrail.md#cloudtrail-details-get-log-file")

### You configure CloudTrail to
 encrypt log files with your AWS KMS key


When you [update
 your CloudTrail configuration to use your KMS key](create-kms-key-policy-for-cloudtrail-update-trail.md "create-kms-key-policy-for-cloudtrail-update-trail.md"), CloudTrail sends a [`GenerateDataKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html")
 request to AWS KMS to verify that the KMS key exists and that CloudTrail has permission to
 use it for encryption. CloudTrail does not use the resulting data key.


The `GenerateDataKey` request includes the following information for
 the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html "https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html"):



* The [Amazon Resource
 Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html "https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html") of the CloudTrail trail
* The ARN of the S3 bucket and path where the CloudTrail log files are
 delivered

The `GenerateDataKey` request results in an entry in your CloudTrail logs
 similar to the following example. When you see a log entry like this one, you can
 determine that CloudTrail called the AWS KMS `GenerateDataKey` operation for a specific trail. 
 AWS KMS created the data key under a specific KMS key.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AWSService",
        **"invokedBy": "cloudtrail.amazonaws.com"**
    },
    "eventTime": "2024-12-06T20:14:46Z",
    **"eventSource": "kms.amazonaws.com",**
    **"eventName": "GenerateDataKey",**
    "awsRegion": "us-east-1",
    "sourceIPAddress": "cloudtrail.amazonaws.com",
    "userAgent": "cloudtrail.amazonaws.com",
    "requestParameters": {
        "keySpec": "AES_256",
        **"keyId": "arn:aws:kms:us-east-1:123456789012:key/example1-6736-4661-bf00-exampleeb770",**
        "encryptionContext": {
            **"aws:cloudtrail:arn": "arn:aws:cloudtrail:us-east-1:123456789012:trail/management-events"**,
            "aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-logging-bucket-123456789012-9af1fb49/AWSLogs/123456789012/CloudTrail/us-east-1/2024/12/06/123456789012_CloudTrail_us-east-1_20241206T2010Z_TO50OLMG1hIQ1png.json.gz"
        }
    },
    "responseElements": null,
    "requestID": "a0555e85-7e8a-4765-bd8f-2222295558e1",
    "eventID": "e4f3557e-7dbd-4e37-a00a-d86c137d1111",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::KMS::Key",
            **"ARN": "arn:aws:kms:us-east-1:123456789012:key/example1-6736-4661-bf00-exampleeb770"**
         }],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "sharedEventID": "ce71d6be-0846-498e-851f-111a1af9078f",
    "eventCategory": "Management"
}        
```

### CloudTrail puts a log file into your S3
 bucket


Each time CloudTrail puts a log file into your S3 bucket, Amazon S3 sends a [`GenerateDataKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html")
 request to AWS KMS on behalf of CloudTrail. In response to this request, AWS KMS generates a
 unique data key and then sends Amazon S3 two copies of the data key, one in plaintext and
 one that is encrypted with the specified KMS key. Amazon S3 uses the plaintext data key
 to encrypt the CloudTrail log file and then removes the plaintext data key from memory as
 soon as possible after use. Amazon S3 stores the encrypted data key as metadata with the
 encrypted CloudTrail log file.


The `GenerateDataKey` request includes the following information for
 the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html "https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html"):



* The [Amazon Resource
 Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html "https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html") of the CloudTrail trail
* The ARN of the S3 object (the CloudTrail log file)

Each `GenerateDataKey` request results in an entry in your CloudTrail logs
 similar to the following example. When you see a log entry like this one, you can
 determine that CloudTrail called the AWS KMS `GenerateDataKey` operation 
 for a specific trail to protect a specific log file. AWS KMS created the data key under the specified KMS key, 
 shown twice in the same log entry.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AWSService",
        **"invokedBy": "cloudtrail.amazonaws.com"**
    },
    "eventTime": "2024-12-06T21:49:28Z",
    **"eventSource": "kms.amazonaws.com",**
    **"eventName": "GenerateDataKey",**
    "awsRegion": "us-east-1",
    "sourceIPAddress": "cloudtrail.amazonaws.com",
    "userAgent": "cloudtrail.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            **"aws:cloudtrail:arn": "arn:aws:cloudtrail:us-east-1::trail/insights-trail",**
            "aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-logging-bucket1-123456789012-7867ab0c/AWSLogs/123456789012/CloudTrail/us-east-1/2024/12/06/123456789012_CloudTrail_us-east-1_20241206T2150Z_hVXmrJzjZk2wAM2V.json.gz"
        },
        "keySpec": "AES_256",
        **"keyId": "arn:aws:kms:us-east-1:123456789012:key/example9-16ef-48ba-9163-example67a5a"**
    },
    "responseElements": null,
    "requestID": "11117d14-9232-414a-b3d1-01bab4dc9f99",
    "eventID": "999e9a50-512c-4e2a-84a3-111a5f511111",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::KMS::Key",
            **"ARN": "arn:aws:kms:us-east-1:123456789012:key/example9-16ef-48ba-9163-example67a5a"**
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "sharedEventID": "5e663acc-b7fd-4cdd-8328-0eff862952fa",
    "eventCategory": "Management"
}
```

### You get an encrypted log file from
 your S3 bucket


Each time you get an encrypted CloudTrail log file from your S3 bucket, Amazon S3 sends a
 [`Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html") request
 to AWS KMS on your behalf to decrypt the log file's encrypted data key. In response to
 this request, AWS KMS uses your KMS key to decrypt the data key and then sends the
 plaintext data key to Amazon S3. Amazon S3 uses the plaintext data key to decrypt the CloudTrail log
 file and then removes the plaintext data key from memory as soon as possible after
 use.


The `Decrypt` request includes the following information for the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html "https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html"):



* The [Amazon Resource
 Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html "https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html") of the CloudTrail trail
* The ARN of the S3 object (the CloudTrail log file)

Each `Decrypt` request results in an entry in your CloudTrail logs similar to
 the following example. When you see a log entry like this one, you can determine
 that an assumed role called the AWS KMS `Decrypt` operation for a specific
 trail and a specific log file. AWS KMS decrypted the data key under a specific
 KMS key.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2024-12-06T22:04:04Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2024-12-06T22:26:34Z",
    **"eventSource": "kms.amazonaws.com",**
    **"eventName": "Decrypt"**,
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "encryptionContext": {
            **"aws:cloudtrail:arn": "arn:aws:cloudtrail:us-east-1:123456789012:trail/insights-trail"**,
            "aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-logging-bucket1-123456789012-7867ab0c/AWSLogs/123456789012/CloudTrail/us-east-1/2024/12/06/123456789012_CloudTrail_us-east-1_20241206T0000Z_aAAsHbGBdye3jp2R.json.gz"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "1ab2d2d2-111a-2222-a59b-11a2b3832b53",
    "eventID": "af4d4074-2849-4b3d-1a11-a1aaa111a111",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::KMS::Key",
            **"ARN": "arn:aws:kms:us-east-1:123456789012:key/example9-16ef-48ba-9163-example67a5a"**
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "sessionCredentialFromConsole": "true"
}
```
