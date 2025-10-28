# Generate an asymmetric RSA key

pair with CloudHSM CLI

Use the **key generate-asymmetric-pair rsa** command in CloudHSM CLI to
generate an asymmetric RSA key pair in your AWS CloudHSM cluster.

## User type

The following types of users can run this command.

- Crypto users (CUs)

## Requirements

To run this command, you must be logged in as a CU.

## Syntax

```
`aws-cloudhsm >` `help key generate-asymmetric-pair rsa``Generate an RSA key pair

Usage: key generate-asymmetric-pair rsa [OPTIONS] --public-label `<PUBLIC_LABEL>` --private-label `<PRIVATE_LABEL>` --modulus-size-bits `<MODULUS_SIZE_BITS>` --public-exponent `<PUBLIC_EXPONENT>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --public-label `<PUBLIC_LABEL>`
 Label for the public key
 --private-label `<PRIVATE_LABEL>`
 Label for the private key
 --session
 Creates a session key pair that exists only in the current session. The key cannot be recovered after the session ends
 --modulus-size-bits `<MODULUS_SIZE_BITS>`
 Modulus size in bits used to generate the RSA key pair
 --public-exponent `<PUBLIC_EXPONENT>`
 Public exponent used to generate the RSA key pair
 --public-attributes [`<PUBLIC_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated RSA public key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --private-attributes [`<PRIVATE_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated RSA private key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --share-crypto-users [`<SHARE_CRYPTO_USERS>`...]
 Space separated list of Crypto User usernames to share the RSA key with
 --manage-private-key-quorum-value `<MANAGE_PRIVATE_KEY_QUORUM_VALUE>`
 The quorum value for key management operations for the private key
 --use-private-key-quorum-value `<USE_PRIVATE_KEY_QUORUM_VALUE>`
 The quorum value for key usage operations for the private key
 -h, --help
 Print help`
```

## Examples

These examples show how to use `key generate-asymmetric-pair rsa` to create a RSA key pair.

###### Example: Create an RSA key pair

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
--public-exponent 65537 \
--modulus-size-bits 2048 \
--public-label rsa-public-key-example \
--private-label rsa-private-key-example``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x0000000000160010",
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
 "label": "rsa-public-key-example",
 "id": "",
 "check-value": "0x498e1f",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
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
 "modulus": "0xdfca0669dc8288ed3bad99509bd21c7e6192661407021b3f4cdf4a593d939dd24f4d641af8e4e73b04c847731c6dbdff3385818e08dd6efcbedd6e5b130344968c
e89a065e7d1a46ced96b46b909db2ab6be871ee700fd0a448b6e975bb64cae77c49008749212463e37a577baa57ce3e574cb057e9db131e119badf50c938f26e8a5975c61a8ba7ffe7a1115a
bcebb7d20bd6df1948ae336ae23b52d73b7f3b6acc2543edb6358e08d326d280ce489571f4d34e316a2ea1904d513ca12fa04075fc09ad005c81b7345d7804ff24c45117f0a1020dca7794df037a10aadec8653473b2088711f7b7d8b58431654e14e31af0e00511da641058fb7475ffdbe60f",
 "modulus-size-bits": 2048
 }
 },
"private_key": {
 "key-reference": "0x0000000000160011",
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
 "label": "rsa-private-key-example",
 "id": "",
 "check-value": "0x498e1f",
 "class": "private-key",
 "encrypt": false,
 "decrypt": false,
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
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1217,
 "public-exponent": "0x010001",
 "modulus": "0xdfca0669dc8288ed3bad99509bd21c7e6192661407021b3f4cdf4a593d939dd24f4d641af8e4e73b04c847731c6dbdff3385818e08dd6efcbedd6e5b130344968ce89a065e7d1a46ced96b46b909db2ab6be871ee700fd0a448b6e975bb64cae77c49008749212463e37a577baa57ce3e574cb057e9db131e119badf50c938f26e8a5975c61a8ba7ffe7a1115abcebb7d20bd6df1948ae336ae23b52d73b7f3b6acc2543edb6358e08d326d280ce489571f4d34e316a2ea1904d513ca12fa04075fc09ad005c81b7345d7804ff24c45117f0a1020dca7794df037a10aadec8653473b2088711f7b7d8b58431654e14e31af0e00511da641058fb7475ffdbe60f",
 "modulus-size-bits": 2048
 }
 }
 }
}`
```

###### Example: Create an RSA key pair with optional attributes

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
--public-exponent 65537 \
--modulus-size-bits 2048 \
--public-label rsa-public-key-example \
--private-label rsa-private-key-example \
--public-attributes encrypt=true \
--private-attributes decrypt=true``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x0000000000280cc8",
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
 "label": "rsa-public-key-example",
 "id": "",
 "check-value": "0x01fe6e",
 "class": "public-key",
 "encrypt": true,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
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
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c
73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634d
f6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc
133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0ac
ac3160f0ca9725d38318b7",
 "modulus-size-bits": 2048
 }
 },
 "private_key": {
 "key-reference": "0x0000000000280cc7",
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
 "label": "rsa-private-key-example",
 "id": "",
 "check-value": "0x01fe6e",
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
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1217,
 "public-exponent": "0x010001",
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634df6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0acac3160f0ca9725d38318b7",
 "modulus-size-bits": 2048
 }
 }
 }
}`
```

###### Example: Create an RSA key pair with quorum values

When generating a key with quorum controls, the key must be associated with a minimum number of users equal to the largest key quorum value.
Associated users include the key owner and Crypto Users with whom the key is shared with. To determine the number of minimum users to share the key with,
get the largest quorum value between the key usage quorum value and the key management quorum value and subtract 1 to account for the key owner,
who is by default associated with the key. To share the key with more users, use
the **[Share a key using CloudHSM CLI](cloudhsm_cli-key-share.md "cloudhsm_cli-key-share.md")** command.

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
--public-exponent 65537 \
--modulus-size-bits 2048 \
--public-label rsa-public-key-example \
--private-label rsa-private-key-example \
--public-attributes verify=true \
--private-attributes sign=true
--share-crypto-users cu2 cu3 cu4 \
--manage-private-key-quorum-value 4 \
--use-private-key-quorum-value 2``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x0000000000280cc8",
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
 "label": "rsa-public-key-example",
 "id": "",
 "check-value": "0x01fe6e",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": false,
 "sign": true,
 "trusted": false,
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 512,
 "public-exponent": "0x010001",
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c
73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634d
f6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc
133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0ac
ac3160f0ca9725d38318b7",
 "modulus-size-bits": 2048
 }
 },
 "private_key": {
 "key-reference": "0x0000000000280cc7",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "cu2",
 "key-coverage": "full"
 },
 {
 "username": "cu3",
 "key-coverage": "full"
 },
 {
 "username": "cu4",
 "key-coverage": "full"
 },
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 4,
 "use-key-quorum-value": 2
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "rsa-private-key-example",
 "id": "",
 "check-value": "0x01fe6e",
 "class": "private-key",
 "encrypt": false,
 "decrypt": false,
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
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1217,
 "public-exponent": "0x010001",
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634df6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0acac3160f0ca9725d38318b7",
 "modulus-size-bits": 2048
 }
 }
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<MODULUS_SIZE_BITS>`**

Specifies the length of the modulus in bits. The minimum value is 2048.

Required: Yes

**`<PRIVATE_KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated RSA private key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`)

For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<PRIVATE_LABEL>`**

Specifies a user defined label for the private-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.

Required: Yes

**`<PUBLIC_EXPONENT>`**

Specifies the public exponent. The value must be an odd number greater than or equal to 65537.

Required: Yes

**`<PUBLIC_KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated RSA public key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `verify=true`)

For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<PUBLIC_LABEL>`**

Specifies a user defined label for the public-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.

Required: Yes

**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends.

Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key. Do not use a session key to encrypt data that you might need to decrypt after the session ends.

By default, keys that are generated are persistent (token) keys. Passing in <SESSION> changes this, ensuring a key generated with this argument is a session (ephemeral) key.

Required: No

**`<SHARE_CRYPTO_USERS>`**

Specifies a space separated list of Crypto User usernames to share the RSA private key with

Required: No

**`<MANAGE_PRIVATE_KEY_QUORUM_VALUE>`**

The quorum value for the private key's key management operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared with and the key owner. Max value of 8.

Required: No

**`<USE_PRIVATE_KEY_QUORUM_VALUE>`**

The quorum value for private key's key usage operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared with and the key owner. Max value of 8.

Required: No

## Related topics

- [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
- [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
