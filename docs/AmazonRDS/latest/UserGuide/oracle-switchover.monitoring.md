# Monitoring the Oracle Data Guard switchover

To check the status of your instances, use the AWS CLI command `describe-db-instances`. The following
command checks the status of the DB instance `orcl2`. This database was a standby database
before the switchover, but is the new primary database after the switchover.

```
aws rds describe-db-instances \
    --db-instance-identifier `orcl2`
```

To confirm that the switchover completed successfully, query `V$DATABASE.OPEN_MODE`. Check that the value
for the new primary database is `READ WRITE`.

```
SELECT OPEN_MODE FROM V$DATABASE;
```

To look for switchover-related events, use the AWS CLI command `describe-events`. The following
example looks for events on the `orcl2` instance.

```
aws rds describe-events \
    --source-identifier `orcl2` \
    --source-type db-instance
```
