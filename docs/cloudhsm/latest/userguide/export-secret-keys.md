# Export secret keys with the AWS CloudHSM KMU

Complete the following steps to export a secret key from AWS CloudHSM using the key_mgmt_util (KMU).

###### To export a secret key

1. Use the [genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md") command to create a
   wrapping key. The following command creates a 128-bit AES wrapping key that is valid
   only for the current session.

```
`Command:` `genSymKey -t 31 -s 16 -sess -l export-wrapping-key``Cfm3GenerateSymmetricKey returned: 0x00 : HSM Return: SUCCESS

Symmetric Key Created. Key Handle: 524304

Cluster Error Status
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```

2. Use one of the following commands, depending on the type of secret key that you are
   exporting.
   - To export a symmetric key, use the [exSymKey](key_mgmt_util-exSymKey.md "key_mgmt_util-exSymKey.md") command. The following command exports an AES key to a file named
     `aes256.key.exp`. To see all available options, use the
     **exSymKey -h** command.

   ```
   `Command:` `exSymKey -k 524295 -out aes256.key.exp -w 524304``Cfm3WrapKey returned: 0x00 : HSM Return: SUCCESS

   Cfm3UnWrapHostKey returned: 0x00 : HSM Return: SUCCESS


   Wrapped Symmetric Key written to file "aes256.key.exp"`
   ```

   ###### Note

   The command's output says that a "Wrapped Symmetric Key" is written to the
   output file. However, the output file contains a plaintext (not wrapped) key. To
   export a wrapped (encrypted) key to a file, use the [wrapKey](key_mgmt_util-wrapKey.md "key_mgmt_util-wrapKey.md") command.
   - To export a private key, use the **exportPrivateKey** command.
     The following command exports a private key to a file named
     `rsa2048.key.exp`. To see all available options, use the
     **exportPrivateKey -h** command.

   ```
   `Command:` `exportPrivateKey -k 524296 -out rsa2048.key.exp -w 524304``Cfm3WrapKey returned: 0x00 : HSM Return: SUCCESS

   Cfm3UnWrapHostKey returned: 0x00 : HSM Return: SUCCESS

   PEM formatted private key is written to rsa2048.key.exp`
   ```
