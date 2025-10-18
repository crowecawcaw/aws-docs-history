# Export keys with the AWS CloudHSM KMU

To export AWS CloudHSM secret keys—that is, symmetric keys and asymmetric private
 keys—from the hardware security module (HSM) using the AWS CloudHSM key\_mgmt\_util (KMU), you must
 first create a wrapping key. You can export public keys directly without a wrapping key. 

Only the key owner can export a key. Users with whom the key is shared can use the key in
 cryptographic operations, but they cannot export it. When running this example, be sure to
 export a key that you created. 

###### Important

The [exSymKey](key_mgmt_util-exSymKey.md "key_mgmt_util-exSymKey.md") command writes a plaintext
 (unencrypted) copy of the secret key to a file. The export process requires a wrapping key,
 but the key in the file is ***not*** a
 wrapped key. To export a wrapped (encrypted) copy of a key, use the [wrapKey](key_mgmt_util-wrapKey.md "key_mgmt_util-wrapKey.md") command.

###### Topics

* [Export secret keys](export-secret-keys.md "export-secret-keys.md")
* [Export public keys](export-public-keys.md "export-public-keys.md")
