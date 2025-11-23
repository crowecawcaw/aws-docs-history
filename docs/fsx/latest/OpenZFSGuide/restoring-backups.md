# Restoring backups

You can use an available backup to create a new file system, effectively restoring a
point-in-time snapshot of another file system. You can restore a backup using the Amazon FSx console, AWS CLI,
or one of the AWS SDKs. You can also restore backups using the AWS Backup console. For more information about using the AWS Backup console,
see [Restore an FSx file System](../../../aws-backup/latest/devguide/restoring-fsx.md "../../../aws-backup/latest/devguide/restoring-fsx.md")
in the AWS Backup Developer Guide.

###### Note

Backups of Multi-AZ FSx for OpenZFS file systems can be restored only by using the Amazon FSx console or CLI.

Restoring a backup to a new file system takes the same amount of time as
creating a new file system. The data restored from the backup is lazy-loaded onto the file system,
during which time you will experience slightly higher latency.

###### Note

Restoring from a backup with a given storage class to a file system with a different storage class is not supported.

###### To restore a file system from backup (Amazon FSx console)

1.  Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2.  From the console dashboard, choose **Backups** from the left side
    navigation.
3.  Choose the backup that you want to restore from the **Backups** table,
    and then choose **Restore backup**. Doing so opens the file system creation wizard.
4.  For **File system name - optional**, you can enter a name using a maximum of 256 Unicode
    letters, white space, and numbers, plus these special characters: + - = . \_ : /
5.  For **Storage capacity**, enter a value that is equal to or greater than the storage
    capacity of the original file of which the backup was taken, in GiB. The range of valid values is 64–524288 GiB.
6.  For **Provisioned SSD IOPS**, you have two options to provision
    the number of IOPS for your file system:
    - Choose **Automatic** (the default) if you
      want Amazon FSx to automatically provision 3 IOPS per GiB of SSD storage.
    - Choose **User-provisioned** if you want to specify the number of IOPS. You
      can provision a maximum of 160,000 SSD IOPS per file system for Single-AZ 1 (non-HA and HA) and a maximum of
      400,000 SSD IOPS per file system for Single-AZ 2 (non-HA and HA) and Multi-AZ (HA)\*. You pay for SSD IOPS that you
      provision that exceed 3 IOPS per GiB of SSD storage.

    ###### Note

    \*The maximum SSD IOPS you can provision for Multi-AZ file systems depends on the AWS Region your file system is located in. For more information, see
    [Data access from disk](performance-ssd.md#data-access-disk "performance-ssd.md#data-access-disk").

7.  For **Throughput capacity**, you have two options to provide
    your desired throughput capacity in megabytes per second (MBps).
    **Throughput capacity** is the sustained speed
    at which the file server that hosts your file system can serve data.

        * Choose **Recommended throughput capacity**
         (the default) if you want Amazon FSx to automatically choose the throughput
         capacity. The recommended value is based on the amount of storage capacity
         that you chose.
        * Choose **Specify throughput capacity** if you
         want to specify the throughput capacity value, and choose a value of
         64, 128, 256, 512, 1024, 2048, 3072, or 4096 MBps. You pay for additional
         throughput capacity that you provision above the recommended amount.

    You can increase the amount of throughput capacity as needed at
    any time after you create the file system. For more information, see
    [Modifying throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

8.  In the **Network & security** section, provide networking and
    security group information:
    - For **Virtual Private Cloud (VPC)**, choose the Amazon VPC that
      you want to associate with your file system.
    - For **VPC Security Groups**, the ID for the default security group
      for your VPC should be already added.
    - For **Subnet**, choose any value from the list of available subnets.

9.  In the **Encryption** section, for
    **Encryption key**, choose the AWS Key Management Service (AWS KMS)
    encryption key that protects your file system's data at rest.

###### Note

When restoring a file system with a storage capacity greater than 144 TiB, you must use the same KMS key
that you used when creating the backup. If you want to restore the file system with a new KMS key, you must first
copy the backup using the new KMS key, and then restore the file system with this backup. 10. In **Root volume configuration**, you can set the
following options for the file system's root volume:

    * For **Data compression type**, choose the type of compression
     to use for your volume, either **Zstandard**, **LZ4**,
     or **No compression**. Zstandard compression provides more data compression
     and higher read throughput than LZ4 compression. LZ4 compression provides less compression
     and higher write throughput performance than Zstandard compression. For more information about the
     storage and performance benefits of the volume data compression options,
     see [Data compression](performance.md#perf-data-compression "performance.md#perf-data-compression").
    * For **Copy tags to snapshots**, enable or
     disable the option to copy tags to the volume's snapshot.
    * For **NFS exports**, there is a default client configuration setting
     which you can modify or remove. Client configurations define which clients can access
     the volume and their permissions.


    To provide additional client configurations:




    	1. In the **Client addresses** field, specify which
    	 clients can access the volume. Enter an asterisk (`*`) for
    	 any client, a specific IP address, or a CIDR range of IP addresses.
    	2. In the **NFS options** field, enter a
    	 comma-delimited set of exports options. For example, enter `rw`
    	 to allow read and write permissions to the volume for the
    	 specified **Client addresses**.
    	3. Choose **Add client configuration**.
    	4. Repeat the procedure to add another client configuration.
    For more information, see [NFS exports](creating-volumes.md#nfs-exports "creating-volumes.md#nfs-exports").
    * For **Record size**, choose whether to use the
     default suggested record size of 128 KiB, or to set a custom suggested record
     size for the volume. Generally, workloads that write in fixed small or large
     record sizes may benefit from setting a custom record size, like database workloads
     (small record size) or media streaming workloads (large record size). We recommend
     using the default setting for the majority of use cases. For more information about the
     record size setting, see [Configurable volume properties](creating-volumes.md#volume-properties "creating-volumes.md#volume-properties").
    * For **User and group quotas**, you can set a storage quota for
     a user or group:




    	1. For **Quota type**, choose `USER` or
    	 `GROUP`.
    	2. For **User or group ID**, choose a number that is
    	 the ID of the user or group.
    	3. For **Usage quota**, choose a number that is
    	 the storage quota of the user or group.
    	4. Choose **Add quota**.
    	5. Repeat the procedure to add a quota for another user or group.

11. In **Backup and maintenance -
    _optional_**, you can set the
    following options:
    - For **Daily automatic backup**, choose
      **Enabled** for automatic daily backups.
      This option is enabled by default.
    - For **Daily automatic backup window**,
      set the time of the day in Coordinated Universal Time (UTC)
      that you want the daily automatic backup window to start.
      The window is 30 minutes starting from this specified time.
      This window can't overlap with the
      weekly maintenance backup window.
    - For **Automatic backup retention
      period**, set a period from 1–90
      days that you want to retain automatic backups.
    - For **Weekly maintenance window**, you can
      set the time of the week that you want the maintenance window
      to start. Day 1 is Monday, 2 is Tuesday, and so on. The
      window is 30 minutes starting from this specified time.
      This window can't overlap with the daily automatic backup window.

12. For **Tags - _optional_**, you can enter a key and value
    to add tags to your file system. A tag is a case-sensitive key-value
    pair that helps you manage, filter, and search for your file
    system.

Choose **Next**. 13. Review the file system configuration shown on the
**Create file system** page. For your reference, note
which file system settings you can modify after the file system is
created. 14. Choose **Create file system**.
