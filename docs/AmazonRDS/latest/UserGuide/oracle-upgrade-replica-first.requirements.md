

# Requirements and limitations for Replica First Patching

Before you use Replica First Patching, review the following requirements and limitations.

## Supported AWS Regions for Replica First Patching
<a name="oracle-upgrade-replica-first.requirements.regions"></a>

Replica First Patching is available in all commercial AWS Regions where RDS for Oracle is available.

## Requirements for Replica First Patching
<a name="oracle-upgrade-replica-first.requirements.list"></a>

To use Replica First Patching, your DB instances must meet the following requirements:
+ Your primary DB instance runs Oracle Database Enterprise Edition. Standard Edition 2 isn't supported.
+ Your primary DB instance has at least one Oracle replica in the same AWS Region. This same-Region replica is the replica that you upgrade first. The replica can be in read-only mode or mounted mode. Read-only mode requires Oracle Active Data Guard.
+ The replica's status is `available`.
+ The target engine version is a newer minor engine version of the same major version as your DB instances. For example, if your DB instances run 19.0.0.0.ru-2026-07.mrp-2026-07.r1, the target can be 19.0.0.0.ru-2026-07.mrp-2026-09.r2. The target can be a Release Update (RU), Monthly Recommended Patch (MRP), or a Supplemental Patch Bundle (SPB).
+ Your primary DB instance doesn't have a pending or scheduled maintenance action that upgrades it to the same target engine version.
+ Your replica meets the requirements for an Oracle Data Guard switchover, including that automatic backups are turned on. For more information, see [Requirements for the Oracle Data Guard switchover](oracle-switchover.preparing.md).

Multi-AZ deployments are supported. Amazon RDS updates the Multi-AZ standby instance automatically as part of the switchover.

## Limitations for Replica First Patching
<a name="oracle-upgrade-replica-first.requirements.limitations"></a>

You can't start Replica First Patching in the following cases:
+ A Replica First Patching operation is already in progress on the same replica or on another replica of the same primary DB instance.
+ The target engine version is a major version. Replica First Patching supports only minor version upgrades.
+ The replica that you want to upgrade is in a different AWS Region from your primary DB instance. Your primary DB instance can still have cross-Region replicas, but you can't use a cross-Region replica for Replica First Patching.
+ Your primary DB instance already has a pending or scheduled maintenance action for the same target engine version.

## Operations that aren't allowed while a replica is waiting for a switchover
<a name="oracle-upgrade-replica-first.requirements.blocked"></a>

A replica's status changes to `replica-patched-pending-switchover` (**Patch pending switchover** in the console) when Amazon RDS finishes upgrading its Oracle Database software. The replica keeps this status until you switch over to it, it's rolled back, or the 48-hour window ends.

While a replica has this status, you can't do the following:
+ Start Replica First Patching on another replica of the same primary DB instance.
+ Change the option group of the replica. You can change the option group only through your primary DB instance, after it finishes upgrading.
+ Change the parameter group of the replica. The replica's database isn't fully upgraded yet, and a parameter change could cause the rest of the upgrade to fail.

## Automatic minor version upgrades and Replica First Patching
<a name="oracle-upgrade-replica-first.requirements.amvu"></a>

Replica First Patching and automatic minor version upgrade are separate operations. If automatic minor version upgrade is turned on for your primary DB instance and an upgrade is scheduled for its maintenance window, the automatic upgrade takes precedence. If the maintenance window starts before you switch over, Amazon RDS rolls back the replica and sends an event notification that explains why. Then Amazon RDS upgrades your primary DB instance and its replicas as a standard automatic minor version upgrade.

To complete Replica First Patching instead, do one of the following before the maintenance window starts:
+ Switch over to the replica.
+ Turn off automatic minor version upgrade for your primary DB instance. This unschedules the pending automatic upgrade. You can turn it on again after the upgrade is complete. For more information, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades).