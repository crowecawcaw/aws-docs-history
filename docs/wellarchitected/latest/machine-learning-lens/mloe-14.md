# MLOE-14: Establish deployment environment metrics

Measure machine learning operations metrics to determine the
performance of a deployed environment. These metrics include
memory and CPU/GPU usage, disk utilization, ML endpoint
invocations, and latency.

## Implementation plan

- **Record performance-related
  metrics** - Use a monitoring and observability
  service to record performance-related metrics. These
  metrics can include database transactions, slow queries,
  I/O latency, HTTP request throughput, service latency, and
  other key data.
- **Analyze metrics when events or
  incidents occur** - Use monitoring dashboards and
  reports to understand and diagnose the impact of an event
  or incident. These views provide insight into what
  portions of the workload are not performing as expected.
- **Establish key performance
  indicators (KPIs) to measure workload
  performance** - Identify the KPIs that indicate
  whether the workload is performing as intended. An
  API-based workload might use overall response latency as
  an indication of overall performance, while an e-commerce
  site might choose to use the number of purchases as its
  KPI.
- **Use monitoring to generate
  alarm-based notifications** - Monitor metrics for
  the defined KPIs and generate alarms automatically when the
  measurements are outside expected boundaries.
- **Review metrics at regular
  intervals** - As routine maintenance, or in
  response to events or incidents, review what metrics are
  collected and identify the metrics that were key in
  addressing issues. Identify any additional metrics that
  would help to identify, address, or prevent issues.
- **Monitor and alarm
  proactively** - Use KPIs, combined with
  monitoring and alerting systems, to proactively address
  performance-related issues. Use alarms to initiate
  automated actions to remediate issues where possible.
  Escalate the alarm to those able to respond if an
  automated response is not possible. Use a system to
  predict expected KPI values, and generate alerts and
  automatically halt or roll back deployments if KPIs are
  outside of the expected values.
- **Use Amazon CloudWatch** -
  Use
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") metrics for SageMaker AI endpoints to
  determine the memory, CPU usage, and disk utilization. Set
  up
  [CloudWatch
  Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") to visualize the environment metrics and
  establish
  [CloudWatch
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") to initiate a notification via
  [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") (Email, SMS, WebHook) to notify on events
  occurring in the runtime environment.
- **Use Amazon EventBridge**

* Consider defining an automated workflow using
  [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") to respond automatically to events.
  These events can include training job status changes,
  endpoint status changes, and increasing the compute
  environment capacity after it crosses a defined threshold
  (such as CPU or disk utilization).

- **Use AWS Application Cost
  Profiler** - Use
  [AWS Application Cost Profiler](https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/ "https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/") to report the cost per
  tenant (model/user).

## Documents

- [DevOps
  and AWS](https://aws.amazon.com/devops/?ref=wellarchitected-wp "https://aws.amazon.com/devops/?ref=wellarchitected-wp")
- [Next
  Generation SageMaker AI Notebooks – Now with Built-in Data Preparation, Real-Time Collaboration, and Notebook Automation](https://aws.amazon.com/blogs/aws/next-generation-sagemaker-notebooks-now-with-built-in-data-preparation-real-time-collaboration-and-notebook-automation/ "https://aws.amazon.com/blogs/aws/next-generation-sagemaker-notebooks-now-with-built-in-data-preparation-real-time-collaboration-and-notebook-automation/")

## Videos

- [DevOps
  at Amazon: A Look at Our Tools and Processes](https://www.youtube.com/watch?v=esEFaY0FDKc "https://www.youtube.com/watch?v=esEFaY0FDKc")
