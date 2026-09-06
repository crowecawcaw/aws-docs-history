

# Onboarding EC2 instances to Accelerate
<a name="acc-get-feature-ec2-onboarding"></a>

EC2 instances are onboarded to AMS Accelerate through a process called Automated Instance Configuration, which ensures that each instance is writing the correct logs and emitting the correct metrics for AMS to properly manage the instance. You should onboard all of your EC2 intances, unless you specifically want AMS to ignore some. Automated Instance Configuration requires that specific conditions are met that enable AMS to configure the instance (for details see [Prerequisites for automated instance configuration in Accelerate](inst-auto-config-pre-reqs.md)). The most important condition is that the AWS Systems Manager agent (SSM agent) needs to be installed on each Amazon EC2 instance that you want AMS to manage for you. For more information on SSM agent, see [Working with SSM agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html). 

## SSM pre-installed in standard AMIs for Accelerate
<a name="acc-get-feature-config-ssm-preinstalled"></a>

The SSM agent is already installed on AWS-provided AMIs for the following operating systems.
+ Amazon Linux and Amazon Linux 2
+ SUSE Linux Enterprise Server (SLES) 12 and 15
+ Microsoft Windows Server 2019, 2016, 2012 R2, 2012
+ Ubuntu Linux 18.04 and 20.04

If you are using one of these AWS-provided AMIs, see [Tagging instances in Accelerate](#acc-get-feature-config-tags).

## Manual SSM installation of SSM in Accelerate
<a name="acc-get-feature-config-ssm-install"></a>

For the following operating systems, or when using a custom AMI, you can manually install the SSM agent. Or, you can use the AMS SSM Agent auto installation feature. To learn more about SSM auto installation, see [SSM Agent automatic installation](ssm-agent-auto-install.md). For instructions on manual installation, select the link for your operating system:
+ [ CentOS SSM installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-centos.html)
+ [ Oracle SSM installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-oracle.html)
+ [ Red Hat SSM installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-rhel.html)
+ [ SUSE Linux Enterprise Server SSM installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-sles.html)
+ [ Windows SSM installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-win.html)

## Tagging instances in Accelerate
<a name="acc-get-feature-config-tags"></a>

After the SSM agent is installed, you must tag your instances. See [Tagging in AMS Accelerate](acc-tagging.md).

## Automated instance configuration in Accelerate
<a name="acc-get-feature-config-aic"></a>

Once your instance is tagged, AMS performs an **Automated instance configuration**, which includes:
+ Record operating system logs and metrics
+ Enable remote access for AMS engineers
+ Execute remote commands on the instance

 These tasks are essential for AMS monitoring, patch, and log services; and for AMS to respond to incidents. For details on setting up **Automated Instance Configuration**, see [Automated instance configuration in AMS Accelerate](acc-inst-auto-config.md). 

After **Automated instance configuration** is complete, you are able to:
+ Create incidents and service requests for Amazon EC2 instances and operating systems using the Support Center Console. For more information, see [Incident reports, service requests, and billing questions in AMS Accelerate](acc-supp-ex.md).
+ Access and audit Amazon EC2 logs
+ Obtain patch reports