# Install and manage agents for EC2 instances

Follow the steps in this section to install Network Flow Monitor agents for workloads on Amazon EC2 instances. You can install agents
 by using SSM or by downloading and installing prebuilt packages for the Network Flow Monitor agent by using the command line.

Regardless of the method that you use to install agents on EC2 instances, you must configure permissions for the
 agents to enable them to send performance metrics to the Network Flow Monitor backend.

###### Contents

* [Configure permissions for agents](#CloudWatch-NetworkFlowMonitor-agents-ec2-permissions "#CloudWatch-NetworkFlowMonitor-agents-ec2-permissions")
* [EC2 instance agents with SSM](CloudWatch-NetworkFlowMonitor-agents-ec2-install-ssm.md "CloudWatch-NetworkFlowMonitor-agents-ec2-install-ssm.md")
* [Download and install the agent](CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline.md "CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline.md")

## Configure permissions for agents


To enable agents to send metrics to the Network Flow Monitor ingestion backend, the EC2 instances that the agents run
 in must use a role that has a policy attached with the correct permissions. To provide the required permissions, 
 use a role that has the following AWS managed policy attached: [CloudWatchNetworkFlowMonitorAgentPublishPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html"). Attach this policy to the IAM roles of the 
 EC2 instances where you plan to install Network Flow Monitor agents.


We recommend that you add the permissions before you install agents on the EC2 instances. You 
 can choose to wait until after you install agents, but the agents won't be able to send metrics to the 
 service until the permissions are in place.


###### To add permissions for Network Flow Monitor agents

1. In the AWS Management Console, in the Amazon EC2 console, locate the EC2 instances that you plan to
 install Network Flow Monitor agents on.
2. Attach the [CloudWatchNetworkFlowMonitorAgentPublishPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html") to the IAM role for each
 instance.


If an instance doesn't have an IAM role attached, choose a role by doing the following:




	1. Under
	 **Actions**, choose **Security**.
	2. Choose **Modify IAM role**, or create a new role by choosing 
	 **Create new IAM role**.
	3. Choose a role for the instance, and attach the [CloudWatchNetworkFlowMonitorAgentPublishPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html") policy.
