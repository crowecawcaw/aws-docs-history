# Use the previous CloudWatch agent to get started with CloudWatch Logs

###### Important

CloudWatch includes a unified CloudWatch agent that can collect both logs and metrics from EC2 instances
and on-premises servers. The older logs-only agent is deprecated and is no longer supported.

For information about migrating from the older logs-only agent to the unified agent, see
[Create the CloudWatch agent configuration file with the wizard](../monitoring/create-cloudwatch-agent-configuration-file-wizard.md "../monitoring/create-cloudwatch-agent-configuration-file-wizard.md").

The rest of this section explains the use of the older CloudWatch Logs agent for customers
who are still using it.

Using the CloudWatch Logs agent, you can publish log data from Amazon EC2 instances running Linux or Windows Server, and logged
events from AWS CloudTrail. We recommend instead using the CloudWatch unified agent to publish your log data. For more information about
the new agent, see [Collect Metrics and Logs from Amazon EC2 Instances and On-Premises Servers
with the CloudWatch Agent](../monitoring/Install-CloudWatch-Agent.md "../monitoring/Install-CloudWatch-Agent.md") in the _Amazon CloudWatch User Guide_.

###### Contents

- [CloudWatch Logs agent prerequisites](#CWL_Prerequisites "#CWL_Prerequisites")
- [Quick Start: Install the agent on a running EC2 Linux instance](QuickStartEC2Instance.md "QuickStartEC2Instance.md")
- [Quick Start: Install the agent on an EC2 Linux instance at launch](EC2NewInstanceCWL.md "EC2NewInstanceCWL.md")
- [Quick Start: Use CloudWatch Logs with Windows Server 2016 instances](QuickStartWindows2016.md "QuickStartWindows2016.md")
- [Quick Start: Use CloudWatch Logs with Windows Server 2012 and Windows Server 2008 instances](QuickStartWindows20082012.md "QuickStartWindows20082012.md")
- [Report the CloudWatch Logs agent status](ReportCWLAgentStatus.md "ReportCWLAgentStatus.md")
- [Start the CloudWatch Logs agent](StartTheCWLAgent.md "StartTheCWLAgent.md")
- [Stop the CloudWatch Logs agent](StopTheCWLAgent.md "StopTheCWLAgent.md")
- [CloudWatch Logs agent reference](AgentReference.md "AgentReference.md")

## CloudWatch Logs agent prerequisites

The CloudWatch Logs agent requires Python version 2.7, 3.0, or 3.3, and any of the
following versions of Linux:

- Amazon Linux version 2014.03.02 or later. Amazon Linux 2 is not supported
- Ubuntu Server version 12.04, 14.04, or 16.04
- CentOS version 6, 6.3, 6.4, 6.5, or 7.0
- Red Hat Enterprise Linux (RHEL) version 6.5 or 7.0
- Debian 8.0
