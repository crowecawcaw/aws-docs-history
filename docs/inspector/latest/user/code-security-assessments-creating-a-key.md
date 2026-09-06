

# Creating a customer managed key to access AWS KMS
<a name="code-security-assessments-creating-a-key"></a>

 By default, your data is encrypted with an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). This means the key is created, owned, and managed by the service. If you want to own and manage the key used to encrypt your data, you can create a [customer managed KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). Amazon Inspector doesn't interact with your data. Amazon Inspector only ingests metadata from repositories in your source code provider. For information about how to create a customer managed KMS key, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service User Guide*. 

**Sample policy**  
 When you [create your customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html), use the following sample policy. 

**Note**  
 The [FAS permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) in the following policy are specific to Amazon Inspector, as they allow Amazon Inspector to perform only those API calls. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Id": "key-policy",
  "Statement": [
    {
      "Sid": "Allow Q to use Encrypt Decrypt GenerateDataKey and GenerateDataKeyWithoutPlaintext",
      "Effect": "Allow",
      "Principal": {
        "Service": "q.amazonaws.com"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
        "aws:SourceAccount": "111122223333"
        },
        "StringLike": {
        "kms:EncryptionContext:aws:qdeveloper:codesecurity-scope": "111122223333"
        },
        "ArnLike": {
        "aws:SourceArn": "arn:aws:inspector2:us-east-1:111122223333:codesecurity-integration/*"
        }
      }
    },
    {
      "Sid": "Allow Q to use DescribeKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "q.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    },
    {
      "Sid": "Allow Inspector to use Encrypt Decrypt GenerateDataKey and GenerateDataKeyWithoutPlaintext using FAS",
      "Effect": "Allow",
      "Principal": {
      "AWS": "arn:aws:iam::{{111122223333}}:role/inspectorCodeSecurity"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "inspector2.us-east-1.amazonaws.com"
        },
        "StringLike": {
        "kms:EncryptionContext:aws:qdeveloper:codesecurity-scope": "111122223333"
        }
      }
    },
    {
      "Sid": "Allow Inspector to use DescribeKey using FAS",
      "Effect": "Allow",
      "Principal": {
      "AWS": "arn:aws:iam::{{111122223333}}:role/inspectorCodeSecurity"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "inspector2.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}
```

------

 After you create your KMS key, you can use the following Amazon Inspector APIs. 
+  UpdateEncryptionKey – Use with `CODE_REPOSITORY` for `resourceType` and `CODE` as the scan type to configure the use of your customer managed KMS key. 
+  GetEncryptionKey – Use with `CODE_REPOSITORY` for `resourceType` and `CODE` as the scan type to configure the retrieval of your KMS key configuration. 
+  ResetEncryptionKey – Use with `CODE_REPOSITORY` for `resourceType` and `CODE` to reset your KMS key configuration and to use an AWS owned KMS key. 