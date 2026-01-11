# The crypto sign category in CloudHSM CLI

In the CloudHSM CLI, **crypto sign** is a parent category for a group of
commands that, when combined with the parent category, uses a chosen private key in your AWS CloudHSM
cluster to generate a signature. **crypto sign** has the following
subcommands:

- [Generate a signature with the ECDSA mechanism in
  CloudHSM CLI](cloudhsm_cli-crypto-sign-ecdsa.md "cloudhsm_cli-crypto-sign-ecdsa.md")
- [Generate a signature with the HashEdDSA mechanism in
  CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519ph.md "cloudhsm_cli-crypto-sign-ed25519ph.md")
- [Generate a signature with the RSA-PKCS
  mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-rsa-pkcs.md "cloudhsm_cli-crypto-sign-rsa-pkcs.md")
- [Generate a signature with the
  RSA-PKCS-PSS mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-rsa-pkcs-pss.md "cloudhsm_cli-crypto-sign-rsa-pkcs-pss.md")
  To use **crypto sign**, you must have a private key in your HSM. You can generate a private key with the following commands:

- [key generate-asymmetric-pair ec](cloudhsm_cli-key-generate-asymmetric-pair-ec.md "cloudhsm_cli-key-generate-asymmetric-pair-ec.md")
- [key generate-asymmetric-pair rsa](cloudhsm_cli-key-generate-asymmetric-pair-rsa.md "cloudhsm_cli-key-generate-asymmetric-pair-rsa.md")

## Related topics

- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
