# Finding information about replicated backups for Amazon RDS

You can use the following CLI commands to find information about replicated backups:

- [`describe-source-regions`](../../../cli/latest/reference/rds/describe-source-regions.md "../../../cli/latest/reference/rds/describe-source-regions.md")
- [`describe-db-instances`](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
- [`describe-db-instance-automated-backups`](../../../cli/latest/reference/rds/describe-db-instance-automated-backups.md "../../../cli/latest/reference/rds/describe-db-instance-automated-backups.md")
  The following `describe-source-regions` example lists the source AWS Regions from which automated backups can be
  replicated to the US West (Oregon) destination Region.

###### To show information about source Regions

- Run the following command.

```
aws rds describe-source-regions --region us-west-2
```

The output shows that backups can be replicated from US East (N. Virginia), but not from US East (Ohio) or
US West (N. California), into US West (Oregon).

```
{
    "SourceRegions": [
        ...
        {
            "RegionName": "us-east-1",
            "Endpoint": "https://rds.us-east-1.amazonaws.com",
            "Status": "available",
            "SupportsDBInstanceAutomatedBackupsReplication": true
        },
        {
            "RegionName": "us-east-2",
            "Endpoint": "https://rds.us-east-2.amazonaws.com",
            "Status": "available",
            "SupportsDBInstanceAutomatedBackupsReplication": false
        },
            "RegionName": "us-west-1",
            "Endpoint": "https://rds.us-west-1.amazonaws.com",
            "Status": "available",
            "SupportsDBInstanceAutomatedBackupsReplication": false
        }
    ]
}
```

The following `describe-db-instances` example shows the automated backups for a DB instance.

###### To show the replicated backups for a DB instance

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds describe-db-instances \
--db-instance-identifier `mydatabase`
```

For Windows:

```
aws rds describe-db-instances ^
--db-instance-identifier `mydatabase`
```

The output includes the replicated backups.

```
{
    "DBInstances": [
        {
            "StorageEncrypted": false,
            "Endpoint": {
                "HostedZoneId": "Z1PVIF0B656C1W",
                "Port": 1521,
            ...

            "BackupRetentionPeriod": 7,
            "DBInstanceAutomatedBackupsReplications": [{"DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE"}]
        }
    ]
}
```

The following `describe-db-instance-automated-backups` example shows the automated backups for a DB
instance.

###### To show automated backups for a DB instance

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds describe-db-instance-automated-backups \
--db-instance-identifier `mydatabase`
```

For Windows:

```
aws rds describe-db-instance-automated-backups ^
--db-instance-identifier `mydatabase`
```

The output shows the source DB instance and automated backups in US West (Oregon), with backups replicated to
US East (N. Virginia).

```
{
    "DBInstanceAutomatedBackups": [
        {
            "DBInstanceArn": "arn:aws:rds:us-west-2:868710585169:db:mydatabase",
            "DbiResourceId": "db-L2IJCEXJP7XQ7HOJ4SIEXAMPLE",
            "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-west-2:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE",
            "BackupRetentionPeriod": 7,
            "DBInstanceAutomatedBackupsReplications": [{"DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE"}]
            "Region": "us-west-2",
            "DBInstanceIdentifier": "mydatabase",
            "RestoreWindow": {
                "EarliestTime": "2020-10-26T01:09:07Z",
                "LatestTime": "2020-10-31T19:09:53Z",
            }
            ...
        }
    ]
}
```

The following `describe-db-instance-automated-backups` example uses the
`--db-instance-automated-backups-arn` option to show the replicated backups in the destination Region.

###### To show replicated backups

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds describe-db-instance-automated-backups \
--db-instance-automated-backups-arn "arn:aws:rds:us-east-1:`123456789012`:auto-backup:`ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`"
```

For Windows:

```
aws rds describe-db-instance-automated-backups ^
--db-instance-automated-backups-arn "arn:aws:rds:us-east-1:`123456789012`:auto-backup:`ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`"
```

The output shows the source DB instance in US West (Oregon), with replicated backups in US East (N. Virginia).

```
{
    "DBInstanceAutomatedBackups": [
        {
            "DBInstanceArn": "arn:aws:rds:us-west-2:868710585169:db:mydatabase",
            "DbiResourceId": "db-L2IJCEXJP7XQ7HOJ4SIEXAMPLE",
            "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE",
            "Region": "us-west-2",
            "DBInstanceIdentifier": "mydatabase",
            "RestoreWindow": {
                "EarliestTime": "2020-10-26T01:09:07Z",
                "LatestTime": "2020-10-31T19:01:23Z"
            },
            "AllocatedStorage": 50,
            "BackupRetentionPeriod": 7,
            "Status": "replicating",
            "Port": 1521,
            ...
        }
    ]
}

```
