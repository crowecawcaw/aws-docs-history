

# Modifying a replication instance
<a name="CHAP_ReplicationInstance.Modifying"></a>

You can modify the settings for a replication instance to, for example, change the instance class or to increase storage. 

When you modify a replication instance, you can apply the changes immediately. To apply changes immediately, choose the **Apply changes immediately** option in the AWS Management Console. Or use the `--apply-immediately` parameter when calling the AWS CLI, or set the `ApplyImmediately` parameter to `true` when using the DMS API. 

If you don't choose to apply changes immediately, the changes are put into the pending modifications queue. During the next maintenance window, any pending changes in the queue are applied. 

**Note**  
If you choose to apply changes immediately, any changes in the pending modifications queue are also applied. If any of the pending modifications require downtime, choosing **Apply changes immediately** can cause unexpected downtime. 

**To modify a replication instance by using the AWS console**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. In the navigation pane, choose **Replication instances**.

1. Choose the replication instance you want to modify. The following table describes the modifications you can make. 


<table>
<thead>
  <tr><th>Option</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>You can change the name of the replication instance. Enter a name for the replication instance that contains from 8 to 16 printable ASCII characters (excluding /,", and @). The name should be unique for your account for the AWS Region you selected. You can choose to add some intelligence to the name, such as including the AWS Region and task you are performing, for example <b>west2-mysql2mysql-instance1</b>.</td></tr>
  <tr><td> <b>Description</b> </td><td>Revise or enter a brief description of the replication instance.</td></tr>
  <tr><td> <b>Instance class</b> </td><td>You can change the instance class. Choose an instance class with the configuration you need for your migration. Changing the instance class causes the replication instance to reboot. This reboot occurs during the next maintenance window or can occur immediately if you choose the <b>Apply changes immediately</b> option.<br /> For more information on how to determine which instance class is best for your migration, see <a href="CHAP_ReplicationInstance.md">Working with an AWS DMS replication instance</a>. </td></tr>
  <tr><td> <b>Engine version</b> </td><td>You can upgrade the engine version that is used by the replication instance. Upgrading the replication engine version causes the replication instance to shut down while it is being upgraded. <br /></td></tr>
  <tr><td><b>Multi-AZ</b></td><td>You can change this option to create a standby replica of your replication instance in another Availability Zone for failover support or remove this option. If you intend to use change data capture (CDC), ongoing replication, you should enable this option.</td></tr>
  <tr><td> <b>Allocated storage (GiB)</b> </td><td>Storage is primarily consumed by log files and cached transactions. For caches transactions, storage is used only when the cached transactions need to be written to disk. Therefore, AWS DMS doesn't use a significant amount of storage. Some exceptions include the following: <ul><li> Very large tables that incur a significant transaction load. Loading a large table can take some time, so cached transactions are more likely to be written to disk during a large table load. </li><li> Tasks that are configured to pause before loading cached transactions. In this case, all transactions are cached until the full load completes for all tables. With this configuration, a fair amount of storage might be consumed by cached transactions. </li><li> Tasks configured with tables being loaded into Amazon Redshift. However, this configuration isn't an issue when Amazon Aurora is the target. </li></ul><br />In most cases, the default allocation of storage is sufficient. However, it's always a good idea to pay attention to storage related metrics and scale up your storage if you find you are consuming more than the default allocation. </td></tr>
  <tr><td><b>Network type</b></td><td>DMS supports the <b>IPv4</b> addressing protocol network type, and supports both IPv4 and IPv6 addressing protocol network types in <b>Dual-stack</b> mode. When you have resources that must communicate to your replication instance using an IPv6 addressing protocol network type, choose <b>Dual-stack</b> mode. For information about limitations in dual-stack mode, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.IP_addressing.dual-stack-limitations"> Limitations for dual-stack network DB instances</a> in the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"> Amazon Relational Database Service</a> userguide. </td></tr>
  <tr><td> <b>VPC Security Group(s)</b> </td><td>The replication instance is created in a VPC. If your source database is in a VPC, choose the VPC security group that provides access to the DB instance where the database resides.</td></tr>
  <tr><td><b>Automatic version upgrade</b></td><td>AWS DMS doesn't differentiate between major and minor versions. For example, upgrading from version 3.4.x to 3.5.x isn't considered a major upgrade, so all changes should be backward-compatible. When <b>Automatic version upgrade</b> is enabled, DMS automatically upgrades the replication instance's version during the maintenance window if it is deprecated. <br />When <b>Automatic version upgrade</b> is enabled, DMS uses the current default engine version when you create a replication instance. For example, if you set <b>Engine version</b> to a lower version number than the current default version, DMS uses the default version.<br />If <b>Automatic version upgrade</b> isn't enabled when you create a replication instance, DMS uses the engine version specified by the <b>Engine version</b> parameter.</td></tr>
  <tr><td> <b>Maintenance window</b> </td><td>Choose a weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).<br />Default: A 30-minute window selected at random from an 8-hour block of time per AWS Region, occurring on a random day of the week.</td></tr>
  <tr><td> <b>Apply changes immediately</b> </td><td>Choose this option to apply any modifications you made immediately. Depending on the settings you choose, choosing this option could cause an immediate reboot of the replication instance.<br />If you choose <b>Test connection</b> while AWS DMS applies changes, then you will see an error message. After AWS DMS applies changes to your replication instance, choose <b>Test connection</b> again.</td></tr>
  <tr><td> <b>Apply changes during next scheduled maintenance window</b> </td><td>Choose this option if you want DMS to wait until the next scheduled maintenance window to apply your changes.</td></tr>
</tbody>
</table>


## Best practices when modifying a replication instance
<a name="CHAP_ReplicationInstance.Modifying.best.practice"></a>

When modifying a replication instance, following these best practices helps ensure a successful update with minimal impact to your migration workflows. Take the following key steps before, during, and after modifications to maintain data integrity and operational efficiency throughout the process.

**Plan modification timing:**  
+ You can either apply changes immediately or schedule them for the next maintenance window.
+ Schedule during low-traffic periods to minimize impact.

**Pre-modification steps:**  
+ Stop all active replication tasks.
+ Verify all tasks have successfully stopped.
+ Document current configuration task settings.

**During modification:**  
+ Monitor the modification progress.
+ Wait for "Available" status before proceeding.

**Post-modification steps:**  
+ Resume all previously stopped tasks.
+ Confirm tasks are running correctly.