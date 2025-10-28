# Import secret keys with the AWS CloudHSM KMU

Complete the following steps to import a secret key into AWS CloudHSM using the key_mgmt_util (KMU).
Before you import a secret key, save it to a file. Save symmetric keys as raw bytes, and
asymmetric private keys in PEM format.

This example shows how to import a plaintext secret key from a file into the HSM. To
import an encrypted key from a file into the HSM, use the [unWrapKey](key_mgmt_util-unwrapKey.md "key_mgmt_util-unwrapKey.md") command.

###### To import a secret key

1. Use the [genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md") command to create a
   wrapping key. The following command creates a 128-bit AES wrapping key that is valid
   only for the current session. You can use a session key or a persistent key as a
   wrapping key.

```
`Command:` `genSymKey -t 31 -s 16 -sess -l import-wrapping-key``Cfm3GenerateSymmetricKey returned: 0x00 : HSM Return: SUCCESS

Symmetric Key Created. Key Handle: 524299

Cluster Error Status
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```

2. Use one of the following commands, depending on the type of secret key that you are
   importing.
   - To import a symmetric key, use the [imSymKey](key_mgmt_util-imSymKey.md "key_mgmt_util-imSymKey.md") command. The
     following command imports an AES key from a file named
     `aes256.key` using the wrapping key created in the previous step.
     To see all available options, use the **imSymKey -h** command.

   ```
   `Command:` `imSymKey -f aes256.key -t 31 -l aes256-imported -w 524299``Cfm3WrapHostKey returned: 0x00 : HSM Return: SUCCESS

   Cfm3CreateUnwrapTemplate returned: 0x00 : HSM Return: SUCCESS

   Cfm3UnWrapKey returned: 0x00 : HSM Return: SUCCESS

   Symmetric Key Unwrapped. Key Handle: 524300

   Cluster Error Status
   Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
   Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
   Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
   ```

   - To import an asymmetric private key, use the [importPrivateKey](key_mgmt_util-importPrivateKey.md "key_mgmt_util-importPrivateKey.md")
     command. The following command imports a private key from a file named
     `rsa2048.key` using the wrapping key created in the previous
     step. To see all available options, use the **importPrivateKey -h**
     command.

   ```
   `Command:` `importPrivateKey -f rsa2048.key -l rsa2048-imported -w 524299``BER encoded key length is 1216

   Cfm3WrapHostKey returned: 0x00 : HSM Return: SUCCESS

   Cfm3CreateUnwrapTemplate returned: 0x00 : HSM Return: SUCCESS

   Cfm3UnWrapKey returned: 0x00 : HSM Return: SUCCESS

   Private Key Unwrapped. Key Handle: 524301

   Cluster Error Status
   Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
   Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
   Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
   ```
