# Working with AWS CloudHSM cluster backups

 When you add a hardware security module (HSM) to a cluster in AWS CloudHSM that previously
 contained one or more active HSMs, the service restores the latest backup onto the new HSM.
 Use backups to manage HSMs you use infrequently. When you don't need the HSM, delete it to
 trigger a backup. Later, when you need the HSM, create a new one in the same cluster, and this
 action will restore the backup you previously created with the delete HSM operation. 


## Removing expired keys or inactive users


 You may want to remove unwanted cryptographic materials from your environment such as
 expired keys or inactive users. This is a two-step process. First, delete these materials
 from your HSM. Next, delete all existing backups. Following this process ensures you do not
 restore deleted information when initializing a new cluster from backup. For more
 information, see [Delete AWS CloudHSM cluster backups](delete-restore-backup.md "delete-restore-backup.md") . 


## Considering disaster recovery


 You can create a cluster from a backup. You might want to do this to set a recovery
 point for your cluster. Nominate a backup that contains all the users, key material,
 certificates that you want in your recovery point, and then use that backup to create a new
 cluster. For more information about creating a cluster from a backup, see [Creating clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md"). 


 You can also copy a backup of a cluster into a different region, where you can create a
 new cluster as a clone of the original. You may want to do this for a number of reasons,
 including simplification of the disaster recovery process. For more information about
 copying backups to regions, see [Copying backups across Regions](copy-backup-to-region.md "copy-backup-to-region.md").
