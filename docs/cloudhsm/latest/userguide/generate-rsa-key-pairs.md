# Generate RSA key pairs with the AWS CloudHSM KMU

To generate an RSA key pair for AWS CloudHSM, use the [genRSAKeyPair](key_mgmt_util-genRSAKeyPair.md "key_mgmt_util-genRSAKeyPair.md") command in AWS CloudHSM key\_mgmt\_util. To see
 all available options, use the **genRSAKeyPair -h** command.

The following example generates an RSA 2048-bit key pair.


```
`Command:` `genRSAKeyPair -m 2048 -e 65537 -l rsa2048``Cfm3GenerateKeyPair returned: 0x00 : HSM Return: SUCCESS

Cfm3GenerateKeyPair: public key handle: 524294 private key handle: 524296

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```
