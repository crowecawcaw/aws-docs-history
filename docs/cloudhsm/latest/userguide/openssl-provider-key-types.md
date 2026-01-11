# Supported key types for OpenSSL Provider for AWS CloudHSM Client SDK 5

The AWS CloudHSM OpenSSL Provider supports the following key types with Client SDK 5.

| Key Type | Description                                                                                                                                                                                                                                                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RSA**  | RSA sign/verify and asymmetric encryption operations. Verification is offloaded to OpenSSL software. To generate RSA keys that are interoperable with the OpenSSL Provider, see [Export an asymmetric key with<br>CloudHSM CLI](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md"). |
| **EC**   | ECDSA sign/verify for P-256, P-384, and P-521 curves. Verification is offloaded to OpenSSL software. To generate EC keys that are interoperable with the OpenSSL Provider, see [Export an asymmetric key with<br>CloudHSM CLI](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md").  |
