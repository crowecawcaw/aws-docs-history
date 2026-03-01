# Failover process for an RDS Custom for SQL Server Multi-AZ deployment

If a planned or unplanned outage of your DB instance results from an infrastructure
defect, Amazon RDS automatically switches to a standby replica in another Availability Zone
if you have turned on Multi-AZ. The time that it takes for the failover to complete
depends on the database activity and other conditions at the time that the primary DB
instance became unavailable. Failover times are typically 60 – 120 seconds. However,
large transactions or a lengthy recovery process can increase failover time. When the
failover is complete, it can take additional time for the RDS console to show the new
Availability Zone.

###### Note

You can force a failover manually when you reboot a DB instance with failover.
For more information on rebooting a DB instance, see
[Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md")

Amazon RDS handles failovers automatically so you can resume database operations as quickly as
possible without administrative intervention. The primary DB instance switches over
automatically to the standby replica if any of the conditions described in the following
table occurs. You can view these failover reasons in the RDS event log.

| Failover reason                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `The operating system for the RDS Custom for SQL Server Multi-AZ DB instance is being patched in an offline operation`       | A failover was triggered during the maintenance window for an OS patch or a security update.<br>For more information, see<br>[Maintaining a DB instance](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `The primary host of the RDS Custom for SQL Server Multi-AZ DB instance is unhealthy.`                                       | The Multi-AZ DB instance deployment detected an impaired primary DB instance and failed over.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `The primary host of the RDS Custom for SQL Server Multi-AZ DB instance is unreachable due to loss of network connectivity.` | RDS monitoring detected a network reachability failure to the primary DB instance and triggered a failover.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `The RDS Custom for SQL Server Multi-AZ DB instance was modified by the customer.`                                           | A DB instance modification triggered a failover.<br>For more information, see<br>[Modifying an RDS Custom for SQL Server DB instance](custom-managing.md "custom-managing.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `The storage volume of the primary host of the RDS Custom for SQL Server Multi-AZ DB instance experienced a failure.`        | The Multi-AZ DB instance deployment detected a storage issue on the primary DB instance and failed over.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `The user requested a failover of the RDS Custom for SQL Server Multi-AZ DB instance.`                                       | The RDS Custom for SQL Server Multi-AZ DB instance was rebooted with failover.<br>For more information, see<br>[Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `The RDS Custom for SQL Server Multi-AZ primary DB instance is busy or unresponsive.`                                        | The primary DB instance is unresponsive. We recommend that you try the following steps:<br>• Examine the event logs and CloudWatch logs for excessive CPU, memory, or swap space usage.<br>For more information, see<br>[Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").<br>• Create a rule that triggers on an Amazon RDS event. For more information, see [Creating a rule that triggers on an Amazon RDS event](rds-cloud-watch-events.md "rds-cloud-watch-events.md").<br>• Evaluate your workload to determine whether you're using the appropriate DB instance class.<br>For more information, see<br>[DB instance classes](Concepts.md "Concepts.md"). |

To determine if your Multi-AZ DB instance has failed over, you can do the following:

- Set up DB event subscriptions to notify you by email or SMS that a failover has been initiated.
  For more information about events, see
  [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
- View your DB events by using the RDS console or API operations.
- View the current state of your RDS Custom for SQL Server Multi-AZ DB instance deployment by using the RDS console,
  CLI, or API operations.

## Time to live (TTL) settings with applications using an RDS Custom for SQL Server Multi-AZ deployment

The failover mechanism automatically changes the Domain Name System (DNS) record of
the DB instance to point to the standby DB instance. As a result, you need to
re-establish any existing connections to your DB instance. Ensure that any DNS cache
time-to-live (TTL) configuration value is low, and validate that your application will
not cache DNS for an extended time. A high TTL value might prevent your application from
quickly reconnecting to the DB instance after failover.
