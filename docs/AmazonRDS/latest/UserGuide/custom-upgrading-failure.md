

# Troubleshooting an upgrade failure for an RDS Custom for Oracle DB instance
<a name="custom-upgrading-failure"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

If an RDS Custom DB instance upgrade fails, an RDS event is generated and the DB instance status becomes `upgrade-failed`.

You can see this status by using the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) AWS CLI command, as shown in the following example.

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
+ Retrying the same upgrade
+ Pausing and resuming RDS Custom automation
+ Point-in-time recovery (PITR)
+ Deleting the DB instance

**Note**  
If automation has been paused for the RDS Custom DB instance, you can't retry the upgrade until you resume automation.  
The same actions apply to an upgrade failure for an RDS-managed read replica as for the primary.

For more information, see [Troubleshooting upgrades for RDS Custom for Oracle](custom-troubleshooting.md#custom-troubleshooting-upgrade).