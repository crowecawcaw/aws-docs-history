

# Maintenance preparation in RDS for Oracle

Amazon RDS can prepare resources for minor version upgrades and operating system updates on an RDS for Oracle DB instance before the maintenance window starts. Before the window, the preparation does work that doesn't require downtime. This helps reduce the time that the maintenance takes.

The preparation starts up to 30 minutes before the maintenance window. If the preparation doesn't finish, Amazon RDS applies the maintenance without it. You don't need to take any action.

Amazon RDS prepares resources for the following maintenance only when it applies the maintenance during the maintenance window:
+ Minor version upgrades, including upgrades that Amazon RDS schedules because automatic minor version upgrade is turned on. For more information, see [Oracle minor version upgrades](USER_UpgradeDBInstance.Oracle.Minor.md).
+ Operating system updates, which use the `system-update` maintenance action. For more information, see [Operating system updates for RDS DB instances](USER_UpgradeDBInstance.Maintenance.md#OS_Updates).

Amazon RDS doesn't prepare resources for read replicas, for major version upgrades, or for upgrades and updates that you apply immediately.

**Topics**
+ [How preparation affects your DB instance](#maintenance-preparation.availability)
+ [Events for maintenance preparation](#maintenance-preparation.events)

## How preparation affects your DB instance
<a name="maintenance-preparation.availability"></a>

During the preparation, the status of your DB instance stays `available`, and the DB instance accepts connections and API requests as usual. The preparation doesn't add or change any value that the RDS API returns for the DB instance. Amazon RDS doesn't charge for the resources that it stages for the preparation.

Amazon RDS doesn't block or delay any operation because of the preparation. In the following cases, Amazon RDS applies the maintenance without the preparation:
+ An operation on the DB instance conflicts with the preparation. Amazon RDS rolls back the staged resources, and the operation continues. If the rollback happens during the maintenance window, the maintenance can take longer than it does without the preparation.
+ Amazon RDS can't finish the preparation. Amazon RDS still applies the maintenance during the maintenance window.

**Note**  
We recommend that you avoid unnecessary changes to your DB instance during the 30 minutes before the maintenance window starts. If a change conflicts with the preparation, the maintenance doesn't get the benefit of the preparation.

## Events for maintenance preparation
<a name="maintenance-preparation.events"></a>

Amazon RDS publishes the following events for maintenance preparation. The events have the DB instance source type and the `maintenance` category.

[RDS-EVENT-0624](USER_Events.Messages.md#RDS-EVENT-0624)  
Amazon RDS started to prepare resources for the maintenance.

[RDS-EVENT-0625](USER_Events.Messages.md#RDS-EVENT-0625)  
Amazon RDS staged the resources for the maintenance.

[RDS-EVENT-0626](USER_Events.Messages.md#RDS-EVENT-0626)  
Amazon RDS couldn't stage the resources. Amazon RDS applies the maintenance without the preparation.

[RDS-EVENT-0627](USER_Events.Messages.md#RDS-EVENT-0627)  
Amazon RDS rolled back the staged resources because an operation on the DB instance conflicted with the preparation.

To get notifications for these events, subscribe to the `maintenance` category. For more information, see [Subscribing to Amazon RDS event notification](USER_Events.Subscribing.md). For more information about the event messages, see [DB instance events](USER_Events.Messages.md#USER_Events.Messages.instance).