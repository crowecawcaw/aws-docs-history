

# Encryption context
<a name="encrypt_context"></a>

**Note**  
You cannot specify an encryption context in a cryptographic operation with an [asymmetric KMS key](symmetric-asymmetric.md) or an [HMAC KMS key](hmac.md). Asymmetric algorithms and MAC algorithms do not support an encryption context.

All AWS KMS [cryptographic operations](kms-cryptography.md#cryptographic-operations) with [symmetric encryption KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks) accept an *encryption context*, an optional set of non-secret key–value pairs that can contain additional contextual information about the data. You can insert encryption context in `Encrypt` operations in AWS KMS to enhance the authorization and auditability of your AWS KMS API decryption calls. AWS KMS uses the encryption context as additional authenticated data (AAD) to support authenticated encryption. The encryption context is cryptographically bound to the ciphertext so that the same encryption context is required to decrypt the data.

The encryption context is not secret and not encrypted. It appears in plaintext in [AWS CloudTrail Logs](logging-using-cloudtrail.md) so you can use it to identify and categorize your cryptographic operations. Your encryption context should not include sensitive information. We recommend that your encryption context describe the data being encrypted or decrypted. For example, when you encrypt a file, you might use part of the file path as encryption context.

```
"encryptionContext": {
    "department": "10103.0"
}
```

For example, when encrypting volumes and snapshots created with the [Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) (Amazon EBS) [CreateSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshot.html) operation, Amazon EBS uses the volume ID as encryption context value.

```
"encryptionContext": {
  "aws:ebs:id": "{{vol-abcde12345abc1234}}"
}
```

You can also use the encryption context to refine or limit access to AWS KMS keys in your account. You can use the encryption context [as a constraint in grants](grants.md) and as a *[condition in policy statements](policy-conditions.md)*. Encryption context keys and their values can be arbitrary strings with `aws`. These values contrasts [AWS generated tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-conventions) like [aws:cloudformation:stack-name](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html). For more information, see [kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context) 

To learn how to use encryption context to protect the integrity of encrypted data, see the post [How to Protect the Integrity of Your Encrypted Data by Using AWS Key Management Service and EncryptionContext](https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/) on the AWS Security Blog.

## Encryption context rules
<a name="encryption-context-rules"></a>

AWS KMS enforces the following rules for encryption context keys and values.
+ The key and value in an encryption context pair must be simple literal strings. If you use a different type, such as an integer or float, AWS KMS interprets it as a string.
+ The keys and values in an encryption context can include Unicode characters. If an encryption context includes characters that are not permitted in key policies or IAM policies, you won't be able to specify the encryption context in policy condition keys, such as [`kms:EncryptionContext:context-key`](conditions-kms.md#conditions-kms-encryption-context) and [`kms:EncryptionContextKeys`](conditions-kms.md#conditions-kms-encryption-context-keys). For details about key policy document rules, see [Key policy format](key-policy-overview.md#key-policy-format). For details about IAM policy document rules, see [IAM name requirements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-names) in the *IAM User Guide*.

## Encryption context in policies
<a name="encryption-context-authorization"></a>

The encryption context is used primarily to verify integrity and authenticity. But you can also use the encryption context to control access to symmetric encryption AWS KMS keys in key policies and IAM policies. 

The [kms:EncryptionContext:](conditions-kms.md#conditions-kms-encryption-context) and [kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context) condition keys allow (or deny) a permission only when the request includes particular encryption context keys or key–value pairs. 

For example, the following key policy statement allows the `RoleForExampleApp` role to use the KMS key in `Decrypt` operations. It uses the `kms:EncryptionContext:context-key` condition key to allow this permission only when the encryption context in the request includes an `AppName:ExampleApp` encryption context pair.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:AppName": "ExampleApp"
    }
  }
}
```

For more information about these encryption context condition keys, see [Condition keys for AWS KMS](policy-conditions.md).

## Encryption context in grants
<a name="encryption-context-grants"></a>

When you [create a grant](grants.md), you can include [grant constraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html) that establish conditions for the grant permissions. AWS KMS supports two encryption context grant constraints, `EncryptionContextEquals` and `EncryptionContextSubset`, both of which involve the [encryption context](#encrypt_context) in a request for a cryptographic operation. When you use these grant constraints, the permissions in the grant are effective only when the encryption context in the request for the cryptographic operation satisfies the requirements of the grant constraints. 

For example, you can add an `EncryptionContextEquals` grant constraint to a grant that allows the [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) operation. With this constraint, the grant allows the operation only when the encryption context in the request is a case-sensitive match for the encryption context in the grant constraint.

```
$ aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-principal arn:aws:iam::111122223333:user/exampleUser \
    --retiring-principal arn:aws:iam::111122223333:role/adminRole \
    --operations GenerateDataKey \
    --constraints EncryptionContextEquals={Purpose=Test}
```

A request like the following from the grantee principal would satisfy the `EncryptionContextEquals` constraint.

```
$ aws kms generate-data-key \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --key-spec AES_256 \
    --encryption-context Purpose=Test
```

For details about the grant constraints, see [Using grant constraints](create-grant-overview.md#grant-constraints). For detailed information about grants, see [Grants in AWS KMS](grants.md).

## Logging encryption context
<a name="encryption-context-auditing"></a>

AWS KMS uses AWS CloudTrail to log the encryption context so you can determine which KMS keys and data have been accessed. The log entry shows exactly which KMS keys was used to encrypt or decrypt specific data referenced by the encryption context in the log entry.

**Important**  
Because the encryption context is logged, it must not contain sensitive information.

## Storing encryption context
<a name="encryption-context-storing"></a>

To simplify use of any encryption context when you call the [`Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) or [`ReEncrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) operations, you can store the encryption context alongside the encrypted data. We recommend that you store only enough of the encryption context to help you create the full encryption context when you need it for encryption or decryption. 

For example, if the encryption context is the fully qualified path to a file, store only part of that path with the encrypted file contents. Then, when you need the full encryption context, reconstruct it from the stored fragment. If someone tampers with the file, such as renaming it or moving it to a different location, the encryption context value changes and the decryption request fails.