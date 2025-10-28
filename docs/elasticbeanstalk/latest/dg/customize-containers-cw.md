# Example: Using custom Amazon CloudWatch metrics

This topic provides a configuration example that integrates Elastic Beanstalk metrics with Amazon CloudWatch agent for platforms based on Amazon Linux 2 and later. The configuration
example uses files and commands in an `.ebextensions` configuration file.

Amazon CloudWatch is a web service that enables you to monitor, manage, and publish various metrics, as well as configure alarm actions based on data from
metrics. You can define custom metrics for your own use, and Elastic Beanstalk will push those metrics to Amazon CloudWatch. Once Amazon CloudWatch contains your custom metrics, you can
view those in the Amazon CloudWatch console.

###### The Amazon CloudWatch agent

The Amazon CloudWatch agent enables CloudWatch metric and log collection from both Amazon EC2 instances and on-premises servers across operating systems. The agent
supports metrics collected at the system level. It also supports custom log and metric collection from your applications or services. For more information
about the Amazon CloudWatch agent, see [Collecting metrics and
logs with the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") in the _Amazon CloudWatch User Guide_.

###### Note

Elastic Beanstalk [Enhanced Health Reporting](health-enhanced.md "health-enhanced.md") has native support for publishing a wide range of instance and environment
metrics to CloudWatch. See [Publishing Amazon CloudWatch custom metrics for an environment](health-enhanced-cloudwatch.md "health-enhanced-cloudwatch.md") for details.

###### Topics

- [.Ebextensions configuration file](#customize-containers-cw-update-roles "#customize-containers-cw-update-roles")
- [Permissions](#customize-containers-cw-policy "#customize-containers-cw-policy")
- [Viewing metrics in the CloudWatch console](#customize-containers-cw-console "#customize-containers-cw-console")

## .Ebextensions configuration file

This example uses files and commands in an .ebextensions configuration file to configure and run the Amazon CloudWatch agent on the Amazon Linux 2 platform. The agent
is prepackaged with Amazon Linux 2. If you're using a different operating system, additional steps for installing the agent may be necessary. For more information,
see [Installing the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md")
in the _Amazon CloudWatch User Guide_.

To use this sample, save it to a file named `cloudwatch.config` in a directory named `.ebextensions` at the top
level of your project directory, then deploy your application using the Elastic Beanstalk console (include the .ebextensions directory in your [source bundle](applications-sourcebundle.md "applications-sourcebundle.md")) or the [EB CLI](eb-cli3.md "eb-cli3.md").

For more information about configuration files, see [Advanced environment customization with configuration files (.ebextensions)](ebextensions.md "ebextensions.md").

This file has two sections:

- `files` — This section adds the agent configuration file. It indicates which metrics and logs the agent should send to Amazon CloudWatch.
  In this example, we're only sending the _mem_used_percent_ metric. For a complete listing of system level metrics supported by the
  Amazon CloudWatch agent, see [Metrics
  collected by the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md "../../../AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.md") in the _Amazon CloudWatch User Guide_.
- `container_commands` — This section contains the command that starts the agent, passing in the configuration file as a parameter.
  For more details about `container_commands`, see [Container commands](customize-containers-ec2.md#linux-container-commands "customize-containers-ec2.md#linux-container-commands").

**.ebextensions/cloudwatch.config**

```
files:
  "/opt/aws/amazon-cloudwatch-agent/bin/config.json":
    mode: "000600"
    owner: root
    group: root
    content: |
      {
        "agent": {
          "metrics_collection_interval": 60,
          "run_as_user": "root"
        },
        "metrics": {
          "namespace": "System/Linux",
          "append_dimensions": {
            "AutoScalingGroupName": "${aws:AutoScalingGroupName}"
          },
          "metrics_collected": {
            "mem": {
              "measurement": [
                "mem_used_percent"
              ]
            }
          }
        }
      }
container_commands:
  start_cloudwatch_agent:
    command: /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
```

## Permissions

The instances in your environment need the proper IAM permissions in order to publish custom Amazon CloudWatch metrics using the Amazon CloudWatch agent. You grant
permissions to your environment's instances by adding them to the environment's [instance profile](concepts-roles-instance.md "concepts-roles-instance.md"). You can
add permissions to the instance profile before or after deploying your application.

###### To grant permissions to publish CloudWatch metrics

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose your environment's instance profile role. By default, when you create an environment with the Elastic Beanstalk console or [EB
   CLI](eb-cli3.md "eb-cli3.md"), this is `aws-elasticbeanstalk-ec2-role`.
4. Choose the **Permissions** tab.
5. Under **Permissions Policies**, in the **Permissions** section, choose **Attach
   policies**.
6. Under **Attach Permissions**, choose the AWS managed policy **CloudWatchAgentServerPolicy**. Then click
   **Attach policy**.

For more information about managing policies, see [Working with
Policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md") in the _IAM User Guide_.

## Viewing metrics in the CloudWatch console

After deploying the CloudWatch configuration file to your environment, check the [Amazon CloudWatch
console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home") to view your metrics. Custom metrics will be located in the **CWAgent** namespace.

For more information, see [Viewing available
metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md") in the _Amazon CloudWatch User Guide_.
