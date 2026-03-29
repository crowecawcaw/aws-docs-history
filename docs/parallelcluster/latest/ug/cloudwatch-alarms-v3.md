# Amazon CloudWatch alarms for cluster metrics

AWS ParallelCluster configures Amazon CloudWatch alarms to monitor the health and resource utilization of the head node.
Alarms are named ``cluster-name`-HeadNode-`metric``,
where `cluster-name` is the name of your cluster and `metric`
identifies the metric being monitored.

Access the alarms in the CloudWatch console by choosing **Alarms** in the navigation pane.

A composite alarm named ``cluster-name`-HeadNode`enters the
`ALARM` state when any of the individual head node alarms triggers.

## Disk and memory alarms

Starting with AWS ParallelCluster version 3.6.0, the following CloudWatch alarms are created:

- ``cluster-name`-HeadNode-Disk`— Monitors the root volume`disk_used_percent`metric. Enters the`ALARM` state when disk usage is greater than 90%
  for 1 data point within a 1 minute period.
- ``cluster-name`-HeadNode-Mem`— Monitors the`mem_used_percent`metric. Enters the`ALARM` state when memory usage is greater than 90%
  for 1 data point within a 1 minute period.

For more information, see [Metrics collected by the CloudWatch
agent](../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md "../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md") in the _Amazon CloudWatch User Guide_.

## Health check and CPU alarms

Starting with AWS ParallelCluster version 3.8.0, the following CloudWatch alarms are created:

- ``cluster-name`-HeadNode-Health`— Monitors the Amazon EC2`StatusCheckFailed`metric. Enters the`ALARM` state when the value is greater than 0
  for 1 data point within a 1 minute period.
- ``cluster-name`-HeadNode-Cpu`— Monitors the Amazon EC2`CPUUtilization`metric. Enters the`ALARM` state when CPU utilization is greater than 90%
  for 1 data point within a 1 minute period.

## Cluster management daemon heartbeat alarm

Starting with AWS ParallelCluster version 3.15.0, when Amazon CloudWatch logging is enabled and the Slurm scheduler is
used, the following alarm is created:

- ``cluster-name`-HeadNode-ClustermgtdHeartbeat`— Monitors the`ClustermgtdHeartbeat`metric in the`ParallelCluster`namespace. The alarm enters the`ALARM`
  state when fewer than 1 heartbeat is received for 10 consecutive data points within a 1 minute period. Missing
  data is treated as breaching.

###### Note

All alarms recover symmetrically: the same data points and evaluation period that trigger the alarm also
govern recovery. For example, alarms with 1 data point recover after 1 good data point within the same observation
period, similarly the `ClustermgtdHeartbeat` alarm requires 10 consecutive good data points (10 minutes)
to return to `OK`.

###### Note

AWS ParallelCluster doesn't configure alarm actions. For information about how to set up alarm actions, such as
sending notifications, see [Alarm actions](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions").
For more information about Amazon CloudWatch alarms, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
in the _Amazon CloudWatch User Guide_.

For AWS ParallelCluster version 3.8.0 and later, disable alarms by setting [Monitoring](Monitoring-v3.md "Monitoring-v3.md") /
[Alarms](Monitoring-v3.md#yaml-Monitoring-Alarms "Monitoring-v3.md#yaml-Monitoring-Alarms") / [Enabled](Monitoring-v3.md#yaml-Monitoring-Alarms-Enabled "Monitoring-v3.md#yaml-Monitoring-Alarms-Enabled")
to `false` in your cluster configuration.

For AWS ParallelCluster versions before 3.8.0, disable alarms by setting [Monitoring](Monitoring-v3.md "Monitoring-v3.md") /
[Dashboards](Monitoring-v3.md#yaml-Monitoring-Dashboards "Monitoring-v3.md#yaml-Monitoring-Dashboards") / [CloudWatch](Monitoring-v3.md#yaml-Monitoring-Dashboard-CloudWatch "Monitoring-v3.md#yaml-Monitoring-Dashboard-CloudWatch") / [Enabled](Monitoring-v3.md#yaml-Monitoring-Dashboard-CloudWatch-Enabled "Monitoring-v3.md#yaml-Monitoring-Dashboard-CloudWatch-Enabled") to `false` in your
cluster configuration. Note that this setting also disables the Amazon CloudWatch dashboard. See [Amazon CloudWatch dashboard](cloudwatch-dashboard-v3.md "cloudwatch-dashboard-v3.md") for additional details.
