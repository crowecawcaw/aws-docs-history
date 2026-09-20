

# Step 3: Create a Replication Instance
<a name="chap-on-premoracle2aurora.steps.createreplicationinstance"></a>

An AWS DMS replication instance performs the actual data migration between source and target. The replication instance also caches the changes during the migration. How much CPU and memory capacity a replication instance has influences the overall time required for the migration. Use the following procedure to set the parameters for a replication instance.

To create an AWS DMS replication instance, do the following:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/), and open the AWS DMS console at https://console.aws.amazon.com/dms/v2/ and choose **Replication instances**. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information on the permissions required, see [IAM Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

1. Choose **Create replication instance**.

1. On the **Create replication instance** page, specify your replication instance information as shown following.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>If you plan to launch multiple replication instances or share a user, choose a name that helps you quickly differentiate between the different replication instances.</td></tr>
  <tr><td> <b>Description</b> </td><td>A good description gives others an idea of what the replication instance is being used for and can prevent accidents.</td></tr>
  <tr><td> <b>Instance class</b> </td><td> AWS DMS can use a fair bit of memory and CPU. If you have a large database (many tables) or use a number of LOB data types, setting up a larger instance is probably better. As described following, you might be able to boost your throughput by running multiple tasks. Multiple tasks consume more resources and require a larger instance. Keep an eye on CPU and memory consumption as you run your tests. If you find you are using the full capacity of the CPU or swap space, you can easily scale up.</td></tr>
  <tr><td> <b>VPC</b> </td><td>Here you can choose the VPC where your replication instance will be launched. We recommend that, if possible, you select the same VPC where either your source or target database is (or both). AWS DMS needs to access your source and target database from within this VPC. If either or both of your database endpoints are outside of this VPC, modify your firewall rules to allow AWS DMS access.</td></tr>
  <tr><td> <b>Multi-AZ</b> </td><td>If you choose Multi-AZ, AWS DMS launches a primary and secondary replication instance in separate Availability Zones. In the case of a catastrophic disk failure, the primary replication instance automatically fails over to the secondary, preventing an interruption in service. In most situations, if you are performing a migration, you won’t need Multi-AZ. If your initial data load takes a long time and you need to keep the source and target databases in sync for a significant portion of time, you might consider running your migration server in a Multi-AZ configuration.</td></tr>
  <tr><td> <b>Publicly accessible</b> </td><td>If either your source or your target database are outside of the VPC where your replication instance is, you need to make your replication instance publicly accessible.</td></tr>
</tbody>
</table>


1. In the **Advanced** section, set the **Allocated storage (GB)** parameter, and then choose **Next**.


<table>
<thead>
  <tr><th>For This Option</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Allocated storage (GB)</b> </td><td>Storage is primarily consumed by log files and cached transactions. For caches transactions, storage is used only when the cached transactions need to be written to disk. Therefore, AWS DMS doesn’t use a significant amount of storage. Some exceptions include the following:<br />* <i>Very large tables that incur a significant transaction load.</i> Loading a large table can take some time, so cached transactions are more likely to be written to disk during a large table load.<br />* <i>Tasks that are configured to pause prior to loading cached transactions.</i> In this case, all transactions are cached until the full load completes for all tables. With this configuration, a fair amount of storage might be consumed by cached transactions.<br />* <i>Tasks configured with tables being loaded into Amazon Redshift.</i> However, this configuration isn’t an issue when Aurora MySQL is the target.<br />In most cases, the default allocation of storage is sufficient. However, it’s always a good idea to pay attention to storage related metrics and scale up your storage if you find you are consuming more than the default allocation.</td></tr>
  <tr><td> <b>Replication Subnet Group</b> </td><td>If you run in a Multi-AZ configuration, you need at least two subnet groups.</td></tr>
  <tr><td> <b>Availability Zone</b> </td><td>If possible, locate your primary replication server in the same Availability Zone as your target database.</td></tr>
  <tr><td> <b>VPC Security group(s)</b> </td><td>With security groups you can control ingress and egress to your VPC. With AWS DMS you can associate one or more security groups with the VPC where your replication server launches.</td></tr>
  <tr><td> <b> KMS key </b> </td><td>With AWS DMS, all data is encrypted at rest using a KMS encryption key. By default, AWS DMS creates a new encryption key for your replication server. However, you can use an existing key if desired.</td></tr>
</tbody>
</table>
