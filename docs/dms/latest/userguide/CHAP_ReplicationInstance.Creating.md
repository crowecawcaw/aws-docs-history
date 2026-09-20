

# Creating a replication instance
<a name="CHAP_ReplicationInstance.Creating"></a>

Your first task in migrating a database is to create a replication instance. This replication instance requires sufficient storage and processing power to perform the tasks that you assign and migrate data from your source database to the target database. The required size of this instance varies depending on the amount of data you need to migrate and the tasks that you need the instance to perform. For more information about replication instances, see [Working with an AWS DMS replication instance](CHAP_ReplicationInstance.md). 

**To create a replication instance by using the AWS console**

1. Choose **Replication instances** in the navigation pane of the AWS DMS console and then choose **Create replication instance**.

1. On the **Create replication instance** page, specify your replication instance information. The following table describes the settings you can make.


<table>
<thead>
  <tr><th>Option</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>Enter a name for the replication instance that contains from 8 to 16 printable ASCII characters (excluding /,", and @). The name should be unique for your account for the AWS Region you selected. You can choose to add some intelligence to the name, such as including the AWS Region and task you are performing, for example <b>west2-mysql2mysql-instance1</b>.</td></tr>
  <tr><td> <b>Descriptive Amazon Resource Name (ARN) - <i>Optional</i></b> </td><td>A friendly name to override the default DMS ARN. You can't modify it after creation.</td></tr>
  <tr><td> <b>Description</b> </td><td>Enter a brief description of the replication instance.</td></tr>
  <tr><td> <b>Instance class</b> </td><td>Choose an instance class with the configuration you need for your migration. Keep in mind that the instance must have enough storage, network, and processing power to successfully complete your migration. For more information on how to determine which instance class is best for your migration, see <a href="CHAP_ReplicationInstance.md">Working with an AWS DMS replication instance</a>. </td></tr>
  <tr><td> <b>Engine version</b> </td><td>In the AWS DMS console, you can choose any supported engine version that you want. From the AWS CLI, the replication instance runs the latest non-beta version of the AWS DMS replication engine unless you specify a different engine version in the AWS CLI.</td></tr>
  <tr><td><b>High Availability</b></td><td>Use this optional parameter to create a standby replica of your replication instance in another Availability Zone for failover support. If you intend to use change data capture (CDC) or ongoing replication, you should turn on this option.</td></tr>
  <tr><td> <b>Allocated storage (GiB)</b> </td><td>Storage is primarily consumed by log files and cached transactions. For caches transactions, storage is used only when the cached transactions need to be written to disk. Therefore, AWS DMS doesn't use a significant amount of storage. Some exceptions include the following: <ul><li> Very large tables that incur a significant transaction load. Loading a large table can take some time, so cached transactions are more likely to be written to disk during a large table load. </li><li> Tasks that are configured to pause before loading cached transactions. In this case, all transactions are cached until the full load completes for all tables. With this configuration, a fair amount of storage might be consumed by cached transactions. </li><li> Tasks configured with tables being loaded into Amazon Redshift. However, this configuration isn't an issue when Amazon Aurora is the target. </li></ul><br />In most cases, the default allocation of storage is sufficient. However, it's always a good idea to pay attention to storage-related metrics. Make sure to scale up your storage if you find you are consuming more than the default allocation. </td></tr>
  <tr><td><b>Network type</b></td><td>DMS supports the <b>IPv4</b> addressing protocol network type, and supports both IPv4 and IPv6 addressing protocol network types in <b>Dual-stack</b> mode. When you have resources that must communicate with your replication instance using an IPv6 addressing protocol network type, use <b>Dual-stack</b> mode. For information about limitations in dual-stack mode, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.IP_addressing.dual-stack-limitations"> Limitations for dual-stack network DB instances</a> in the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"> Amazon Relational Database Service</a> userguide. </td></tr>
  <tr><td> <b>VPC</b> </td><td>Choose the VPC that you want to use. If your source or your target database is in a VPC, choose that VPC. If your source and your target databases are in different VPCs, ensure that they are both in public subnets and are publicly accessible. Then choose the VPC where the replication instance is to be located. The replication instance must be able to access the data in the source VPC. If neither your source or target database is in a VPC, choose a VPC where the replication instance is to be located.</td></tr>
  <tr><td> <b>Replication Subnet Group</b> </td><td>Choose the replication subnet group in your selected VPC where you want the replication instance to be created. If your source database is in a VPC, choose the subnet group that contains the source database as the location for your replication instance. For more information about replication subnet groups, see <a href="CHAP_ReplicationInstance.VPC.md#CHAP_ReplicationInstance.VPC.Subnets">Creating a replication subnet group</a>.</td></tr>
  <tr><td><b>Publicly accessible</b></td><td>Choose this option if you want the replication instance to be accessible from the internet. The default is publicly accessible, and once the option is chosen, you can't modify it after you create the replication instance.</td></tr>
</tbody>
</table>


1. Choose the **Advanced** tab to set values for network and encryption settings if you need them. The following table describes the settings.


<table>
<thead>
  <tr><th>Option</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Availability zone</b> </td><td>Choose the Availability Zone where your source database is located.</td></tr>
  <tr><td> <b>VPC Security group(s)</b> </td><td>The replication instance is created in a VPC. If your source database is in a VPC, choose the VPC security group that provides access to the DB instance where the database resides.</td></tr>
  <tr><td> <b>KMS key</b> </td><td>Choose the encryption key to use to encrypt replication storage and connection information. If you choose <b>(Default) aws/dms</b>, the default AWS Key Management Service (AWS KMS) key associated with your account and AWS Region is used. A description and your account number are shown, along with the key's ARN. For more information on using the encryption key, see <a href="CHAP_Security.md#CHAP_Security.EncryptionKey">Setting an encryption key and specifying AWS KMS permissions</a>.</td></tr>
</tbody>
</table>


1. Specify the **Maintenance** settings. The following table describes the settings. For more information about maintenance settings, see [Working with the AWS DMS maintenance window](CHAP_ReplicationInstance.MaintenanceWindow.md).


<table>
<thead>
  <tr><th>Option</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Automatic version upgrade</b> </td><td>AWS DMS doesn't differentiate between major and minor versions. For example, upgrading from version 3.4.x to 3.5.x isn't considered a major upgrade, so all changes should be backward-compatible. <br />When <b>Automatic version upgrade</b> is enabled, DMS automatically upgrades the replication instance's version during the maintenance window if it is deprecated.<br />When <b>AutoMinorVersionUpgrade</b> is enabled, DMS uses the current default engine version when you create a replication instance. For example, if you set <b>Engine version</b> to a lower version number than the current default version, DMS uses the default version.<br />If <b>AutoMinorVersionUpgrade</b> isn't enabled when you create a replication instance, DMS uses the engine version specified by the <b>Engine version</b> parameter.</td></tr>
  <tr><td> <b>Maintenance window</b> </td><td>Choose a weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).<br />Default: A 30-minute window selected at random from an 8-hour block of time per AWS Region, occurring on a random day of the week.</td></tr>
</tbody>
</table>


1. Choose **Create replication instance**.