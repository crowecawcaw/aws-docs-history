

# Installing the CloudWatch agent
<a name="install-CloudWatch-Agent-on-EC2-Instance"></a>

You can install the CloudWatch agent on your Amazon EC2 instances, on-premises servers, and in containerized environments to collect metrics, logs, and traces. The agent supports Linux, Windows, and macOS operating systems. There are several ways to install the agent, including using Systems Manager, from the CloudWatch console, installing from the command line, or installing using a configuration file. Before installing, make sure you have the required IAM permissions and network access configured.

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
+ [Install and Configure Amazon CloudWatch Agent with Workload Detection in the CloudWatch console](install-cloudwatch-agent-workload-detection.md)
+ [Manual installation on Amazon EC2](manual-installation.md)
+ [Install the CloudWatch agent using AWS Systems Manager](installing-cloudwatch-agent-ssm.md)
+ [Install the CloudWatch agent on on-premises servers](install-CloudWatch-Agent-on-premise.md)
+ [Install the CloudWatch agent on Azure](install-CloudWatch-Agent-on-Azure.md)
+ [Install the CloudWatch agent on Google Cloud](install-CloudWatch-Agent-on-Google-Cloud.md)
+ [Install the CloudWatch agent on new instances using CloudFormation](Install-CloudWatch-Agent-New-Instances-CloudFormation.md)