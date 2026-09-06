

# ENCRYPT
<a name="recipe-actions.ENCRYPT"></a>

Encrypts values in the source columns with the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html). The DECRYPT transform can be used to decrypt inside of DataBrew. You can also decrypt the data outside of DataBrew using the AWS Encryption SDK.

The ENCRYPT transform can encrypt up to 128 MiB per cell. It will attempt to preserve the format on decryption. To preserve the data type, the data type metadata must serialize to less than 1KB. Otherwise, you must set the `preserveDataType` parameter to false. The data type metadata will be stored in plaintext in the encryption context. For more information on the encryption context, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the *AWS Key Management Service Developer Guide*.

**Parameters**
+ `sourceColumns` – An array of existing columns.
+ `kmsKeyArn` – The key ARN of the AWS Key Management Service key to use to encrypt the source columns. For more information on the key ARN, see [Key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the *AWS Key Management Service Developer Guide*.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.
+ `preserveDataType` – Optional boolean. Defaults to true. If false, the data type will not be stored.

In the following example, `entityTypeFilter` and `preserveDataType` are optional.

**Example**

```
{
    "sourceColumns": ["phonenumber"],
    "kmsKeyArn": "arn:aws:kms:us-east-1:012345678901:key/kms-key-id",
    "entityTypeFilter": ["USA_ALL"],
    "preserveDataType": "true"
}
```

When working in the interactive experience, in addition to the project’s role, the console user must have permission to `kms:GenerateDataKey` on the provided AWS KMS key.

**Sample policy:**

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
        "Resource": [
            "arn:aws:kms:us-east-1:012345678901:key/kms-key-id"
        ]
    }
  ]
}
```

------