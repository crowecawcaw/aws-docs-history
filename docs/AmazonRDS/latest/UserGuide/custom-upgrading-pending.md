# Viewing pending database upgrades for RDS Custom DB

instances

You can see pending database upgrades for your Amazon RDS Custom DB instances by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") or
[describe-pending-maintenance-actions](../../../cli/latest/reference/rds/describe-pending-maintenance-actions.md "../../../cli/latest/reference/rds/describe-pending-maintenance-actions.md") AWS CLI command.

However, this approach doesn't work if you used the `--apply-immediately`
option or if the upgrade is in progress.

The following `describe-db-instances` command shows pending database upgrades
for `my-custom-instance`.

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
        }
    ]
}
```
