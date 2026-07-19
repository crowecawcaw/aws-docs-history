# Getting started with Nitro Enclaves

These tutorials help you get started with AWS Nitro Enclaves. An enclave has no external
network connectivity, no persistent storage, and no interactive access. An enclave
communicates only with its associated parent instance over a local channel called a
_vsock_. Understanding how to launch, validate, and communicate with
an enclave helps you design secure, isolated workloads that protect sensitive data.

The following sections walk you through three foundational topics:

- **Hello Enclaves sample application** – Launch
  an enclave-enabled parent instance, build an enclave image file, validate that the
  enclave is running, and terminate it when you are finished.
- **Vsock communication** – Establish a
  virtio-vsock channel between the parent instance and the enclave to pass data
  securely over the local socket.
- **AWS KMS integration with cryptographic attestation**
  – Use AWS KMS and cryptographic attestation to decrypt secrets from inside a
  validated enclave, ensuring that only an enclave launched from a specific enclave
  image file can access sensitive data.

###### Topics

- [Getting started: Hello Enclaves](getting-started.md "getting-started.md")
- [Getting started: Using the virtio-vsock](enclave-networking.md "enclave-networking.md")
- [Getting started: Integrating with AWS KMS](connect-enclave-kms.md "connect-enclave-kms.md")
