# Migrating from hsm1.medium to hsm2m.medium

You can migrate your AWS CloudHSM cluster from hsm1.medium to hsm2m.medium. This topic describes
 the prerequisites, migration process, and rollback procedures.

Before starting the migration, make sure your application follows the recommendations in [Architect your cluster for high availability](bp-cluster-management.md#bp-high-availability "bp-cluster-management.md#bp-high-availability").
 This helps avoid downtime during the process.


## Overview of the hsm1.medium to hsm2m.medium migration process


You can start the migration using the AWS CloudHSM Console, the AWS CLI, or the AWS CloudHSM API. No
 matter where you initiate it, the AWS CloudHSM cluster migration uses the
 `modify-cluster` API endpoint. Once the migration starts, your entire cluster
 enters a limited-write mode. For more information, see [Cluster limited-write mode](#migration-limited-write-mode "#migration-limited-write-mode").


To minimize impact, AWS CloudHSM changes HSMs from hsm1.medium to hsm2m.medium one at a time. The replacement HSMs maintain the same IP addresses, 
 thereby requiring no configuration changes during or after migration.


Here's how the migration works:



1. Before migrating the first HSM, AWS CloudHSM creates a full backup of the entire
 cluster.
2. Using this backup, AWS CloudHSM creates a new HSM of the requested type
 (hsm2m.medium) to replace the first HSM.
3. Before migrating each subsequent HSM, AWS CloudHSM creates a new full backup of the
 entire cluster.
4. AWS CloudHSM repeats steps 3 and 4 for each HSM in the cluster, migrating one HSM at
 a time.
5. Each individual HSM migration takes approximately 30 minutes.

AWS CloudHSM monitors cluster health and performs validations throughout the migration
 process. If AWS CloudHSM detects an increase in errors or a validation check fails, it will
 automatically stop the migration and revert the cluster to its original HSM type. You
 can also roll back manually for up to 24 hours after starting the migration. Before
 rolling back, see [HSM type rollback
 considerations](#rollback-migration "#rollback-migration").


## Prerequisites for migrating to hsm2m.medium


Your existing AWS CloudHSM cluster must meet these requirements to migrate to hsm2m.medium. If any condition isn't met during validation checks,
 AWS CloudHSM automatically reverts the cluster to its original HSM type.


For a list of known migration issues, see [Known issues for AWS CloudHSM cluster modification](ki-cluster-modification.md "ki-cluster-modification.md")



* In the last 7 days:




	+ All client connections have used SDK 5.9 or higher.
	
	
	
	
		- If performing ECDSA Verify, all client connections have used SDK 5.13 or higher.
	+ AWS CloudHSM instances have used only supported (and none of the deprecated)
	 functionalities. See [Deprecation
	 notifications](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details.
	+ You must have used an SDK to connect with at least one HSM in the cluster in the past 7 days.
* The cluster is in an ACTIVE state.
* The cluster has 27 HSMs or fewer.
* The error rate for HSM operations doesn't increase during migration.

###### Note

The previous restriction which prevented customers with token key workloads from migrating has been removed.


## Cluster limited-write mode


When you start the cluster migration, it enters a limited-write mode. Operations that can change the HSM state are rejected. All read operations remain unaffected.


During migration, your application receives an error from the HSM when attempting these operations:



* Token key generation and deletion (session key workloads continue to operate).
* All user creation, deletion, or modification.
* Quorum operations.
* Modification of keys within the HSM, such as changing key attributes.
* mTLS registration.

AWS CloudHSM also places your cluster in a `MODIFY_IN_PROGRESS` state during migration. 
 During this time, you can't add or remove HSMs from the cluster.


## Starting the migration


The cluster migration process replaces individual HSMs in your cluster one at a time.
 The duration depends on the number of HSMs in your cluster. On average, this process takes 
 about 30 minutes per HSM. You can track progress by monitoring the HSM type of individual HSMs
 in the cluster to see how many have been migrated to the new type.



Console
###### To change the HSM type (console)

1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Select the radio button next to the ID of the cluster you want to change
3. From the Actions menu, choose `Modify HSM Type` and select the desired HSM type

This procedure puts your cluster into the `MODIFY_IN_PROGRESS` state. After migration,
 your cluster returns to the `ACTIVE` state.



AWS CLI
###### To change the HSM type ([AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/ "https://docs.aws.amazon.com/cli/latest/userguide/"))

* At a command prompt, run the **[modify-cluster](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/modify-cluster.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/modify-cluster.html")** command. Specify the cluster ID and
 the desired HSM type.
 



```
`$` `aws cloudhsmv2 modify-cluster --cluster-id `<cluster ID>` --hsm-type `<HSM Type>``
                                                 `{
 "Cluster": {
 "BackupPolicy": "DEFAULT",
 "BackupRetentionPolicy": {
 "Type": "DAYS",
 "Value": 90
 },
 "VpcId": "vpc-50ae0636",
 "SubnetMapping": {
 "us-west-2b": "subnet-49a1bc00",
 "us-west-2c": "subnet-6f950334",
 "us-west-2a": "subnet-fd54af9b"
 },
 "SecurityGroup": "sg-6cb2c216",
 "HsmType": "hsm2m.medium",
 "HsmTypeRollbackExpiration": 1730383180.000,
 "Certificates": {},
 "State": "MODIFY_IN_PROGRESS",
 "Hsms": [],
 "ClusterId": "cluster-igklspoyj5v",
 "ClusterMode": "FIPS",
 "CreateTimestamp": 1502423370.069
 }
 }`  
                            
```

This procedure puts your cluster into the `MODIFY_IN_PROGRESS` state. After migration, your cluster returns to the `ACTIVE` state.



AWS CloudHSM API
###### To change the HSM type (AWS CloudHSM API)

* Send a [ModifyCluster](../APIReference/API_ModifyCluster.md "../APIReference/API_ModifyCluster.md")
 request. Specify the cluster ID and the desired HSM type for the cluster.

This procedure puts your cluster into the `MODIFY_IN_PROGRESS` state. After migration,
 your cluster returns to the `ACTIVE` state.




## Rolling back the migration


AWS CloudHSM monitors for elevated error rates and performs continuous validation checks
 throughout the migration. If AWS CloudHSM detects a decrease in service quality or any
 validation failures, it automatically initiates a rollback to your cluster's original
 HSM type. During a rollback, for each HSM in the cluster:



* AWS CloudHSM uses the backup taken at the start of that HSM's migration.
* It replaces one HSM at a time until all HSMs are returned to the original type.
* Your cluster remains in limited-write mode throughout the process.

You can roll back the migration within 24 hours of starting it. To check the rollback deadline:



1. Run the [describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html") command.
2. Look for the `HsmTypeRollbackExpiration` value. This timestamp is
 your rollback deadline.

If you decide to roll back, do it before this deadline. The rollback uses the latest backup of your original HSM type.


###### Warning

Be cautious about rolling back after a migration is complete. If you complete a migration and then use AWS CloudHSM to create new keys or users, rolling back can result in data loss.
 See [Synchronizing Data After a Rollback](#cluster-rollback-datasync "#cluster-rollback-datasync") to learn how to mitigate data loss after a rollback.



Console
###### To roll back your HSM type (console)

1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Select the ID of the cluster you want to roll back.
3. From the Actions menu, choose `Modify HSM Type` and select the original HSM type

This procedure puts your cluster into the `ROLLBACK_IN_PROGRESS` state. After rollback,
 your cluster returns to the `ACTIVE` state.



AWS CLI
###### To roll back your HSM type ([AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/ "https://docs.aws.amazon.com/cli/latest/userguide/"))

* At a command prompt, run the **[modify-cluster](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/modify-cluster.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/modify-cluster.html")** command. Specify the cluster ID and
 the original HSM type.
 



```
`$` `aws cloudhsmv2 modify-cluster --cluster-id `<cluster ID>` --hsm-type `<HSM Type>``
                                `{
 "Cluster": {
 "BackupPolicy": "DEFAULT",
 "BackupRetentionPolicy": {
 "Type": "DAYS",
 "Value": 90
 },
 "VpcId": "vpc-50ae0636",
 "SubnetMapping": {
 "us-west-2b": "subnet-49a1bc00",
 "us-west-2c": "subnet-6f950334",
 "us-west-2a": "subnet-fd54af9b"
 },
 "SecurityGroup": "sg-6cb2c216",
 "HsmType": "hsm1.medium",
 "HsmTypeRollbackExpiration": 1730383180.000,
 "Certificates": {},
 "State": "ROLLBACK_IN_PROGRESS",
 "Hsms": [],
 "ClusterId": "cluster-igklspoyj5v",
 "ClusterMode": "FIPS",
 "CreateTimestamp": 1502423370.069
 }
}` 
                         
```

This procedure puts your cluster into the `ROLLBACK_IN_PROGRESS` state. After rollback, your cluster returns to the `ACTIVE` state.



AWS CloudHSM API
###### To roll back your HSM type (AWS CloudHSM API)

* Send a [ModifyCluster](../APIReference/API_ModifyCluster.md "../APIReference/API_ModifyCluster.md")
 request. Specify the cluster ID and the original HSM type for the cluster.

This procedure puts your cluster into the `ROLLBACK_IN_PROGRESS` state. After rollback,
 your cluster returns to the `ACTIVE` state.




## Synchronizing data after a rollback


During migration, HSMs are in limited-write mode, preventing changes to HSM state. 
 If you roll back during this time (while the cluster is `MODIFY_IN_PROGRESS`), it results in a cluster with content identical to the original cluster.
 


After your cluster returns to the `ACTIVE` state, limited-write mode is lifted. If you create a key or user while in `ACTIVE` state and then roll back,
 that key or user won't be present in your rolled back cluster.


To address user synchronization, use [user management](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md") with CloudHSM CLI to recreate the missing users on your rolled back cluster.
 The users must be manually recreated because the `user replicate` command does not support syncing users from hsm2m.medium to hsm1.medium.
 See user replicate [known issues](troubleshoot-sdk5-user-replicate-failures.md#troubleshoot-sdk5-user-replicate-failures-hsm2m-to-hsm1 "troubleshoot-sdk5-user-replicate-failures.md#troubleshoot-sdk5-user-replicate-failures-hsm2m-to-hsm1").
 


To address key synchronization, use the [key replicate](cloudhsm_cli-key-replicate.md "cloudhsm_cli-key-replicate.md") command to replicate a key between two clusters. 
 If you haven't installed CloudHSM CLI, see the instructions in [Getting started with AWS CloudHSM Command Line
 Interface (CLI)](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md").


###### To synchronize keys after rollback

Follow these steps after completing the rollback. We'll use these terms:


* "cluster-1": Your rolled back cluster (now hsm1.medium)
* "cluster-2": A new temporary hsm2m.medium cluster that you will create
1. Create a new hsm2m.medium cluster (cluster-2) using the latest hsm2m.medium backup from cluster-1:



```
aws cloudhsmv2 create-cluster --hsm-type hsm2m.medium \
                                --subnet-ids `<subnet ID 1>` `<subnet ID 2>` `<subnet ID N>` \
                                --source-backup-id `<backup ID>`
                                --mode `<FIPS>`
                    
```
2. Create an HSM in cluster-2:



```
aws cloudhsmv2 create-hsm --cluster-id `<cluster-2 ID>`
```
3. List keys in cluster-2 that need replication:



```
cloudhsm-cli key list --cluster-id `<cluster-2 ID>`
```
4. Replicate each key from cluster-2 to cluster-1:



```
cloudhsm-cli key replicate --source-cluster-id `<cluster-2 ID>` \
                        --destination-cluster-id `<cluster-1 ID>` \
                        --filter attr.label=`<key ID>`
                    
```
5. Repeat step 4 for each key that needs copying.
6. Delete the HSM in cluster-2:



```
aws cloudhsmv2 delete-hsm --cluster-id `<cluster-2 ID>` --hsm-id `<HSM ID>`
```
7. Delete cluster-2:



```
aws cloudhsmv2 delete-cluster --cluster-id `<cluster-2 ID>`
```
