# Failing over a Multi-AZ DB instance for Amazon RDS

If a planned or unplanned outage of your Multi-AZ DB instance results from an infrastructure
defect, Amazon RDS automatically switches to a standby replica in another Availability Zone.

The time that it takes for the failover to complete depends on the database activity
and other conditions at the time the primary DB instance became unavailable. Failover
times are typically 60–120 seconds. However, large transactions or a lengthy
recovery process can increase failover time. When the failover is complete, it can take
additional time for the RDS console to reflect the new Availability Zone.

###### Note

You can force a failover manually when you reboot a Multi-AZ DB instance. For more
information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

Amazon RDS handles failovers automatically so you can resume database operations as quickly as possible without administrative
intervention. The primary DB instance switches over automatically to the standby replica if any of the conditions described in
the following table occurs. You can view these failover reasons in the event log.

| Failover reason                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`The operating system underlying the RDS database instance is being patched in an offline<br>operation.`** | A failover was triggered during the maintenance window for an OS patch or a security update.<br>For more information, see [Maintaining a DB instance](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **`The primary host of the RDS Multi-AZ instance is unhealthy.`**                                            | The Multi-AZ DB instance deployment detected an impaired primary DB instance and failed over.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **`The primary host of the RDS Multi-AZ instance is unreachable due to loss of network<br>connectivity.`**   | RDS monitoring detected a network reachability failure to the primary DB instance and triggered a<br>failover.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **`The RDS instance was modified by customer.`**                                                             | An RDS DB instance modification triggered a failover.<br>For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **`The RDS Multi-AZ primary instance is busy and unresponsive.`**                                            | The primary DB instance is unresponsive. We recommend that you do the following:<br>• Examine the event and CloudWatch logs for excessive CPU, memory, or swap space usage. For more<br>information, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md") and [Creating a rule that triggers on an Amazon RDS event](rds-cloud-watch-events.md "rds-cloud-watch-events.md").<br>• Evaluate your workload to determine whether you're using the appropriate DB instance class. For<br>more information, see [DB instance classes](Concepts.md "Concepts.md").<br>• Use Enhanced Monitoring for real-time operating system metrics. For more information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md").<br>• Use Performance Insights to help analyze any issues that affect your DB instance's performance.<br>For more information, see [Monitoring DB load with Performance Insights on Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md").<br>For more information on these recommendations, see [Monitoring tools for Amazon RDS](MonitoringOverview.md "MonitoringOverview.md") and [Best practices for Amazon RDS](CHAP_BestPractices.md "CHAP_BestPractices.md"). |
| **`The storage volume underlying the primary host of the RDS Multi-AZ instance experienced a<br>failure.`**  | The Multi-AZ DB instance deployment detected a storage issue on the primary DB instance and failed over.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`The user requested a failover of the DB instance.`**                                                      | You rebooted the DB instance and chose **Reboot with failover**.<br>For more information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

To determine if your Multi-AZ DB instance has failed over, you can do the following:

- Set up DB event subscriptions to notify you by email or SMS that a failover has been
  initiated. For more information about events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
- View your DB events by using the RDS console or API operations.
- View the current state of your Multi-AZ DB instance deployment by using the RDS
  console or API operations.
  For information on how you can respond to failovers, reduce recovery time, and other best
  practices for Amazon RDS, see [Best practices for Amazon RDS](CHAP_BestPractices.md "CHAP_BestPractices.md").

## Setting the JVM TTL for DNS name lookups

The failover mechanism automatically changes the Domain Name System (DNS) record of the DB
instance to point to the standby DB instance. As a result, you need to re-establish
any existing connections to your DB instance. In a Java virtual machine (JVM)
environment, due to how the Java DNS caching mechanism works, you might need to
reconfigure JVM settings.

The JVM caches DNS name lookups. When the JVM resolves a host name to an IP address, it caches the IP address for a specified period
of time, known as the _time-to-live_ (TTL).

Because AWS resources use DNS name entries that occasionally change, we recommend that you configure your JVM with a TTL value of
no more than 60 seconds. Doing this makes sure that when a resource's IP address changes, your application can receive
and use the resource's new IP address by requerying the DNS.

On some Java configurations, the JVM default TTL is set so that it never refreshes DNS entries until the JVM is restarted. Thus, if
the IP address for an AWS resource changes while your application is still running, it can't use that resource until
you manually restart the JVM and the cached IP information is refreshed. In this case, it's crucial to set the
JVM's TTL so that it periodically refreshes its cached IP information.

You can get the JVM default TTL by retrieving the [`networkaddress.cache.ttl`](https://docs.oracle.com/javase/7/docs/technotes/guides/net/properties.html "https://docs.oracle.com/javase/7/docs/technotes/guides/net/properties.html") property value:

```
String ttl = java.security.Security.getProperty("networkaddress.cache.ttl");
```

###### Note

The default TTL can vary according to the version of your JVM and whether a security
manager is installed. Many JVMs provide a default TTL less than 60 seconds. If
you're using such a JVM and not using a security manager, you can ignore
the rest of this topic. For more information on security managers in Oracle, see
[The security manager](https://docs.oracle.com/javase/tutorial/essential/environment/security.html "https://docs.oracle.com/javase/tutorial/essential/environment/security.html") in the Oracle documentation.

To modify the JVM's TTL, set the `networkaddress.cache.ttl` property
value. Use one of the following methods, depending on your needs:

- To set the property value globally for all applications that use the JVM, set `networkaddress.cache.ttl` in the
  `$JAVA_HOME/jre/lib/security/java.security` file.

```
networkaddress.cache.ttl=60
```

- To set the property locally for your application only, set `networkaddress.cache.ttl` in your application's
  initialization code before any network connections are established.

```
java.security.Security.setProperty("networkaddress.cache.ttl" , "60");
```
