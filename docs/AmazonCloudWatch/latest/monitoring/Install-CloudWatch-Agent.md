

# Collect metrics, logs, and traces using the CloudWatch agent
<a name="Install-CloudWatch-Agent"></a>

The CloudWatch agent is a software component that collects metrics, logs, and traces from your Amazon EC2 instances, on-premises servers, and containerized applications. It enables you to monitor your infrastructure and applications more comprehensively than the basic monitoring provided by default.

The CloudWatch agent enables you to do the following:
+ Collect internal system-level metrics from Amazon EC2 instances across operating systems. The metrics can include in-guest metrics, in addition to the metrics for Amazon EC2 instances. For a list of additional metrics that you can collect, see [Metrics collected by the CloudWatch agent](metrics-collected-by-CloudWatch-agent.md).
+ Collect system-level metrics from on-premises servers. These can include servers in a hybrid environment as well as servers not managed by AWS.
+ Retrieve custom metrics from your applications or services using the `StatsD` and `collectd` protocols. `StatsD` is supported on both Linux servers and servers running Windows Server. `collectd` is supported only on Linux servers.
+ Collect logs from Amazon EC2 instances and on-premises servers, running either Linux or Windows Server.
**Note**  
The CloudWatch agent does not support collecting logs from FIFO pipes.
+ Send the metrics to either CloudWatch or Amazon Managed Service for Prometheus, or to both. The CloudWatch agent configuration file contains a `metrics_destinations` parameter in the `metrics` section. You can specify `cloudwatch`, `amp`, or both in this parameter.
+ Version 1.300031.0 and later can be used to enable CloudWatch Application Signals. For more information, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md).
+ Version 1.300025.0 and later can collect traces from [OpenTelemetry](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html#xray-instrumenting-opentel) or [X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html#xray-instrumenting-xray-sdk) client SDKs, and send them to X-Ray.

  Using the CloudWatch agent allows you to collect traces without needing to run a separate trace collection daemon, helping to reduce the number of agents that you run and manage.

Metrics sent to CloudWatch can be viewed in CloudWatch just as any other CloudWatch metrics. The default CloudWatch namespace for metrics collected by the CloudWatch agent is `CWAgent`, although you can specify a different namespace when you configure the agent.

The logs collected by the CloudWatch agent are processed and stored in Amazon CloudWatch Logs, just like logs collected by the older CloudWatch Logs agent. For information about CloudWatch Logs pricing, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing).

Metrics collected by the CloudWatch agent are billed as custom metrics. For more information about CloudWatch metrics pricing, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing).

The CloudWatch agent is open-source under the MIT license, and is [ hosted on GitHub](https://github.com/aws/amazon-cloudwatch-agent/). If you would like to build, customize or contribute to the CloudWatch agent, see the GitHub repository for the latest instructions. If you think you've found a potential security issue, do not post it on GitHub or any public forum. Instead, follow the instructions at [ Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/) or [ email AWS security directly](mailto:aws-security@amazon.com).

You can download and install the CloudWatch agent manually using the command line, or you can integrate it with AWS Systems Manager. The general flow of installing the CloudWatch agent is as follows:

1. Create IAM roles or users that enable the agent to collect metrics from the server and optionally to integrate with AWS Systems Manager.

1. Download the agent package.

1. Modify the CloudWatch agent configuration file and specify the metrics that you want to collect.

1. Install and start the agent on your servers.

**Topics**
+ [Supported operating systems](supported-operating-systems.md)
+ [Prerequisites](prerequisites.md)
+ [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md)
+ [Verifying the signature of the CloudWatch agent package](verify-CloudWatch-Agent-Package-Signature.md)
+ [Installing the CloudWatch agent](install-CloudWatch-Agent-on-EC2-Instance.md)
+ [Set up the CloudWatch agent with security-enhanced Linux (SELinux)](CloudWatch-Agent-SELinux.md)
+ [Create the CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md)
+ [Starting the CloudWatch agent](start-CloudWatch-Agent-on-premise-SSM-onprem.md)
+ [Metrics collected by the CloudWatch agent](metrics-collected-by-CloudWatch-agent.md)
+ [Using the CloudWatch agent with related telemetry](CloudWatch-Agent-RelatedEntities.md)
+ [Common scenarios with the CloudWatch agent](CloudWatch-Agent-common-scenarios.md)
+ [CloudWatch agent credentials preference](CloudWatch-Agent-Credentials-Preference.md)
+ [Troubleshooting the CloudWatch agent](troubleshooting-CloudWatch-Agent.md)