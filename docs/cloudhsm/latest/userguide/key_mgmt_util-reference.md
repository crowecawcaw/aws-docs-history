# Reference for AWS CloudHSM Key Management Utility

commands

The **key_mgmt_util** command line tool helps you to manage
keys in the hardware security modules (HSM) in your AWS CloudHSM cluster, including creating, deleting,
and finding keys and their attributes. It includes multiple commands, each of which is described
in detail in this topic.

For a quick start, see [Getting started with AWS CloudHSM
key_mgmt_util](key_mgmt_util-getting-started.md "key_mgmt_util-getting-started.md"). For help interpreting the key attributes, see the [AWS CloudHSM key attribute reference for KMU](key-attribute-table.md "key-attribute-table.md"). For information about
the cloudhsm_mgmt_util command line tool, which includes commands to manage the HSM and users in your
cluster, see [AWS CloudHSM Management Utility (CMU)](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md").

Before you run any key_mgmt_util command, you must [start
key_mgmt_util](key_mgmt_util-setup.md#key_mgmt_util-start "key_mgmt_util-setup.md#key_mgmt_util-start") and [log in](key_mgmt_util-log-in.md "key_mgmt_util-log-in.md") to the HSM as a crypto user
(CU).

To list all key_mgmt_util commands, type:

```
`Command:` `help`
```

To get help for a particular key_mgmt_util command, type:

```
`Command:` ``<command-name>` -h`
```

To end your key_mgmt_util session, type:

```
`Command:` `exit`
```

The following topics describe commands in key_mgmt_util.

###### Note

Some commands in key_mgmt_util and cloudhsm_mgmt_util have the same names. However, the commands typically have
different syntax, different output, and slightly different functionality.

| Command                                                                                                                      | Description                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [aesWrapUnwrap](key_mgmt_util-aesWrapUnwrap.md "key_mgmt_util-aesWrapUnwrap.md")                                             | Encrypts and decrypts the contents of a key in a file.                                                                                                                                                                                                                       |
| [deleteKey](key_mgmt_util-deleteKey.md "key_mgmt_util-deleteKey.md")                                                         | Deletes a key from the HSMs.                                                                                                                                                                                                                                                 |
| [Error2String](key_mgmt_util-Error2String.md "key_mgmt_util-Error2String.md")                                                | Gets the error that corresponds to a key_mgmt_util hexadecimal error<br>code.                                                                                                                                                                                                |
| [exit](key_mgmt_util-exit.md "key_mgmt_util-exit.md")                                                                        | Exits the key_mgmt_util.                                                                                                                                                                                                                                                     |
| [exportPrivateKey](key_mgmt_util-exportPrivateKey.md "key_mgmt_util-exportPrivateKey.md")                                    | Exports a copy of a private key from an HSM to a file on disk.                                                                                                                                                                                                               |
| [exportPubKey](key_mgmt_util-exportPubKey.md "key_mgmt_util-exportPubKey.md")                                                | Exports a copy of a public key from an HSM to a file.                                                                                                                                                                                                                        |
| [exSymKey](key_mgmt_util-exSymKey.md "key_mgmt_util-exSymKey.md")                                                            | Exports a plaintext copy of a symmetric key from the HSMs to a<br>file.                                                                                                                                                                                                      |
| [extractMaskedObject](key_mgmt_util-extractMaskedObject.md "key_mgmt_util-extractMaskedObject.md")                           | Extracts a key from an HSM as a masked object file.                                                                                                                                                                                                                          |
| [findKey](key_mgmt_util-findKey.md "key_mgmt_util-findKey.md")                                                               | Search for keys by key attribute value.                                                                                                                                                                                                                                      |
| [findSingleKey](key_mgmt_util-findSingleKey.md "key_mgmt_util-findSingleKey.md")                                             | Verifies that a key exists on all HSMs in the cluster.                                                                                                                                                                                                                       |
| [genDSAKeyPair](key_mgmt_util-genDSAKeyPair.md "key_mgmt_util-genDSAKeyPair.md")                                             | Generates a [Digital Signing Algorithm](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm "https://en.wikipedia.org/wiki/Digital_Signature_Algorithm") (DSA) key pair in your HSMs.                                                                                  |
| [genECCKeyPair](key_mgmt_util-genECCKeyPair.md "key_mgmt_util-genECCKeyPair.md")                                             | Generates an [Elliptic Curve<br>Cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography "https://en.wikipedia.org/wiki/Elliptic-curve_cryptography") (ECC) key pair in your HSMs.                                                                            |
| [genRSAKeyPair](key_mgmt_util-genRSAKeyPair.md "key_mgmt_util-genRSAKeyPair.md")                                             | Generates an [RSA](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29 "https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29") asymmetric key pair in your HSMs.                                                                                                            |
| [genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md")                                                         | Generates a symmetric key in your HSMs                                                                                                                                                                                                                                       |
| [getAttribute](key_mgmt_util-getAttribute.md "key_mgmt_util-getAttribute.md")                                                | Gets the attribute values for an AWS CloudHSM key and writes them to a<br>file.                                                                                                                                                                                              |
| [getCaviumPrivKey](key_mgmt_util-getCaviumPrivKey.md "key_mgmt_util-getCaviumPrivKey.md")                                    | Creates a fake PEM-format version of a private key and exports it to a<br>file.                                                                                                                                                                                              |
| [getCert](key_mgmt_util-getCert.md "key_mgmt_util-getCert.md")                                                               | Retrieves an HSM's partitions certificates and saves them to a file.                                                                                                                                                                                                         |
| [getKeyInfo](key_mgmt_util-getKeyInfo.md "key_mgmt_util-getKeyInfo.md")                                                      | Gets the HSM user IDs of users who can use the key.<br>If the key is quorum controlled, it gets the number of users in the<br>quorum.                                                                                                                                        |
| [help](key_mgmt_util-help.md "key_mgmt_util-help.md")                                                                        | Displays help information about the commands available in key_mgmt_util.                                                                                                                                                                                                     |
| [importPrivateKey](key_mgmt_util-importPrivateKey.md "key_mgmt_util-importPrivateKey.md")                                    | Imports a private key into an HSM.                                                                                                                                                                                                                                           |
| [importPubKey](key_mgmt_util-importPubKey.md "key_mgmt_util-importPubKey.md")                                                | Imports a public key into an HSM.                                                                                                                                                                                                                                            |
| [imSymKey](key_mgmt_util-imSymKey.md "key_mgmt_util-imSymKey.md")                                                            | Imports a plaintext copy of a symmetric key from a file into the HSM.                                                                                                                                                                                                        |
| [insertMaskedObject](key_mgmt_util-insertMaskedObject.md "key_mgmt_util-insertMaskedObject.md")                              | Inserts a masked object from a file on disk into an HSM contained by related<br>cluster to the object's origin cluster. Related clusters are any clusters [generated from a backup of the origin<br>cluster](create-cluster-from-backup.md "create-cluster-from-backup.md"). |
| [Validate key file using AWS CloudHSM<br>KMU](key_mgmt_util-IsValidKeyHandlefile.md "key_mgmt_util-IsValidKeyHandlefile.md") | Determines whether or not a given file contains a real private key or a example<br>PEM key.                                                                                                                                                                                  |
| [listAttributes](key_mgmt_util-listAttributes.md "key_mgmt_util-listAttributes.md")                                          | Lists the attributes of an AWS CloudHSM key and the constants that represent<br>them.                                                                                                                                                                                        |
| [listUsers](key_mgmt_util-listUsers.md "key_mgmt_util-listUsers.md")                                                         | Gets the users in the HSMs, their user type and ID, and other attributes.                                                                                                                                                                                                    |
| [loginHSM and<br>logoutHSM](key_mgmt_util-loginHSM.md "key_mgmt_util-loginHSM.md")                                           | Log in and out of the HSMs in a cluster.                                                                                                                                                                                                                                     |
| [setAttribute](key_mgmt_util-setAttribute.md "key_mgmt_util-setAttribute.md")                                                | Converts a session key to a persistent key.                                                                                                                                                                                                                                  |
| [sign](key_mgmt_util-sign.md "key_mgmt_util-sign.md")                                                                        | Generate a signature for a file using a chosen private key.                                                                                                                                                                                                                  |
| [unWrapKey](key_mgmt_util-unwrapKey.md "key_mgmt_util-unwrapKey.md")                                                         | Imports a wrapped (encrypted) key from a file into the HSMs.                                                                                                                                                                                                                 |
| [verify](key_mgmt_util-verify.md "key_mgmt_util-verify.md")                                                                  | Verifies whether a given key was used to sign a given file.                                                                                                                                                                                                                  |
| [wrapKey](key_mgmt_util-wrapKey.md "key_mgmt_util-wrapKey.md")                                                               | Exports an encrypted copy of a key from the HSM to a file.                                                                                                                                                                                                                   |
