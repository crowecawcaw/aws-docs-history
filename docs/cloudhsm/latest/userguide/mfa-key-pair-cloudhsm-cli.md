# MFA key pair requirements for AWS CloudHSM using
 CloudHSM CLI

To enable multi-factor authentication (MFA) for a hardware security module (HSM) user
 in AWS CloudHSM, you can create a new key pair or use an existing key that meets the following
 requirements:


* **Key type:** Asymmetric
* **Key usage:** Sign and verify
* **Key spec:** RSA\_2048
* **Signing algorithm includes:** sha256WithRSAEncryption
###### Note

If you are using quorum authentication or plan to use quorum authentication, see [Quorum authentication and MFA in AWS CloudHSM
 clusters using CloudHSM CLI](quorum-mfa-cloudhsm-cli.md "quorum-mfa-cloudhsm-cli.md")

You can use CloudHSM CLI and the key pair to create a new admin user with MFA enabled.
