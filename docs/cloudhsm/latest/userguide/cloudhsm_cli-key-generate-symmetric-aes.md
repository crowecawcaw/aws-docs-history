# Generate a symmetric AES key with
 CloudHSM CLI

Use the **key generate-symmetric aes** command in CloudHSM CLI to generate a
 symmetric AES key in your AWS CloudHSM cluster.


## User type


The following types of users can run this command.



* Crypto users (CUs)

## Requirements


To run this command, you must be logged in as a CU.


## Syntax



```
`aws-cloudhsm >` `help key generate-symmetric aes``Generate an AES key

Usage: key generate-symmetric aes [OPTIONS] --label `<LABEL>` --key-length-bytes `<KEY_LENGTH_BYTES>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --label `<LABEL>`
 Label for the key
 --session
 Creates a session key that exists only in the current session. The key cannot be recovered after the session ends
 --key-length-bytes `<KEY_LENGTH_BYTES>`
 Key length in bytes
 --attributes [`<KEY_ATTRIBUTES>`...]
 Space separated list of key attributes to set for the generated AES key in the form of KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE
 --share-crypto-users [`<SHARE_CRYPTO_USERS>`...]
 Space separated list of Crypto User usernames to share the AES key with
 --manage-key-quorum-value `<MANAGE_KEY_QUORUM_VALUE>`
 The quorum value for key management operations
 --use-key-quorum-value `<USE_KEY_QUORUM_VALUE>`
 The quorum value for key usage operations
 -h, --help
 Print help`
```

## Examples


These examples show how to use the **key generate-symmetric aes** command to create an AES key.


###### Example: Create an AES key


```
`aws-cloudhsm >` `key generate-symmetric aes \
--label example-aes \
--key-length-bytes 24``{
 "error_code": 0,
 "data": {
 "key": {
 "key-reference": "0x00000000002e06bf",
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
 "key-type": "aes",
 "label": "example-aes",
 "id": "",
 "check-value": "0x9b94bd",
 "class": "secret-key",
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
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 24
 }
 }
 }
}`
```

###### Example: Create an AES key with optional attributes


```
`aws-cloudhsm >` `key generate-symmetric aes \
--label example-aes \
--key-length-bytes 24 \
--attributes decrypt=true encrypt=true``{
 "error_code": 0,
 "data": {
 "key": {
 "key-reference": "0x00000000002e06bf",
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
 "key-type": "aes",
 "label": "example-aes",
 "id": "",
 "check-value": "0x9b94bd",
 "class": "secret-key",
 "encrypt": true,
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
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 24
 }
 }
 }
}`
```

###### Example: Create an AES key with quorum values

When generating a key with quorum controls, the key must be associated with a minimum number of users equal to the largest key quorum value. 
 Associated users include the key owner and Crypto Users with whom the key is shared with. To determine the number of minimum users to share the key with, 
 get the largest quorum value between the key usage quorum value and the key management quorum value and subtract 1 to account for the key owner, 
 who is by default associated with the key. To share the key with more users, use 
 the **[Share a key using CloudHSM CLI](cloudhsm_cli-key-share.md "cloudhsm_cli-key-share.md")** command.


```
`aws-cloudhsm >` `key generate-symmetric aes \
--label example-aes \
--key-length-bytes 24 \
--attributes decrypt=true encrypt=true
--share-crypto-users cu2 cu3 cu4 \
--manage-key-quorum-value 4 \
--use-key-quorum-value 2``{
 "error_code": 0,
 "data": {
 "key": {
 "key-reference": "0x00000000002e06bf",
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
 "key-type": "aes",
 "label": "example-aes",
 "id": "",
 "check-value": "0x9b94bd",
 "class": "secret-key",
 "encrypt": true,
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
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 24
 }
 }
 }
}`
```

## Arguments




**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.


Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")



**`<KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated AES key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`).


For a list of supported key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").


Required: No



**`<KEY-LENGTH-BYTES>`**

Specifies the key length in bytes.


Valid values:


* 16, 24, and 32

Required: Yes



**`<LABEL>`**

Specifies a user defined label for the AES key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.


Required: Yes



**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends.


Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key. Do not use a session key to encrypt data that you might need to decrypt after the session ends.


By default, keys that are generated are persistent (token) keys. Passing in <SESSION> changes this, ensuring a key generated with this argument is a session (ephemeral) key.


Required: No



**`<SHARE_CRYPTO_USERS>`**

Specifies a space separated list of Crypto User usernames to share the AES key with


Required: No



**`<MANAGE_KEY_QUORUM_VALUE>`**

The quorum value for key management operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared with and the key owner. Max value of 8.


Required: No



**`<USE_KEY_QUORUM_VALUE>`**

The quorum value for key usage operations. This value must be less than or equal to the number of users that the key is associated with. This includes users with whom the key is shared with and the key owner. Max value of 8.


Required: No




## Related topics



* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
* [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
