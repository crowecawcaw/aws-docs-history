

# Configure the CloudWatch agent with the Classic configuration

With the Classic configuration, the agent publishes metrics as CloudWatch metrics in a namespace, `CWAgent` by default, and you query them with CloudWatch metric queries and Metrics Insights. Use the Classic configuration for the agent features that only it offers, such as the configuration wizard, StatsD, collectd, procstat, JMX, NVIDIA GPU, EFA, NVMe, network performance metrics, and Application Signals. For a comparison with the OpenTelemetry configuration, see [Choose a configuration model for the CloudWatch agent](CloudWatch-Agent-config-model.md).

**Topics**
+ [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md)
+ [Enable CloudWatch Application Signals](CloudWatch-Agent-Application_Signals.md)
+ [Collect network performance metrics](CloudWatch-Agent-network-performance.md)
+ [Collect Amazon EBS NVMe driver metrics](Container-Insights-metrics-EBS-Collect.md)
+ [Collect Amazon EC2 instance store volume NVMe driver metrics](Container-Insights-metrics-instance-store-Collect.md)
+ [Collect NVIDIA GPU metrics](CloudWatch-Agent-NVIDIA-GPU.md)
+ [Collect EFA metrics](CloudWatch-Agent-EFA.md)
+ [Collect Java Management Extensions (JMX) metrics](CloudWatch-Agent-JMX-metrics.md)
+ [Receive OTLP data with the Classic configuration (legacy)](CloudWatch-Agent-OpenTelemetry-metrics.md)
+ [Collect process metrics with the procstat plugin](CloudWatch-Agent-procstat-process-metrics.md)
+ [Retrieve custom metrics with StatsD](CloudWatch-Agent-custom-metrics-statsd.md)
+ [Retrieve custom metrics with collectd](CloudWatch-Agent-custom-metrics-collectd.md)
+ [Configure CloudWatch agent service and environment names for related entities](CloudWatch-Agent-configure-related-telemetry.md)
+ [Metrics collected by the CloudWatch agent](metrics-collected-by-CloudWatch-agent.md)
+ [Embedding metrics within logs](CloudWatch_Embedded_Metric_Format.md)