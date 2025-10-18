# Delete a key with CloudHSM CLI

Use the **key delete** command in CloudHSM CLI to delete a key from an AWS CloudHSM cluster. You can only delete one key at a time. 
 Deleting one key in a key pair has no effect on the other key in the pair. 

Only the CU who created the key and consequently owns it can delete the key. Users who share the key, but do not own it, can use the key in cryptographic operations, but can not delete it.


## User type


The following types of users can run this command.



* Crypto users (CUs)

## Requirements



* To run this command, you must be logged in as a CU.

## Syntax



```
`aws-cloudhsm >` `help key delete``Delete a key in the HSM cluster

Usage: key delete [OPTIONS] --filter [`<FILTER>`...]

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --filter [`<FILTER>`...] Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key for deletion
 -h, --help Print help`
```

## Example



```
`aws-cloudhsm >` `key delete --filter attr.label="ec-test-public-key"``{
 "error_code": 0,
 "data": {
 "message": "Key deleted successfully"
 }
}`
```

## Arguments




**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.


Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")



**`<FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key for deletion.


For a list of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")


Required: Yes




## Related topics



* [List keys for a user with CloudHSM CLI](cloudhsm_cli-key-list.md "cloudhsm_cli-key-list.md")
* [Export an asymmetric key with
 CloudHSM CLI](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md")
* [Unshare a key using CloudHSM CLI](cloudhsm_cli-key-unshare.md "cloudhsm_cli-key-unshare.md")
* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
* [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md "manage-keys-cloudhsm-cli-filtering.md")
