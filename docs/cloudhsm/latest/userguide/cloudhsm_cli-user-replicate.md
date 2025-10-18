# Replicate a user with CloudHSM CLI

Use the **user replicate** command in CloudHSM CLI to replicate a user from a
 source AWS CloudHSM cluster to a destination AWS CloudHSM cluster.


## User type


The following types of users can run this command.



* Admins (COs)

## Requirements



* The source and destination clusters must be clones. This means one was created from a backup of the other, or they were both created from a common backup.
 See [Creating clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md") for more information.
* To run this command, you must be logged in as an admin on both the source and destination clusters.




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
`aws-cloudhsm >` `help user replicate``Replicate a user from a source to a destination cluster

Usage: user replicate --username `<USERNAME>` --role `<ROLE>` --source-cluster-id `<SOURCE_CLUSTER_ID>` --destination-cluster-id `<DESTINATION_CLUSTER_ID>`

Options:
 --username `<USERNAME>`
 Username of the user to replicate

 --role `<ROLE>`
 Role the user has in the cluster

 Possible values:
 - crypto-user: A CryptoUser has the ability to manage and use keys
 - admin: An Admin has the ability to manage user accounts

 --source-cluster-id `<SOURCE_CLUSTER_ID>`
 Source cluster ID

 --destination-cluster-id `<DESTINATION_CLUSTER_ID>`
 Destination cluster ID

 -h, --help
 Print help (see a summary with '-h')`
```

## Examples


###### Example: Replicate user

This command replicates a user from a source cluster with to a cloned destination cluster. The example below demonstrates the output when logged in as an admin on both clusters.


```
admin-user@cluster-1234abcdefg > `user replicate \
 --username example-admin \
 --role admin \
 --source-cluster-id cluster-1234abcdefg \
 --destination-cluster-id cluster-2345bcdefgh``{
 "error_code": 0,
 "data": {
 "user": {
 "username": "example-admin",
 "role": "admin",
 "locked": "false",
 "mfa": [],
 "quorum": [],
 "cluster-coverage": "full"
 },
 "message": "Successfully replicated user"
 }
}`
```

## Arguments




**`<USERNAME>`**

Specifies the username of the user to replicate in the source cluster.


Required: Yes



**`<ROLE>`**

Specifies the role assigned to this user. This parameter is required. 
 Valid values are **admin**, **crypto-user**.


To get the user’s role, use the **user list** command. For detailed information about the user types on an HSM, see [Understanding HSM users](manage-hsm-users.md "manage-hsm-users.md").


Required: Yes



**`<SOURCE_CLUSTER_ID>`**

The source cluster ID.


Required: Yes



**`<DESTINATION_CLUSTER_ID>`**

The destination cluster ID.


Required: Yes




## Related topics



* [Connecting to multiple clusters with CloudHSM CLI](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")
