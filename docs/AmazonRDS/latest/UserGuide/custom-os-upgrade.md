

# RDS Custom for SQL Server Operating system updates
<a name="custom-os-upgrade"></a>

RDS Custom for SQL Server provides the following methods to apply operating system updates to your RDS Provided Engine Version (RPEV) instances:
+ *system-update maintenance actions*
+ *database minor version upgrades*
  + DB minor engine version upgrades using RPEV include up to date Operating System updates. This approach is particularly useful if you want to combine OS updates with SQL Server minor version upgrades. For more information, see [Upgrading an Amazon RDS Custom for SQL Server DB instance](custom-upgrading-sqlserver.md).

## Scenarios for Operating system update
<a name="custom-os-upgrade.Scenarios"></a>

There are two ways to ways to manage Operating system updates for your RDS Custom for SQL Server instances:
+ For Single-AZ instances, the instance is unavailable during the Operating system update.
+ For Multi-AZ deployments, RDS applies operating system updates in the following manner:
  + First, RDS performs an Operating system update on the standby instance.
  + RDS fails over to the upgraded standby DB instance, making it the new primary DB instance.
  + Lastly, RDS performs an Operating system update on the new standby DB instance.

The downtime for Multi-AZ deployments is the time it takes for the failover. 

## Applying Operating system updates using system-update maintenance actions
<a name="custom-os-upgrade.SystemUpdates"></a>

To apply Operating system updates to your Amazon RDS RPEV instances, you can use the AWS Management Console, AWS CLI, or RDS API. For more information, see [Operating system updates for RDS DB instances](USER_UpgradeDBInstance.Maintenance.md#OS_Updates).

**Example**  
For Linux, macOS, or Unix:  
**Step 1: Check for available updates**  
Use the `describe-pending-maintenance-actions` command to see if OS updates are available for your instances:  

```
aws rds describe-pending-maintenance-actions
```
Example response:  

```
{
    "PendingMaintenanceActions": [
        {
            "ResourceIdentifier": "arn:aws:rds:us-east-1:111122223333:db:my-sqlserver-instance",
            "PendingMaintenanceActionDetails": [
                {
                    "Action": "system-update",
                    "Description": "New Operating System update is available"
                }
            ]
        }
    ]
}
```
An action type of `system-update` indicates that an OS update is available for your instance.  
**Step 2: Apply the OS update**  
Use the `apply-pending-maintenance-action` command to schedule the update:  

```
aws rds apply-pending-maintenance-action \ 
                --resource-identifier arn:aws:rds:us-east-1:111122223333:db:my-sqlserver-instance \ 
                --apply-action system-update \ 
                --opt-in-type {{immediate}}
```
The `opt-in-type` input has the following options:  
+ `immediate`: Apply the update right away
+ `next-maintenance`: Apply the update during the next scheduled maintenance window
+ `undo-opt-in`: Cancel a previously scheduled update
Example response:  

```
{
    "ResourcePendingMaintenanceActions": {
        "ResourceIdentifier": "arn:aws:rds:us-east-1:111122223333:db:my-sqlserver-instance",
        "PendingMaintenanceActionDetails": [
            {
                "Action": "system-update",
                "AutoAppliedAfterDate": "2024-04-10T20:41:01.695000+00:00",
                "ForcedApplyDate": "2024-04-10T20:41:01.694000+00:00",
                "CurrentApplyDate": "2024-04-10T20:41:01.695000+00:00",
                "Description": "New Operating System update is available"
            }
        ]
    }
}
```

## OS update notifications
<a name="custom-os-upgrade.OSNotifications"></a>

To be notified when a new, optional operating system patch becomes available, you can subscribe to [RDS-EVENT-0230](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html#RDS-EVENT-0230) in the security patching event category. For information about subscribing to RDS events, see [Subscribing to Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html).

## Considerations
<a name="custom-os-upgrade.Considerations"></a>

The following consideations and limitations apply to OS updates:
+ Any operating system customizations made to the C:\\ drive are not preserved during Operating system updates. 
+ We recommend taking a manual snapshot before applying updates.