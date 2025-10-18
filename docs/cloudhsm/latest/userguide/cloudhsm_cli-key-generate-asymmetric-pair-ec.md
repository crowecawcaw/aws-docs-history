# Generate an asymmetric EC key
 pair with CloudHSM CLI

Use the **key asymmetric-pair ec** command in CloudHSM CLI to generate an asymmetric Elliptic-curve (EC) key pair in your AWS CloudHSM cluster.


## User type


The following types of users can run this command.



* Crypto users (CUs)

## Requirements


To run this command, you must be logged in as a CU.


## Syntax



```
`aws-cloudhsm >` `help key generate-asymmetric-pair ec``Generate an Elliptic-Curve Cryptography (ECC) key pair

Usage: key generate-asymmetric-pair ec [OPTIONS] --public-label `<PUBLIC_LABEL>` --private-label `<PRIVATE_LABEL>` --curve `<CURVE>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --public-label `<PUBLIC_LABEL>`
 Label for the public key
 --private-label `<PRIVATE_LABEL>`
 Label for the private key
 --session
 Creates a session key pair that exists only in the current session. The key cannot be recovered after the session ends
 --curve `<CURVE>`
 Elliptic curve used to generate the key pair [possible values: prime256v1, secp256r1, secp224r1, secp384r1, secp256k1, secp521r1]
 --public-attributes [`<PUBLIC_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated EC public key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --private-attributes [`<PRIVATE_KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated EC private key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --share-crypto-users [`<SHARE_CRYPTO_USERS>`...]
 Space separated list of Crypto User usernames to share the EC private key with
 --manage-private-key-quorum-value `<MANAGE_PRIVATE_KEY_QUORUM_VALUE>`
 The quorum value for key management operations for the private key
 --use-private-key-quorum-value `<USE_PRIVATE_KEY_QUORUM_VALUE>`
 The quorum value for key usage operations for the private key
 -h, --help
 Print help`
```

## Examples


These examples show how to use the **key generate-asymmetric-pair ec** command to create an EC key pair.


###### Example: Create an EC key pair


```
`aws-cloudhsm >` `key generate-asymmetric-pair ec \
 --curve secp224r1 \
 --public-label ec-public-key-example \
 --private-label ec-private-key-example``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x000000000012000b",
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
 "key-type": "ec",
 "label": "ec-public-key-example",
 "id": "",
 "check-value": "0xd7c1a7",
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
 "key-length-bytes": 57,
 "ec-point": "0x047096513df542250a6b228fd9cb67fd0c903abc93488467681974d6f371083fce1d79da8ad1e9ede745fb9f38ac8622a1b3ebe9270556000c",
 "curve": "secp224r1"
 }
 },
"private_key": {
 "key-reference": "0x000000000012000c",
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
 "key-type": "ec",
 "label": "ec-private-key-example",
 "id": "",
 "check-value": "0xd7c1a7",
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
 "key-length-bytes": 122,
 "ec-point": "0x047096513df542250a6b228fd9cb67fd0c903abc93488467681974d6f371083fce1d79da8ad1e9ede745fb9f38ac8622a1b3ebe9270556000c",
 "curve": "secp224r1"
 }
 }
 }
}`
```

###### Example: Create an EC key pair with optional attributes


```
`aws-cloudhsm >` `key generate-asymmetric-pair ec \
 --curve secp224r1 \
 --public-label ec-public-key-example \
 --private-label ec-private-key-example \
 --public-attributes encrypt=true \
 --private-attributes decrypt=true``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x00000000002806eb",
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
 "key-type": "ec",
 "label": "ec-public-key-example",
 "id": "",
 "check-value": "0xedef86",
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
 "key-length-bytes": 57,
 "ec-point": "0x0487af31882189ec29eddf17a48e8b9cebb075b7b5afc5522fe9c83a029a450cc68592889a1ebf45f32240da5140d58729ffd7b2d44262ddb8",
 "curve": "secp224r1"
 }
 },
 "private_key": {
 "key-reference": "0x0000000000280c82",
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
 "key-type": "ec",
 "label": "ec-private-key-example",
 "id": "",
 "check-value": "0xedef86",
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
 "key-length-bytes": 122,
 "ec-point": "0x0487af31882189ec29eddf17a48e8b9cebb075b7b5afc5522fe9c83a029a450cc68592889a1ebf45f32240da5140d58729ffd7b2d44262ddb8",
 "curve": "secp224r1"
 }
 }
 }
}`
```

###### Example: Create an EC key pair with quorum values

When generating a key with quorum controls, the key must be associated with a minimum number of users equal to the largest key quorum value. 
 Associated users include the key owner and Crypto Users with whom the key is shared with. To determine the number of minimum users to share the key with, 
 get the largest quorum value between the key usage quorum value and the key management quorum value and subtract 1 to account for the key owner, 
 who is by default associated with the key. To share the key with more users, use 
 the **[Share a key using CloudHSM CLI](cloudhsm_cli-key-share.md "cloudhsm_cli-key-share.md")** command.


```
`aws-cloudhsm >` `key generate-asymmetric-pair ec \
 --curve secp224r1 \
 --public-label ec-public-key-example \
 --private-label ec-private-key-example \
 --public-attributes verify=true \
 --private-attributes sign=true
 --share-crypto-users cu2 cu3 cu4 \
 --manage-private-key-quorum-value 4 \
 --use-private-key-quorum-value 2``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x00000000002806eb",
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
 "key-type": "ec",
 "label": "ec-public-key-example",
 "id": "",
 "check-value": "0xedef86",
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
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 57,
 "ec-point": "0x0487af31882189ec29eddf17a48e8b9cebb075b7b5afc5522fe9c83a029a450cc68592889a1ebf45f32240da5140d58729ffd7b2d44262ddb8",
 "curve": "secp224r1"
 }
 },
 "private_key": {
 "key-reference": "0x0000000000280c82",
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
 "key-type": "ec",
 "label": "ec-private-key-example",
 "id": "",
 "check-value": "0xedef86",
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
 "key-length-bytes": 122,
 "ec-point": "0x0487af31882189ec29eddf17a48e8b9cebb075b7b5afc5522fe9c83a029a450cc68592889a1ebf45f32240da5140d58729ffd7b2d44262ddb8",
 "curve": "secp224r1"
 }
 }
 }
}`
```

## Arguments




**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.


Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")



**`<CURVE>`**

Specifies the identifier for the elliptic curve.



* prime256v1
* secp256r1
* secp224r1
* secp384r1
* secp256k1
* secp521r1

Required: Yes



**`<PUBLIC_KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated EC public key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `verify=true`)


For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").


Required: No



**`<PUBLIC_LABEL>`**

Specifies a user defined label for the public-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.


Required: Yes



**`<PRIVATE_KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated EC private key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`)


For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").


Required: No



**`<PRIVATE_LABEL>`**

Specifies a user defined label for the private-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.


Required: Yes



**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends.


Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key. Do not use a session key to encrypt data that you might need to decrypt after the session ends.


By default, keys that are generated are persistent (token) keys. Passing in <SESSION> changes this, ensuring a key generated with this argument is a session (ephemeral) key.


Required: No



**`<SHARE_CRYPTO_USERS>`**

Specifies a space separated list of Crypto User usernames to share the EC private key with


Required: No



**`<MANAGE_PRIVATE_KEY_QUORUM_VALUE>`**

The quorum value for the private key's key management operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared with and the key owner. Max value of 8.


Required: No



**`<USE_PRIVATE_KEY_QUORUM_VALUE>`**

The quorum value for private key's key usage operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared with and the key owner. Max value of 8.


Required: No




## Related topics



* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
* [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
