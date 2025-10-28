# How Migration Changes Your Resource

The ingestion RFC described in this section takes the next step of adding configurations to the instance, once it is migrated to your AMS account, so
that AMS can manage it.

The configurations added are AMS-specific as follows.

_Changes made to ingested Linux instances_:

- Software that is installed:
  - [Cloud Init](https://cloud-init.io/ "https://cloud-init.io/"): Used to configure private keys for
    Jarvis Access.
  - [Python 3](https://www.python.org/downloads/release/python-367/ "https://www.python.org/downloads/release/python-367/") (scripting language)
    for all supported operating systems (Except for CentOS 6, RHEL 8, OracleLinux 7).
  - [AWS CloudFormation Python Helper Scripts](../../../AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.md "../../../AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.md"): AWS CloudFormation provides scripts used to install
    software and start services on an Amazon EC2 instances.
  - [AWS CLI](../../../cli/index.md#lang/en_us "../../../cli/index.md#lang/en_us"): The AWS CLI is an open source tool built on top of the AWS SDK for Python (Boto)
    that provides commands for interacting with AWS services.
  - [AWS SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md"): The SSM Agent processes requests from the Systems
    Manager service configures the machine as specified in the request.
  - [AWS CloudWatch Logs Agent](../../../AmazonCloudWatch/latest/logs/QuickStartEC2Instance.md "../../../AmazonCloudWatch/latest/logs/QuickStartEC2Instance.md"): Sends logs to CloudWatch.
  - [AWS CodeDeploy](../../../codedeploy/index.md#lang/en_us "../../../codedeploy/index.md#lang/en_us"): A deployment service that automates application
    deployments to Amazon EC2 instances, on-premises instances, or serverless Lambda functions.
  - [Ruby](https://www.ruby-lang.org/en/documentation/installation/ "https://www.ruby-lang.org/en/documentation/installation/"): Required for CodeDeploy
  - [System Performance Tools (sysstat)](https://github.com/sysstat/sysstat "https://github.com/sysstat/sysstat"): Sysstat contains various utilities to monitor system performance
    and usage activity.
  - [AD Bridge (Formerly PowerBroker Identity Services)](https://github.com/BeyondTrust/pbis-open "https://github.com/BeyondTrust/pbis-open"): Joins non-Microsoft hosts to Active Directory domains.
  - [Trend Micro Deep Security Agent](https://success.trendmicro.com/solution/1104569-deploying-deep-security-agent-dsa-for-linux "https://success.trendmicro.com/solution/1104569-deploying-deep-security-agent-dsa-for-linux"): Anti-Virus software.

- Software that is changed:

      + The instances are configured to use the UTC timezone.

  _Changes made to ingested Windows instances_:

- Software that is installed:
  - [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell "https://aws.amazon.com/powershell"): The AWS Tools for PowerShell let developers and administrators manage their
    AWS services and resources in the PowerShell scripting environment.
  - [Trend Micro Deep Security Agent](https://help.deepsecurity.trendmicro.com/Welcome.html "https://help.deepsecurity.trendmicro.com/Welcome.html"): Anti-Virus protection
  - AMS PowerShell Modules containing PowerShell code for controlling Boot, Active Directory Join, Monitoring, Security, and Logging.

- Software that is changed:
  - Server Message Block (SMB) version 1 is disabled.
  - Windows Remote Management (WinRM) is enabled and configured to listen on port 5986. A firewall rule allowing this inbound port is also created.

- Software that _might be_ installed or changed:
  - [Microsoft .Net Framework 4.5 (Developer platform)](https://www.microsoft.com/net "https://www.microsoft.com/net"), if a version lower then .Net Framework 4.5 is detected.
  - For Windows 2012, ad Windows 2012R2, we upgrade to
    [PowerShell 5.1](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1 "https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1").
