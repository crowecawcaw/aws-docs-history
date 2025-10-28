# Send logs to CloudWatch Logs

To send logs from your containers to Amazon CloudWatch Logs, you can use Fluent Bit. For more
information, see [Fluent Bit](https://fluentbit.io/ "https://fluentbit.io/").

###### Note

As of February 10 2025, AWS has deprecated support for FluentD as a log forwarder
to CloudWatch Logs. We recommend that you use Fluent Bit, which is a lightweight and
resource-efficient alternative. Existing FluentD deployments will continue to function.
Migrate your logging pipeline to Fluent Bit to ensure continued support and optimal
performance.

Container Insights previously also supported using FluentD to send logs from your
containers. FluentD has been deprecated and is now not supported for Container Insights.
Use Fluent Bit instead.

###### Topics

- [Set up Fluent Bit as a
  DaemonSet to send logs to CloudWatch Logs](Container-Insights-setup-logs-FluentBit.md "Container-Insights-setup-logs-FluentBit.md")
- [(Optional) Set up Amazon EKS
  control plane logging](Container-Insights-setup-control-plane-logging.md "Container-Insights-setup-control-plane-logging.md")
- [(Optional) Enable the Use_Kubelet
  feature for large clusters](ContainerInsights-use-kubelet.md "ContainerInsights-use-kubelet.md")
