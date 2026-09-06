

# Configure permissions for agents
<a name="CloudWatch-NetworkFlowMonitor-agents-ec2-permissions"></a>

To enable agents to send metrics to the Network Flow Monitor ingestion backend, the EC2 instances that the agents run in must use a role that has a policy attached with the correct permissions. To provide the required permissions, use a role that has the following AWS managed policy attached: [CloudWatchNetworkFlowMonitorAgentPublishPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html). Attach this policy to the IAM roles of the EC2 instances where you plan to install Network Flow Monitor agents.

We recommend that you add the permissions before you install agents on the EC2 instances. You can choose to wait until after you install agents, but the agents won't be able to send metrics to the service until the permissions are in place.

**To add permissions for Network Flow Monitor agents**

1. In the AWS Management Console, in the Amazon EC2 console, locate the EC2 instances that you plan to install Network Flow Monitor agents on.

1. Attach the [CloudWatchNetworkFlowMonitorAgentPublishPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html) to the IAM role for each instance.

   If an instance doesn't have an IAM role attached, choose a role by doing the following:

   1. Under **Actions**, choose **Security**.

   1. Choose **Modify IAM role**, or create a new role by choosing **Create new IAM role**.

   1. Choose a role for the instance, and attach the [CloudWatchNetworkFlowMonitorAgentPublishPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.html) policy.