# Import public keys with the AWS CloudHSM KMU

Use the [importPubKey](key_mgmt_util-importPubKey.md "key_mgmt_util-importPubKey.md") command in the
AWS CloudHSM key_mgmt_util (KMU) to import a public key. To see all available options, use the
**importPubKey -h** command.

The following example imports an RSA public key from a file named
`rsa2048.pub`.

```
`Command:` `importPubKey -f rsa2048.pub -l rsa2048-public-imported``Cfm3CreatePublicKey returned: 0x00 : HSM Return: SUCCESS

Public Key Handle: 524302

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```
