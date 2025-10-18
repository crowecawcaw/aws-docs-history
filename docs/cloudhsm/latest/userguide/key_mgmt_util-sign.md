# Generate a signature using AWS CloudHSM KMU

Use the **sign** command in the AWS CloudHSM key\_mgmt\_util to use a chosen private key to
 generate a signature for a file.

In order to use **sign**, you must first have a private key in your HSM.
 You can generate a private key with the **[genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md")**, **[genRSAKeyPair](key_mgmt_util-genRSAKeyPair.md "key_mgmt_util-genRSAKeyPair.md")**, or **[genECCKeyPair](key_mgmt_util-genECCKeyPair.md "key_mgmt_util-genECCKeyPair.md")** commands. You
 can also import one with the **[importPrivateKey](key_mgmt_util-importPrivateKey.md "key_mgmt_util-importPrivateKey.md")** command. For more information, see [Generate Keys](generate-keys.md "generate-keys.md").

The **sign** command uses a user-designated signing mechanism, represented
 by an integer, to sign a message file. For a list of possible signing mechanisms, see [Parameters](#sign-parameters "#sign-parameters").

Before you run any key\_mgmt\_util command, you must [start
 key\_mgmt\_util](key_mgmt_util-setup.md#key_mgmt_util-start "key_mgmt_util-setup.md#key_mgmt_util-start") and [log in](key_mgmt_util-log-in.md "key_mgmt_util-log-in.md") to the HSM
 as a crypto user (CU).


## Syntax



```
sign -h

sign -f `<file name>`
     -k `<private key handle>`
     -m `<signature mechanism>`
     -out `<signed file name>`
```

## Example


This example shows how to use **sign** to sign a file.


###### Example : Sign a file

This command signs a file named `messageFile` with a private key with
 handle `266309`. It uses the `SHA256_RSA_PKCS`
 (`1`) signing mechanism and saves the resulting signed file as
 `signedFile`.


```
`Command:` `sign -f messageFile -k 266309 -m 1 -out signedFile`

`Cfm3Sign returned: 0x00 : HSM Return: SUCCESS

signature is written to file signedFile

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```

## Parameters


This command takes the following parameters.




**`-f`**

The name of the file to sign.


Required: Yes



**`-k`**

The handle of the private key to be used for signing.


Required: Yes



**`-m`**

An integer that represents the signing mechanism to be used for signing.
 The possible mechanisms correspond to the follow integers:




| Signing Mechanism | Corresponding Integer |
| --- | --- |
| `SHA1_RSA_PKCS` | 0 |
| `SHA256_RSA_PKCS` | 1 |
| `SHA384_RSA_PKCS` | 2 |
| `SHA512_RSA_PKCS` | 3 |
| `SHA224_RSA_PKCS` | 4 |
| `SHA1_RSA_PKCS_PSS` | 5 |
| `SHA256_RSA_PKCS_PSS` | 6 |
| `SHA384_RSA_PKCS_PSS` | 7 |
| `SHA512_RSA_PKCS_PSS` | 8 |
| `SHA224_RSA_PKCS_PSS` | 9 |
| `ECDSA_SHA1` | 15 |
| `ECDSA_SHA224` | 16 |
| `ECDSA_SHA256` | 17 |
| `ECDSA_SHA384` | 18 |
| `ECDSA_SHA512` | 19 | Required: Yes **`-out`** The name of the file to which the signed file will be saved. Required: Yes ## Related topics <br>• [verify](key_mgmt_util-verify.md "key_mgmt_util-verify.md") <br>• [importPrivateKey](key_mgmt_util-importPrivateKey.md "key_mgmt_util-importPrivateKey.md") <br>• [genRSAKeyPair](key_mgmt_util-genRSAKeyPair.md "key_mgmt_util-genRSAKeyPair.md") <br>• [genECCKeyPair](key_mgmt_util-genECCKeyPair.md "key_mgmt_util-genECCKeyPair.md") <br>• [genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md") <br>• [Generate Keys](generate-keys.md "generate-keys.md")
