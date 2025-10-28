# Share a key using CloudHSM CLI

Use the **key share** command in CloudHSM CLI to share a key with other CUs in
your AWS CloudHSM cluster.

Only the CU who created the key and consequently owns it can share the key. Users with whom a key is shared can use the key in cryptographic operations,
but they cannot delete, export, share, or unshare the key. Additionally, these users cannot change [key attributes](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help key share``Share a key in the HSM cluster with another user

Usage: key share --filter [`<FILTER>`...] --username `<USERNAME>` --role `<ROLE>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --filter [`<FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key for sharing

 --username `<USERNAME>`
 A username with which the key will be shared

 --role `<ROLE>`
 Role the user has in the cluster

 Possible values:
 - crypto-user: A CryptoUser has the ability to manage and use keys
 - admin: An Admin has the ability to manage user accounts

 --approval `<APPROVAL>`
 Filepath of signed quorum token file to approve operation

 -h, --help
 Print help (see a summary with '-h')`
```

## Example: Share a key with another CU

The following example shows how to use the **key share** command to share a key with the CU `alice`.

1. Run the **key share** command to share the key with `alice`.

```
`aws-cloudhsm >` `key share --filter attr.label="rsa_key_to_share" attr.class=private-key --username alice --role crypto-user``{
 "error_code": 0,
 "data": {
 "message": "Key shared successfully"
 }
}`
```

2. Run the **key list** command.

```
`aws-cloudhsm >` `key list --filter attr.label="rsa_key_to_share" attr.class=private-key --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000001c0686",
 "key-info": {
 "key-owners": [
 {
 "username": "cu3",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "cu2",
 "key-coverage": "full"
 },
 {
 "username": "cu1",
 "key-coverage": "full"
 },
 {
 "username": "cu4",
 "key-coverage": "full"
 },
 {
 "username": "cu5",
 "key-coverage": "full"
 },
 {
 "username": "cu6",
 "key-coverage": "full"
 },
 {
 "username": "cu7",
 "key-coverage": "full"
 },
 {
 "username": "alice",
 "key-coverage": "full"
 }
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "rsa_key_to_share",
 "id": "",
 "check-value": "0xae8ff0",
 "class": "private-key",
 "encrypt": false,
 "decrypt": true,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": false,
 "unwrap": true,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1219,
 "public-exponent": "0x010001",
 "modulus": "0xa8855cba933cec0c21a4df0450ec31675c024f3e65b2b215a53d2bda6dcd191f75729150b59b4d86df58254c8f518f7d000cc04d8e958e7502c7c33098e28da4d94378ef34fb57d1cc7e042d9119bd79be0df728421a980a397095157da24cf3cc2b6dab12225d33fdca11f0c6ed1a5127f12488cda9a556814b39b06cd8373ff5d371db2212887853621b8510faa7b0779fbdec447e1f1d19f343acb02b22526487a31f6c704f8f003cb4f7013136f90cc17c2c20e414dc1fc7bcfb392d59c767900319679fc3307388633485657ce2e1a3deab0f985b0747ef4ed339de78147d1985d14fdd8634219321e49e3f5715e79c298f18658504bab04086bfbdcd3b",
 "modulus-size-bits": 2048
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```

3. In the above list, verify `alice` is in the list of `shared-users`

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key for deletion.

For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: Yes

**`<USERNAME>`**

Specifies a friendly name for the user. The maximum length is 31 characters. The only special character permitted is an underscore ( \_ ).
The username is not case sensitive in this command, username is always displayed in lowercase.

Required: Yes

**`<ROLE>`**

Specifies the role assigned to this user. This parameter is required.
To get the user’s role, use the user list command. For detailed information about the user types on an HSM, see [HSM user types for CloudHSM CLI](understanding-users.md "understanding-users.md").

Required: Yes

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if the key management service quorum value of the key is greater than 1.

## Related topics

- [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
- [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
