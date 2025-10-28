# How to make attested calls to AWS KMS

To make an attested call to AWS KMS, use the `Recipient` parameter in the
request to provide the signed attestation document and the encryption algorithm to use
with the public key in the attestation document. When a request includes the
`Recipient` parameter with a signed attestation document, the response
includes a `CiphertextForRecipient` field with the ciphertext encrypted by
the public key. The plaintext field is null or empty.

The `Recipient` parameter must specify a signed attestation document from
an AWS Nitro Enclaves or AWS NitroTPM. AWS KMS relies on the digital signature
for the attestation document to prove that the public key in the request came from a
valid source. You cannot supply your own certificate to digitally sign the attestation
document.

The AWS Nitro Enclaves SDK, which is supported only within a Nitro enclave, automatically
adds the `Recipient` parameter and its values to every AWS KMS request.

To make attested requests in the AWS SDKs, you have to specify the
`Recipient` parameter and its values. The attestation document can be
retrieved from the NitroTPM using the [nitro-tpm-attest utility](../../../AWSEC2/latest/UserGuide/attestation-get-doc.md "../../../AWSEC2/latest/UserGuide/attestation-get-doc.md") or from the Nitro Secure Module (NSM) using [the NSM API](https://github.com/aws/aws-nitro-enclaves-nsm-api "https://github.com/aws/aws-nitro-enclaves-nsm-api").

AWS KMS supports [policy condition keys](conditions-attestation.md "conditions-attestation.md")
that you can use to allow or deny attested operations with an AWS KMS key based on the
content of the attestation document. You can also [monitor
attested requests to AWS KMS](ct-attestation.md "ct-attestation.md") in your AWS CloudTrail logs.

For detailed information about the `Recipient` parameter and the AWS
`CiphertextForRecipient` response field, see the [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md"), [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"), and [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md") topics in the _AWS Key Management Service API Reference_, the [AWS Nitro Enclaves SDK](../../../enclaves/latest/user/developing-applications.md#sdk "../../../enclaves/latest/user/developing-applications.md#sdk"), or any AWS
SDK. For information about setting up your data and data keys for encryption, see [Using cryptographic attestation
with AWS KMS](../../../enclaves/latest/user/kms.md "../../../enclaves/latest/user/kms.md").
