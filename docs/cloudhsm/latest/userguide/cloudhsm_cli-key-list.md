# List keys for a user with CloudHSM CLI

Use the **key list** command in CloudHSM CLI to find all keys for the current
 user present in your AWS CloudHSM cluster. The output includes keys that the user owns and shares, as
 well as all public keys in the CloudHSM cluster.


## User type


The following types of users can run this command.



* Admins (COs)
* Crypto users (CUs)

## Syntax



```
`aws-cloudhsm >` `help key list``List the keys the current user owns, shares, and all public keys in the HSM cluster

Usage: key list [OPTIONS]

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --filter [`<FILTER>`...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select matching key(s) to list
 --max-items `<MAX_ITEMS>`
 The total number of items to return in the command's output. If the total number of items available is more than the value specified, a next-token is provided in the command's output. To resume pagination, provide the next-token value in the starting-token argument of a subsequent command [default: 10]
 --starting-token `<STARTING_TOKEN>`
 A token to specify where to start paginating. This is the next-token from a previously truncated response
 -v, --verbose
 If included, prints all attributes and key information for each matched key. By default each matched key only displays its key-reference and label attribute. This flag when used by Admins has no effect
 -h, --help
 Print help`
```

## Examples


The following examples show the different ways you run the **key list** command. The following examples show the outputs as a crypto user.


###### Example: Find all keys – default

This command lists the keys of the logged in user present in the AWS CloudHSM cluster.

###### Note

By default, only 10 keys of the currently logged in user are displayed, and only the `key-reference` and `label` are displayed as output. 
 Use the appropriate pagination options to display more or less keys as output.


```
`aws-cloudhsm >` `key list``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000000003d5",
 "attributes": {
 "label": "test_label_1"
 }
 },
 {
 "key-reference": "0x0000000000000626",
 "attributes": {
 "label": "test_label_2"
 }
 },.
 ...8 keys later...
 ],
 "total_key_count": 56,
 "returned_key_count": 10,
 "next_token": "10"
 }
}`
```

###### Example: Find all keys – verbose

The output includes keys that the user owns and shares, as well as all public keys in the HSMs.

###### Note

Note: By default, only 10 keys of the currently logged in user are displayed. Use the appropriate pagination options to display more or less keys as output.


```
`aws-cloudhsm >` `key list --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
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
 "label": "ec-test-private-key",
 "id": "",
 "check-value": "0x2a737d",
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
 "ec-point": "0x0442d53274a6c0ec1a23c165dcb9ccdd72c64e98ae1a9594bb5284e752c746280667e11f1e983493c1c605e0a8071ede47ca280f94c6b2aa33",
 "curve": "secp224r1"
 }
 },
 {
 "key-reference": "0x000000000012000d",
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
 "label": "ec-test-public-key",
 "id": "",
 "check-value": "0x2a737d",
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
 "ec-point": "0x0442d53274a6c0ec1a23c165dcb9ccdd72c64e98ae1a9594bb5284e752c746280667e11f1e983493c1c605e0a8071ede47ca280f94c6b2aa33",
 "curve": "secp224r1"
 }
 }
 ],
 ...8 keys later...
 "total_key_count": 1580,
 "returned_key_count": 10
 }
}`
```

###### Example: Paginated return

The following example displays a paginated subset of the keys which shows only two keys. The example then provides a subsequent call to display the next two keys.


```
`aws-cloudhsm >` `key list --verbose --max-items 2``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000000030",
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
 "label": "98a6688d1d964ed7b45b9cec5c4b1909",
 "id": "",
 "check-value": "0xb28a46",
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
 "key-length-bytes": 32
 }
 },
 {
 "key-reference": "0x0000000000000042",
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
 "label": "4ad6cdcbc02044e09fa954143efde233",
 "id": "",
 "check-value": "0xc98104",
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
 "unwrap": true,
 "verify": true,
 "wrap": true,
 "wrap-with-trusted": false,
 "key-length-bytes": 16
 }
 }
 ],
 "total_key_count": 1580,
 "returned_key_count": 2,
 "next_token": "2"
 }
}`
```
To display the next 2 keys, a subsequent call can be made:


```
`aws-cloudhsm >` `key list --verbose --max-items 2 --starting-token 2``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000000081",
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
 "label": "6793b8439d044046982e5b895791e47f",
 "id": "",
 "check-value": "0x3f986f",
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
 "key-length-bytes": 32
 }
 },
 {
 "key-reference": "0x0000000000000089",
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
 "label": "56b30fa05c6741faab8f606d3b7fe105",
 "id": "",
 "check-value": "0xe9201a",
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
 "key-length-bytes": 32
 }
 }
 ],
 "total_key_count": 1580,
 "returned_key_count": 2,
 "next_token": "4"
 }
}`
```
For more examples that demonstrate how the key filtration mechanism works in the CloudHSM CLI, see [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md").


## Arguments




**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.


Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")



**`<FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select matching key(s) to list.


For a listing of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")


Required: No



**`<MAX_ITEMS>`**

The total number of items to return in the command's output. If the total number of items available is more than the value specified, a next-token is provided in the command's output. 
 To resume pagination, provide the next-token value in the starting-token argument of a subsequent command.


Required: No



**`<STARTING_TOKEN>`**

A token to specify where to start paginating. This is the next-token from a previously truncated response.


Required: No



**`<VERBOSE>`**

If included, prints all attributes and key information for each matched key. By default each matched key only displays its key-reference and label attribute. This flag when used by Admins has no effect.


Required: No




## Related topics



* [Delete a key with CloudHSM CLI](cloudhsm_cli-key-delete.md "cloudhsm_cli-key-delete.md")
* [Export an asymmetric key with
 CloudHSM CLI](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md")
* [Unshare a key using CloudHSM CLI](cloudhsm_cli-key-unshare.md "cloudhsm_cli-key-unshare.md")
* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
* [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
