# Manually installing SSM Agent on Red Hat Enterprise Linux

instances

The Amazon Machine Images (AMIs) for Red Hat Enterprise Linux (RHEL) that are provided by AWS
do not come with AWS Systems Manager Agent (SSM Agent) preinstalled by default. For a list
of AWS managed AMIs on which the agent might be preinstalled, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

Use the information in this section to help you manually install or reinstall
SSM Agent on a RHEL instance.

###### Before you begin

Before you install SSM Agent on a RHEL instance, note the
following:

- For important information that applies to installation of SSM Agent on
  all Linux-based operating systems, see [Manually installing and
  uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md").
- If you use a `yum` command to update SSM Agent on a managed node after the agent
  has been installed or updated using the SSM document `AWS-UpdateSSMAgent`, you
  might see the following message: `"Warning: RPMDB altered outside of yum."` This
  message is expected and can be safely ignored.

###### Topics

- [Install SSM Agent on RHEL 8.x,
  9.x, and 10.x](agent-install-rhel-8-9.md "agent-install-rhel-8-9.md")
- [Install SSM Agent on RHEL
  7.x](agent-install-rhel-7.md "agent-install-rhel-7.md")
