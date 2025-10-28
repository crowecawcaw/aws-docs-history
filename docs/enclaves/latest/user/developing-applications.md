# Nitro Enclaves application development

An enclave application is an application that is designed and developed to run inside
the isolated enclave environment. An enclave application typically consists of at least
two components:

- An application that runs on the parent instance
- An application that runs inside the enclave
  Due to the isolated environment of the enclave, the only channel of communication
  between applications that are running on the instance and applications that are running
  in the enclave is the vsock socket.

###### Topics

- [Nitro Enclaves Developer AMI](#dev-ami "#dev-ami")
- [Nitro Enclaves SDK](#sdk "#sdk")
- [Application development
  on Linux](developing-applications-linux.md "developing-applications-linux.md")
- [Application
  development on Windows](developing-applications-windows.md "developing-applications-windows.md")

## Nitro Enclaves Developer AMI

AWS provides a Nitro Enclaves Developer AMI that contains the tools and
components needed to develop enclave applications and to build enclave image files.
It also contains samples applications, such as hello-enclave, vsock_sample and
kmstool, to demonstrate how to use and develop your own enclave applications. For
more information, see [AWS Nitro Enclaves Developer AMI](https://aws.amazon.com/marketplace/pp/B08R69DKQ1 "https://aws.amazon.com/marketplace/pp/B08R69DKQ1").

## Nitro Enclaves SDK

The Nitro Enclaves SDK is a set of open-source libraries that you can use to develop
your enclave applications. The SDKs also integrate with AWS KMS and provide built-in
support for attestation and cryptographic operations. For more information about the
SDKs and how to use them, see the [Nitro Enclaves SDK Github
repository](https://github.com/aws/aws-nitro-enclaves-sdk-c "https://github.com/aws/aws-nitro-enclaves-sdk-c").
