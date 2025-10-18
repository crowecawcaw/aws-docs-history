# Creating AWS CloudHSM clusters from backups

To restore an AWS CloudHSM cluster from a backup, follow the steps in this topic. Your cluster will contain the same users, key material, certificates, configuration, and
 policies that were in the backup. 
 For more information about managing backups, see [Cluster backups](manage-backups.md "manage-backups.md").
 


## Create clusters from backups (console)


1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Choose **Create cluster**.
3. In the **Cluster configuration** section, do the following:


	1. For **VPC**, choose a VPC for the cluster that you are
	 creating.
	2. For **AZ(s)**, choose a private subnet for each Availability Zone
	 that you are adding to the cluster.
	3. For **Network type**, choose the IP protocol your HSMs will use for connections.
4. In the **Cluster source** section, do the following:


	1. Choose **Restore cluster from existing backup**.
	2. Choose the backup that you are restoring.
5. Choose **Next: Review**.
6. Review your cluster configuration, then choose **Create
 cluster**.
7. Specify how long the service should retain backups.


Accept the default retention period of 90 days or type a new value between 7 and 379
 days. The service will automatically delete backups in this cluster older than the value
 you specify here. You can change this later. For more information, see [Configure backup retention](manage-backup-retention.md "manage-backup-retention.md").
8. Choose **Next**.
9. (Optional) Type a tag key and an optional tag value. To add more than one tag to the
 cluster, choose **Add tag**.
10. Choose **Review**.
11. Review your cluster configuration, and then choose **Create
 cluster**.

###### Tip

To create an HSM in this cluster that contains the same users, key material, certificates, configuration,
 and policies that were in the backup that you restored, [add an HSM](add-hsm.md "add-hsm.md") to the cluster.


## Create clusters from backups (AWS CLI)


To determine the backup ID, issue the **[describe-backups](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html")** command.


* At a command prompt, issue the **[create-cluster](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/create-cluster.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/create-cluster.html")** command.
 Specify the HSM instance type, the subnet IDs of the subnets where you plan to create HSMs,
 and the backup ID of the backup that you are restoring. 
 



```
`$` `aws cloudhsmv2 create-cluster --hsm-type hsm2m.medium \
 --subnet-ids `<subnet ID 1>` `<subnet ID 2>` `<subnet ID N>` \
 --source-backup-id `<backup ID>`
 --mode `<FIPS>` \
 --network-type `<IPV4>```{
 "Cluster": {
 "HsmType": "hsm2m.medium",
 "VpcId": "vpc-641d3c0d",
 "Hsms": [],
 "State": "CREATE_IN_PROGRESS",
 "SourceBackupId": "backup-rtq2dwi2gq6",
 "BackupPolicy": "DEFAULT",
 "BackupRetentionPolicy": {
 "Type": "DAYS",
 "Value": 90
 },
 "NetworkType": "IPV4",
 "SecurityGroup": "sg-640fab0c",
 "CreateTimestamp": 1504907311.112,
 "SubnetMapping": {
 "us-east-2c": "subnet-0e358c43",
 "us-east-2a": "subnet-f1d6e798",
 "us-east-2b": "subnet-40ed9d3b"
 },
 "Certificates": {
 "ClusterCertificate": "`<certificate string>`"
 },
 "ClusterId": "cluster-jxhlf7644ne"
 }
}`
```

## Create clusters from backups (AWS CloudHSM API)


Refer to the following topic to learn how to create clusters from backups by using the API.



* [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")
