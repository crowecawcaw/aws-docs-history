# Copying AWS CloudHSM cluster backups across AWS
 Regions

 You can copy AWS CloudHSM cluster backups across Regions for many reasons, including
 cross-region resilience, global workloads, and [disaster
 recovery](backups-using.md#recovery-backups "backups-using.md#recovery-backups"). After you copy backups, they appear in the destination region with a
 `CREATE_IN_PROGRESS` status. Upon successful completion of the copy, the
 status of the backup changes to `READY`. If the copy fails, the status of the
 backup changes to `DELETED`. Check your input parameters for errors and ensure
 that the specified source backup is not in a `DELETED` state before rerunning the
 operation. For information about backups or how to create a cluster from a backup, see [Cluster backups](manage-backups.md "manage-backups.md") or [Creating clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md"). 


 Note the following:
 


* To copy a cluster backup to a destination region, your account must have the
 proper IAM policy permissions. In order to copy the backup to a different
 region, your IAM policy must allow access to the source region in which the
 backup is located. Once copied across regions, your IAM policy must allow
 access to the destination region in order to interact with the copied backup,
 which includes using the [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") operation. For more information,
 see [Create IAM administrators](create-iam-user.md "create-iam-user.md").
* The original cluster and the cluster that may be built from a backup in the
 destination region are not linked. You must manage each of these clusters
 independently. For more information, see [Clusters](manage-clusters.md "manage-clusters.md").
* Backups cannot be copied between AWS partitions. Backups can be copied 
 between AWS restricted regions and standard regions within the same partition.

## Copy backups to different Regions (console)


###### To copy backups to different Regions (console)

1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
 page.
3. In the navigation pane, choose **Backups**.
4. Choose a backup to copy to a different region.
5. To copy the selected backup, choose **Actions, Copy backup to another region**.


The Copy backup to another region dialog box appears.
6. In **Destination region**, choose a region from **Select a region**.
7. (Optional) Type a tag key and an optional tag value. To add more than one tag to
 the cluster, choose **Add tag**.
8. Choose **Copy backup**.

## Copy backups to different Regions (AWS CLI)


To determine the backup ID, run the **[describe-backups](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html")** command.


###### To copy backups to different regions (AWS CLI)

* At a command prompt, run the **[copy-backup-to-region](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/copy-backup-to-region.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/copy-backup-to-region.html")** command. Specify the destination region and the backup ID of 
 the source backup. If you specify a backup ID, the associated backup is copied.



```
`$` `aws cloudhsmv2 copy-backup-to-region --destination-region `<destination region>` \
 --backup-id `<backup ID>``
```

## Copy backups to different Regions (AWS CloudHSM API)


Refer to the following topic to learn how to copy backups to different regions by using the API.



* [CopyBackupToRegion](../APIReference/API_CopyBackupToRegion.md "../APIReference/API_CopyBackupToRegion.md")
