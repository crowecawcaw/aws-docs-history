# Checking uptime for Aurora clusters and instances

You can check and monitor the length of time since the last reboot for each DB instance in your Aurora cluster.
The Amazon CloudWatch metric `EngineUptime` reports the number of seconds since the last time a DB instance
was started. You can examine this metric at a point in time to find out the uptime for the DB instance. You
can also monitor this metric over time to detect when the instance is rebooted.

You can also examine the `EngineUptime` metric at the cluster level. The `Minimum` and
`Maximum` dimensions report the smallest and largest uptime values for all DB instances in the
cluster. To check the most recent time when any reader instance in a cluster was rebooted, or restarted for
another reason, monitor the cluster-level metric using the `Minimum` dimension. To check which
instance in the cluster has gone the longest without a reboot, monitor the cluster-level metric using the
`Maximum` dimension. For example, you might want to confirm that all DB instances in the cluster
were rebooted after a configuration change.

###### Tip

For long-term monitoring, we recommend monitoring the `EngineUptime` metric for individual
instances instead of at the cluster level. The cluster-level `EngineUptime` metric is set to zero
when a new DB instance is added to the cluster. Such cluster changes can happen as part of maintenance and
scaling operations such as those performed by Amazon EC2 Auto Scaling.

The following CLI examples show how to examine the `EngineUptime` metric for the writer and reader
instances in a cluster. The examples use a cluster named `tpch100g`. This cluster has a writer DB
instance `instance-1234`. It also has two reader DB instances, `instance-7448` and
`instance-6305`.

First, the `reboot-db-instance` command reboots one of the reader instances. The `wait`
command waits until the instance is finished rebooting.

```
$ aws rds reboot-db-instance --db-instance-identifier instance-6305
{
    "DBInstance": {
        "DBInstanceIdentifier": "instance-6305",
        "DBInstanceStatus": "rebooting",
...
$ aws rds wait db-instance-available --db-instance-id instance-6305

```

The CloudWatch `get-metric-statistics` command examines the `EngineUptime` metric over the
last five minutes at one-minute intervals. The uptime for the `instance-6305` instance is reset to
zero and begins counting upwards again. This AWS CLI example for Linux uses `$()` variable
substitution to insert the appropriate timestamps into the CLI commands. It also uses the Linux
`sort` command to order the output by the time the metric was collected. That timestamp value is
the third field in each line of output.

```
$ aws cloudwatch get-metric-statistics --metric-name "EngineUptime" \
  --start-time "$(date -d '5 minutes ago')" --end-time "$(date -d 'now')" \
  --period 60 --namespace "AWS/RDS" --statistics Maximum \
  --dimensions Name=DBInstanceIdentifier,Value=instance-6305 --output text \
  | sort -k 3
EngineUptime
DATAPOINTS	231.0	2021-03-16T18:19:00+00:00	Seconds
DATAPOINTS	291.0	2021-03-16T18:20:00+00:00	Seconds
DATAPOINTS	351.0	2021-03-16T18:21:00+00:00	Seconds
DATAPOINTS	411.0	2021-03-16T18:22:00+00:00	Seconds
DATAPOINTS	471.0	2021-03-16T18:23:00+00:00	Seconds

```

The minimum uptime for the cluster is reset to zero because one of the instances in the cluster was rebooted.
The maximum uptime for the cluster isn't reset because at least one of the DB instances in the cluster
remained available.

```
$ aws cloudwatch get-metric-statistics --metric-name "EngineUptime" \
  --start-time "$(date -d '5 minutes ago')" --end-time "$(date -d 'now')" \
  --period 60 --namespace "AWS/RDS" --statistics Minimum \
  --dimensions Name=DBClusterIdentifier,Value=tpch100g --output text \
  | sort -k 3
EngineUptime
DATAPOINTS	63099.0	2021-03-16T18:12:00+00:00	Seconds
DATAPOINTS	63159.0	2021-03-16T18:13:00+00:00	Seconds
DATAPOINTS	63219.0	2021-03-16T18:14:00+00:00	Seconds
DATAPOINTS	63279.0	2021-03-16T18:15:00+00:00	Seconds
DATAPOINTS	51.0	2021-03-16T18:16:00+00:00	Seconds

$ aws cloudwatch get-metric-statistics --metric-name "EngineUptime" \
  --start-time "$(date -d '5 minutes ago')" --end-time "$(date -d 'now')" \
  --period 60 --namespace "AWS/RDS" --statistics Maximum \
  --dimensions Name=DBClusterIdentifier,Value=tpch100g --output text \
  | sort -k 3
EngineUptime
DATAPOINTS	63389.0	2021-03-16T18:16:00+00:00	Seconds
DATAPOINTS	63449.0	2021-03-16T18:17:00+00:00	Seconds
DATAPOINTS	63509.0	2021-03-16T18:18:00+00:00	Seconds
DATAPOINTS	63569.0	2021-03-16T18:19:00+00:00	Seconds
DATAPOINTS	63629.0	2021-03-16T18:20:00+00:00	Seconds

```

Then another `reboot-db-instance` command reboots the writer instance of the cluster. Another
`wait` command pauses until the writer instance is finished rebooting.

```
$ aws rds reboot-db-instance --db-instance-identifier instance-1234
{
  "DBInstanceIdentifier": "instance-1234",
  "DBInstanceStatus": "rebooting",
...
$ aws rds wait db-instance-available --db-instance-id instance-1234

```

Now the `EngineUptime` metric for the writer instance shows that the instance
`instance-1234` was rebooted recently. The reader instance `instance-6305` was also
rebooted automatically along with the writer instance. This cluster is running Aurora MySQL 2.09, which
doesn't keep the reader instances running as the writer instance reboots.

```
$ aws cloudwatch get-metric-statistics --metric-name "EngineUptime" \
  --start-time "$(date -d '5 minutes ago')" --end-time "$(date -d 'now')" \
  --period 60 --namespace "AWS/RDS" --statistics Maximum \
  --dimensions Name=DBInstanceIdentifier,Value=instance-1234 --output text \
  | sort -k 3
EngineUptime
DATAPOINTS	63749.0	2021-03-16T18:22:00+00:00	Seconds
DATAPOINTS	63809.0	2021-03-16T18:23:00+00:00	Seconds
DATAPOINTS	63869.0	2021-03-16T18:24:00+00:00	Seconds
DATAPOINTS	41.0	2021-03-16T18:25:00+00:00	Seconds
DATAPOINTS	101.0	2021-03-16T18:26:00+00:00	Seconds

$ aws cloudwatch get-metric-statistics --metric-name "EngineUptime" \
  --start-time "$(date -d '5 minutes ago')" --end-time "$(date -d 'now')" \
  --period 60 --namespace "AWS/RDS" --statistics Maximum \
  --dimensions Name=DBInstanceIdentifier,Value=instance-6305 --output text \
  | sort -k 3
EngineUptime
DATAPOINTS	411.0	2021-03-16T18:22:00+00:00	Seconds
DATAPOINTS	471.0	2021-03-16T18:23:00+00:00	Seconds
DATAPOINTS	531.0	2021-03-16T18:24:00+00:00	Seconds
DATAPOINTS	49.0	2021-03-16T18:26:00+00:00	Seconds

```
