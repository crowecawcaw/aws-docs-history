

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# How Migration Changes Your Resource
<a name="ex-migrate-changes"></a>

The ingestion RFC described in this section takes the next step of adding configurations to the instance, once it is migrated to your AMS account, so that AMS can manage it.

The configurations added are AMS-specific as follows.

*Changes made to ingested Linux instances*:
+ Software that is installed:
  + [Cloud Init](https://cloud-init.io/): Used to configure private keys for Jarvis Access.
  + [Python 3](https://www.python.org/downloads/release/python-367/) (scripting language) for all supported operating systems (Except for CentOS 6, RHEL 8, OracleLinux 7).
  +  [ AWS CloudFormation Python Helper Scripts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html): AWS CloudFormation provides scripts used to install software and start services on an Amazon EC2 instances.
  + [AWS CLI](https://docs.aws.amazon.com/cli/index.html#lang/en_us): The AWS CLI is an open source tool built on top of the AWS SDK for Python (Boto) that provides commands for interacting with AWS services.
  + [AWS SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html): The SSM Agent processes requests from the Systems Manager service configures the machine as specified in the request.
  + [AWS CloudWatch Logs Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html): Sends logs to CloudWatch.
  + [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/index.html#lang/en_us): A deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, or serverless Lambda functions.
  + [Ruby](https://www.ruby-lang.org/en/documentation/installation/): Required for CodeDeploy
  + [System Performance Tools (sysstat)](https://github.com/sysstat/sysstat): Sysstat contains various utilities to monitor system performance and usage activity.
  + [AD Bridge (Formerly PowerBroker Identity Services)](https://docs.beyondtrust.com/adb/docs/adb-overview): Joins non-Microsoft hosts to Active Directory domains.
  + [Trend Micro Deep Security Agent](https://success.trendmicro.com/solution/1104569-deploying-deep-security-agent-dsa-for-linux): Anti-Virus software.
+ Software that is changed:
  + The instances are configured to use the UTC timezone.

*Changes made to ingested Windows instances*:
+ Software that is installed:
  + [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell): The AWS Tools for PowerShell let developers and administrators manage their AWS services and resources in the PowerShell scripting environment.
  + [Trend Micro Deep Security Agent](https://help.deepsecurity.trendmicro.com/Welcome.html): Anti-Virus protection
  + AMS PowerShell Modules containing PowerShell code for controlling Boot, Active Directory Join, Monitoring, Security, and Logging.
+ Software that is changed:
  + Server Message Block (SMB) version 1 is disabled.
  + Windows Remote Management (WinRM) is enabled and configured to listen on port 5986. A firewall rule allowing this inbound port is also created.
+ Software that *might be* installed or changed:
  + [Microsoft .Net Framework 4.5 (Developer platform)](https://www.microsoft.com/net), if a version lower then .Net Framework 4.5 is detected.
  + For Windows 2012, ad Windows 2012R2, we upgrade to [PowerShell 5.1](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1).