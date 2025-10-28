# Troubleshooting an upgrade failure for an RDS Custom for Oracle DB instance

If an RDS Custom DB instance upgrade fails, an RDS event is generated and the DB instance status becomes `upgrade-failed`.

You can see this status by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") AWS CLI command,
as shown in the following example.

```
aws rds describe-db-instances --db-instance-identifier my-custom-instance
```

The output resembles the following.

```
{
    "DBInstances": [
        {
           "DBInstanceIdentifier": "my-custom-instance",
            "EngineVersion": "19.my_cev1",
            ...
            "PendingModifiedValues": {
                "EngineVersion": "19.my_cev3"
            ...
            }
            "DBInstanceStatus": "upgrade-failed"
        }
    ]
}
```

After an upgrade failure, all database actions are blocked except for modifying the DB instance to perform the following tasks:

- Retrying the same upgrade
- Pausing and resuming RDS Custom automation
- Point-in-time recovery (PITR)
- Deleting the DB instance

###### Note

If automation has been paused for the RDS Custom DB instance, you can't retry the upgrade until you resume automation.

The same actions apply to an upgrade failure for an RDS-managed read replica as for the primary.

For more information, see [Troubleshooting upgrades for RDS Custom for Oracle](custom-troubleshooting.md#custom-troubleshooting-upgrade "custom-troubleshooting.md#custom-troubleshooting-upgrade").
