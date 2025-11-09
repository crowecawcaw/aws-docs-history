# Finding the reasons for Aurora MySQL major version upgrade failures

In the [tutorial](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md"), the upgrade from Aurora MySQL version 2 to version 3 succeeded. But if the
upgrade had failed, you would want to know why.

You can start by using the `describe-events` AWS CLI command to look at the DB cluster events. This example shows the events for
`mydbcluster` for the last 10 hours.

```
aws rds describe-events \
    --source-type db-cluster \
    --source-identifier mydbcluster \
    --duration 600
```

In this case, we had an upgrade precheck failure.

```
{
    "Events": [
        {
            "SourceIdentifier": "mydbcluster",
            "SourceType": "db-cluster",
            "Message": "Database cluster engine version upgrade started.",
            "EventCategories": [
                "maintenance"
            ],
            "Date": "2024-04-11T13:23:22.846000+00:00",
            "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster"
        },
        {
            "SourceIdentifier": "mydbcluster",
            "SourceType": "db-cluster",
            "Message": "Database cluster is in a state that cannot be upgraded: Upgrade prechecks failed. For more details, see the
             upgrade-prechecks.log file. For more information on troubleshooting the cause of the upgrade failure, see
             https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Upgrading.Troubleshooting.html",
            "EventCategories": [
                "maintenance"
            ],
            "Date": "2024-04-11T13:23:24.373000+00:00",
            "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster"
        }
    ]
}

```

To diagnose the exact cause of the problem, examine the database logs for the writer DB instance. When an upgrade to Aurora MySQL version 3 fails, the
writer instance contains a log file with the name `upgrade-prechecks.log`. This example shows how to detect the presence of that log and then
download it to a local file for examination.

```
aws rds describe-db-log-files --db-instance-identifier mydbcluster-instance \
    --query '*[].[LogFileName]' --output text

error/mysql-error-running.log
error/mysql-error-running.log.2024-04-11.20
error/mysql-error-running.log.2024-04-11.21
error/mysql-error.log
external/mysql-external.log
upgrade-prechecks.log

aws rds download-db-log-file-portion --db-instance-identifier mydbcluster-instance \
    --log-file-name upgrade-prechecks.log \
    --starting-token 0 \
    --output text >upgrade_prechecks.log
```

The `upgrade-prechecks.log` file is in JSON format. We download it using the `--output text` option to avoid encoding JSON
output within another JSON wrapper. For Aurora MySQL version 3 upgrades, this log always includes certain informational and warning messages. It only
includes error messages if the upgrade fails. If the upgrade succeeds, the log file isn't produced at all.

To summarize all of the errors and display the associated object and description fields, you can run the command `grep -A 2 '"level":
 "Error"'` on the contents of the `upgrade-prechecks.log` file. Doing so displays each error line and the two lines after it. These
contain the name of the corresponding database object and guidance about how to correct the problem.

```
`$` cat upgrade-prechecks.log | grep -A 2 '"level": "Error"'

"level": "Error",
"dbObject": "problematic_upgrade.dangling_fulltext_index",
"description": "Table `problematic_upgrade.dangling_fulltext_index` contains dangling FULLTEXT index. Kindly recreate the table before upgrade."
```

In this example, you can run the following SQL command on the offending table to try to fix the issue, or you can re-create the table without the
dangling index.

```
OPTIMIZE TABLE problematic_upgrade.dangling_fulltext_index;
```

Then retry the upgrade.
