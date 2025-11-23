# Install and Configure Amazon CloudWatch Agent with Workload Detection in the CloudWatch console

## Introduction

You can use the CloudWatch Getting Started console to install and configure the CloudWatch agent on Amazon EC2 instances. The Amazon CloudWatch agent is a lightweight software component that collects system-level metrics, logs, and traces from your Amazon EC2 instances. By automating the collection and delivery of monitoring data to CloudWatch, the agent enables you to gain actionable insights, optimize resource utilization, and ensure your applications are running smoothly with minimal configuration effort.

Configure the CloudWatch agent with pre-defined, workload-specific configurations that leverage automatic workload detection to identify running applications and services on your instances. You can customize data collection with specific metrics, logs, and traces, enabling you to monitor application performance and troubleshoot issues effectively.

## How it Works

The CloudWatch agent detects workloads running on your Amazon EC2 instances through automatic workload detection capabilities. This feature identifies running applications and services on your instances, enabling intelligent monitoring without manual configuration.

Observability solutions provide pre-defined, workload-specific configurations tailored to common applications such as Apache Kafka, Apache Tomcat, Java Virtual Machines (JVM), NGINX, and NVIDIA GPU workloads. These solutions streamline the monitoring setup by automatically collecting the right metrics, logs, and traces specific to each detected workload, eliminating the need for manual instrumentation and configuration.

When workload detection is enabled, the agent analyzes your instance environment and automatically selects relevant pre-configured monitoring templates. These configurations are optimized by AWS subject-matter experts to capture the most important telemetry data for each workload type, ensuring you have comprehensive observability from the start.

## Prerequisites

### SSM Agent Installation (Required)

You must have AWS Systems Manager (SSM) agent installed on your Amazon EC2 instances. SSM agent comes pre-installed on most AWS-supplied Amazon Machine Images (AMIs), If you need to manually install or update the SSM agent, refer to the [Systems Manager documentation](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").

###### Note

Default Host Management Configuration (DHMC) is a Systems Manager feature that automatically grants Amazon EC2 instances permissions to connect to Systems Manager without requiring you to manually attach an IAM instance profile to each instance. If your Amazon EC2 instances are using DHMC and the CloudWatch agent installation process attaches the CloudWatch policy to your instances, it can take up to 30 minutes for the new policy to take effect. This delay can postpone the publication of metrics, logs, and traces to CloudWatch. To mitigate, you can create your Amazon EC2 instances with an IAM role that contains the [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") policy.

### Workload Detection (Recommended)

Workload detection is an opt-in feature that automatically identifies running applications and services on your instances. We recommend turning on workload detection to take advantage of pre-configured, workload-specific monitoring templates. You can enable workload detection in the [CloudWatch console settings](https://console.aws.amazon.com/cloudwatch/home#settings "https://console.aws.amazon.com/cloudwatch/home#settings").

## Getting started

Open the Getting Started with Amazon CloudWatch agent page in the Amazon CloudWatch console: [https://console.aws.amazon.com/cloudwatch/home#cloudwatch-agent](https://console.aws.amazon.com/cloudwatch/home#cloudwatch-agent "https://console.aws.amazon.com/cloudwatch/home#cloudwatch-agent")

**Manual instance deployment for CloudWatch Agent**

Manually select up to 50 instances for CloudWatch agent installation and configuration. This targeted approach allows you to enhance monitoring for specific Amazon EC2 instances.

**Tag-based deployment for CloudWatch Agent**

Use tag-based deployment to install and configure the CloudWatch agent on fleets of Amazon EC2 instances. This method applies to all current and future instances with matching tags.

**Tag-based configuration**

Tag-based configurations allow you to efficiently organize, view, and modify configurations, helping you to manage CloudWatch agent and its configuration across fleets of Amazon EC2 instances.

**CloudWatch agent installation**

Install the CloudWatch agent to collect metrics, logs, and traces from Amazon EC2 instances and on-premises hosts. This telemetry provides important health and performance data about your infrastructure and applications.

**CloudWatch agent configuration**

Configure the CloudWatch agent with pre-defined, workload-specific configurations. You can customize data collection with specific metrics, logs, and traces, enabling you to monitor application performance and troubleshoot issues effectively.

## Costs

Additional metrics that you add during this process are billed as custom metrics. For more information about CloudWatch metrics pricing, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").
