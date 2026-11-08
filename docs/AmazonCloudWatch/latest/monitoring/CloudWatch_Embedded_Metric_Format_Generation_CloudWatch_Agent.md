

# Using the CloudWatch agent to send embedded metric format logs
<a name="CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent"></a>

 This section describes how to install and use the CloudWatch agent. The first part of this section describes how to install the CloudWatch agent. The second part of this section describes how to use the CloudWatch agent to send embedded metric format logs. If you want to use this method, you must install the CloudWatch agent for the AWS services you want to send embedded metric format logs from. Then you can begin sending the events. The CloudWatch agent must be version 1.230621.0 or later.

To publish custom metrics from containerized applications running on Amazon ECS and Amazon EKS, we recommend sending them to the CloudWatch OTLP endpoint rather than using the embedded metric format. For more information, see [Publish custom metrics with OpenTelemetry](metrics-otel-send.md). Container infrastructure metrics are covered by CloudWatch Container Insights.

You do not need the CloudWatch agent to publish embedded metric format logs from Lambda functions. For more information, see [Using the embedded metric format with Lambda](CloudWatch_Embedded_Metric_Format_Lambda.md).

## Installing the CloudWatch agent
<a name="CloudWatch_Embedded_Metric_Format_Generation_Install_Agent"></a>

Install the CloudWatch agent for each service that sends embedded metric format logs. To install the agent, see [Installing the CloudWatch agent](install-CloudWatch-Agent-on-EC2-Instance.md).

After you install the agent, configure it to listen on a UDP or TCP port for the embedded metric format logs. The following example configuration listens on the default socket `tcp:25888`. For more information about agent configuration, see [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md).

```
{
  "logs": {
    "metrics_collected": {
      "emf": { }
    }
  }
}
```

## Using the CloudWatch agent to send embedded metric format logs
<a name="CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent_Send_Logs"></a>

When you have the CloudWatch agent installed and running, you can send the embedded metric format logs over TCP or UDP. There are two requirements when sending the logs over the agent:
+ The logs must contain a `LogGroupName` key that tells the agent which log group to use.
+ Each log event must be on a single line. In other words, a log event cannot contain the newline (\\n) character.

The log events must also follow the embedded metric format specification. For more information, see [Specification: Embedded metric format](CloudWatch_Embedded_Metric_Format_Specification.md).

If you plan to create alarms on metrics created using embedded metric format, see [Setting alarms on metrics created with the embedded metric format](CloudWatch_Embedded_Metric_Format_Alarms.md) for recommendations.

The following is an example of sending log events manually from a Linux bash shell. You can instead use the UDP socket interfaces provided by your programming language of choice. 

```
echo '{"_aws":{"Timestamp":1574109732004,"LogGroupName":"Foo","CloudWatchMetrics":[{"Namespace":"MyApp","Dimensions":[["Operation"]],"Metrics":[{"Name":"ProcessingLatency","Unit":"Milliseconds","StorageResolution":60}]}]},"Operation":"Aggregator","ProcessingLatency":100}' \
> /dev/udp/0.0.0.0/25888
```

**Note**  
 With the embedded metric format, you can track the processing of your EMF logs by metrics that are published in the `AWS/Logs` namespace of your account. These can be used to track failed metric generation from EMF, as well as whether failures happen due to parsing or validation. For more details see [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.html). 