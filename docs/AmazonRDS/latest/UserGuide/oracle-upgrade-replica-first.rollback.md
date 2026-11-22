

# Rolling back Replica First Patching

If you don't start the switchover within 48 hours after the replica's status changes to `replica-patched-pending-switchover` (**Patch pending switchover** in the console), Amazon RDS rolls back the replica to its original engine version. You can also roll back the replica yourself before then. A rollback doesn't affect your primary DB instance, which continues to serve read and write traffic on its current engine version.

## Automatic rollback after 48 hours
<a name="oracle-upgrade-replica-first.rollback.automatic"></a>

When the replica's status changes to `replica-patched-pending-switchover`, a 48-hour window starts. If you don't call `switchover-read-replica` within this window, Amazon RDS rolls back the replica and sends an event notification that the switchover window ended.

If testing shows a problem with the new engine version, you can let the window expire, and Amazon RDS rolls back the replica. To roll back sooner, see [Rolling back manually](#oracle-upgrade-replica-first.rollback.manual).

## Actions that roll back the replica
<a name="oracle-upgrade-replica-first.rollback.actions"></a>

Amazon RDS also rolls back the replica when one of the following happens while the replica's status is `replica-patched-pending-switchover`:


**Actions that roll back a replica during Replica First Patching**  

| Action | What Amazon RDS does | Event message (event ID) | 
| --- | --- | --- | 
| You upgrade your primary DB instance | Rolls back the replica. Your primary DB instance continues with its upgrade, and Amazon RDS then upgrades the replica to the same version, as in a standard upgrade. You don't need to do anything else. | The minor version upgrade was rolled back because the primary DB instance was upgraded before the switchover. No further action is needed. ([RDS-EVENT-0527](USER_Events.Messages.md#RDS-EVENT-0527)) | 
| An automatic minor version upgrade starts on your primary DB instance | Rolls back the replica. Amazon RDS then upgrades your primary DB instance and the replica as a standard automatic minor version upgrade. You don't need to do anything else. For more information, see [Automatic minor version upgrades and Replica First Patching](oracle-upgrade-replica-first.requirements.md#oracle-upgrade-replica-first.requirements.amvu). | The minor version upgrade was rolled back because the primary DB instance was automatically upgraded before the switchover. No further action is needed. ([RDS-EVENT-0548](USER_Events.Messages.md#RDS-EVENT-0548)) | 
| You promote the replica | Rolls back the replica, and then promotes it to a standalone DB instance. To upgrade it, apply a minor version upgrade to it directly. | The minor version upgrade was rolled back because the replica was promoted to a standalone DB instance. To upgrade the DB instance, apply a minor version upgrade directly, or create a new replica and run Replica First Patching again. ([RDS-EVENT-0526](USER_Events.Messages.md#RDS-EVENT-0526)) | 
| You delete your primary DB instance | Rolls back the replica, and promotes it to a standalone DB instance. To upgrade it, apply a minor version upgrade to it directly. | The minor version upgrade was rolled back because the primary DB instance was deleted before the switchover. The replica was promoted to a standalone DB instance. To upgrade the DB instance, apply a minor version upgrade directly, or create a new replica and run Replica First Patching again. ([RDS-EVENT-0528](USER_Events.Messages.md#RDS-EVENT-0528)) | 
| You switch over to a cross-Region replica of your primary DB instance | Rolls back the replica. The new primary DB instance is now in a different AWS Region. To use Replica First Patching again, upgrade a replica that's in the same AWS Region as the new primary DB instance. | The minor version upgrade was rolled back because a switchover to a cross-Region replica was performed before this replica's switchover was completed. Retry the minor version upgrade on the replica. ([RDS-EVENT-0529](USER_Events.Messages.md#RDS-EVENT-0529)) | 
| You roll back manually | Rolls back the replica. | The minor version upgrade was rolled back because a rollback was requested. Retry the minor version upgrade on the replica. ([RDS-EVENT-0549](USER_Events.Messages.md#RDS-EVENT-0549)) | 

## What happens during a rollback
<a name="oracle-upgrade-replica-first.rollback.what-happens"></a>

During a rollback, Amazon RDS does the following:

1. Reverts the Oracle Database software on the replica to the original engine version.

1. Changes the replica's status back to `available`, on the original engine version.

1. Resumes replication from your primary DB instance.

## Rolling back manually
<a name="oracle-upgrade-replica-first.rollback.manual"></a>

You can roll back at any time while the replica's status is `replica-patched-pending-switchover` (**Patch pending switchover** in the console). There's no separate cancel operation. To roll back, modify the replica to use its original engine version, and apply the change immediately. Amazon RDS sends an event notification when it rolls back the replica.

In the console, choose the replica, choose **Modify**, set **DB engine version** to the original version, and apply the change immediately.

With the AWS CLI, use the [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-oracle-replica}} \
    --engine-version {{original-engine-version}} \
    --apply-immediately
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my-oracle-replica}} ^
    --engine-version {{original-engine-version}} ^
    --apply-immediately
```