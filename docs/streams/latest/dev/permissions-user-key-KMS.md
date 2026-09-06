

# Permissions to use user-generated KMS keys
<a name="permissions-user-key-KMS"></a>

Before you can use server-side encryption with a user-generated KMS key, you must configure AWS KMS key policies to allow encryption of streams and encryption and decryption of stream records. For examples and more information about AWS KMS permissions, see [AWS KMS API Permissions: Actions and Resources Reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html). 

**Note**  
The use of the default service key for encryption does not require application of custom IAM permissions.

Before you use user-generated KMS master keys, ensure that your Kinesis stream producers and consumers (IAM principals) are users in the KMS master key policy. Otherwise, writes and reads from a stream will fail, which could ultimately result in data loss, delayed processing, or hung applications. You can manage permissions for KMS keys using IAM policies. For more information, see [Using IAM Policies with AWS KMS](http://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

## Kinesis Data Streams encryption context
<a name="sse-kms-encryption-context"></a>

When Amazon Kinesis Data Streams calls AWS KMS on your behalf, it passes an encryption context to AWS KMS that can be used as a condition for authorization in key policies and grants. Kinesis Data Streams uses the stream ARN as the encryption context in all AWS KMS calls.

```
"encryptionContext": {
    "aws:kinesis:arn": "arn:aws:kinesis:{{region}}:{{account-id}}:stream/{{stream-name}}"
}
```

You can use the encryption context to identify the use of your KMS key in audit records and logs. It also appears in plaintext in logs, such as AWS CloudTrail.

To limit the use of your KMS key to requests from Kinesis Data Streams for a specific stream, use the `kms:EncryptionContext:aws:kinesis:arn` condition key in the KMS key policy or IAM policy.

## Example producer permissions
<a name="example-producer-permissions"></a>

Your Kinesis stream producers must have the `kms:GenerateDataKey` permission.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "kms:GenerateDataKey"
        ],
        "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }, 
    {
        "Effect": "Allow",
        "Action": [
            "kinesis:PutRecord",
            "kinesis:PutRecords"
        ],
        "Resource": "arn:aws:kinesis:*:123456789012:MyStream"
    }
  ]
}
```

------

## Example consumer permissions
<a name="example-consumer-permissions"></a>

Your Kinesis stream consumers must have the `kms:Decrypt` permission.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "kms:Decrypt"
        ],
        "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }, 
    {
        "Effect": "Allow",
        "Action": [
            "kinesis:GetRecords",
            "kinesis:DescribeStream"
        ],
        "Resource": "arn:aws:kinesis:*:123456789012:MyStream"
    }
  ]
}
```

------

Amazon Managed Service for Apache Flink and AWS Lambda use roles to consume Kinesis streams. Make sure to add the `kms:Decrypt` permission to the roles that these consumers use.

## Stream administrator permissions
<a name="stream-administrator-permissions"></a>

Kinesis stream administrators must have authorization to call `kms:List*` and ```kms:DescribeKey*`.