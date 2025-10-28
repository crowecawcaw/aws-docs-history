# Generate ECC (elliptic curve cryptography) key

pairs using the AWS CloudHSM KMU

To generate an ECC key pair for AWS CloudHSM, use the [genECCKeyPair](key_mgmt_util-genECCKeyPair.md "key_mgmt_util-genECCKeyPair.md") command in AWS CloudHSM key_mgmt_util. To see
all available options, including a list of the supported elliptic curves, use the
**genECCKeyPair -h** command.

The following example generates an ECC key pair using the P-384 elliptic curve defined
in [NIST FIPS publication
186-4](http://dx.doi.org/10.6028/NIST.FIPS.186-4 "http://dx.doi.org/10.6028/NIST.FIPS.186-4").

```
`Command:` `genECCKeyPair -i 14 -l ecc-p384``Cfm3GenerateKeyPair returned: 0x00 : HSM Return: SUCCESS

Cfm3GenerateKeyPair: public key handle: 524297 private key handle: 524298

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`
```
