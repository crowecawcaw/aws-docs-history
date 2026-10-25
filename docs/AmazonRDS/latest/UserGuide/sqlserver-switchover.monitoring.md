

# Monitoring the SQL Server switchover
<a name="sqlserver-switchover.monitoring"></a>

To check the status of your instances, use the AWS CLI command `describe-db-instances`. The following command checks the status of the DB instance {{replica-to-be-made-primary}}. This DB instance was a read replica before the switchover, but is the new primary DB instance after the switchover.

```
aws rds describe-db-instances \
    --db-instance-identifier {{replica-to-be-made-primary}}
```

You can also confirm the role change in the Amazon RDS console. On the **Databases** page, the **Role** value of the switchover target changes from **Replica** to **Source**.

To look for switchover-related events, use the AWS CLI command `describe-events`. The following example looks for events on the {{replica-to-be-made-primary}} instance.

```
aws rds describe-events \
    --source-identifier {{replica-to-be-made-primary}} \
    --source-type db-instance
```