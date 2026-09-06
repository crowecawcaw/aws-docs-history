

# Encrypt lookup tables in CloudWatch Logs using AWS Key Management Service
<a name="encrypt-lookup-tables-kms"></a>

Lookup table data is always encrypted in CloudWatch Logs. By default, CloudWatch Logs uses server-side encryption with 256-bit Advanced Encryption Standard Galois/Counter Mode (AES-GCM) to encrypt lookup table data at rest. As an alternative, you can use AWS Key Management Service for this encryption. If you do, the encryption is done using an AWS KMS key. Encryption using AWS KMS is enabled at the lookup table level, by associating a KMS key with a lookup table, either when you create the lookup table or when you update it.

**Important**  
CloudWatch Logs supports only symmetric KMS keys. Do not use an asymmetric key to encrypt the data in your lookup tables. For more information, see [Using Symmetric and Asymmetric Keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html).

After you associate a KMS key with a lookup table, all data stored in the lookup table is encrypted using this key. CloudWatch Logs decrypts this data whenever it is requested. CloudWatch Logs must have permissions for the KMS key whenever encrypted data is requested.

If you later disassociate a KMS key from a lookup table, CloudWatch Logs encrypts the data using the CloudWatch Logs default encryption method. However, if the key is disabled or deleted before you disassociate it, then CloudWatch Logs is unable to read the data that was encrypted with that key.

For general information about how CloudWatch Logs uses AWS KMS to encrypt log data, see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](encrypt-log-data-kms.md).

## How CloudWatch Logs uses AWS KMS for lookup tables
<a name="encrypt-lookup-tables-how-it-works"></a>

CloudWatch Logs uses AWS KMS envelope encryption to protect lookup table data. When you associate a KMS key with a lookup table, CloudWatch Logs sends a `GenerateDataKey` request to AWS KMS. AWS KMS generates a unique data encryption key (DEK) and returns both a plaintext copy and an encrypted copy of the DEK. CloudWatch Logs uses the plaintext DEK to encrypt the lookup table data, and then stores the encrypted DEK alongside the encrypted data. The plaintext DEK is not stored and is discarded from memory after use.

When CloudWatch Logs needs to read the lookup table data, it sends a `Decrypt` request to AWS KMS with the encrypted DEK. AWS KMS decrypts the DEK and returns the plaintext DEK to CloudWatch Logs, which then uses it to decrypt the lookup table data.

CloudWatch Logs uses the following encryption context when making requests to AWS KMS:

```
{
    "aws:logs:arn": "arn:aws:logs:{{region}}:{{account-id}}:lookup-table:{{lookup-table-name}}"
}
```

You can use this encryption context in IAM policies and AWS KMS key policies to control access to the KMS key. For more information, see [AWS KMS keys and encryption context](encrypt-log-data-kms.md#encrypt-log-data-kms-policy).

## Required permissions
<a name="encrypt-lookup-tables-permissions"></a>

To use AWS KMS encryption with lookup tables, the IAM principal must have the following AWS KMS permissions on the KMS key:
+ `kms:Decrypt`
+ `kms:GenerateDataKey`

The `kms:Decrypt` permission is required when calling `GetLookupTable` on a lookup table that is encrypted with a KMS key, so that CloudWatch Logs can decrypt the data on your behalf. The `kms:Decrypt` permission is also required on the key (the KMS key used to encrypt the lookup table) when calling `StartQuery` with a query that uses the `lookup` command on an encrypted lookup table. The `kms:GenerateDataKey` permission is required when calling `CreateLookupTable` or `UpdateLookupTable` with a KMS key, so that CloudWatch Logs can generate a data encryption key to encrypt the lookup table data.

In addition, the CloudWatch Logs service must have permission to use the KMS key. You grant these permissions by adding a policy statement to the KMS key policy, as described in the following section.

## Step 1: Create an AWS KMS key
<a name="encrypt-lookup-tables-create-key"></a>

To create a symmetric KMS key, use the following [create-key](https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html) command:

```
aws kms create-key
```

The output contains the key ID and Amazon Resource Name (ARN) of the key. The following is example output:

```
{
    "KeyMetadata": {
        "Origin": "AWS_KMS",
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Description": "",
        "KeyManager": "CUSTOMER",
        "Enabled": true,
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "CreationDate": 1478910250.94,
        "Arn": "arn:aws:kms:us-west-2:123456789012:key/6f815f63-e628-448c-8251-e40cb0d29f59",
        "AWSAccountId": "123456789012",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ]
    }
}
```

Record the key ARN. You need it in the following steps.

## Step 2: Set permissions on the KMS key
<a name="encrypt-lookup-tables-key-policy"></a>

By default, all AWS KMS keys are private. Only the resource owner can use it to encrypt and decrypt data. You must grant the CloudWatch Logs service principal permission to use the key, and also grant the calling role permission to use the key.

First, save the default policy for your KMS key as `policy.json` using the following [get-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/get-key-policy.html) command:

```
aws kms get-key-policy --key-id {{key-id}} --policy-name default --output text > ./policy.json
```

Open the `policy.json` file in a text editor and add the following statement to grant the CloudWatch Logs service principal permission to use the key. This example uses a `Condition` section that matches the encryption context to restrict the key to a specific lookup table.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "logs.{{region}}.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:{{region}}:{{account-id}}:lookup-table:{{lookup-table-name}}",
            "aws:SourceAccount": "{{account-id}}",
            "aws:SourceArn": "arn:aws:logs:{{region}}:{{account-id}}:lookup-table:{{lookup-table-name}}"
        }
    }
}
```

Next, add permissions to the role that will be calling the CloudWatch Logs `CreateLookupTable` or `UpdateLookupTable` APIs. CloudWatch Logs uses `kms:ViaService` to make calls to AWS KMS on the customer's behalf. For more information, see [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service).

```
{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{account-id}}:role/{{role-name}}"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "logs.{{region}}.amazonaws.com"
            ]
        }
    }
}
```

Finally, add the updated policy using the following [put-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html) command:

```
aws kms put-key-policy --key-id {{key-id}} --policy-name default --policy file://policy.json
```

## Step 3: Associate a KMS key with a lookup table
<a name="encrypt-lookup-tables-associate"></a>

You can associate a KMS key with a lookup table when you create it using the `CreateLookupTable` API, or update an existing lookup table using the `UpdateLookupTable` API. Both APIs are part of the AWSLogsConfigService.

**To associate the KMS key with a lookup table when you create it**  
Use the `CreateLookupTable` API and specify the `kmsKeyArn` parameter with the ARN of your KMS key:

```
aws logs create-lookup-table \
    --lookup-table-name {{my-lookup-table}} \
    --kms-key-arn "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
```

**To associate the KMS key with an existing lookup table**  
Use the `UpdateLookupTable` API and specify the `kmsKeyArn` parameter with the ARN of your KMS key:

```
aws logs update-lookup-table \
    --lookup-table-name {{my-lookup-table}} \
    --kms-key-arn "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
```

## Considerations
<a name="encrypt-lookup-tables-considerations"></a>
+ After you associate or disassociate a KMS key from a lookup table, it can take up to five minutes for the operation to take effect.
+ If you revoke CloudWatch Logs access to an associated key or delete an associated KMS key, your encrypted lookup table data in CloudWatch Logs can no longer be retrieved.
+ To perform the steps in this topic, you must have the following permissions: `kms:CreateKey`, `kms:GetKeyPolicy`, `kms:PutKeyPolicy`, and the appropriate CloudWatch Logs permissions to call `CreateLookupTable` or `UpdateLookupTable`.