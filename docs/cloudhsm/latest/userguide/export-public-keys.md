# Export public keys with the AWS CloudHSM KMU

Use the **exportPubKey** command in the AWS CloudHSM key\_mgmt\_util (KMU) to export a
 public key. To see all available options, use the **exportPubKey -h**
 command.

The following example exports an RSA public key to a file named
 `rsa2048.pub.exp`.


```
`Command:` `exportPubKey -k 524294 -out rsa2048.pub.exp``PEM formatted public key is written to rsa2048.pub.key

Cfm3ExportPubKey returned: 0x00 : HSM Return: SUCCESS`
```
