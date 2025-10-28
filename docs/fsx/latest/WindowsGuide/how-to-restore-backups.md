# Restoring a backup to a new file system

You can restore a file system backup to create new file system using the AWS Management Console, CLI, and API, as
described in the following procedure.

###### To restore a file system from a backup

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose **Backups** from the left side
   navigation.
3. Choose the backup that you want to restore from the **Backups** table,
   and then choose **Restore backup**.

Doing so opens the file system creation wizard. This wizard is identical to the standard
file system creation wizard, except the **Deployment type** and
**Storage capacity** are already set and can't be changed.
However, you can change the throughput capacity, associated VPC, and
other settings, and storage type. The storage type is set to **SSD** by default,
but you can change it to **HDD** under the following conditions:

    * The file system deployment type is **Multi-AZ** or **Single-AZ 2**.
    * The storage capacity is at least 2,000 GiB.

4. Complete the wizard as you do when you create a new file system.
5. Choose **Review and create**.
6. Review the settings you chose for your Amazon FSx file system, and then choose **Create
   file system**.

Amazon FSx is creating a new file system, and once its status
changes to `AVAILABLE`, you can use the file system as normal.
