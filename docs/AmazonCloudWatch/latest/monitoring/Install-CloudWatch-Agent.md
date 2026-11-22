

# Collect metrics, logs, and traces using the CloudWatch agent

The CloudWatch agent is a software component that collects metrics, logs, and traces from your Amazon EC2 instances, on-premises servers, and containerized applications. It enables you to monitor your infrastructure and applications more comprehensively than the basic monitoring provided by default. The CloudWatch agent is built on the OpenTelemetry Collector, so it can receive OpenTelemetry data and send it to the CloudWatch OTLP endpoints.

The agent supports three configuration models:
+ **Classic** – The agent publishes metrics as CloudWatch metrics in a namespace, `CWAgent` by default, which are billed as custom metrics. The Classic configuration also provides StatsD, collectd, procstat, JMX, NVIDIA GPU, EFA, NVMe, and network performance metrics, and CloudWatch Application Signals. For more information, see [Configure the CloudWatch agent with the Classic configuration](CloudWatch-Agent-Classic-configuration.md).
+ **Curated OpenTelemetry (recommended)** – You configure the `opentelemetry` section of the agent JSON configuration file. The agent collects metrics, logs, and traces and sends them to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints. Metrics use OpenTelemetry semantic conventions, keep their labels, and are queried with PromQL. They're billed per GB ingested. For more information, see [Configure the CloudWatch agent with OpenTelemetry (recommended)](CloudWatch-Agent-OpenTelemetry-configuration.md).
+ **Native OpenTelemetry (YAML)** – You provide a standard OpenTelemetry Collector configuration in YAML, appended to the agent configuration file (the agent requires at least one JSON configuration file). This exposes the full OpenTelemetry Collector receiver set, including receivers that the `opentelemetry` section doesn't expose, such as `collectd` and `statsd`, and sends the data to the CloudWatch OTLP endpoints. For more information, see [Appending OpenTelemetry collector configuration files](CloudWatch-Agent-appending-OpenTelemetry-config-files.md).

In all three models, the agent collects logs from Amazon EC2 instances and on-premises servers into Amazon CloudWatch Logs. The agent doesn't support collecting logs from FIFO pipes. For pricing, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing).

To get started:

1. Choose a configuration model. For more information, see [Choose a configuration model for the CloudWatch agent](CloudWatch-Agent-config-model.md).

1. Complete the IAM and network prerequisites. For more information, see [Prerequisites](prerequisites.md).

1. Install the agent. For more information, see [Installing the CloudWatch agent](install-CloudWatch-Agent-on-EC2-Instance.md).

1. Create the agent configuration file for the model that you chose, and start the agent.

The CloudWatch agent is open-source under the MIT license, and is [ hosted on GitHub](https://github.com/aws/amazon-cloudwatch-agent/). If you would like to build, customize or contribute to the CloudWatch agent, see the GitHub repository for the latest instructions. If you think you've found a potential security issue, do not post it on GitHub or any public forum. Instead, follow the instructions at [ Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/) or [ email AWS security directly](mailto:aws-security@amazon.com).

**Topics**
+ [Choose a configuration model for the CloudWatch agent](CloudWatch-Agent-config-model.md)
+ [Supported operating systems](supported-operating-systems.md)
+ [Prerequisites](prerequisites.md)
+ [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md)
+ [Installing the CloudWatch agent](install-CloudWatch-Agent-on-EC2-Instance.md)
+ [Configure the CloudWatch agent with OpenTelemetry (recommended)](CloudWatch-Agent-OpenTelemetry-configuration.md)
+ [Configure the CloudWatch agent with the Classic configuration](CloudWatch-Agent-Classic-configuration.md)
+ [Starting the CloudWatch agent](start-CloudWatch-Agent-on-premise-SSM-onprem.md)
+ [Using the CloudWatch agent with related telemetry](CloudWatch-Agent-RelatedEntities.md)
+ [Using the CloudWatch agent for Amazon EKS Container Insights](CloudWatch-Agent-container-insights-eks.md)
+ [Common scenarios with the CloudWatch agent](CloudWatch-Agent-common-scenarios.md)
+ [CloudWatch agent credentials preference](CloudWatch-Agent-Credentials-Preference.md)
+ [Troubleshooting the CloudWatch agent](troubleshooting-CloudWatch-Agent.md)