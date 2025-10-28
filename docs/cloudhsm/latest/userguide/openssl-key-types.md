# Supported key types for OpenSSL Dynamic Engine for AWS CloudHSM

Client SDK 5

The AWS CloudHSM OpenSSL Dynamic Engine supports the following key types with Client SDK 5.

| Key Type | Description                                                                                                                                                                                                                                               |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EC**   | ECDSA sign/verify for P-256, P-384, and secp256k1 key types. To generate EC keys that are interoperable with the OpenSSL engine, see [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md"). |
| **RSA**  | RSA key generation for 2048, 3072, and 4096-bit keys.RSA sign/verify. Verification is offloaded to OpenSSL software.                                                                                                                                      |
