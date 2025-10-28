# Import a PEM format key with CloudHSM CLI

Use the **key import pem** command in AWS CloudHSM to import a PEM format key into a
hardware security module (HSM). You can use it to import public keys that were generated outside
of the HSM.

###### Note

Use the [Export an asymmetric key with
CloudHSM CLI](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md") command to create a standard PEM file from a public key or to create a reference PEM file from a private key.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

- To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help key import pem``Import key from a PEM file

Usage: key import pem [OPTIONS] --path `<PATH>` --label `<LABEL>` --key-type-class `<KEY_TYPE_CLASS>`
Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --path `<PATH>`
 Path where the key is located in PEM format
 --label `<LABEL>`
 Label for the imported key
 --key-type-class `<KEY_TYPE_CLASS>`
 Key type and class of the imported key [possible values: ec-public, rsa-public]
 --attributes [`<IMPORT_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE for the imported key
 -h, --help
 Print help`
```

## Examples

These example shows how to use the **key import pem** command to import an RSA public key from a file in PEM format.

###### Example: Import an RSA public key

```
`aws-cloudhsm >` `key import pem --path /home/example --label example-imported-key --key-type-class rsa-public``{
 "error_code": 0,
 "data": {
 "key": {
 "key-reference": "0x00000000001e08e3",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "example-imported-key",
 "id": "0x",
 "check-value": "0x99fe93",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": false,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": false,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 512,
 "public-exponent": "0x010001",
 "modulus": "0x8e9c172c37aa22ed1ce25f7c3a7c936dadc532201400128b044ebb4b96│··3e4930ab910df5a2896eaeb8853cfea0e341227654a8337a7864cc8a87d136f006cfba9e68d0b329│··746c1ad60941668b18699fc8169ff1ec363d0d18292845b2454d6a0b8c5d111b79c047619d460cdf│··be59debbacb66b7abeaf3f3d35dd2b9cfa6b6b7b1258b6866cb4085ac749e9d8552b3a4509e1b86c│··828cc794e22767b4f6b5bc6ff5c96f4b7e60eab305d669cfa2197e85379cb35c659bb58fcd246d48│··d9f6a7f36063b42da025459275aa8e3abedad775387086bd6c198ded868403f4b87ffda5a2d455ac│··aa6cbd00003c31d8d2f51d10cd272b31cf0c4037791f48ad51fb35",
 "modulus-size-bits": 2048
 }
 },
 "message": "Successfully imported key"
 }
}`
```

###### Example: Import an RSA public key with optional attributes

```
`aws-cloudhsm >` `key import pem --path /home/example --label example-imported-key-with-attributes --key-type-class rsa-public --attributes verify=true``{
 "error_code": 0,
 "data": {
 "key": {
 "key-reference": "0x00000000001e08e3",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "example-imported-key-with-attributes",
 "id": "0x",
 "check-value": "0x99fe93",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": false,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": false,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 512,
 "public-exponent": "0x010001",
 "modulus": "0x8e9c172c37aa22ed1ce25f7c3a7c936dadc532201400128b044ebb4b96│··3e4930ab910df5a2896eaeb8853cfea0e341227654a8337a7864cc8a87d136f006cfba9e68d0b329│··746c1ad60941668b18699fc8169ff1ec363d0d18292845b2454d6a0b8c5d111b79c047619d460cdf│··be59debbacb66b7abeaf3f3d35dd2b9cfa6b6b7b1258b6866cb4085ac749e9d8552b3a4509e1b86c│··828cc794e22767b4f6b5bc6ff5c96f4b7e60eab305d669cfa2197e85379cb35c659bb58fcd246d48│··d9f6a7f36063b42da025459275aa8e3abedad775387086bd6c198ded868403f4b87ffda5a2d455ac│··aa6cbd00003c31d8d2f51d10cd272b31cf0c4037791f48ad51fb35",
 "modulus-size-bits": 2048
 }
 },
 "message": "Successfully imported key"
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<PATH>`**

Specifies the file path where the key file is located.

Required: Yes

**`<LABEL>`**

Specifies a user defined label for the imported key. The maximum size allowable for `label` is 126 characters.

Required: Yes

**`<KEY_TYPE_CLASS>`**

Key type and class of wrapped key.

Possible values:

- ec-public
- rsa-public

Required: Yes

**`<IMPORT_KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the imported key in the form of
`KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`).
For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

## Related topics

- [The crypto sign category in CloudHSM CLI](cloudhsm_cli-crypto-sign.md "cloudhsm_cli-crypto-sign.md")
- [The crypto verify category in CloudHSM CLI](cloudhsm_cli-crypto-verify.md "cloudhsm_cli-crypto-verify.md")
