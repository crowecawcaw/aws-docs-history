

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Manually installing SSM Agent on Ubuntu Server instances
<a name="agent-install-ubuntu"></a>

In most cases, the Amazon Machine Images (AMIs) for Ubuntu Server that are provided by AWS come with AWS Systems Manager Agent (SSM Agent) preinstalled by default. For more information, see [Find AMIs with the SSM Agent preinstalled](ami-preinstalled-agent.md).

In the event that SSM Agent isn’t preinstalled on a new Ubuntu Server instance, or if you need to manually reinstall the agent, use the information in this section to help you.

**Before you begin**  
Before you install SSM Agent on an Ubuntu Server instance, note the following:
+ For important information that applies to installation of SSM Agent on all Linux-based operating systems, see [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md).

**Topics**
+ [Install SSM Agent on Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04](agent-install-ubuntu-64-snap.md)