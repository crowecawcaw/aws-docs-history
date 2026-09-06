

# Rotating key material
<a name="rotate-customer-master-key"></a>

Authorized users can enable automatic annual rotation of their customer managed KMS keys. AWS managed keys are always rotated every year. 

When a KMS key is rotated, a new HBK is created and marked as the current version of the key material for all new encrypt requests. All previous versions of the HBK remain available for use in perpetuity to decrypt any ciphertexts that were encrypted using this HBK version. Because AWS KMS does not store any ciphertext encrypted under a KMS key, ciphertexts encrypted under an older, rotated HBK require that HBK to decrypt. You can use the [`ReEncrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) API to reencrypt any ciphertext under the new HBK for the KMS key or under a different KMS key without exposing the plaintext.

For information about enabling and disabling key rotation, see [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *AWS Key Management Service Developer Guide*.