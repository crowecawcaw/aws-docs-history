# 2FA key pair requirements for AWS CloudHSM using AWS CloudHSM

Management Utility

To enable two-factor authentication (2FA) for an AWS CloudHSM hardware security module (HSM) user, use a key that meets the following requirements.

You can create a new key pair or use an existing key that meets the following
requirements.

- Key type: Asymmetric
- Key usage: Sign and Verify
- Key spec: RSA_2048
- Signing algorithm includes:
  - `sha256WithRSAEncryption`

###### Note

If you are using quorum authentication or plan to use quorum authentication, see [Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM
Management Utility](quorum-2fa.md "quorum-2fa.md").
