# Onboarding EC2 instances to Accelerate

EC2 instances are onboarded to AMS Accelerate through a process called Automated Instance Configuration, which ensures
that each instance is writing the correct logs and emitting the correct metrics for AMS to properly manage the instance. You should
onboard all of your EC2 intances, unless you specifically want AMS to ignore some. Automated Instance Configuration requires that
specific conditions are met that enable AMS to configure the instance (for details see
[Prerequisites for automated instance configuration in Accelerate](inst-auto-config-pre-reqs.md "inst-auto-config-pre-reqs.md")). The most important condition is that the
AWS Systems Manager agent (SSM agent) needs to be installed on each Amazon EC2 instance that you want AMS to manage for you. For more
information on SSM agent, see
[Working with SSM agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").

## SSM pre-installed in standard AMIs for Accelerate

The SSM agent is already installed on AWS-provided AMIs for the following operating systems.

- Amazon Linux and Amazon Linux 2
- SUSE Linux Enterprise Server (SLES) 12 and 15
- Microsoft Windows Server 2019, 2016, 2012 R2, 2012
- Ubuntu Linux 18.04 and 20.04

If you are using one of these AWS-provided AMIs, see
[Tagging instances in Accelerate](#acc-get-feature-config-tags "#acc-get-feature-config-tags").

## Manual SSM installation of SSM in Accelerate

For the following operating systems, or when using a custom AMI, you can manually install the SSM agent. Or, you can use the AMS SSM Agent auto installation feature. To learn more about SSM auto installation, see [SSM Agent automatic installation](ssm-agent-auto-install.md "ssm-agent-auto-install.md").
For instructions on manual installation, select the link for your operating system:

- [CentOS SSM installation](../../../systems-manager/latest/userguide/agent-install-centos.md "../../../systems-manager/latest/userguide/agent-install-centos.md")
- [Oracle SSM installation](../../../systems-manager/latest/userguide/agent-install-oracle.md "../../../systems-manager/latest/userguide/agent-install-oracle.md")
- [Red Hat SSM installation](../../../systems-manager/latest/userguide/agent-install-rhel.md "../../../systems-manager/latest/userguide/agent-install-rhel.md")
- [SUSE Linux Enterprise Server SSM installation](../../../systems-manager/latest/userguide/agent-install-sles.md "../../../systems-manager/latest/userguide/agent-install-sles.md")
- [Windows SSM installation](../../../systems-manager/latest/userguide/sysman-install-win.md "../../../systems-manager/latest/userguide/sysman-install-win.md")

## Tagging instances in Accelerate

After the SSM agent is installed, you must tag your instances. See
[Tagging in AMS Accelerate](acc-tagging.md "acc-tagging.md").

## Automated instance configuration in Accelerate

Once your instance is tagged, AMS performs an **Automated instance configuration**, which includes:

- Record operating system logs and metrics
- Enable remote access for AMS engineers
- Execute remote commands on the instance

These tasks are essential for AMS monitoring, patch, and log services; and for AMS to respond to incidents. For
details on setting up **Automated Instance Configuration**, see
[Automated instance configuration in AMS Accelerate](acc-inst-auto-config.md "acc-inst-auto-config.md").

After **Automated instance configuration** is complete, you are able to:

- Create incidents and service requests for Amazon EC2 instances and operating systems using the
  Support Center Console. For more information, see [Incident reports, service requests, and billing questions in AMS Accelerate](acc-supp-ex.md "acc-supp-ex.md").
- Access and audit Amazon EC2 logs
- Obtain patch reports
