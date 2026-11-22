

# Installing the CloudWatch agent

You can install the CloudWatch agent on your Amazon EC2 instances, on-premises servers, and in containerized environments to collect metrics, logs, and traces. The agent supports Linux, Windows, and macOS operating systems. There are several ways to install the agent, including using Systems Manager, from the CloudWatch console, installing from the command line, or installing using a configuration file. Before installing, make sure you have the required IAM permissions and network access configured.

The best way to install the agent depends on where you run your workloads. Use the following guidance to choose an installation method for your environment, and then follow the linked instructions.
+ **Amazon EKS** – Install the agent through the `amazon-cloudwatch-observability` Amazon EKS add-on, or its Helm chart. You don't configure the agent manually, and this setup turns on Container Insights and CloudWatch Application Signals. For more information, see [Install the CloudWatch agent on Amazon EKS](install-CloudWatch-Agent-on-EKS.md). To install the add-on directly, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md).
+ **Amazon ECS** – Deploy the agent as a sidecar container in your task definition. For Container Insights on Amazon ECS, use the quick-start setup. For more information, see [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](deploy-container-insights-ECS-instancelevel.md).
+ **Amazon EC2 instances and on-premises servers** – You can install and configure the agent from the CloudWatch console with workload detection (see [Install and Configure Amazon CloudWatch Agent with Workload Detection in the CloudWatch console](install-cloudwatch-agent-workload-detection.md)), or download and install the agent manually (see [Manual installation on Amazon EC2](manual-installation.md)). To install and automatically update the agent across a fleet, we recommend using Systems Manager. Systems Manager Distributor with State Manager keeps the `AmazonCloudWatchAgent` managed package current on every instance. For more information, see [Install the CloudWatch agent using AWS Systems Manager](installing-cloudwatch-agent-ssm.md).

## Installation method comparison
<a name="CloudWatch-Agent-installation-method-comparison"></a>

The following table compares the supported ways to install and maintain the CloudWatch agent. Use it to choose the approach that fits your environment.


| Method | Best for | Configuration | Updates | 
| --- | --- | --- | --- | 
| SSM Run Command | Fleets of instances | Stored in Parameter Store, applied centrally | Updated via `AWS-ConfigureAWSPackage`; a running agent is restarted on its existing configuration | 
| Manual download (CLI) | Single instance or testing | Local config file on the instance | Manual re-download and reinstall; generated configuration files are left in place | 
| Package manager (Linux) | Linux instances with existing config management | Local config file | Configuration preserved across package updates | 

**Topics**
+ [Installation method comparison](#CloudWatch-Agent-installation-method-comparison)
+ [Install the CloudWatch agent on Amazon EC2](install-CloudWatch-Agent-on-EC2.md)
+ [Install the CloudWatch agent on Amazon ECS](install-CloudWatch-Agent-on-ECS.md)
+ [Install the CloudWatch agent on Amazon EKS](install-CloudWatch-Agent-on-EKS.md)
+ [Install the CloudWatch agent on on-premises servers](install-CloudWatch-Agent-on-premise.md)
+ [Install the CloudWatch agent on Azure](install-CloudWatch-Agent-on-Azure.md)
+ [Install the CloudWatch agent on Google Cloud (GCP)](install-CloudWatch-Agent-on-Google-Cloud.md)