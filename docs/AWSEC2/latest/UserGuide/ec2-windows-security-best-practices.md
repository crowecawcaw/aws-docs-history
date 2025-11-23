# Security best practices for Windows instances

We recommend that you follow these security best practices for your Windows instances.

###### Contents

- [High-level security best practices](#high-level-security "#high-level-security")
- [Update management](#ec2-windows-update-management "#ec2-windows-update-management")
- [Configuration management](#configuration-management "#configuration-management")
- [Change management](#change-management "#change-management")
- [Audit and accountability for Amazon EC2 Windows instances](#audit-accountability "#audit-accountability")

## High-level security best practices

You should adhere to the following high-level security best practices for your
Windows instances:

- Least access – Grant access only to systems and
  locations that are trusted and expected. This applies to all Microsoft products such
  as Active Directory, Microsoft business productivity servers, and infrastructure
  services such as Remote Desktop Services, reverse proxy servers, IIS web servers,and
  more. Use AWS capabilities such as Amazon EC2 instance security groups, network access
  control lists (ACLs), and Amazon VPC public/private subnets to layer security across
  multiple locations in an architecture. Within a Windows instance, customers can use
  Windows Firewall to further layer a defense-in-depth strategy within their
  deployment. Install only the OS components and applications that are necessary for
  the system to function as designed. Configure infrastructure services such as IIS to
  run under service accounts, or to use features such as application pool identities
  to access resources locally and remotely across your infrastructure.
- Least privilege – Determine the minimum set of
  privileges that instances and accounts need in order to perform their functions.
  Restrict these servers and users to only allow these defined permissions. Use
  techniques such as Role Based Access Controls to reduce the surface area of
  administrative accounts, and create the most limited roles to accomplish a task. Use
  OS features such as Encrypting File System (EFS) within NTFS to encrypt sensitive
  data at rest, and control application and user access to it.
- Configuration management – Create a baseline
  server configuration that incorporates up-to-date security patches and host-based
  protection suites that include anti-virus, anti-malware, intrusion
  detection/prevention, and file integrity monitoring. Assess each server against the
  current recorded baseline to identify and flag any deviations. Ensure each server is
  configured to generate and securely store appropriate log and audit data.
- Change management – Create processes to control
  changes to server configuration baselines and work toward fully automated change
  processes. Also, leverage Just Enough Administration (JEA) with Windows PowerShell
  DSC to limit administrative access to the minimum required functions.
- Patch management – Implement processes that
  regularly patch, update, and secure the operating system and applications on your
  EC2 instances.
- Audit logs – Audit access and all changes to Amazon EC2
  instances to verify server integrity and ensure only authorized changes are made.
  Leverage features such as [Enhanced Logging for IIS](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-85/enhanced-logging-for-iis85 "https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-85/enhanced-logging-for-iis85") to enhance default logging capabilities. AWS
  capabilities such as VPC Flow Logs and AWS CloudTrail are also available to audit network
  access, including allowed/denied requests and API calls, respectively.

## Update management

To ensure the best results when you run Windows Server on Amazon EC2, we recommend
that you implement the following best practices:

- [Configure Windows Update](#windows-update "#windows-update")
- [Update drivers](#drivers "#drivers")
- [Use the latest Windows AMIs](#AMI "#AMI")
- [Test performance before migration](#test "#test")
- [Update launch agents](#agents "#agents")
- Reboot your Windows instance after you install updates. For
  more information, see [Reboot your Amazon EC2 instance](ec2-instance-reboot.md "ec2-instance-reboot.md").

For information about how to upgrade or migrate a Windows instance to a newer
version of Windows Server, see [Upgrade an EC2 Windows instance to a newer version of
Windows Server](serverupgrade.md "serverupgrade.md").

###### Configure Windows Update

By default, instances that are launched from AWS Windows Server AMIs
don't receive updates through Windows Update.

###### Update Windows drivers

Maintain the latest drivers on all Windows EC2 instances to ensure that the latest
issue fixes and performance enhancements are applied across your fleet. Depending on
your instance type, you should update the AWS PV, Amazon ENA, and AWS NVMe drivers.

- Use [SNS topics](xen-drivers-overview.md#drivers-subscribe-notifications "xen-drivers-overview.md#drivers-subscribe-notifications") to receive updates for new driver releases.
- Use the AWS Systems Manager Automation runbook [AWSSupport-UpgradeWindowsAWSDrivers](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-upgradewindowsawsdrivers.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-upgradewindowsawsdrivers.md") to easily apply the updates across
  your instances.

###### Launch instances using

the latest Windows AMIs

AWS releases new Windows AMIs each month, which contain the latest OS patches, drivers,
and launch agents. You should leverage the latest AMI when you launch new instances or when
you build your own custom images.

- To view updates to each release of the AWS Windows AMIs, see [AWS Windows AMI version history](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md").
- To build with the latest available AMIs, see [Query for the Latest Windows AMI Using Systems Manager Parameter
  Store](https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/ "https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/").
- For more information about specialized Windows AMIs that you can use to
  launch instances for your database and compliance hardening use cases, see
  [Specialized Windows AMIs](../../../ec2/latest/windows-ami-reference/specialized-windows-amis.md "../../../ec2/latest/windows-ami-reference/specialized-windows-amis.md")
  in the _AWS Windows AMI Reference_.

###### Test

system/application performance before migration

Migrating enterprise applications to AWS can involve many variables and
configurations. Always performance test the EC2 solution to ensure that:

- Instance types are properly configured, including instance size, enhanced
  networking, and tenancy (shared or dedicated).
- Instance topology is appropriate for the workload and leverages high-performance
  features when necessary, such as dedicated tenancy, placement groups, instance store
  volumes, and bare metal.

###### Install the latest version of EC2Launch v2

Install the latest EC2Launch v2 agent to ensure that the latest enhancements are
applied across your fleet. For more information, see [Install EC2Launch v2](ec2launch-v2-install.md "ec2launch-v2-install.md").

If you have a mixed fleet, or if you want to continue to use
the EC2Launch (Windows Server 2016 and 2019) or EC2 Config (legacy OS only) agents, update to the latest versions of the respective agents.

Automatic updates are supported on the following combinations of Windows
Server version and launch agents. You can opt in to automatic updates in the [SSM Quick
Setup Host Management](../../../systems-manager/latest/userguide/quick-setup-host-management.md "../../../systems-manager/latest/userguide/quick-setup-host-management.md") console under **Amazon EC2 Launch
Agents**.

| Windows Version | EC2Launch v1 | EC2Launch v2 |
| --------------- | ------------ | ------------ |
| 2016            | ✓            | ✓            |
| 2019            | ✓            | ✓            |
| 2022            |              | ✓            |

- For more information about updating to EC2Launch v2, see [Install the latest version of
  EC2Launch v2](ec2launch-v2-install.md "ec2launch-v2-install.md").
- For information to manually update EC2Config, see [Install the latest version of EC2Config](UsingConfig_Install.md "UsingConfig_Install.md").
- For information to manually update EC2Launch, see [Install the latest version of EC2Launch](ec2launch-download.md "ec2launch-download.md").

## Configuration management

Amazon Machine Images (AMIs) provide an initial configuration for an Amazon EC2 instance, which
includes the Windows OS and optional customer-specific customizations, such as applications
and security controls. Create an AMI catalog containing customized security configuration
baselines to ensure that all Windows instances are launched with standard security controls.
Security baselines can be baked into an AMI, bootstrapped dynamically when an EC2 instance is
launched, or packaged as a product for uniform distribution through AWS Service Catalog
portfolios. For more information on securing an AMI, see [Best Practices for Building an AMI](../../../marketplace/latest/userguide/best-practices-for-building-your-amis.md "../../../marketplace/latest/userguide/best-practices-for-building-your-amis.md").

Each Amazon EC2 instance should adhere to organizational security standards. Do not install any
Windows roles and features that are not required, and do install software to protect against
malicious code (antivirus, antimalware, exploit mitigation), monitor host-integrity, and
perform intrusion detection. Configure security software to monitor and maintain OS security
settings, protect the integrity of critical OS files, and alert on deviations from the
security baseline. Consider implementing recommended security configuration benchmarks
published by Microsoft, the Center for Internet Security (CIS), or the National Institute of
Standards and Technology (NIST). Consider using other Microsoft tools for particular
application servers, such as
the [Best Practice Analyzer for SQL Server](https://www.microsoft.com/en-us/download/details.aspx?id=29302 "https://www.microsoft.com/en-us/download/details.aspx?id=29302").

AWS customers can also run Amazon Inspector assessments to improve the security and
compliance of applications deployed on Amazon EC2 instances. Amazon Inspector automatically assesses
applications for vulnerabilities or deviations from best practices and includes a knowledge
base of hundreds of rules mapped to common security compliance standards (for example, PCI DSS) and
vulnerability definitions. Examples of built-in rules include checking if remote root login is
enabled, or if vulnerable software versions are installed. These rules are regularly updated
by AWS security researchers.

When securing Windows instances, we recommend that you implement Active Directory
Domain Services to enable a scalable, secure, and manageable infrastructure for
distributed locations. Additionally, after launching instances from the Amazon EC2 console or
by using an Amazon EC2 provisioning tool, such as AWS CloudFormation, it is good practice to utilize
native OS features, such as Microsoft Windows PowerShell DSC to maintain configuration state in the
event that configuration drift occurs.

## Change management

After initial security baselines are applied to Amazon EC2 instances at launch, control ongoing
Amazon EC2 changes to maintain the security of your virtual machines. Establish a change management
process to authorize and incorporate changes to AWS resources (such as security groups, route
tables, and network ACLs) as well as to OS and application configurations (such as Windows or
application patching, software upgrades, or configuration file updates).

AWS provides several tools to help manage changes to AWS resources, including
AWS CloudTrail, AWS Config, CloudFormation, and AWS Elastic Beanstalk, and management packs for Systems Center
Operations Manager and System Center Virtual Machine Manager. Note that Microsoft releases
Windows patches the second Tuesday of each month (or as needed) and AWS updates all
Windows AMIs managed by AWS within five days after Microsoft releases a patch. Therefore
it is important to continually patch all baseline AMIs, update CloudFormation templates and Auto
Scaling group configurations with the latest AMI IDs, and implement tools to automate
running instance patch management.

Microsoft provides several options for managing Windows OS and application changes. SCCM,
for example, provides full lifecycle coverage of environment modifications. Select tools that
address business requirements and control how changes will affect application SLAs, capacity,
security, and disaster recovery procedures. Avoid manual changes and instead leverage
automated configuration management software or command line tools such as the EC2 Run Command
or Windows PowerShell to implement scripted, repeatable change processes. To assist with this
requirement, use bastion hosts with enhanced logging for all interactions with your Windows
instances to ensure that all events and tasks are automatically recorded.

## Audit and accountability for Amazon EC2 Windows instances

AWS CloudTrail, AWS Config, and AWS Config Rules provide audit and change tracking features for auditing AWS
resource changes. Configure Windows event logs to send local log files to a centralized log
management system to preserve log data for security and operational behavior analysis.
Microsoft System Center Operations Manager (SCOM) aggregates information about Microsoft
applications deployed to Windows instances and applies preconfigured and custom rulesets based
on application roles and services. System Center Management Packs build on SCOM to provide
application-specific monitoring and configuration guidance. These [Management Packs](https://learn.microsoft.com/en-us/archive/technet-wiki/16174.microsoft-management-packs "https://learn.microsoft.com/en-us/archive/technet-wiki/16174.microsoft-management-packs") support Windows Server Active Directory, SharePoint Server 2013,
Exchange Server 2013, Lync Server 2013, SQL Server 2014, and many more servers and
technologies.

In addition to Microsoft systems management tools, customers can use Amazon CloudWatch to monitor
instance CPU utilization, disk performance, network I/O, and perform host and instance status
checks. The EC2Config, EC2Launch, and EC2Launch v2 launch agents provide access to additional,
advanced features for Windows instances. For example, they can export Windows system,
security, application, and Internet Information Services (IIS) logs to CloudWatch Logs which can then be
integrated with Amazon CloudWatch metrics and alarms. Customers can also create scripts that export
Windows performance counters to Amazon CloudWatch custom metrics.
