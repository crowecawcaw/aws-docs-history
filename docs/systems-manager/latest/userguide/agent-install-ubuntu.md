• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Manually installing SSM Agent on

Ubuntu Server instances

###### Important

Before you install SSM Agent on a 64-bit version of Ubuntu Server, ensure
that you are using the correct installation tools. Beginning with Amazon
Machine Images (AMIs) that are identified with 20180627, SSM Agent is
pre-installed on version 16.04 using Snap packages. On instances created
from earlier AMIs, SSM Agent must be installed using deb installer packages.
For more information, see [Determining the correct
SSM Agent version to install on 64-bit Ubuntu Server 16.04
instances](agent-install-ubuntu-about-v16.md "agent-install-ubuntu-about-v16.md").

In most cases, the Amazon Machine Images (AMIs) for Ubuntu Server that are provided
by AWS come with AWS Systems Manager Agent (SSM Agent) preinstalled by default. For more
information, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

In the event that SSM Agent isn’t preinstalled on a new Ubuntu Server instance,
or if you need to manually reinstall the agent, use the information in this
section to help you.

###### Before you begin

Before you install SSM Agent on an Ubuntu Server instance, note the
following:

- For important information that applies to installation of SSM Agent on
  all Linux-based operating systems, see [Manually installing and
  uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md").

###### Topics

- [Install SSM Agent on
  Ubuntu Server 16.04 LTS 64-bit (Snap), 18.04, 20.04, 22.04 LTS, 23.10,
  24.04 LTS, 24.0, and 25.04](agent-install-ubuntu-64-snap.md "agent-install-ubuntu-64-snap.md")
- [Install SSM Agent on
  Ubuntu Server 16.04 64-bit (deb)](agent-install-ubuntu-64-deb.md "agent-install-ubuntu-64-deb.md")
- [Install SSM Agent on Ubuntu Server
  16.04 32-bit](agent-install-ubuntu-32.md "agent-install-ubuntu-32.md")
- [Determining the correct
  SSM Agent version to install on 64-bit Ubuntu Server 16.04
  instances](agent-install-ubuntu-about-v16.md "agent-install-ubuntu-about-v16.md")
