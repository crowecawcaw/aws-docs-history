# Keys in AWS CloudHSM

Before you can use your AWS CloudHSM cluster for cryptoprocessing, you must create [users](manage-hsm-users.md "manage-hsm-users.md") and keys
on the hardware security modules (HSM) in your cluster.

In AWS CloudHSM, use any of the following to manage keys on the HSMs in your cluster:

- PKCS #11 library
- JCE provider
- CNG and KSP providers
- CloudHSM CLI
  Before you can manage keys, you must log in to the HSM with the user name and password of a
  crypto user (CU). Only a CU can create a key. The CU who creates a key owns and manages that
  key.

See the following topics for more information about managing keys
in AWS CloudHSM.

###### Topics

- [Key sync and durability](manage-key-sync.md "manage-key-sync.md")
- [AES key wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md")
- [Trusted keys](manage-keys-using-trusted-keys.md "manage-keys-using-trusted-keys.md")
- [Key management with CloudHSM CLI](manage-keys-chsm-cli.md "manage-keys-chsm-cli.md")
- [Key management with KMU](manage-keys-kmu-cmu.md "manage-keys-kmu-cmu.md")
