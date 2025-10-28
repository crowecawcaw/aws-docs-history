# Get the NitroTPM Attestation Document

The Attestation Document is a key component of the NitroTPM attestation process. It contains a series
of cryptographic measurements that can be used to verify the identity of the instance and to prove that
it is running only trusted software. You can use the Attestation Document with AWS KMS, which provides
built-in support for NitroTPM attestation, or to build your own cryptographic attestation mechanisms.

The `nitro-tpm-attest` utility enables you to retrieve a signed NitroTPM Attestation Document
for an Amazon EC2 instance during runtime.

The sample Amazon Linux 2023 image description automatically installs the utility in the built image in the
`/usr/bin/` directory. This ensures that the utility is preinstalled on instances launched
using the AMI. You don't need to manually install the utility. For more information, see
[Build the sample Amazon Linux 2023 image description](build-sample-ami.md "build-sample-ami.md").

###### Topics

- [Install the nitro-tpm-attest utility](#nitro-tpm-attest-install "#nitro-tpm-attest-install")
- [Use the nitro-tpm-attest utility](#nitro-tpm-attest-use "#nitro-tpm-attest-use")
- [NitroTPM Attestation Document](nitrotpm-attestation-document-content.md "nitrotpm-attestation-document-content.md")
- [Validate Attestation Document](nitrotpm-attestation-document-validate.md "nitrotpm-attestation-document-validate.md")

## Install the `nitro-tpm-attest` utility

If you are using Amazon Linux 2023, you can install the `nitro-tpm-attest` utility
from the Amazon Linux repository as follows.

```
sudo yum install aws-nitro-tpm-tools
```

## Use the `nitro-tpm-attest` utility

The utility provides a single command, `nitro-tpm-attest`, for retrieving the Attestation Document.
The command returns the Attestation Document encoded in Concise Binary Object Representation
(CBOR) and signed using CBOR Object Signing and Encryption (COSE).

When you run the command, you can specify the following optional parameters:

- `public-key` — A public key that can be used by AWS KMS or an external service
  to encrypt response data before it is returned. This ensures that only the intended recipient, that
  has possession of the private key, can decrypt the data. For example, if you are attesting with AWS KMS,
  the service encrypts the plaintext data with the public key in the Attestation Document, and returns
  the resulting ciphertext in the `CiphertextForRecipient` field in the response. Only RSA
  keys are supported.
- `user-data` — The user data can be used to deliver any additional signed
  data to an external service. This user data can be used to complete an agreed protocol between
  the requesting instance and the external service. Not used for attestation with AWS KMS.
- `nonce` — The nonce can be used to set up challenge-response authentication
  between the instance and the external service to help prevent impersonation attacks. Using a nonce
  enables the external service to verify that it is interacting with a live instance and not an
  impersonator that is reusing an old Attestation Document. Not used for attestation with AWS KMS.

###### To retrieve the Attestation Document

Use the following command and optional parameters:

```
/usr/bin/nitro-tpm-attest \
--public-key `rsa_public_key` \
--user-data `user_data` \
--nonce `nonce`
```

For a complete example that shows how to generate an RSA key pair, and how to request an attestation
with the public key, see the [nitro-tpm-attest GitHub repo](https://github.com/aws/NitroTPM-Tools/ "https://github.com/aws/NitroTPM-Tools/").
