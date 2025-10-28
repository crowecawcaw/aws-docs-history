# AWS KMS condition keys for attested platforms

AWS KMS provides condition keys to support cryptographic attestation for [AWS Nitro Enclaves](../../../enclaves/latest/user.md "../../../enclaves/latest/user.md")
and NitroTPM. AWS Nitro Enclaves is an Amazon EC2 capability that lets you create isolated compute environments called
[enclaves](../../../enclaves/latest/user/nitro-enclave-concepts.md#term-enclave "../../../enclaves/latest/user/nitro-enclave-concepts.md#term-enclave") to protect
and process highly sensitive data. NitroTPM extends similar attestation functionality to EC2 instances.

When you call the [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md"), [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"), or [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md") API operations with a
signed attestation document, these APIs encrypt the plaintext in the response under the
public key from the attestation document, and return ciphertext instead of plaintext. This
ciphertext can be decrypted only by using the private key in the enclave. For more
information, see [Cryptographic attestation support in
AWS KMS](cryptographic-attestation.md "cryptographic-attestation.md").

###### Note

If you don't provide a key policy when you create an AWS KMS key, AWS creates one for you.
This [default key policy](key-policy-default.md "key-policy-default.md") grants the
AWS accounts that own the KMS key full access to the key and allows the account to use
IAM policies to allow access to the key. This policy allows all actions like [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"). AWS
recommends applying principal of [Least-privilege permissions](least-privilege.md "least-privilege.md") to your KMS key policies. You can also restrict access by
[modifying the KMS key policy](key-policy-modifying.md "key-policy-modifying.md") action for
`kms:*` to `NotAction:kms:Decrypt`.

The following condition keys let you limit the permissions for these operations based on
the contents of the signed attestation document. Before allowing an operation, AWS KMS compares
the attestation document to the values in these AWS KMS condition keys.
