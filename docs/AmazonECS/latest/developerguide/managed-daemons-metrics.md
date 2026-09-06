

# Daemon metrics
<a name="managed-daemons-metrics"></a>

Amazon ECS publishes CloudWatch metrics for Managed Daemons. You can use these metrics to track CPU and memory utilization for daemon tasks across your cluster.

Daemon metrics use the same `AWS/ECS` namespace as service metrics. Amazon ECS distinguishes daemon metrics from service metrics by the `ServiceName` dimension value, which uses the prefix `daemon:` followed by the daemon name (for example, `daemon:{{my-daemon}}`).

## Daemon utilization metrics
<a name="managed-daemons-metrics-cpu-memory"></a>

Amazon ECS measures daemon CPU and memory utilization as the percentage of resources used by daemon tasks compared to the resources specified in the daemon task definition.

CloudWatch provides the following statistics for daemon utilization metrics:
+ **Average** - The average utilization across all daemon tasks in the cluster.
+ **Minimum** - The utilization of the daemon task with the lowest resource usage.
+ **Maximum** - The utilization of the daemon task with the highest resource usage.

### Utilization formulas
<a name="managed-daemons-metrics-formulas"></a>

Amazon ECS calculates the Average statistic using the following formulas:

```
                                      (Total CPU units used by daemon tasks) x 100
Daemon CPU utilization =  -------------------------------------------------------------------------------
                          (Total CPU units specified in daemon task definition) x (Number of daemon tasks)
```

```
                                         (Total MiB of memory used by daemon tasks) x 100
Daemon memory utilization =  ------------------------------------------------------------------------------------
                             (Total MiB of memory specified in daemon task definition) x (Number of daemon tasks)
```

These formulas apply only to the Average statistic. The Minimum and Maximum statistics represent the individual daemon task with the lowest and highest resource utilization, respectively.

The Amazon ECS container agent samples CPU and memory usage for each running daemon task every 20 seconds. Each minute, the agent reports three samples to Amazon ECS. Amazon ECS aggregates the samples across all daemon tasks in the cluster and publishes the Average, Minimum, and Maximum values to CloudWatch as a percentage of the total resources specified in the daemon task definition.

### Example: Utilization calculation
<a name="managed-daemons-metrics-example-calculation"></a>

A daemon task definition specifies 256 CPU units and 512 MiB of memory. The daemon has 2 running tasks across 2 container instances. One daemon task uses 200 CPU units and 400 MiB of memory. The other uses 100 CPU units and 256 MiB of memory. Amazon ECS reports the following metrics:
+ Average CPU utilization: ((200 \+ 100) x 100) / (256 x 2) = 58.6%
+ Average memory utilization: ((400 \+ 256) x 100) / (512 x 2) = 64.1%

## Viewing daemon metrics
<a name="managed-daemons-metrics-viewing"></a>

You can view daemon metrics by using the AWS Management Console or the AWS CLI.

### AWS Management Console
<a name="managed-daemons-metrics-viewing-console"></a>

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics**, then choose **All metrics**.

1. Choose the **AWS/ECS** namespace.

1. Choose the **ClusterName, ServiceName** dimension.

1. Filter for `ServiceName` values that begin with `daemon:` to locate your daemon metrics.

### AWS CLI
<a name="managed-daemons-metrics-viewing-cli"></a>

Run the `get-metric-statistics` command to retrieve daemon metrics from CloudWatch. Specify the `ServiceName` dimension with the `daemon:` prefix.

### Example: Viewing daemon CPU utilization
<a name="managed-daemons-metrics-example-cpu"></a>

The following command retrieves the average CPU utilization for a daemon over a 12-hour period with 5-minute intervals.

```
aws cloudwatch get-metric-statistics \
    --namespace AWS/ECS \
    --metric-name CPUUtilization \
    --dimensions Name=ClusterName,Value={{my-cluster}} Name=ServiceName,Value=daemon:{{my-daemon}} \
    --start-time {{2026-03-24T00:00:00Z}} \
    --end-time {{2026-03-24T12:00:00Z}} \
    --period 300 \
    --statistics Average
```

### Example: Viewing daemon memory utilization
<a name="managed-daemons-metrics-example-memory"></a>

The following command retrieves the average memory utilization for a daemon over a 12-hour period with 5-minute intervals.

```
aws cloudwatch get-metric-statistics \
    --namespace AWS/ECS \
    --metric-name MemoryUtilization \
    --dimensions Name=ClusterName,Value={{my-cluster}} Name=ServiceName,Value=daemon:{{my-daemon}} \
    --start-time {{2026-03-24T00:00:00Z}} \
    --end-time {{2026-03-24T12:00:00Z}} \
    --period 300 \
    --statistics Average
```