

# Install and manage agents for EC2 instances
<a name="CloudWatch-NetworkFlowMonitor-agents-ec2"></a>

Follow the steps in this section to install Network Flow Monitor agents for workloads on Amazon EC2 instances. Installing agents requires two steps: first, configure permissions to allow the agents to send metrics to the Network Flow Monitor backend, and then install the agents using one of the available methods.

Regardless of the method that you use to install agents on EC2 instances, you must configure permissions for the agents to enable them to send performance metrics to the Network Flow Monitor backend.

**Step 1: Configure permissions**  
Before installing agents, set up the required IAM permissions. See [Configure permissions for agents](CloudWatch-NetworkFlowMonitor-agents-ec2-permissions.md).

**Step 2: Install agents**  
Choose one of the following methods to install the Network Flow Monitor agent on your EC2 instances:
+ [Install agents via CloudShell script](CloudWatch-NetworkFlowMonitor-agents-ec2-install-cloudshell.md) – The fastest way to install agents. Select your instances in the Network Flow Monitor console and run an automated script in .
+ [Install agents by using CDK](CloudWatch-NetworkFlowMonitor-agents-ec2-install-cdk.md) – Use AWS Cloud Development Kit (AWS CDK) to install agents as part of your infrastructure-as-code deployment.
+ [Install agents using SSM](CloudWatch-NetworkFlowMonitor-agents-ec2-install-ssm.md) – Use AWS Systems Manager Distributor to install and manage agents from the console.
+ [Download and install the agent from the command line](CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline.md) – Download prebuilt RPM or DEB packages and install them directly on your instances.
+ [Install agents using AWS CLI with SSM commands](CloudWatch-NetworkFlowMonitor-agents-ec2-install-cli-ssm.md) – Use the AWS Command Line Interface to send SSM commands to install and activate agents.

**Topics**
+ [Configure permissions for agents](CloudWatch-NetworkFlowMonitor-agents-ec2-permissions.md)
+ [Install via CloudShell](CloudWatch-NetworkFlowMonitor-agents-ec2-install-cloudshell.md)
+ [EC2 instance agents with SSM](CloudWatch-NetworkFlowMonitor-agents-ec2-install-ssm.md)
+ [Download and install the agent](CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline.md)
+ [Install via CLI SSM commands](CloudWatch-NetworkFlowMonitor-agents-ec2-install-cli-ssm.md)
+ [Install with CDK](CloudWatch-NetworkFlowMonitor-agents-ec2-install-cdk.md)