

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with SSM Agent
<a name="ssm-agent"></a>

AWS Systems Manager Agent (SSM Agent) is Amazon software that runs on Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, on-premises servers, and virtual machines (VMs). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources. The agent processes requests from the Systems Manager service in the AWS Cloud, and then runs them as specified in the request. SSM Agent then sends status and execution information back to the Systems Manager service by using the [Amazon Message Gateway Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagegatewayservice.html) (`ssmmessages`). (In AWS Regions launched before 2024, status and execution information might also be sent back by the [Amazon Message Delivery Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagedeliveryservice.html) (service prefix: `ec2messages`).)

If you monitor traffic, you see that your managed nodes communicate with `ssmmessages.*` endpoints and possibly `ec2messages.*` endpoints. For more information, see [Reference: ec2messages, ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md). For information about porting SSM Agent logs to Amazon CloudWatch Logs, see [Logging and monitoring in AWS Systems Manager](monitoring.md).

**Topics**
+ [Learn technical details about the SSM Agent](ssm-agent-technical-details.md)
+ [Find AMIs with the SSM Agent preinstalled](ami-preinstalled-agent.md)
+ [Working with SSM Agent on EC2 instances for Linux](ssm-agent-linux.md)
+ [Working with SSM Agent on EC2 instances for macOS](ssm-agent-macos.md)
+ [Working with SSM Agent on EC2 instances for Windows Server](ssm-agent-windows.md)
+ [Checking SSM Agent status and starting the agent](ssm-agent-status-and-restart.md)
+ [Checking the SSM Agent version number](ssm-agent-get-version.md)
+ [Viewing SSM Agent logs](ssm-agent-logs.md)
+ [Restricting access to root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md)
+ [Automating updates to SSM Agent](ssm-agent-automatic-updates.md)
+ [Subscribing to SSM Agent notifications](ssm-agent-subscribe-notifications.md)
+ [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md)