

# DETERMINISTIC\_DECRYPT
<a name="recipe-actions.DETERMINISTIC_DECRYPT"></a>

Decrypts data encrypted with DETERMINISTIC\_ENCRYPT.

This transformation is a no-op if the provided secret id and version does not match what was used to encrypt the column.

**Parameters**
+ `sourceColumns` – An array of existing columns.
+ `secretId` – The ARN of the Secrets Manager secret key to use to decrypt the source columns.
+ `secretVersion` – Optional. Defaults to the latest secret version.

**Example**

```
{
   "sourceColumns": ["phonenumber"],   
   "secretId": "arn:aws:secretsmanager:us-east-1:012345678901:secret:mysecret",
   "secretVersion": "adfe-1232-7563-3123"
}
```

When working in the interactive experience, in addition to the project’s role, the console user must have permission to secretsmanager:GetSecretValue on the provided Secrets Manager secret.

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