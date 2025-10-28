# OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 3

The AWS CloudHSM OpenSSL Dynamic Engine enables you to offload cryptographic operations to your CloudHSM
cluster through the OpenSSL API.

AWS CloudHSM Client SDK 3 does require a client daemon to connect to the cluster. It
supports:

- RSA key generation for 2048, 3072, and 4096-bit keys.
- RSA sign/verify.
- RSA encrypt/decrypt.
- Random number generation that is cryptographically secure and FIPS-validated.

Use the following sections to install and configure the AWS CloudHSM dynamic engine for
OpenSSL.

###### Topics

- [Prerequisites for OpenSSL Dynamic Engine with AWS CloudHSM
  Client SDK 3](openssl3-install-dyn3-prereqs.md "openssl3-install-dyn3-prereqs.md")
- [Install the OpenSSL Dynamic Engine for AWS CloudHSM
  Client SDK 3](openssl3-install-openssl-library.md "openssl3-install-openssl-library.md")
- [Use the OpenSSL Dynamic Engine for AWS CloudHSM
  Client SDK 3](openssl3-use-library.md "openssl3-use-library.md")
