# Integrating with AWS KMS

Your instance should have an application that can make AWS KMS API requests with the Attestation Document retrieved from the
NitroTPM. When you make a request with an Attestation Document, AWS KMS validates the measurements in the provided Attestation Document against
the reference measurements in the KMS key policy. Requests are allowed only if the measurements in the Attestation Document match the
reference measurements in the KMS key policy.

When you call the [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md"),
[DeriveSharedSecret](../../../kms/latest/APIReference/API_DeriveSharedSecret.md "../../../kms/latest/APIReference/API_DeriveSharedSecret.md"),
[GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md"),
[GenerateDataKeyPair](../../../kms/latest/APIReference/API_GenerateDataKeyPair.md "../../../kms/latest/APIReference/API_GenerateDataKeyPair.md"),
or [GenerateRandom](../../../kms/latest/APIReference/API_GenerateRandom.md "../../../kms/latest/APIReference/API_GenerateRandom.md") API
operations with an Attestation Document, these APIs encrypt the plaintext in the response under the public key
from the Attestation Document, and return ciphertext instead of plaintext. This ciphertext can be decrypted only
by using the matching private key that was generated in the instance.

For more information, see the [Cryptographic attestation for NitroTPM](../../../kms/latest/developerguide/services-nitro-enclaves.md "../../../kms/latest/developerguide/services-nitro-enclaves.md") in the _AWS Key Management Service Developer Guide_.

###### Note

If you are attesting to a third-party service, you must build your own custom mechanisms for receiving,
parsing, and validating Attestation Documents. For more information, see [Validate a NitroTPM Attestation Document](nitrotpm-attestation-document-validate.md "nitrotpm-attestation-document-validate.md").
