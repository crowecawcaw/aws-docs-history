

# Upgrading with Replica First Patching

With Replica First Patching, you upgrade the minor engine version of an [RDS for Oracle replica](oracle-read-replicas.overview.md) first, and then switch over to it. Your primary DB instance continues to serve read and write traffic while the replica is upgraded. Amazon RDS uses Oracle Data Guard switchover to switch the roles of your primary DB instance and the upgraded replica.

With a standard minor version upgrade, Amazon RDS takes your primary DB instance offline while it upgrades the Oracle Database software. With Replica First Patching, the software upgrade happens on the replica instead. Your primary DB instance is unavailable only during the switchover and while Amazon RDS completes the upgrade on the new primary DB instance.

Use Replica First Patching when you want to do the following:
+ Test the new minor engine version with your read traffic before you switch over, if your Oracle replica is in read-only mode.
+ Reduce downtime during minor version upgrades.

**Topics**
+ [How Replica First Patching works](#oracle-upgrade-replica-first.how-it-works)
+ [DB instance status during Replica First Patching](#oracle-upgrade-replica-first.status)
+ [The 48-hour switchover window](#oracle-upgrade-replica-first.window)
+ [Connecting to the new primary DB instance](#oracle-upgrade-replica-first.connecting)
+ [Cost of Replica First Patching](#oracle-upgrade-replica-first.cost)
+ [Requirements and limitations for Replica First Patching](oracle-upgrade-replica-first.requirements.md)
+ [Performing Replica First Patching](oracle-upgrade-replica-first.performing.md)
+ [Rolling back Replica First Patching](oracle-upgrade-replica-first.rollback.md)

## How Replica First Patching works
<a name="oracle-upgrade-replica-first.how-it-works"></a>

Replica First Patching has three phases. Your primary DB instance serves read and write traffic until you start the switchover.

1. **You upgrade the replica.** You modify the replica to use the target minor engine version. Amazon RDS then replaces the Oracle Database software on the replica with the new version. Your primary DB instance isn't affected. If the replica is in read-only mode, read traffic to the replica is briefly interrupted while Amazon RDS replaces the software.

1. **You switch over to the replica.** When you're ready, you initiate a switchover to the replica. The replica becomes the new primary DB instance, and your previous primary DB instance becomes a replica.

1. **Amazon RDS completes the upgrade.** Amazon RDS completes the upgrade on the new primary DB instance by running the Oracle data dictionary update (datapatch). After datapatch finishes and the new primary DB instance is available and accepting connections, Amazon RDS upgrades your previous primary DB instance (now a replica) and your other replicas, including cross-Region replicas.

## DB instance status during Replica First Patching
<a name="oracle-upgrade-replica-first.status"></a>

During Replica First Patching, the status of the replica changes as follows:
+ `available`: The replica is operating normally, before you start.
+ `upgrading`: Amazon RDS is upgrading the Oracle Database software on the replica.
+ `replica-patched-pending-switchover` (**Patch pending switchover** in the console): Amazon RDS finished upgrading the software on the replica, and the replica is waiting for you to switch over to it. The upgrade finishes after the switchover.

Your primary DB instance's status stays `available` until you start the switchover.

## The 48-hour switchover window
<a name="oracle-upgrade-replica-first.window"></a>

When the replica's status changes to `replica-patched-pending-switchover`, you have 48 hours to start the switchover. If you don't start it within 48 hours, Amazon RDS rolls back the replica to its original minor engine version, and the replica's status returns to `available`. For more information, see [Rolling back Replica First Patching](oracle-upgrade-replica-first.rollback.md).

You can use this time to test the upgraded replica, for example by sending read traffic to it if the replica is in read-only mode.

To see how much time is left, open the **Databases** page in the Amazon RDS console and choose **Patch pending switchover** in the replica's **Status** column. The pop-up shows the time remaining and an **Initiate switchover** button. Amazon RDS also sends event notifications when the window starts and when half of it has passed. For more information, see [Step 2: Monitor the replica](oracle-upgrade-replica-first.performing.md#oracle-upgrade-replica-first.performing.monitor).

## Connecting to the new primary DB instance
<a name="oracle-upgrade-replica-first.connecting"></a>

**Note**  
We recommend that your applications connect through the Primary Endpoint when you use Replica First Patching.

After the switchover, the replica that you upgraded is the primary DB instance. How your applications connect to it depends on the endpoint that they use:
+ **Primary Endpoint**: The Primary Endpoint is a DNS name that resolves to the current primary DB instance in your replica configuration. After the switchover, it resolves to the new primary DB instance, so your applications connect to it without any change to their connection strings. Every RDS for Oracle Enterprise Edition DB instance has a Primary Endpoint at no additional charge, and you don't have to create it. For more information, see [Using the Primary Endpoint for Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-primary-endpoint.html).
+ **Instance endpoint**: If your applications connect through the instance endpoint of your previous primary DB instance, update them to use the instance endpoint of the new primary DB instance after the switchover.

## Cost of Replica First Patching
<a name="oracle-upgrade-replica-first.cost"></a>

Replica First Patching doesn't incur additional costs. You pay for your replica as usual. To create a replica in read-only mode, you need the Oracle Active Data Guard option.