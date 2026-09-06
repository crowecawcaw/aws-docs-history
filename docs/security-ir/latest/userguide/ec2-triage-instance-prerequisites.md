

# Instance prerequisites for EC2 Triage
<a name="ec2-triage-instance-prerequisites"></a>

For EC2 Triage to collect investigative data from an Amazon EC2 instance, the instance must meet the following requirements:
+ The Systems Manager Agent (SSM Agent) must be installed and running on the instance. For more information, see [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) in the *AWS Systems Manager User Guide*.
+ The instance must be managed by AWS Systems Manager. This requires the instance to have an IAM instance profile with the appropriate Systems Manager permissions and network connectivity to the Systems Manager endpoints. For more information, see [Setting up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html) in the *AWS Systems Manager User Guide*.
+ The instance must be running a supported operating system:
  + **Linux**:
    + Amazon Linux 2
    + Amazon Linux 2023
    + Ubuntu 18.04, 20.04, 22.04, 24.04
    + Red Hat Enterprise Linux (RHEL) 7.x, 8.x, 9.x
    + CentOS 7.x, 8.x
    + SUSE Linux Enterprise Server (SLES) 12.x, 15.x
    + Debian 10, 11, 12
  + **Windows**:
    + Windows Server 2012 R2
    + Windows Server 2016
    + Windows Server 2019
    + Windows Server 2022