# The key wrap command in CloudHSM CLI

The **key wrap** command in CloudHSM CLI exports an encrypted copy of a
 symmetric or asymmetric private key from the hardware security module (HSM) to a file. When you
 run **key wrap**, you specify two things: The key to export and the output file.
 The key to export is a key on the HSM that will encrypt (wrap) the key that you want to
 export.

The **key wrap** command does not remove the key from the HSM or prevent you from using it in cryptographic operations. 
 You can export the same key multiple times. To import the encrypted key back into the HSM, use [The key unwrap command in CloudHSM CLI](cloudhsm_cli-key-unwrap.md "cloudhsm_cli-key-unwrap.md"). 
 Only the owner of a key, that is the crypto user (CU) who created the key, can wrap the key. Users with whom the key is shared can only use the key in cryptographic operations.

The **key wrap** command consists of the following subcommands:


* [aes-gcm](cloudhsm_cli-key-wrap-aes-gcm.md "cloudhsm_cli-key-wrap-aes-gcm.md")
* [aes-no-pad](cloudhsm_cli-key-wrap-aes-no-pad.md "cloudhsm_cli-key-wrap-aes-no-pad.md")
* [aes-pkcs5-pad](cloudhsm_cli-key-wrap-aes-pkcs5-pad.md "cloudhsm_cli-key-wrap-aes-pkcs5-pad.md")
* [aes-zero-pad](cloudhsm_cli-key-wrap-aes-zero-pad.md "cloudhsm_cli-key-wrap-aes-zero-pad.md")
* [cloudhsm-aes-gcm](cloudhsm_cli-key-wrap-cloudhsm-aes-gcm.md "cloudhsm_cli-key-wrap-cloudhsm-aes-gcm.md")
* [rsa-aes](cloudhsm_cli-key-wrap-rsa-aes.md "cloudhsm_cli-key-wrap-rsa-aes.md")
* [rsa-oaep](cloudhsm_cli-key-wrap-rsa-oaep.md "cloudhsm_cli-key-wrap-rsa-oaep.md")
* [rsa-pkcs](cloudhsm_cli-key-wrap-rsa-pkcs.md "cloudhsm_cli-key-wrap-rsa-pkcs.md")
