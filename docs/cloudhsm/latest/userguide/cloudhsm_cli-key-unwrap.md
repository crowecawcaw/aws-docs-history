# The key unwrap command in CloudHSM CLI

The **key unwrap** parent command in CloudHSM CLI imports an encrypted (wrapped) symmetric or asymmetric private key from a file and into the HSM.
This command is designed to import encrypted keys that were wrapped by the [The key wrap command in CloudHSM CLI](cloudhsm_cli-key-wrap.md "cloudhsm_cli-key-wrap.md") command, but it can also be used to unwrap keys that were wrapped with other tools.
However, in those situations, we recommend using the PKCS#11 or JCE software libraries to unwrap the key.

- [aes-gcm](cloudhsm_cli-key-unwrap-aes-gcm.md "cloudhsm_cli-key-unwrap-aes-gcm.md")
- [aes-no-pad](cloudhsm_cli-key-unwrap-aes-no-pad.md "cloudhsm_cli-key-unwrap-aes-no-pad.md")
- [aes-pkcs5-pad](cloudhsm_cli-key-unwrap-aes-pkcs5-pad.md "cloudhsm_cli-key-unwrap-aes-pkcs5-pad.md")
- [aes-zero-pad](cloudhsm_cli-key-unwrap-aes-zero-pad.md "cloudhsm_cli-key-unwrap-aes-zero-pad.md")
- [cloudhsm-aes-gcm](cloudhsm_cli-key-unwrap-cloudhsm-aes-gcm.md "cloudhsm_cli-key-unwrap-cloudhsm-aes-gcm.md")
- [rsa-aes](cloudhsm_cli-key-unwrap-rsa-aes.md "cloudhsm_cli-key-unwrap-rsa-aes.md")
- [rsa-oaep](cloudhsm_cli-key-unwrap-rsa-oaep.md "cloudhsm_cli-key-unwrap-rsa-oaep.md")
- [rsa-pkcs](cloudhsm_cli-key-unwrap-rsa-pkcs.md "cloudhsm_cli-key-unwrap-rsa-pkcs.md")
