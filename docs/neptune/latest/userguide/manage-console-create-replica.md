

# Creating a Neptune reader instance using the console
<a name="manage-console-create-replica"></a>

After creating the primary instance for your Neptune DB cluster, you can add additional Neptune reader instances using the Neptune console.

**To create a Neptune reader instance using the AWS Management Console**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Databases**.

1. Select the DB cluster where you want to create the reader instance.

1. Choose **Actions**, and then choose **Add reader**.

1. On the **Create replica DB instance** page, specify options for your Neptune replica. The following table shows settings for a Neptune read replica.


<table>
<thead>
  <tr><th>For This Option... </th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>DB instance class</b> </td><td>Choose a DB instance class that defines the processing and memory requirements for the Neptune replica. For a current listing of the DB instance classes that Neptune offers in different regions, see <a href="https://aws.amazon.com/neptune/pricing/">the Neptune pricing page</a>.</td></tr>
  <tr><td> <b>Availability zone</b> </td><td>Specify an Availability Zone. Choose a different zone than the primary DB instance. The list includes only those Availability Zones that are mapped by the DB subnet group for the DB cluster.</td></tr>
  <tr><td> <b>Encryption</b> </td><td>Enable or disable encryption.</td></tr>
  <tr><td> <b>Read replica source</b> </td><td>Choose the identifier of the primary instance to create a Neptune replica for.</td></tr>
  <tr><td> <b>DB instance identifier</b> </td><td>Enter a name for the instance that is unique for your account in the Region that you selected. You might choose to add some intelligence to the name, such as including the Availability Zone selected, for example <code>neptune-us-east-1c</code>.</td></tr>
  <tr><td> <b>Database port</b> </td><td>Port number on which the database accepts connections.</td></tr>
  <tr><td> <b>DB parameter group</b> </td><td>The parameter group for this instance.</td></tr>
  <tr><td> <b>Log exports</b> </td><td>Choose the logs you want to publish, if any.</td></tr>
  <tr><td> <b>Auto Minor Version Upgrade</b> </td><td>Choose <b>Yes</b> if you want to enable your Neptune replica to receive minor Neptune DB engine version upgrades automatically when they become available.<br />The <b>Auto Minor Version Upgrade</b> option applies only to minor upgrades. It does not apply to engine maintenance patches, which are always applied automatically to maintain system stability.</td></tr>
</tbody>
</table>


1. Choose **Create read replica** to create the Neptune replica instance.

To remove a Neptune reader instance from a DB cluster, follow the instructions in [Deleting a DB instance in Amazon Neptune](manage-console-instances-delete.md).