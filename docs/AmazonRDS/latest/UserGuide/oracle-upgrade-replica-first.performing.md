

# Performing Replica First Patching

Before you begin, make sure that your DB instances meet the requirements in [Requirements and limitations for Replica First Patching](oracle-upgrade-replica-first.requirements.md).

## Step 1: Upgrade the replica
<a name="oracle-upgrade-replica-first.performing.upgrade"></a>

### Console
<a name="oracle-upgrade-replica-first.performing.upgrade.console"></a>

**To upgrade the replica**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the replica that you want to upgrade.

1. Choose **Modify**.

1. For **DB engine version**, choose the target minor engine version.

1. Choose **Continue**, and then check the summary of modifications.

1. Choose **Apply immediately** or **Apply during the next scheduled maintenance window**, and then choose **Modify DB instance**.

### AWS CLI
<a name="oracle-upgrade-replica-first.performing.upgrade.cli"></a>

To upgrade the replica, use the AWS CLI [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command with the following options:
+ `--db-instance-identifier` – The name of your replica.
+ `--engine-version` – The target minor engine version.
+ `--apply-immediately` – Upgrades the replica now. To upgrade it during the replica's next maintenance window, specify `--no-apply-immediately` instead.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-oracle-replica}} \
    --engine-version {{19.0.0.0.ru-2026-07.rur-2026-07.r1}} \
    --apply-immediately
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my-oracle-replica}} ^
    --engine-version {{19.0.0.0.ru-2026-07.rur-2026-07.r1}} ^
    --apply-immediately
```

### RDS API
<a name="oracle-upgrade-replica-first.performing.upgrade.api"></a>

To upgrade the replica, call the Amazon RDS API [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation with `DBInstanceIdentifier` and `EngineVersion`. Set `ApplyImmediately` to `true` to upgrade the replica now, or to `false` to upgrade it during its next maintenance window.

If you schedule the upgrade for the replica's next maintenance window, Amazon RDS upgrades the replica during that window. The 48-hour switchover window starts when the upgrade on the replica finishes. If you upgrade your primary DB instance before the scheduled replica upgrade starts, Amazon RDS cancels the scheduled replica upgrade and sends an event notification.

## Step 2: Monitor the replica
<a name="oracle-upgrade-replica-first.performing.monitor"></a>

The replica's status is `upgrading` while Amazon RDS upgrades it. When the status changes to `replica-patched-pending-switchover` (**Patch pending switchover** in the console), the replica is ready for a switchover, and the 48-hour switchover window starts.

To see how much time is left in the window, open the **Databases** page in the Amazon RDS console and choose **Patch pending switchover** in the replica's **Status** column. The pop-up shows the time remaining and an **Initiate switchover** button.

To check the status with the AWS CLI, use the [`describe-db-instances`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds describe-db-instances \
    --db-instance-identifier {{my-oracle-replica}} \
    --query 'DBInstances[0].DBInstanceStatus'
```
For Windows:  

```
aws rds describe-db-instances ^
    --db-instance-identifier {{my-oracle-replica}} ^
    --query "DBInstances[0].DBInstanceStatus"
```

Amazon RDS also sends event notifications during Replica First Patching. To receive them, subscribe to Amazon RDS event notifications for the replica, and include both the `maintenance` and `notification` event categories. For more information, see [Subscribing to Amazon RDS event notification](USER_Events.Subscribing.md).

The following table shows the events for the switchover window. For the full list of events, see [DB instance events](USER_Events.Messages.md#USER_Events.Messages.instance).


**Events for the Replica First Patching switchover window**  

| When Amazon RDS sends it | Event message | Category | Event ID | 
| --- | --- | --- | --- | 
| The replica is upgraded and ready for a switchover. The 48-hour window starts. | The replica finished upgrading and is ready for switchover. Switch over the replica within {{hours}} hours to complete Replica First Patching, or the upgrade is automatically rolled back. Previous version: {{version}}. New version: {{version}}. | maintenance | [RDS-EVENT-0510](USER_Events.Messages.md#RDS-EVENT-0510) | 
| Half of the switchover window has passed. | Replica First Patching for replica '{{name}}' is halfway through its switchover window. Switch over the replica before the window expires to complete the upgrade, or the upgrade is automatically rolled back. | notification | [RDS-EVENT-0551](USER_Events.Messages.md#RDS-EVENT-0551) | 
| The window ended, and Amazon RDS rolled back the replica. | The minor version upgrade was rolled back because the switchover wasn't performed within the {{hours}} hour window. Retry the minor version upgrade on the replica. | notification | [RDS-EVENT-0511](USER_Events.Messages.md#RDS-EVENT-0511) | 

For the events that Amazon RDS sends when other actions roll back the replica, see [Actions that roll back the replica](oracle-upgrade-replica-first.rollback.md#oracle-upgrade-replica-first.rollback.actions).

## Step 3: Switch over to the replica
<a name="oracle-upgrade-replica-first.performing.switchover"></a>

Before you switch over, consider the following:
+ If the replica is in read-only mode, test the new engine version by sending read traffic to the replica.
+ Plan the switchover for a period of low traffic, because your primary DB instance is unavailable during the switchover and while Amazon RDS completes the upgrade.
+ Start the switchover within 48 hours after the replica's status changes to `replica-patched-pending-switchover`.
+ Make sure that your applications can reconnect to the new primary DB instance. We recommend that your applications connect through the [Primary Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-primary-endpoint.html), which resolves to the new primary DB instance after the switchover. If your applications connect through instance endpoints, plan to update them after the switchover.

### Console
<a name="oracle-upgrade-replica-first.performing.switchover.console"></a>

**To switch over to the replica**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the replica whose status is **Patch pending switchover**.

1. For **Actions**, choose **Switch over replica**.

1. Choose **I acknowledge**, and then choose **Switch over replica**.

You can also start the switchover from the **Databases** page: choose **Patch pending switchover** in the replica's **Status** column, and then choose **Initiate switchover** in the pop-up.

### AWS CLI
<a name="oracle-upgrade-replica-first.performing.switchover.cli"></a>

To switch over to the replica, use the AWS CLI [`switchover-read-replica`](https://docs.aws.amazon.com/cli/latest/reference/rds/switchover-read-replica.html) command.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds switchover-read-replica \
    --db-instance-identifier {{my-oracle-replica}}
```
For Windows:  

```
aws rds switchover-read-replica ^
    --db-instance-identifier {{my-oracle-replica}}
```

### RDS API
<a name="oracle-upgrade-replica-first.performing.switchover.api"></a>

To switch over to the replica, call the Amazon RDS API [`SwitchoverReadReplica`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverReadReplica.html) operation with `DBInstanceIdentifier` set to the name of your replica.

**What happens during the switchover**

1. Amazon RDS starts an Oracle Data Guard switchover between your primary DB instance and the upgraded replica. Existing connections to your primary DB instance are dropped.

1. The replica becomes the new primary DB instance, and your previous primary DB instance becomes a replica.

1. Amazon RDS completes the upgrade on the new primary DB instance by running the Oracle data dictionary update (datapatch). The new primary DB instance accepts read and write connections after the upgrade is complete.

1. Amazon RDS upgrades your previous primary DB instance (now a replica) and your other replicas, including cross-Region replicas, to the new engine version.

## Step 4: Verify the upgrade
<a name="oracle-upgrade-replica-first.performing.verify"></a>

1. Check that the new primary DB instance's status is `available` and that it runs the target engine version.  
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws rds describe-db-instances \
       --db-instance-identifier {{my-oracle-replica}} \
       --query 'DBInstances[0].[DBInstanceStatus,EngineVersion]'
   ```

   For Windows:

   ```
   aws rds describe-db-instances ^
       --db-instance-identifier {{my-oracle-replica}} ^
       --query "DBInstances[0].[DBInstanceStatus,EngineVersion]"
   ```

1. Check that your applications can read and write. If they connect through the Primary Endpoint, they don't need any change. Otherwise, update them to use the instance endpoint of the new primary DB instance.

1. Check that your previous primary DB instance (now a replica) is being upgraded. Its status is `upgrading` until the upgrade finishes.

## Other replicas during the switchover
<a name="oracle-upgrade-replica-first.performing.other-replicas"></a>

If your primary DB instance has other replicas, including cross-Region replicas, replication to them is briefly interrupted during the switchover. Afterward, they resume replication from the new primary DB instance automatically, and Amazon RDS upgrades them to the new engine version.