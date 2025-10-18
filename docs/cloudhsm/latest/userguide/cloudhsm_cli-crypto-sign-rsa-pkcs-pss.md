# Generate a signature with the
 RSA-PKCS-PSS mechanism in CloudHSM CLI

Use the **crypto sign rsa-pkcs-pss** command in CloudHSM CLI to generate a
 signature using an RSA private key and the `RSA-PKCS-PSS` signing mechanism.

To use the **crypto sign rsa-pkcs-pss** command, you must first have a RSA private key in your AWS CloudHSM cluster. 
 You can generate an RSA private key using the [Generate an asymmetric RSA key
 pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-rsa.md "cloudhsm_cli-key-generate-asymmetric-pair-rsa.md") command with the `sign` attribute set to `true`.

###### Note

Signatures can be verified in AWS CloudHSM with [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md") subcommands.


## User type


The following types of users can run this command.



* Crypto users (CUs)

## Requirements



* To run this command, you must be logged in as a CU.

## Syntax



```
`aws-cloudhsm >` `help crypto sign rsa-pkcs-pss``Sign with the RSA-PKCS-PSS mechanism

Usage: crypto sign rsa-pkcs-pss [OPTIONS] --key-filter [`<KEY_FILTER>`...] --hash-function `<HASH_FUNCTION>` --mgf `<MGF>` --salt-length `<SALT_LENGTH>` <--data-path `<DATA_PATH>`|--data `<DATA>`>

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --key-filter [`<KEY_FILTER>`...] Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key
 --hash-function `<HASH_FUNCTION>` [possible values: sha1, sha224, sha256, sha384, sha512]
 --data-path `<DATA_PATH>` The path to the file containing the data to be signed
 --data `<DATA>` Base64 Encoded data to be signed
 --mgf `<MGF>` The mask generation function [possible values: mgf1-sha1, mgf1-sha224, mgf1-sha256, mgf1-sha384, mgf1-sha512]
 --salt-length `<SALT_LENGTH>` The salt length
 --approval `<APPROVAL>` Filepath of signed quorum token file to approve operation
 --data-type `<DATA_TYPE>` The type of data passed in, either raw or digest [possible values: raw, digest]
 -h, --help Print help`
```

## Example


These examples show how to use **crypto sign rsa-pkcs-pss** to generate a signature using the `RSA-PKCS-PSS` signing mechanism and `SHA256` hash function. This command uses a private key in the HSM.


###### Example: Generate a signature for base 64 encoded data


```
`aws-cloudhsm >` `crypto sign rsa-pkcs-pss --key-filter attr.label=rsa-private --hash-function sha256 --data YWJjMTIz --salt-length 10 --mgf mgf1-sha256``{
 "error_code": 0,
 "data": {
 "key-reference": "0x00000000007008db",
 "signature": "H/z1rYVMzNAa31K4amE5MTiwGxDdCTgQXCJXRBKVOVm7ZuyI0fGE4sT/BUN+977mQEV2TqtWpTsiF2IpwGM1VfSBRt7h/g4o6YERm1tTQLl7q+AJ7uGGK37zCsWQrAo7Vy8NzPShxekePo/ZegrB1aHWN1fE8H3IPUKqLuMDI9o1Jq6kM986ExS7YmeOIclcZkyykTWqHLQVL2C3+A2bHJZBqRcM5XoIpk8HkPypjpN+m4FNUds30GAemoOMl6asSrEJSthaZWV53OBsDOqzA8Rt8JdhXS+GZp3vNLdL1OTBELDPweXVgAu4dBX0FOvpw/gg6sNvuaDK4YOBv2fqKg=="
 }
}`
```

###### Example: Generate a signature for a data file


```
`aws-cloudhsm >` `crypto sign rsa-pkcs-pss --key-filter attr.label=rsa-private --hash-function sha256 --data-path data.txt --salt-length 10 --mgf mgf1-sha256``{
 "error_code": 0,
 "data": {
 "key-reference": "0x00000000007008db",
 "signature": "H/z1rYVMzNAa31K4amE5MTiwGxDdCTgQXCJXRBKVOVm7ZuyI0fGE4sT/BUN+977mQEV2TqtWpTsiF2IpwGM1VfSBRt7h/g4o6YERm1tTQLl7q+AJ7uGGK37zCsWQrAo7Vy8NzPShxekePo/ZegrB1aHWN1fE8H3IPUKqLuMDI9o1Jq6kM986ExS7YmeOIclcZkyykTWqHLQVL2C3+A2bHJZBqRcM5XoIpk8HkPypjpN+m4FNUds30GAemoOMl6asSrEJSthaZWV53OBsDOqzA8Rt8JdhXS+GZp3vNLdL1OTBELDPweXVgAu4dBX0FOvpw/gg6sNvuaDK4YOBv2fqKg=="
 }
}`
```

## Arguments




**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.


Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")



**`<DATA>`**

Base64 encoded data to be signed.


Required: Yes (unless provided through data path)



**`<DATA_PATH>`**

Specifies the location of the data to be signed.


Required: Yes (unless provided through data)



**`<HASH_FUNCTION>`**

Specifies the hash function.
 


Valid values:



* sha1
* sha224
* sha256
* sha384
* sha512

Required: Yes



**`<KEY_FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key.


For a listing of supported CloudHSM CLI key attributes, see Key attributes for CloudHSM CLI.


Required: Yes



**`<MGF>`**

Specifies the mask generation function.


###### Note

The mask generation function hash function must match the signing mechanism hash function.


Valid values:



* mgf1-sha1
* mgf1-sha224
* mgf1-sha256
* mgf1-sha384
* mgf1-sha512

Required: Yes



**`<SALT_LENGTH>`**

Specifies the salt length.


Required: Yes



**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if the key usage service quorum value of the private key is greater than 1.



**`<DATA_TYPE>`**

 Specifies whether the value of the data parameter should be hashed as part of the signing algorithm. Use `raw` for unhashed data; use `digest` for digests, which are already hashed. 


Valid values:



* raw
* digest



## Related topics



* [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
* [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
