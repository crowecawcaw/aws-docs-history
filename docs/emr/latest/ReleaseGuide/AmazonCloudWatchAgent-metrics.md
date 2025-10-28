# Default metrics for CloudWatch agent with Amazon EMR

When you install the Amazon CloudWatch agent on Amazon EMR, the default configuration publishes the
following system metrics for all of the instances in your cluster unless you [configure the agent differently](AmazonCloudWatchAgent-config.md "AmazonCloudWatchAgent-config.md"). For definitions
of each metric, see [Metrics collected by the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md "../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md") in the
_Amazon CloudWatch User Guide_.

CPU

###### CPU metrics

- `cpu_usage_active`
- `cpu_usage_guest`
- `cpu_usage_guest_nice`
- `cpu_usage_idle`
- `cpu_usage_iowait`
- `cpu_usage_irq`
- `cpu_usage_nice`
- `cpu_usage_softirq`
- `cpu_usage_steal`
- `cpu_usage_system`
- `cpu_usage_user`

Disk

###### Disk metrics

- `disk_free`
- `disk_total`
- `disk_used`
- `disk_used_percent`

Memory

###### Memory metrics

- `mem_active`
- `mem_available`
- `mem_available_percent`
- `mem_free`
- `mem_inactive`
- `mem_total`
- `mem_used`
- `mem_used_percent`
- `mem_buffered`
- `mem_cached`

Network IO

###### Network IO metrics

- `net_bytes_recv`
- `net_bytes_sent`
- `net_packets_recv`
- `net_packets_sent`

Process

###### Process metrics

- `processes_running`
- `processes_total`

Swap

###### Swap metrics

- `swap_free`
- `swap_used`
- `swap_used_percent`

By default, the agent publishes all metrics to CloudWatch under the custom namespace
`CWAgent`, and under the schema `cluster.id`, `instance.id`, `node.type`,
`service.name`. Use the following steps to view these default metrics that the
CloudWatch agent publishes for Amazon EMR:

1. Navigate to the Amazon CloudWatch console.
2. Choose the **Metrics** tab, and then **All
   metrics**.
3. Under **Custom namespaces**, select
   **`CWAgent`**. Then, select the schema:
   **`cluster.id`, `instance.id`, `node.type`,
   `service.name`**.
4. Continue to query the metrics from the CloudWatch interface as your use case
   requires.
   Amazon EMR attaches the following labels to each metric:
   `["cluster.id", "instance.id', "node.type", "service.name"]`. Consider the following
   with regard to these labels:

- The value of the `cluster.id` label is the ID of the EMR cluster
  that produced the metric. An example value for the `cluster.id` label
  is: `j-123456789ABC`.
- The value of the `instance.id`
  label is the ID of the instance in the EMR cluster that produced the metric.
  An example value for the `instance.id` label is
  `i-01bcf5f140f3355777`.
- The value of the `node.type` label represents
  the node type of the instance in the cluster that produced the metric. This value can be either
  `master`, `core`, or `task`.
- The value of the `service.name`
  label is the name of the service that produced the metric. The default
  `service.name` value for the default system metrics is
  `system`.

###### Note

Amazon EMR release 7.0.0 uses a slightly different metric label schema. `cluster.id` is `jobflow.id`, and `node.type` is unavailable. `instance.id`
and `service.name` are available.
