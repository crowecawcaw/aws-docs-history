# The crypto verify category in CloudHSM CLI

In the CloudHSM CLI, **crypto verify** is a parent category for a group of
commands that, when combined with the parent category, confirms whether a file has been signed
by a given key. **crypto verify** has the following subcommands:

- [crypto verify ecdsa](cloudhsm_cli-crypto-verify-ecdsa.md "cloudhsm_cli-crypto-verify-ecdsa.md")
- [crypto verify ed25519ph](cloudhsm_cli-crypto-verify-ed25519ph.md "cloudhsm_cli-crypto-verify-ed25519ph.md")
- [crypto verify rsa-pkcs](cloudhsm_cli-crypto-verify-rsa-pkcs.md "cloudhsm_cli-crypto-verify-rsa-pkcs.md")
- [crypto verify rsa-pkcs-pss](cloudhsm_cli-crypto-verify-rsa-pkcs-pss.md "cloudhsm_cli-crypto-verify-rsa-pkcs-pss.md")
  The **crypto verify** command compares a signed file against a source file and analyzes whether they are cryptographically related based on a given public key and signing mechanism.

###### Note

Files can be signed in AWS CloudHSM with the [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md") operation.
