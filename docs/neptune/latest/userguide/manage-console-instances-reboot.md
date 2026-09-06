

# Rebooting a DB instance in Amazon Neptune
<a name="manage-console-instances-reboot"></a>

 In some cases, if you modify an Amazon Neptune DB instance, change the DB parameter group that is associated with the instance, or change a static DB parameter in a parameter group that the instance uses, you must reboot the instance to apply the changes.

Rebooting a DB instance restarts the database engine service. A reboot also applies to the DB instance any changes to the associated DB parameter group that were pending. Rebooting a DB instance results in a momentary outage of the instance, during which the DB instance status is set to *rebooting*. If the Neptune instance is configured for Multi-AZ, the reboot might be conducted through a failover. A Neptune event is created when the reboot is completed.

If your DB instance is a Multi-AZ deployment, you can force a failover from one Availability Zone to another when you choose the **Reboot** option. When you force a failover of your DB instance, Neptune automatically switches to a standby replica in another Availability Zone. It then updates the DNS record for the DB instance to point to the standby DB instance. As a result, you must clean up and re-establish any existing connections to your DB instance. 

**Reboot with failover** is beneficial when you want to simulate a failure of a DB instance for testing or restore operations to the original Availability Zone after a failover occurs. For more information, see [High Availability (Multi-AZ)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) in the *Amazon RDS User Guide*. When you reboot a DB cluster, it fails over to the standby replica. Rebooting a Neptune replica does not initiate a failover.

The time required to reboot is a function of the crash recovery process. To improve the reboot time, we recommend that you reduce database activities as much as possible during the reboot process to reduce rollback activity for in-transit transactions.

On the console, the **Reboot** option might be disabled if the DB instance is not in the **Available** state. This can be due to several reasons, such as an in-progress backup, a customer-requested modification, or a maintenance window action.

**Note**  
Before [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.0.md), all the read-replicas in a DB cluster were automatically rebooted whenever the primary (writer) instance restarted.  
Starting with [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.0.md), restarting the primary instance does not cause any of the replicas to restart. This means that if you are changing a cluster parameter, you must restart each instance separately to pick up the parameter change (see [Parameter groups](parameter-groups.md)).

**To reboot a DB instance using the Neptune console**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Databases**. 

1. Choose the DB instance that you want to reboot. 

1.  Choose **Instance actions**, and then choose **Reboot**.

1. To force a failover from one Availability Zone to another, select **Reboot with failover?** in the **Reboot DB Instance** dialog box.

1. Choose **Reboot**. To cancel the reboot, choose **Cancel** instead. 