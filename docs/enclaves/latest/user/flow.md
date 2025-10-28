# Enclave workflow overview

The following topic explains some of the roles and basic workflows of AWS Nitro Enclaves,
using AWS KMS as the key management service, and Amazon S3 as the data storage service.

###### Topics

- [Involved parties](#roles "#roles")
- [Data and environment preparation](#data-prep "#data-prep")
- [Attestation and data decryption](#attest-decrypt "#attest-decrypt")
- [Nitro Enclaves application development](developing-applications.md "developing-applications.md")
- [Building an enclave image file](building-eif.md "building-eif.md")
- [Creating an enclave](create-enclave.md "create-enclave.md")

## Involved parties

A typical Nitro Enclaves use case involves multiple parties. Each party is responsible for
completing certain tasks to ensure that the enclave is operational. A typical use case
includes the following parties:

- **Data owner**—Owns the AWS KMS key and
  the secret data. The owner is responsible for creating the KMS key in AWS KMS,
  encrypting the secret data, and making the encrypted data and the encrypted data
  key available.
- **Parent instance administrator**—Owns the
  parent instance and manages the enclave's lifecycle. This party launches the
  parent instance and then creates the enclave using the enclave image file or
  Docker image, which is provided by the application developer. The parent
  instance administrator should not have permission to perform cryptographic
  actions using the KMS key, and they should not have permission to change the
  KMS key policy. The parent instance however, will need permissions to call
  `kms-decrypt` using the KMS key, but the request will only
  succeed if it is made from inside the enclave, and it includes values that match
  the condition keys in the KMS key policy.
- **Application developer**—Develops the
  applications that run in the enclave and on the parent instance. The developer
  packages the application into an enclave image file or Docker image and provides
  it to the parent instance administrator, who uses it to create the enclave. The
  application developer might also develop applications that run on the parent
  instance itself.

## Data and environment preparation

The following section provides an overview of the data encryption process, attestation
set up, and enclave creation process.

1. Create a AWS KMS key in AWS KMS. For more information, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.
2. Generate a plaintext and encrypted data key using the KMS key. For more
   information, see [generate-data-key](../../../cli/latest/reference/kms/generate-data-key.md "../../../cli/latest/reference/kms/generate-data-key.md") in the _AWS KMS AWS CLI Command Reference_.
3. Encrypt the secret data under the KMS key using the plaintext data key and a
   client-side cryptographic library, such as the [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md"). For more information, see [Encrypt data
   with a data key](../../../kms/latest/developerguide/concepts.md#data-keys-encrypt "../../../kms/latest/developerguide/concepts.md#data-keys-encrypt") in the _AWS Key Management Service Developer Guide_. You
   will need to modify the key policy of the KMS key to give the IAM principal
   you’re using in your client permission to call the GenerateDataKey API
   action
4. Upload the encrypted secret data and the encrypted data key to a storage
   location, such as Amazon S3. If you’re using the AWS Encryption SDK, the encrypted
   data key is automatically included in the header of the encrypted
   message.
5. Inspect the enclave application. This could be a pre-packaged enclave
   application, an existing application that has been refactored to run in an
   enclave, or a brand new enclave application.
6. If you are satisfied with the security properties of the application, package
   the application into a Docker file, and then use the AWS Nitro Enclaves CLI to
   convert the Docker file into an enclave image file. For more information, see
   [Building an enclave image file](building-eif.md "building-eif.md").

Make a note of the platform configuration registers (PCRs) that are generated
when the enclave image is created. 7. Use the PCRs to add attestation-based condition keys to the KMS key that you
used to encrypt the data. For more information, see [Cryptographic attestation](set-up-attestation.md "set-up-attestation.md"). 8. Launch the enclave-enabled parent instance and boot the enclave using the
enclave image. For more information, see [Creating an enclave](create-enclave.md "create-enclave.md").

## Attestation and data decryption

The following section provides an overview of the attestation and data decryption
process.

1. Download the encrypted data and the encrypted data key from Amazon S3 to the parent
   instance.
2. Transfer the encrypted data and the encrypted data key to the enclave over the
   vsock socket.
3. Call the `kms-decrypt` Nitro Enclaves SDK, which sends the encrypted
   data key and the attestation document to AWS KMS. The attestation document
   includes the enclave's PCRs and public key. The request is sent over the vsock
   socket to the parent instance, and the parent instance forwards the request to
   AWS KMS via the AWS KMS proxy.
4. AWS KMS receives the request and verifies that the attached attestation document
   is signed by the Nitro Hypervisor. AWS KMS then compares the PCRs in the
   attestation document with the PCRs in the condition keys in the policy of the
   requested KMS key.
5. If the PCRs in the attestation document match the PCRs in the condition keys
   of the KMS key policy, AWS KMS encrypts the plaintext data key with the
   enclave's public key from the attestation document.
6. The encrypted plaintext data key is returned to the parent instance over the
   KMS proxy, and the parent instance sends it to the enclave over the vsock
   socket.
7. The encrypted plaintext data key is decrypted using the enclave's private
   key.
8. The plaintext data key is used to decrypt the encrypted data.
9. The data is now ready to be processed inside the enclave.
