

# DETERMINISTIC\_ENCRYPT
<a name="recipe-actions.DETERMINISTIC_ENCRYPT"></a>

Encrypts the column using AES-GCM-SIV with a 256 bit key. Data encrypted with DETERMINISTIC\_ENCRYPT can only be decrypted inside of DataBrew with the DETERMINISTIC\_DECRYPT transform. This transform does not use AWS KMS or the AWS Encryption SDK, and instead uses the [AWS LC github library](https://github.com/awslabs/aws-lc).

Can encrypt up to 400KB per cell. Does not preserve data type on decrypt.

**Note**  
Note: Using a secret for more than a year is discouraged.

**Parameters**
+ `sourceColumns` – An array of existing columns.
+ `secretId` – The ARN of the Secrets Manager secret key to use to encrypt the source columns, or databrew\!default.
+ `secretVersion` – Optional. Defaults to the latest secret version.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.
+ `createSecretIfMissing` – Optional boolean. If true will attempt to create the secret on behalf of the caller.

**Example**

```
{
   "sourceColumns": ["phonenumber"],   
   "secretId": "arn:aws:secretsmanager:us-east-1:012345678901:secret:mysecret",
   "secretVersion": "adfe-1232-7563-3123",
   "entityTypeFilter": ["USA_ALL"]
}
```

When working in the interactive experience, in addition to the project’s role, the console user must have permission to `secretsmanager:GetSecretValue` on the provided Secrets Manager secret.

**Sample policy**

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
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:us-east-1:012345678901:secret:mysecret"
            ]
        }
    ]
}
```

------