# Getting started with cryptographic attestation using the KMS Tool sample application

The AWS Nitro Enclaves SDK ships with a sample application, called **KMS Tool**,
that demonstrates the cryptographic attestation process. The KMS Tool sample application is supported on
both Windows and Linux parent instances.

KMS Tool includes two applications:

- **kmstool-instance**—An application that runs on the parent
  instance. It connects to _kmstool-enclave_ (over the vsock socket), passes
  credentials to the enclave, along with a base64-encoded message for decryption.
- **kmstool-enclave**—An application that runs in an enclave.
  It uses the Nitro Enclaves SDK to call AWS KMS in order to decrypt the base64-encoded message received
  from the application running on the parent instance.
  For instructions on how to set up and use the KMS Tool sample application, see the tutorial in the
  [AWS Nitro Enclaves SDK
  Github repository](https://github.com/aws/aws-nitro-enclaves-sdk-c/blob/main/docs/kmstool.md "https://github.com/aws/aws-nitro-enclaves-sdk-c/blob/main/docs/kmstool.md"). This tutorial shows you how to:

- Launch an enclave-enabled parent instance.
- Build a Docker image from a Docker file.
- Convert a Docker image to an enclave image file.
- Create an AWS KMS key.
- Add attestation-based condition keys to a KMS key policy.
- Create an enclave using an enclave image file.

###### Tip

The tutorial also discusses some best practices for preparing your enclave and KMS key for
attestation. You can use this sample application as a reference for building your own enclave
applications and for preparing your enclave and KMS keys for attestation.
