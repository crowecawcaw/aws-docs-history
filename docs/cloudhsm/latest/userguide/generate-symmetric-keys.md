# Generate symmetric keys with the AWS CloudHSM
 KMU

Use the [genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md") command in AWS CloudHSM key\_mgmt\_util
 (KMU) to generate AES and other types of symmetric keys for AWS CloudHSM. To
 see all available options, use the **genSymKey -h** command.

The following example creates a 256-bit AES key.


```
`Command:` `genSymKey -t 31 -s 32 -l aes256``Cfm3GenerateSymmetricKey returned: 0x00 : HSM Return: SUCCESS

Symmetric Key Created. Key Handle: 524295

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```
