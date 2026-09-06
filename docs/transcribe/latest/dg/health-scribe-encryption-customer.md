

# Creating a customer managed key
<a name="health-scribe-encryption-customer"></a>

 You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs. To create a symmetric customer managed key, follow the steps for [Creating symmetric customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the AWS Key Management Service Developer Guide. 

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Managing access to customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access) in the AWS Key Management Service Developer Guide. 

## AWS KMS key policies for AWS HealthScribe
<a name="health-scribe-key-policies"></a>

 If you are using a key in the same account as the IAM role you specify as the `DataAccessRole` in your [StartMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartMedicalScribeJob.html) or `ResourceAccessRole` in your [StartMedicalScribeStream](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartMedicalScribeStream.html) request, you don't need to update the Key Policy. To use your customer managed key in a different account as your DataAccessRole (for transcription jobs) or ResourceAccessRole (for streaming), you must trust the respective role in the Key Policy for the following actions:
+ [`kms:Encrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) — Allows encryption using the customer managed key
+ [`kms:Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) — Allows decryption using the customer managed key
+ [`kms:DescribeKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) — Provides the customer managed key details to allow AWS HealthScribe to validate the key

The following is an example key policy you can use to grant your ResourceAccessRole cross account permissions to use your customer managed key for AWS HealthScribe streaming. To use this policy for transcription jobs, update the `Principal` to use the DataAccessRole ARN, and remove or modify the encryption context.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {  
         "Sid": "AllowAccessForKeyAdministrators", 
         "Effect": "Allow", 
         "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:root" 
         }, 
         "Action": [
           "kms:*" 
         ], 
         "Resource": "*"
      },
      {
         "Sid": "AllowAccessToResourceAccessRoleForMedicalScribe",
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:role/{{ResourceAccessRole}}"
         },
         "Action": [
            "kms:Encrypt",
            "kms:Decrypt",
            "kms:GenerateDataKey*"
         ],
         "Resource": "*",
         "Condition": {
            "StringEquals": {
                "kms:EncryptionContext:aws:us-east-1:transcribe:medical-scribe:session-id": "{{1234abcd-12ab-34cd-56ef-123456SAMPLE}}"
            }
         }
      },
      {
         "Sid": "AllowAccessToResourceAccessRoleForDescribeKey",
         "Effect": "Allow",
         "Principal": {
             "AWS": "arn:aws:iam::{{111122223333}}:role/{{ResourceAccessRole}}"
         },
         "Action": "kms:DescribeKey",
         "Resource": "*"
     }
   ]
}
```

------

## IAM policy permissions for access roles
<a name="health-scribe-key-data-access-role"></a>

 The IAM policy attached to your DataAccessRole or ResourceAccessRole must grant permissions to perform the necessary AWS KMS actions, regardless of whether the customer-managed key and role are in the same or different accounts. Also, the role's trust policy must grant AWS HealthScribe permission to assume the role.

The following IAM policy example shows how to grant a ResourceAccessRole permissions for AWS HealthScribe streaming. To use this policy for transcription jobs, replace `transcribe.streaming.amazonaws.com` with `transcribe.amazonaws.com` and remove or modify the encryption context.

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
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey*"
            ],
            "Resource": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{KMS-Example-KeyId}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "transcribe.streaming.amazonaws.com",
                    "kms:EncryptionContext:aws:us-east-1:transcribe:medical-scribe:session-id": "{{1234abcd-12ab-34cd-56ef-123456SAMPLE}}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{KMS-Example-KeyId}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "transcribe.streaming.amazonaws.com"
                }
            }
        }
    ]
}
```

------

The following is trust policy example for the ResourceAccessRole. For DataAccessRole, replace `transcribe.streaming.amazonaws.com` with `transcribe.amazonaws.com`.

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
                "Service": "transcribe.streaming.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:transcribe:{{us-west-2}}:{{111122223333}}:*"
                }
            }
        }
    ]
}
```

------

 For more information about [specifying permissions in a policy](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#overview-policy-elements) or [troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html#example-no-iam), see the AWS Key Management Service Developer Guide. 