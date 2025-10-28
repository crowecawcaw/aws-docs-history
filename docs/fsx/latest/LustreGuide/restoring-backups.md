# Restoring backups

You can use an available backup to create a new file system, effectively restoring a
point-in-time snapshot of another file system. You can restore a backup using the console, AWS CLI,
or one of the AWS SDKs. Restoring a backup to a new file system takes the same amount of time as
creating a new file system. The data restored from the backup is lazy-loaded onto the file system,
during which time you will experience slightly higher latency.

###### Note

You can only restore your backup to a file system of the same deployment type,
storage class, throughput capacity, storage capacity, data compression type, and AWS Region as
the original. You can [increase](managing-storage-capacity.md "managing-storage-capacity.md") your restored file
system's storage capacity after it becomes available.

###### To restore a file system from a backup using the console

1. Open the Amazon FSx for Lustre console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose **Backups** from the left side
   navigation.
3. Choose the backup that you want to restore from the **Backups** table,
   and then choose **Restore backup**.

The file system creation wizard opens with most settings pre-populated based on the
configuration of the file system the backup was created from. You can optionally modify the
Virtual Private Cloud (VPC) configuration, or choose a newer Lustre version. Note that other
configuration settings, such as Deployment Type and throughput per unit of storage, cannot
be modified during restore. 4. Complete the wizard as you do when you create a new file system. 5. Choose **Review and create**. 6. Review the settings you chose for your Amazon FSx for Lustre file system, and then choose **Create
file system**.
You have restored from a backup, and a new file system is now being created. When its status
changes to `AVAILABLE`, you can use the file system as normal.
