# Aurora MySQL in-place upgrade tutorial

The following Linux examples show how you might perform the general steps of the in-place
upgrade procedure using the AWS CLI.

This first example creates an Aurora DB cluster that's running a 2.x version of
Aurora MySQL. The cluster includes a writer DB instance and a reader DB instance. The `wait
 db-instance-available` command pauses until the writer DB instance is available.
That's the point when the cluster is ready to be upgraded.

```
aws rds create-db-cluster --db-cluster-identifier mynewdbcluster --engine aurora-mysql \
  --db-cluster-version 5.7.mysql_aurora.2.11.2
`...`
aws rds create-db-instance --db-instance-identifier mynewdbcluster-instance1 \
  --db-cluster-identifier mynewdbcluster --db-instance-class db.t4g.medium --engine aurora-mysql
`...`
aws rds wait db-instance-available --db-instance-identifier mynewdbcluster-instance1
```

The Aurora MySQL 3.x versions that you can upgrade the cluster to depend on the 2.x version that the cluster is currently running and on the
AWS Region where the cluster is located. The first command, with `--output text`, just shows the available target version. The second command
shows the full JSON output of the response. In that response, you can see details such as the `aurora-mysql` value that you use for the
`engine` parameter. You can also see the fact that upgrading to 3.04.0 represents a major version upgrade.

```
aws rds describe-db-clusters --db-cluster-identifier mynewdbcluster \
  --query '*[].{EngineVersion:EngineVersion}' --output text
`5.7.mysql_aurora.2.11.2`

aws rds describe-db-engine-versions --engine aurora-mysql --engine-version 5.7.mysql_aurora.2.11.2 \
  --query '*[].[ValidUpgradeTarget]'
`...
{
 "Engine": "aurora-mysql",
 "EngineVersion": "8.0.mysql_aurora.3.04.0",
 "Description": "Aurora MySQL 3.04.0 (compatible with MySQL 8.0.28)",
 "AutoUpgrade": false,
 "IsMajorVersionUpgrade": true,
 "SupportedEngineModes": [
 "provisioned"
 ],
 "SupportsParallelQuery": true,
 "SupportsGlobalDatabases": true,
 "SupportsBabelfish": false,
 "SupportsIntegrations": false
},
...`
```

This example shows how if you enter a target version number that isn't a valid
upgrade target for the cluster, Aurora doesn't perform the upgrade. Aurora also
doesn't perform a major version upgrade unless you include the
`--allow-major-version-upgrade` parameter. That way, you can't accidentally
perform an upgrade that has the potential to require extensive testing and changes to your
application code.

```
aws rds modify-db-cluster --db-cluster-identifier mynewdbcluster \
  --engine-version 5.7.mysql_aurora.2.09.2 --apply-immediately
`An error occurred (InvalidParameterCombination) when calling the ModifyDBCluster operation: Cannot find upgrade target from 5.7.mysql_aurora.2.11.2 with requested version 5.7.mysql_aurora.2.09.2.`

aws rds modify-db-cluster --db-cluster-identifier mynewdbcluster \
  --engine-version 8.0.mysql_aurora.3.04.0 --region us-east-1 --apply-immediately
`An error occurred (InvalidParameterCombination) when calling the ModifyDBCluster operation: The AllowMajorVersionUpgrade flag must be present when upgrading to a new major version.`

aws rds modify-db-cluster --db-cluster-identifier mynewdbcluster \
  --engine-version 8.0.mysql_aurora.3.04.0 --apply-immediately --allow-major-version-upgrade
`{
 "DBClusterIdentifier": "mynewdbcluster",
 "Status": "available",
 "Engine": "aurora-mysql",
 "EngineVersion": "5.7.mysql_aurora.2.11.2"
}`
```

It takes a few moments for the status of the cluster and associated DB instances to
change to `upgrading`. The version numbers for the cluster and DB instances only
change when the upgrade is finished. Again, you can use the `wait
 db-instance-available` command for the writer DB instance to wait until the upgrade is
finished before proceeding.

```
aws rds describe-db-clusters --db-cluster-identifier mynewdbcluster \
  --query '*[].[Status,EngineVersion]' --output text`upgrading 5.7.mysql_aurora.2.11.2`

aws rds describe-db-instances --db-instance-identifier mynewdbcluster-instance1 \
  --query '*[].{DBInstanceIdentifier:DBInstanceIdentifier,DBInstanceStatus:DBInstanceStatus} | [0]'
`{
 "DBInstanceIdentifier": "mynewdbcluster-instance1",
 "DBInstanceStatus": "upgrading"
}`

aws rds wait db-instance-available --db-instance-identifier mynewdbcluster-instance1
```

At this point, the version number for the cluster matches the one that was specified for
the upgrade.

```
aws rds describe-db-clusters --db-cluster-identifier mynewdbcluster \
  --query '*[].[EngineVersion]' --output text
`8.0.mysql_aurora.3.04.0`
```

The preceding example did an immediate upgrade by specifying the
`--apply-immediately` parameter. To let the upgrade happen at a convenient time
when the cluster isn't expected to be busy, you can specify the
`--no-apply-immediately` parameter. Doing so makes the upgrade start during the
next maintenance window for the cluster. The maintenance window defines the period during
which maintenance operations can start. A long-running operation might not finish during the
maintenance window. Thus, you don't need to define a larger maintenance window even if
you expect that the upgrade might take a long time.

The following example upgrades a cluster that's initially running Aurora MySQL version 2.11.2. In the `describe-db-engine-versions`
output, the `False` and `True` values represent the `IsMajorVersionUpgrade` property. From version 2.11.2, you can
upgrade to some other 2.\* versions. Those upgrades aren't considered major version upgrades and so don't require an in-place upgrade. In-place
upgrade is only available for upgrades to the 3.\* versions that are shown in the list.

```
aws rds describe-db-clusters --db-cluster-identifier mynewdbcluster \
  --query '*[].{EngineVersion:EngineVersion}' --output text
`5.7.mysql_aurora.2.11.2`

aws rds describe-db-engine-versions --engine aurora-mysql --engine-version 5.7.mysql_aurora.2.10.2 \
  --query '*[].[ValidUpgradeTarget]|[0][0]|[*].[EngineVersion,IsMajorVersionUpgrade]' --output text
`5.7.mysql_aurora.2.11.3 False
5.7.mysql_aurora.2.11.4 False
5.7.mysql_aurora.2.11.5 False
5.7.mysql_aurora.2.11.6 False
5.7.mysql_aurora.2.12.0 False
5.7.mysql_aurora.2.12.1 False
5.7.mysql_aurora.2.12.2 False
5.7.mysql_aurora.2.12.3 False
8.0.mysql_aurora.3.04.0 True
8.0.mysql_aurora.3.04.1 True
8.0.mysql_aurora.3.04.2 True
8.0.mysql_aurora.3.04.3 True
8.0.mysql_aurora.3.05.2 True
8.0.mysql_aurora.3.06.0 True
8.0.mysql_aurora.3.06.1 True
8.0.mysql_aurora.3.07.1 True`

aws rds modify-db-cluster --db-cluster-identifier mynewdbcluster \
  --engine-version 8.0.mysql_aurora.3.04.0 --no-apply-immediately --allow-major-version-upgrade
`...`
```

When a cluster is created without a specified maintenance window, Aurora picks a random day
of the week. In this case, the `modify-db-cluster` command is submitted on a
Monday. Thus, we change the maintenance window to be Tuesday morning. All times are
represented in the UTC time zone. The `tue:10:00-tue:10:30` window corresponds to
2:00-2:30 AM Pacific time. The change in the maintenance window takes effect
immediately.

```
aws rds describe-db-clusters --db-cluster-identifier mynewdbcluster --query '*[].[PreferredMaintenanceWindow]'
`[
 [
 "sat:08:20-sat:08:50"
 ]
]`

aws rds modify-db-cluster --db-cluster-identifier mynewdbcluster --preferred-maintenance-window tue:10:00-tue:10:30"
aws rds describe-db-clusters --db-cluster-identifier mynewdbcluster --query '*[].[PreferredMaintenanceWindow]'
`[
 [
 "tue:10:00-tue:10:30"
 ]
]`
```

The following example shows how to get a report of the events generated by the upgrade.
The `--duration` argument represents the number of minutes to retrieve the event
information. This argument is needed, because by default `describe-events` only
returns events from the last hour.

```
aws rds describe-events --source-type db-cluster --source-identifier mynewdbcluster --duration 20160
`{
 "Events": [
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "DB cluster created",
 "EventCategories": [
 "creation"
 ],
 "Date": "2022-11-17T01:24:11.093000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Performing online pre-upgrade checks.",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T22:57:08.450000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Performing offline pre-upgrade checks.",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T22:57:59.519000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Creating pre-upgrade snapshot [preupgrade-mynewdbcluster-5-7-mysql-aurora-2-10-2-to-8-0-mysql-aurora-3-02-0-2022-11-18-22-55].",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T23:00:22.318000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Cloning volume.",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T23:01:45.428000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Purging undo records for old row versions. Records remaining: 164",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T23:02:25.141000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Purging undo records for old row versions. Records remaining: 164",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T23:06:23.036000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Upgrade in progress: Upgrading database objects.",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T23:06:48.208000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 },
 {
 "SourceIdentifier": "mynewdbcluster",
 "SourceType": "db-cluster",
 "Message": "Database cluster major version has been upgraded",
 "EventCategories": [
 "maintenance"
 ],
 "Date": "2022-11-18T23:10:28.999000+00:00",
 "SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:mynewdbcluster"
 }
 ]
}`
```
