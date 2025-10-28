# Download public key

You can download the public key from an asymmetric KMS key pair in the AWS KMS console or
by using the [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") operation.
To download the public key, you must have `kms:GetPublicKey` permission on the
asymmetric KMS key.

The public key that AWS KMS returns is a DER-encoded X.509 public key, also known as
`SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280 "https://datatracker.ietf.org/doc/html/rfc5280"). When you use the HTTP
API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

To download the public key from an asymmetric KMS key pair, you need
`kms:GetPublicKey` permissions. For more information about AWS KMS permissions, see
the [Permissions reference](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

You can use the AWS Management Console to view, copy, and download the public key from an
asymmetric KMS key in your AWS account. To download the public key from an asymmetric
KMS key in different AWS account, use the AWS KMS API.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose the alias or key ID of an asymmetric KMS key.
5. Choose the **Cryptographic configuration** tab. Record the values
   of the **Key spec**, **Key usage**, and
   **Encryption algorithms** or **Signing
   Algorithms** fields. You'll need to use these values to use the public key
   outside of AWS KMS. Be sure to share this information when you share the public
   key.
6. Choose the **Public key** tab.
7. To copy the public key to your clipboard, choose **Copy**. To
   download the public key to a file, choose **Download**.
   The [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") operation
   returns the public key in an asymmetric KMS key. It also returns critical information
   that you need to use the public key correctly outside of AWS KMS, including the key usage
   and encryption algorithms. Be sure to save these values and share them whenever you share
   the public key.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

To specify a KMS key, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id"), [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"), [alias
name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name"), or [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN"). When using an alias
name, prefix it with **alias/**. To specify a KMS key in a
different AWS account, you must use its key ARN or alias ARN.

Before running this command, replace the example alias name with a valid identifier
for the KMS key. To run this command, you must have `kms:GetPublicKey`
permissions on the KMS key.

```
`$` `aws kms get-public-key --key-id `alias/example_RSA_3072``

`{
 "KeySpec": "RSA_3072",
 "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyUsage": "ENCRYPT_DECRYPT",
 "EncryptionAlgorithms": [
 "RSAES_OAEP_SHA_1",
 "RSAES_OAEP_SHA_256"
 ],
 "PublicKey": "MIIBojANBgkqhkiG..."
}`
```
