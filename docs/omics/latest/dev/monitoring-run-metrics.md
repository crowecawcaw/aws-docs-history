

# Run metrics for Private Workflows
<a name="monitoring-run-metrics"></a>

HealthOmics publishes near real-time resource-utilization metrics for your runs and tasks to Amazon CloudWatch. These metrics give you visibility into how your runs are progressing while they execute. You can use these metrics to:
+ Identify Central Processing Unit (CPU) or Graphics Processing Unit (GPU) bottlenecks while tasks are still running.
+ Detect memory pressure or scratch storage exhaustion before a task fails.
+ Right-size the compute and storage configurations for your workflows.
+ Build CloudWatch dashboards and alarms, or integrate with third-party observability tools.

Run metrics are available for private and shared workflows.

HealthOmics vends these metrics under the `cloudwatch.aws/omics` scope in your own CloudWatch account.

These metrics are emitted using the CloudWatch OpenTelemetry (OTel)-compatible metrics standard. This means you can integrate them with OTel-compatible observability tools along with native CloudWatch dashboards and alarms. Query the OTel metrics with Prometheus Query Language (PromQL) to view and analyze the data. For more information, see [CloudWatch OpenTelemetry metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-overview.html).

**Region availability**  
Run metrics are available in all [supported HealthOmics Regions](https://docs.aws.amazon.com/general/latest/gr/healthomics-quotas.html), except for the Israel (Tel Aviv) Region (`il-central-1`).

## Enabling metrics for a run
<a name="monitoring-run-metrics-enabling"></a>

To publish these metrics, the AWS Identity and Access Management (IAM) role you use for your run must have permission to write metrics to CloudWatch. Add the following permission to your workflow run role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*"
    }
  ]
}
```

For more information about permissions, see [Service roles for AWS HealthOmics](permissions-service.md). For more information about starting a run, see [Start a run in HealthOmics](starting-a-run.md).

**CloudWatch `PutMetricData` quota**  
CloudWatch has a default `PutMetricData` quota of 500 requests per second (transactions per second). This default quota is sufficient to view metrics for up to 15,000 concurrent HealthOmics tasks. To view metrics for more than 15,000 concurrent HealthOmics tasks, request a limit increase for the CloudWatch `PutMetricData` quota. For more information, see [CloudWatch service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html).

## Available metrics
<a name="monitoring-run-metrics-available"></a>

**Metric availability**  
HealthOmics emits metrics based on the workflow type. Not every metric is emitted for every workflow.

The following table lists the metrics that HealthOmics vends for each run. The metrics are available in CloudWatch Query Studio. Units follow the OpenTelemetry convention: `By` is bytes, `{cpu}` is vCPUs, `{operation}` is operations, and `%` is a percentage.


**HealthOmics run metrics**  

| Metric name | Description | Unit | Type | Frequency | Availability | 
| --- | --- | --- | --- | --- | --- | 
| aws.omics.run.filesystem.usage | Storage in use on the run's shared filesystem. | By | gauge | 30 seconds | For every run. | 
| aws.omics.run.filesystem.limit | Total capacity of the run's shared filesystem. | By | gauge | 30 seconds | Only for runs that use the STATIC run storage type. | 
| aws.omics.task.cpu.usage | vCPUs in use by the workflow task. | {cpu} | gauge | 30 seconds | For every task in the run. | 
| aws.omics.task.cpu.limit | vCPUs reserved for the workflow task based on workflow definition or default values. | {cpu} | gauge | 30 seconds | For every task in the run. | 
| aws.omics.task.memory.usage | Memory in use by the workflow task. | By | gauge | 30 seconds | For every task in the run. | 
| aws.omics.task.memory.limit | Memory reserved for the workflow task. | By | gauge | 30 seconds | For every task in the run. | 
| aws.omics.task.network.io | The number of bytes transmitted and received by the workflow task. Split by network.io.direction (receive, transmit). | By | sum | 30 seconds | For every task in the run. | 
| aws.omics.task.filesystem.io | The number of filesystem bytes transferred by the workflow task. Split by filesystem.io.direction (read, write). | By | sum | 30 seconds | For every task in the run. | 
| aws.omics.task.filesystem.operations | The number of filesystem operations performed by the workflow task. Split by filesystem.io.direction (read, write). | {operation} | sum | 30 seconds | For every task in the run. | 
| aws.omics.task.filesystem.scratch.storage.usage | Scratch storage in use by the workflow task. | By | gauge | 30 seconds (LOCAL mode) or 20 minutes (SHARED mode) | For every task in the run. | 
| aws.omics.task.filesystem.scratch.storage.limit | Total scratch storage capacity available to the workflow task. | By | gauge | 30 seconds | For every task in a run that sets scratchStorageMode to LOCAL. | 
| aws.omics.task.gpu.utilization | GPU utilization for the workflow task. One data point per GPU, identified by gpu.id. | % | gauge | 30 seconds | Only for tasks that use accelerators. | 
| aws.omics.task.gpu.memory.usage | GPU memory in use by the workflow task. One data point per GPU, identified by gpu.id. | By | gauge | 30 seconds | Only for tasks that use accelerators. | 
| aws.omics.task.gpu.memory.limit | GPU memory available to the workflow task. One data point per GPU, identified by gpu.id. | By | gauge | 30 seconds | Only for tasks that use accelerators. | 

For more information about accelerators, see [Task resources in a HealthOmics workflow definition](task-resources.md).

For more information about ephemeral storage, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).

### Common attributes
<a name="monitoring-run-metrics-common-attributes"></a>

Every HealthOmics run metric carries a common set of resource labels that identify the source of the data point.


**Resource labels**  
<a name="monitoring-run-metrics-common-attributes-table"></a>
<table>
<thead>
  <tr><th>Label</th><th>Description</th><th>Example value</th><th></th><th></th><th></th></tr>
  <tr><th colspan="3">Common resource labels</th><th></th><th></th><th></th></tr>
  <tr><th colspan="3">Task resource labels</th><th></th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td><code>@resource.cloud.provider</code></td><td>The cloud provider that published the metric.</td><td><code>aws</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.cloud.account.id</code></td><td>The AWS account that the run belongs to.</td><td><code>123456789012</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.cloud.region</code></td><td>The AWS Region that the run ran in.</td><td><code>us-west-2</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.cloud.resource_id</code></td><td>The ARN of the run.</td><td><code>arn:aws:omics:us-west-2:123456789012:run/1234567</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.service.name</code></td><td>The service that published the metric.</td><td><code>omics</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.aws.omics.workflow.id</code></td><td>The ID of the workflow that the run used.</td><td><code>1122334</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.aws.omics.run.id</code></td><td>The ID of the run.</td><td><code>1234567</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.aws.omics.storage.type</code></td><td>The run storage type.</td><td><code>DYNAMIC</code></td><td></td><td></td><td></td></tr>
  <tr><td><code>@resource.aws.omics.task.id</code></td><td>The ID of the task that the data point is for. Only the <code>aws.omics.task.*</code> metrics carry this label.</td><td><code>1245938</code></td><td></td><td></td><td></td></tr>
</tbody>
</table>


### Additional attributes
<a name="monitoring-run-metrics-additional-attributes"></a>

Some run metrics carry additional data-point attributes that split the metric into separate time series. You can use these attributes to filter a PromQL query.


**Additional metric attributes**  

| Additional attribute | Metrics | Description | Values | 
| --- | --- | --- | --- | 
| gpu.id | aws.omics.task.gpu.utilization, aws.omics.task.gpu.memory.usage, aws.omics.task.gpu.memory.limit | The zero-based index of the GPU on the instance. | 0, 1, 2, or 3 | 
| scratch.storage.mode | aws.omics.task.filesystem.scratch.storage.usage, aws.omics.task.filesystem.scratch.storage.limit | Where the task writes its scratch data, based on the effective scratchStorageMode. | LOCAL or SHARED | 
| network.io.direction | aws.omics.task.network.io | The direction of the network transfer. | receive or transmit | 
| filesystem.io.direction | aws.omics.task.filesystem.io, aws.omics.task.filesystem.operations | The direction of the file system operation. | read or write | 

## Querying HealthOmics run metrics
<a name="monitoring-run-metrics-viewing"></a>

You can view the HealthOmics run metrics in the CloudWatch console by running a PromQL query in Query Studio.

**To view HealthOmics run metrics (CloudWatch console)**

1. Confirm that your run started with the `cloudwatch:PutMetricData` permission.

1. Sign in to the AWS Management Console and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, choose **Query Studio**.

1. In the query editor, choose **PromQL** from the dropdown list.

1. In **Builder** mode, browse and select a metric name and its labels. Or, in **Editor** mode, enter a PromQL query.

1. Choose a time range with the time-range selector.

1. Choose **Run** to display the results as a time-series graph. To change how the graph displays, choose **Customize**.

For example, the following query returns the vCPUs in use by each task in a run. Replace {{runID}} with the ID of the run that you want to inspect.

```
{"aws.omics.task.cpu.usage", "@resource.aws.omics.run.id"="{{runID}}"}
```

To label each time series with its run ID and task ID, you can choose **Custom label** and enter the following.

```
{@resource.aws.omics.run.id="${@resource.aws.omics.run.id}",@resource.aws.omics.task.id="${@resource.aws.omics.task.id}"}
```

**To query HealthOmics run metrics (API)**  
CloudWatch provides Prometheus-compatible APIs and endpoints for querying metric data. For more information about querying metrics with these APIs, see [Prometheus-compatible APIs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-APIs.html).

## Creating an alarm using CloudWatch
<a name="monitoring-run-metrics-alarm"></a>

You can create a CloudWatch alarm from a PromQL query so that CloudWatch notifies you when a metric crosses a threshold. The alarm can send a notification to an Amazon Simple Notification Service (Amazon SNS) topic, or it can start another action when the alarm changes state.

**To create an alarm from a PromQL query (CloudWatch console)**

1. Sign in to the AWS Management Console and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, choose **Query Studio**.

1. Choose **PromQL**, enter your query, verify the graph, and then choose **Create alarm** button.

## Adding HealthOmics run metrics to a CloudWatch dashboard
<a name="monitoring-run-metrics-dashboard"></a>

You can add a PromQL query to a CloudWatch dashboard as a widget so that you can monitor HealthOmics resource utilization alongside your other metrics.

**To add HealthOmics run metrics to a CloudWatch dashboard (CloudWatch console)**

1. Sign in to the AWS Management Console and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, choose **Query Studio**.

1. Choose **PromQL**, enter your query, and then verify the graph.

1. Choose **Action**, and then choose **Add to dashboard**.

1. Choose an existing dashboard or create a new one, and then save the widget.

## Analyzing run metrics with the HealthOmics MCP server
<a name="monitoring-run-metrics-mcp"></a>

You can use the HealthOmics Model Context Protocol (MCP) server to retrieve run metrics and investigate run failures across multiple dimensions of data with the help of an AI model. You can use the MCP server through Kiro CLI, Claude Code, or any other MCP-compatible agentic client. For more information, see [AWS HealthOmics MCP Server](https://awslabs.github.io/mcp/servers/aws-healthomics-mcp-server) and [supported agentic tools](https://github.com/aws-samples/sample-healthomics-agentic-setup).

## Callouts
<a name="monitoring-run-metrics-callouts"></a>
+ HealthOmics starts emitting run metrics after a task reaches the `RUNNING` status, and stops emitting them after the task reaches the `COMPLETED` status. For more information about task statuses, see [Task status values](workflow-run-tasks.md#task-status-values).
+ The first data points appear after a short delay of around 30 seconds.
+ Tasks that run for less than 30 seconds might not have metrics.
+ When the run's storage type is `DYNAMIC`, `aws.omics.run.filesystem.usage` might experience a delay of more than 30 minutes, so it might not be available for runs that take less than 30 minutes.
+ When `scratchStorageMode` is `SHARED`, `aws.omics.task.filesystem.scratch.storage.usage` might not be available for tasks that create a large number of temporary files. HealthOmics measures usage in this mode with a recursive scan of the task's temporary directory, and the scan does not always complete within its time limit when the file count is high.
+ CPU and memory metrics might differ from the run manifest values because the two measurements use a different scope. Run metrics more closely reflect what your task actually consumes.
+ Run metrics are available only in the AWS account that owns the service role and starts the run.

## Billing
<a name="monitoring-run-metrics-billing"></a>

AWS HealthOmics does not charge you for run metrics. Metrics are published to Amazon CloudWatch in your account, and CloudWatch bills you directly for the associated activity. Charges are based on the volume of metric data ingested. For prices in a specific AWS Region, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/). The following table describes how CloudWatch charges for run metrics.


**How CloudWatch charges for run metrics**  

| Activity | How you are charged | 
| --- | --- | 
| Publishing OpenTelemetry metrics | Per GB of data ingested. Includes 15 months of storage, with no separate charge for storage or for the number of unique metric series. | 
| Running PromQL queries in the CloudWatch console, including Query Studio and dashboards | No charge. | 
| Running PromQL queries with the CloudWatch APIs | Per million samples scanned. | 
| Alarms that evaluate a PromQL query | A standard alarm charge, plus query charges for the samples scanned at each evaluation. | 

## Opting out
<a name="monitoring-run-metrics-opting-out"></a>

By default, HealthOmics publishes run metrics whenever the service role for a run has the `cloudwatch:PutMetricData` permission. To opt out and stop future charges, you can omit this permission from the service role at each run level. To stop publishing even when another policy grants the permission, add an explicit deny to the role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*"
    }
  ]
}
```

Another way to opt out is to turn off logging for a run by setting `LogLevel = OFF` in the **StartRun** request. When you set `LogLevel` to `OFF`, HealthOmics does not publish run metrics.