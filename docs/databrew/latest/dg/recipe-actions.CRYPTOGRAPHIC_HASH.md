

# CRYPTOGRAPHIC\_HASH
<a name="recipe-actions.CRYPTOGRAPHIC_HASH"></a>

Applies an algorithm to hash values in the column.

**Parameters**
+ `sourceColumns` – An array of existing columns.
+ `secretId` – The ARN of the Secrets Manager secret key. The key used in the hash-based message authentication code (HMAC) prefix algorithm to hash the source columns, or `databrew!default` is the base64 decoded output for the value of the Secrets Manager secret key.
+ `secretVersion` – Optional. Defaults to the latest secret version.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.
+ `createSecretIfMissing` – Optional boolean. If true will attempt to create the secret on behalf of the caller.
+ `algorithm` – The algorithm used to hash your data. Valid enum values: MD5, SHA1, SHA256, SHA512, HMAC\_MD5, HMAC\_SHA1, HMAC\_SHA256, HMAC\_SHA512

  Each option refers to a different hashing algorithm. Those options with the "HMAC" prefix refer to a keyed hashing algorithm, and require the `secretId` parameter. For options without the "HMAC" prefix, the `secretId` parameter is not required.

  If you do not provide a hash algorithm, the service defaults to "HMAC\_SHA256".

```
{
   "sourceColumns": ["phonenumber"],   
   "secretId": "arn:aws:secretsmanager:us-east-1:012345678901:secret:mysecret",
   "entityTypeFilter": ["USA_ALL"]
}
```

When working in the interactive experience, in addition to the project’s role, the console user must have permission to `secretsmanager:GetSecretValue` on the provided Secrets Manager secret.

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

You may also opt to use the DataBrew-created default secret by passing `databrew!default` as secretId and parameter `createSecretIfMissing` as true. This is not recommended for production. Anyone with the **AwsGlueDataBrewFullAccessPolicy** role can use the default secret.