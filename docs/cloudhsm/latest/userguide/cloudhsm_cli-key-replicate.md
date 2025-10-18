# Replicate a key with CloudHSM CLI

Use the **key replicate** command in CloudHSM CLI to replicate a key from a
 source AWS CloudHSM cluster to a destination AWS CloudHSM cluster.


## User type


The following types of users can run this command.



* Admins (COs)
* Crypto users (CUs)


###### Note

Crypto Users must own the key to use this command.

## Requirements



* The source and destination clusters must be clones. This means one was created from a backup of the other, or they were both created from a common backup.
 See [Creating clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md") for more information.
* The owner of the key must exist on the destination cluster. Additionally, if the key is shared with any users, those users must also exist on the destination cluster.
* To run this command, you must be logged in as a crypto user or an admin on both the source and destination clusters.




	+ In single command mode, the command will use the CLOUDHSM\_PIN and CLOUDHSM\_ROLE environmental variables to authenticate on the source cluster.
	 See [Single Command mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-single-command "cloudhsm_cli-modes.md#cloudhsm_cli-mode-single-command") for more information.
	 To provide credentials for the destination cluster, you need to set two additional environmental variables: DESTINATION\_CLOUDHSM\_PIN and DESTINATION\_CLOUDHSM\_ROLE:
	
	
	
	```
	`$` `export DESTINATION_CLOUDHSM_ROLE=`<role>``
	```
	
	
	```
	`$` `export DESTINATION_CLOUDHSM_PIN=`<username:password>``
	```
	+ In interactive mode, users will need to explicitly log into both the source and destination clusters.

## Syntax



```
`aws-cloudhsm >` `help key replicate``Replicate a key from a source to a destination cluster

Usage: key replicate --filter [<FILTER>...] --source-cluster-id <SOURCE_CLUSTER_ID> --destination-cluster-id <DESTINATION_CLUSTER_ID>

Options:
 --filter [<FILTER>...]
 Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select matching key on the source cluster
 --source-cluster-id <SOURCE_CLUSTER_ID>
 Source cluster ID
 --destination-cluster-id <DESTINATION_CLUSTER_ID>
 Destination cluster ID
 -h, --help
 Print help`
```

## Examples


###### Example: Replicate key

This command replicates a key from a source cluster with to a cloned destination cluster. The example below demonstrates the output when logged in as a crypto user on both clusters.


```
crypto-user-1@cluster-1234abcdefg > `key replicate \
 --filter attr.label=example-key \
 --source-cluster-id cluster-1234abcdefg \
 --destination-cluster-id cluster-2345bcdefgh``{
 "error_code": 0,
 "data": {
 "key": {
 "key-reference": "0x0000000000300006",
 "key-info": {
 "key-owners": [
 {
 "username": "crypto-user-1",
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
 "label": "example-key",
 "id": "0x",
 "check-value": "0x5e118e",
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
 "never-extractable": true,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": false,
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 16
 }
 },
 "message": "Successfully replicated key"
 }
}`
```

## Arguments




**`<FILTER>`**

Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key on the source cluster.


For a listing of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")


Required: Yes



**`<SOURCE_CLUSTER_ID>`**

The source cluster ID.


Required: Yes



**`<DESTINATION_CLUSTER_ID>`**

The destination cluster ID.


Required: Yes




## Related topics



* [Connecting to multiple clusters with CloudHSM CLI](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")
