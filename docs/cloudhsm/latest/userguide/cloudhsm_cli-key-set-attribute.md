# Set the attributes of keys with

CloudHSM CLI

Use the **key set-attribute** command in CloudHSM CLI to set the attributes of
keys in your AWS CloudHSM cluster. Only the CU who created the key and consequently owns it can change
the key's attributes.

For a list of key attributes that can be used in CloudHSM CLI, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

## User type

The following types of users can run this command.

- Crypto users (CUs) can run this command.
- Admins can set the trusted attribute.

## Requirements

To run this command, you must be logged in as a CU. To set the trusted attribute, you must be logged in as an admin user.

## Syntax

```
`aws-cloudhsm >` `help key set-attribute``Set an attribute for a key in the HSM cluster

Usage: cloudhsm-cli key set-attribute [OPTIONS] --filter [`<FILTER>`...] --name `<KEY_ATTRIBUTE>` --value `<KEY_ATTRIBUTE_VALUE>`

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --filter [`<FILTER>`...] Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key to modify
 --name `<KEY_ATTRIBUTE>` Name of attribute to be set
 --value `<KEY_ATTRIBUTE_VALUE>`... Attribute value to be set
 --approval `<APPROVAL>` Filepath of signed quorum token file to approve operation
 -h, --help Print help`
```

## Example: Setting a key attribute

The following example shows how to use the **key set-attribute** command to set the label.

###### Example

1. Use the key with the label `my_key`, as shown here:

```
`aws-cloudhsm >` `key set-attribute --filter attr.label=my_key --name encrypt --value false``{
 "error_code": 0,
 "data": {
 "message": "Attribute set successfully"
 }
}`
```

2. Use the **key list** command to confirm the `encrypt` attribute has changed:

```
`aws-cloudhsm >` `key list --filter attr.label=my_key --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x00000000006400ec",
 "key-info": {
 "key-owners": [
 {
 "username": "bob",
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
 "label": "my_key",
 "id": "",
 "check-value": "0x6bd9f7",
 "class": "secret-key",
 "encrypt": false,
 "decrypt": true,
 "token": true,
 "always-sensitive": true,
 "derive": true,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": true,
 "unwrap": true,
 "verify": true,
 "wrap": true,
 "wrap-with-trusted": false,
 "key-length-bytes": 32
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<KEY_ATTRIBUTE>`**

Specifies the name of the key's attribute.

Required: Yes

**`<FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key for deletion.

For a listing of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")

Required: No

**`<KEY_ATTRIBUTE_VALUE>`**

Specifies the value of the key's attribute.

Required: Yes

**`<KEY_REFERENCE>`**

A hexadecimal or decimal representation of the key. (such as a key handle).

Required: No

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if the key management service quorum value of the key is greater than 1.

## Related topics

- [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
- [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
