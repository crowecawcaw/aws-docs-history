

# Rotate keys manually
<a name="rotate-keys-manually"></a>

You might want to create a new KMS key and use it in place of a current KMS key instead of using automatic or on-demand key rotation. When the new KMS key has different cryptographic material than the current KMS key, using the new KMS key has the same effect as changing the key material in an existing KMS key. The process of replacing one KMS key with another is known as *manual key rotation*.

![Application with key rotated manually from one key ID to a different key ID.](http://docs.aws.amazon.com/kms/latest/developerguide/images/key-rotation-manual.png)


 Manual rotation is a good choice when you want to rotate KMS keys that are not eligible for automatic or on-demand key rotation, such as asymmetric KMS keys, HMAC KMS keys, and KMS keys in [custom key stores](key-store-overview.md#custom-key-store-overview).

**Note**  
When you begin using the new KMS key, be sure to keep the original KMS key enabled so that AWS KMS can decrypt data that the original KMS key encrypted.

When you rotate KMS keys manually, you also need to update references to the KMS key ID or key ARN in your applications. [Aliases](kms-alias.md), which associate a friendly name with a KMS key, can make this process easier. Use an alias to refer to a KMS key in your applications. Then, when you want to change the KMS key that the application uses, instead of editing your application code, change the target KMS key of the alias. For details, see [Learn how to use aliases in your applications](alias-using.md).

**Note**  
Aliases that point to the latest version of a manually rotated KMS key are a good solution for [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html), [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) and cryptographic operations like [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html), [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html), [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html), [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html), [GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html), [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html), [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) and [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html). Aliases are not permitted in operations that manage KMS keys, such as [DisableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html) or [ScheduleKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html).  
When calling the [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation on manually rotated symmetric encryption KMS keys, omit the `KeyId` parameter from the command. AWS KMS automatically uses the KMS key that encrypted the ciphertext.  
The `KeyId` parameter is required when calling `Decrypt` or [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) with an asymmetric KMS key, or calling [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html) with an HMAC KMS key. These requests fail when the value of the `KeyId` parameter is an alias that no longer points to the KMS key that performed the cryptographic operation, such as when a key is manually rotated. To avoid this error, you must track and specify the correct KMS key for each operation.

To change the target KMS key of an alias, use [UpdateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateAlias.html) operation in the AWS KMS API. For example, this command updates the `alias/TestKey` alias to point to a new KMS key. Because the operation does not return any output, the example uses the [ListAliases](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html) operation to show that the alias is now associated with a different KMS key and the `LastUpdatedDate` field is updated. The ListAliases commands use the [`query` parameter](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html#cli-usage-filter-client-side-specific-values) in the AWS CLI to get only the `alias/TestKey` alias.

```
$ aws kms list-aliases --query 'Aliases[?AliasName==`alias/TestKey`]'
{
    "Aliases": [
        {
            "AliasArn": "arn:aws:kms:us-west-2:111122223333:alias/TestKey",
            "AliasName": "alias/TestKey",
            "TargetKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
            "CreationDate": 1521097200.123,
            "LastUpdatedDate": 1521097200.123
        },
    ]
}


$ aws kms update-alias --alias-name alias/TestKey --target-key-id 0987dcba-09fe-87dc-65ba-ab0987654321
            
$ aws kms list-aliases --query 'Aliases[?AliasName==`alias/TestKey`]'
{
    "Aliases": [
        {
            "AliasArn": "arn:aws:kms:us-west-2:111122223333:alias/TestKey",
            "AliasName": "alias/TestKey",
            "TargetKeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
            "CreationDate": 1521097200.123,
            "LastUpdatedDate": 1604958290.722
        },
    ]
}
```