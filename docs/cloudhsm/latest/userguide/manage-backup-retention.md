# Configure AWS CloudHSM backup retention policy

AWS CloudHSM purges backups based on the backup retention policy you set when you create a
cluster. Backup retention policy applies to clusters. If you move a backup to a different
region, that backup is no longer associated with a cluster and has no backup retention policy.
You must manually delete any backups not associated with a cluster. AWS CloudHSM does not delete a
cluster's last backup. For clusters migrated from hsm1.medium, AWS CloudHSM retains the latest
hsm1.medium backup until hsm1.medium reaches end of life.

[AWS CloudTrail](get-api-logs-using-cloudtrail.md "get-api-logs-using-cloudtrail.md") reports backups marked for
deletion. You can restore backups the service purges just as you would restore [manually deleted backups](delete-restore-backup.md "delete-restore-backup.md"). To prevent a race
condition, you should change the backup retention policy for the cluster before you restore a
backup deleted by the service. If you want to keep the retention policy the same and preserve
select backups, you can specify that the service [exclude backups](#exclude-backups-console-proc "#exclude-backups-console-proc") from the cluster backup retention policy.

For more information on AWS CloudHSM pricing, see [Reduce costs by scaling to your needs](bp-cluster-management.md#bp-reduce-cost "bp-cluster-management.md#bp-reduce-cost").

## Managed backup retention

Clusters created before November 18, 2020 have a backup retention policy of 90 days plus
the age of the cluster. For example, if you created a cluster on November 18, 2019, the
service would assign your cluster a backup retention policy of one year plus 90 days (455
days). You can set this period to any number between 7 and 379 days. AWS CloudHSM does not delete a
cluster's last backup. For more information about managing backups, see [Cluster backups](manage-backups.md "manage-backups.md").

###### Note

You can opt out of managed backup retention altogether by contacting [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support").

The following table describes how to set the backup retention.

Console

###### To configure backup retention policy

(console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of
   the page.
3. Click the cluster ID of a cluster in the Active state to manage the backup
   retention policy for that cluster.
4. To change the backup retention policy, choose **Actions, Change backup
   retention period**.

The Change backup retention period dialog box appears. 5. In **Backup retention period (in days)**, type a value between
7 and 379 days. 6. Choose **Change backup retention period**.

###### To exclude or include a backup from

backup retention policy (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To view your backups, in the navigation pane choose
   **Backups**.
3. Click the backup ID of a backup in the Ready state to exclude or include.
4. On the **Backup details** page, take one of the following
   actions.
   - To exclude a backup with a date in **Expiration time**,
     choose **Actions, Disable expiration**.
   - To include a backup that does not expire, choose **Actions, Use
     cluster retention policy**.

AWS CLI

###### To configure backup retention policy

(AWS CLI)

- At a command prompt, issue the **modify-cluster** command.
  Specify the cluster ID and the backup retention policy.

````
`$` `aws cloudhsmv2 modify-cluster --cluster-id `<cluster ID>` \
 --backup-retention-policy Type=DAYS,Value=`<number of days to retain backups>```{
 "Cluster": {
 "BackupPolicy": "DEFAULT",
 "BackupRetentionPolicy": {
 "Type": "DAYS",
 "Value": 90
 },
 "Certificates": {},
 "ClusterId": "cluster-kdmrayrc7gi",
 "CreateTimestamp": 1504903546.035,
 "Hsms": [],
 "HsmType": "hsm1.medium",
 "SecurityGroup": "sg-40399d28",
 "State": "ACTIVE",
 "SubnetMapping": {
 "us-east-2a": "subnet-f1d6e798",
 "us-east-2c": "subnet-0e358c43",
 "us-east-2b": "subnet-40ed9d3b"
 },
 "TagList": [
 {
 "Key": "Cost Center",
 "Value": "12345"
 }
 ],
 "VpcId": "vpc-641d3c0d"
 }
}`
````

###### To exclude a backup from backup retention

policy (AWS CLI)

- At a command prompt, issue the **modify-backup-attributes**
  command. Specify the backup ID and set the never-expires flag to preserve the
  backup.

```
`$` `aws cloudhsmv2 modify-backup-attributes --backup-id `<backup ID>` \
 --never-expires``{
 "Backup": {
 "BackupId": "backup-ro5c4er4aac",
 "BackupState": "READY",
 "ClusterId": "cluster-dygnwhmscg5",
 "NeverExpires": true
 }
}`
```

###### To include a backup in backup retention policy (AWS CLI)

- At a command prompt, issue the **modify-backup-attributes**
  command. Specify the backup ID and set the no-never-expires flag to include the
  backup in backup retention policy, which means the service will eventually delete
  the backup.

```
`$` `aws cloudhsmv2 modify-backup-attributes --backup-id `<backup ID>` \
 --no-never-expires``{
 "Backup": {
 "BackupId": "backup-ro5c4er4aac",
 "BackupState": "READY",
 "ClusterId": "cluster-dygnwhmscg5",
 "NeverExpires": false
 }
}`
```

AWS CloudHSM API
Refer to the following topics to learn how to manage backup retention by using the
API.

- [ModifyCluster](../APIReference/API_ModifyCluster.md "../APIReference/API_ModifyCluster.md")
- [ModifyBackupAttributes](../APIReference/API_ModifyBackupAttributes.md "../APIReference/API_ModifyBackupAttributes.md")
