# Monitoring Ray jobs with metrics

You can monitor Ray jobs using AWS Glue Studio and Amazon CloudWatch. CloudWatch collects and processes raw metrics from AWS Glue with
Ray, which makes them available for analysis. These metrics are visualized in the AWS Glue Studio console, so you can
monitor your job as it runs.

For a general overview of how to monitor AWS Glue, see [Monitoring AWS Glue using Amazon CloudWatch
metrics](monitoring-awsglue-with-cloudwatch-metrics.md "monitoring-awsglue-with-cloudwatch-metrics.md"). For a general overview of how to use CloudWatch metrics that are published by AWS Glue, see [Monitoring with Amazon CloudWatch](monitor-cloudwatch.md "monitor-cloudwatch.md").

## Monitoring Ray jobs in the AWS Glue console

On the details page for a job run, below the **Run details** section, you can view
pre-built aggregated graphs that visualize your available job metrics. AWS Glue Studio sends job metrics to CloudWatch for
every job run. With these, you can build a profile of your cluster and tasks, as well as access detailed
information about each node.

For more information about available metrics graphs, see [Viewing Amazon CloudWatch metrics for a Ray job
run](view-job-runs.md#monitoring-job-run-metrics-ray "view-job-runs.md#monitoring-job-run-metrics-ray").

## Overview of Ray jobs metrics in CloudWatch

We publish Ray metrics when detailed monitoring is enabled in CloudWatch. Metrics are published to the
`Glue/Ray` CloudWatch namespace.

- **Instance metrics**

We publish metrics about the CPU, memory and disk utilization of instances assigned to a job.
These metrics are identified by features such as `ExecutorId`, `ExecutorType`
and `host`. These metrics are a subset of the standard Linux CloudWatch agent metrics. You can
find information about metric names and features in the CloudWatch documentation. For more information,
see [Metrics
collected by the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md "../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md").

- **Ray cluster metrics**

We forward metrics from the Ray processes that run your script to this namespace, then provide
those most critical for you. The metrics that are available might differ by Ray version. For more
information about which Ray version your job is running, see [AWS Glue versions](release-notes.md "release-notes.md").

Ray collects metrics at the instance level. It also provides metrics for tasks and the cluster.
For more information about Ray's underlying metric strategy, see [Metrics](https://docs.ray.io/en/latest/ray-observability/ray-metrics.html#system-metrics "https://docs.ray.io/en/latest/ray-observability/ray-metrics.html#system-metrics") in the Ray documentation.

###### Note

We don't publish Ray metrics to the `Glue/Job Metrics/` namespace, which is only used for
AWS Glue ETL jobs.
