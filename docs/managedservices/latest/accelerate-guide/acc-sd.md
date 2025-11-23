# Service description

AMS Accelerate is an operation plan of the AWS Managed Services service for managing operations of your AWS infrastructure.

## AWS Managed Services (AMS) AMS Accelerate operation plan features

AMS Accelerate offers the following features:

- **Incident management**:

Incident management is the process the AMS service uses to respond to your reported incidents.

AMS Accelerate proactively detects and responds to incidents and assists your team
in resolving issues. You can reach out to AMS Accelerate operations engineers 24x7
using AWS Support Center, with response time
SLAs depending on the level of response you selected for your account.

- **Monitoring**:

Monitoring is the process the AMS service uses to track your resources.

Accounts enrolled in AMS Accelerate are configured with a baseline deployment of
Amazon CloudWatch events and alarms that have been optimized to reduce noise and to
identify a possible upcoming incident. After receiving the alerts, the AMS
team uses automated remediations, people, and processes, to bring the resources back
to a healthy state and engage with your teams when appropriate to provide insights
into learnings on the behavior and how to prevent it. If remediation fails,
AMS starts the incident management process. You can change the baselines by
updating the default configuration file.

- **Security**:

Security management is the process the AMS service uses to protect your resources.
AWS Managed Services protects your information assets and helps keep your AWS infrastructure
secure by using multiple controls, including AWS Config Rules and Amazon GuardDuty.

AMS Accelerate maintains a library of AWS Config Rules and remediation actions to ensure that all your accounts comply with
industry standards for security and operational integrity. AWS Config Rules continuously tracks the configuration change among your recorded resources. If a change
violates any rule conditions, AMS reports its findings, and allows you to remediate violations
automatically or by request, according to the severity of the violation. AWS Config Rules facilitate compliance with standards set by:
the Center for Internet Security (CIS),
the National Institute of Standards and Technology (NIST) Cloud Security Framework (CSF),
the Health Insurance Portability and Accountability Act (HIPAA),
and the Payment Card Industry (PCI) Data Security Standard (DSS).

In addition, AMS Accelerate leverages Amazon GuardDuty to identify potentially unauthorized
or malicious activity in your AWS environment. GuardDuty findings are monitored 24x7 by
AMS. AMS collaborates with you to understand the impact of the
findings and remediations based on best practice recommendations. AMS also
supports Amazon Macie to protect your sensitive data such as personal health
information (PHI), personally identifiable information (PII), and financial data. Finally, AMS monitors and triages all Amazon Route 53 Resolver **ALERT** and **BLOCK** events generated in managed accounts to further inspect network traffic and augment its detective capabilities.

- **Patch management**:

Patch management is the process the AMS service uses to update your resources.

For an AWS account with the patch add-on, AWS Managed Services applies and installs vendor
updates to Amazon EC2 instances for supported operating systems during your chosen
maintenance windows. AMS creates a snapshot of the instance prior to
patching, monitors the patch installation, and notifies you of the outcome. If the
patch fails, then AMS investigates the failure and recommends a course of action for you to remediate the issue. Or, AMS restores the instance to rollback, if requested. AMS provides reports of patch compliance coverage and
advises you of the recommended course of action for your business.

- **Backup management**:

AMS uses backup management to take snapshots of your resources.

AWS Managed Services creates, monitors, and stores snapshots for AWS services supported by
AWS Backup. You define the backup schedules, frequency, and retention period by creating
AWS Backup plans while onboarding accounts and applications. You associate the plans to
resources. AMS tracks all backup jobs, and, when a backup job fails, alerts
our team to run a remediation. AMS leverages your snapshots to perform
restoration actions during incidents, if needed. AMS provides you with a
backup coverage report and a backup status report.

- **Problem management**:

AMS performs trend analysis to identify and investigate problems and to identify the root
cause. Problems are remediated either with a workaround or a permanent solution that prevents recurrence of
similar future service impact. A post incident report (PIR) may be requested for any "High" incident,
upon resolution. The PIR captures the root cause and preventative actions taken, including implementation
of preventative measures.

- **Designated experts**:

AMS Accelerate also designates a Cloud Service Delivery Manager (CSDM) and a Cloud
Architect (CA) to partner with your organization and drive operational and security
excellence. Your CSDM and CA provide you guidance during and after configuration and
onboarding AMS Accelerate, deliver a monthly report of your operational metrics, and
work with you to identify potential cost savings using tools such as AWS Cost
Explorer, Cost and Usage Reports, and Trusted Advisor.

- **Operations tools**:

AMS Accelerate can provide ongoing operations for your workload's infrastructure in
AWS. Our patch, backup, monitoring, and incident management services depend on
having resources tagged, and the AWS Systems Manager (SSM) and CloudWatch agents
installed and configured on your Amazon EC2 instances with an IAM instance profile that
authorizes them to interact with the SSM and Amazon CloudWatch services. AMS Accelerate
provides tools like Resource Tagger to help you tag your resources based on rules,
and automated instance configuration to install the required agents in your Amazon EC2
instances. If you're following immutable infrastructure practices, you can complete
the prerequisites directly in the console or infrastructure-as-code templates.

- **Cost optimization**:

AMS Resource Scheduler automates the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Relational Database Service (Amazon RDS) instances and
Amazon EC2 Amazon EC2 Auto Scaling groups. AMS Resource Scheduler helps you reduce operational costs by stopping the resources that are not in use and
starting them back when their capacity is needed.

- **Logging and Reporting**:

AWS Managed Services aggregates and stores logs generated as a result of operations in CloudWatch, CloudTrail, and
Amazon VPC Flow Logs. Logging from AMS helps in faster incident resolution and system audits.
AMS Accelerate also provides you with a monthly service report that summarizes key
performance metrics of AMS, including an executive summary and insights,
operational metrics, managed resources, AMS service level agreement (SLA)
adherence, and financial metrics around spending, savings, and cost optimization.
Reports are delivered by the AMS cloud service delivery manager (CSDM) designated to you.

- **Service request management**:

To request information about your managed environment, AMS, or AWS service offerings, submit service requests using the AMS Accelerate console.
You can submit a service request for "How to" questions about AWS services and features or to request additional AMS services.

All AMS Accelerate customers start with incident management, monitoring, security
monitoring, log recording, prerequisite tools, backup management, and reporting
capabilities. You can add the AMS Patch management add-on at an additional price.

###### Note

For a list of features not supported in AWS GovCloud (US), see [How AMS Accelerate differs for AWS GovCloud (US)](../../../govcloud-us/latest/UserGuide/govcloud-ams-acc.md "../../../govcloud-us/latest/UserGuide/govcloud-ams-acc.md")

## Supported configurations

AMS Accelerate supports the following configurations:

- Language: English.
- Regions: See the AWS Regions supported by AWS Managed Services in the
  [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") webpage.

###### Note

AWS Regions introduced before March 20, 2019 are considered "Original" Regions and are enabled by default.
Regions introduced after this date are "Opt-in" Regions and are disabled by default. If your account uses multiple Regions and you onboard
AMS Accelerate to an account with an enabled "Opt-in" Region as the default Region, the AMS Reporting feature is only available in that Region. If you do
not set a default Region, the last Region you visited is your default Region.

To enable a Region, see
[Enabling a Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable").
To set a default Region, see
[Choosing a Region](../../../awsconsolehelpdocs/latest/gsg/select-region.md "../../../awsconsolehelpdocs/latest/gsg/select-region.md").
For a list of the Opt-in status for each Region, see
[Available Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions")
in the _Amazon Elastic Compute Cloud User Guide_.

- Operating system architecture (x86-64 or ARM64): any supported by both
  [Systems Manager](../../../systems-manager/latest/userguide/prereqs-operating-systems.md "../../../systems-manager/latest/userguide/prereqs-operating-systems.md") and
  [CloudWatch](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md").
- Supported operating systems:
  - AlmaLinux 8.3-8.9, 9.x (AlmaLinux is only supported with x86 architecture)
  - Amazon Linux 2023
  - Amazon Linux 2 (**expected AMS support end date June 30, 2026**)
  - Oracle Linux 9.x, 8.x
  - Red Hat Enterprise Linux (RHEL) 9.x, 8.x
  - SUSE Linux Enterprise Server 15 SP6
  - SUSE Linux Enterprise Server for SAP 15 SP3 and later
  - Microsoft Windows Server 2022, 2019, 2016
  - Ubuntu 20.04, 22.04, 24.04

- Supported End of Support (EOS) operating systems:

###### Note

End of Support (EOS) operating systems are outside of the general support period of the operating system manufacturer and have increased security risk.
EOS operating systems are considered supported configurations only if AMS-required agents support the operating system and...

    1. you have extended support with the operating system vendor that allows you to receive updates, or
    2. any instances using an EOS OS follow the [security controls](key-terms.md#CritRec "key-terms.md#CritRec") as specified by AMS in the Accelerate User Guide, or
    3. you comply with any other compensating security controls required by AMS.In the event AMS is no longer able to support an EOS OS, AMS issues a

[Critical Recommendation](key-terms.md#CritRec "key-terms.md#CritRec") to upgrade the operating system.

AMS-required agents may include but are not limited to: AWS Systems Manager, Amazon CloudWatch, Endpoint Security (EPS) agent, and Active Directory
(AD) Bridge (Linux only).

    + Ubuntu Linux 18.04
    + SUSE Linux Enterprise Server 15 SP3, SP4, and SP5
    + SUSE Linux Enterprise Server for SAP 15 SP2
    + SUSE Linux Enterprise Server 12 SP5
    + SUSE Linux Enterprise Service for SAP 12 SP5
    + Microsoft Windows Server 2012/2012 R2
    + Red Hat Enterprise Linux (RHEL):7.x
    + Oracle Linux 7.5-7.9

- If you use AWS Control Tower to manage your multi-account environment, then make sure that you're running the latest version of AWS Control Tower for compatibility with Accelerate. Environments that use AWS Control Tower versions earlier than 2.7 (released in April 2021), aren't supported. For information on how to update AWS Control Tower, see [Update Your Landing Zone](../../../controltower/latest/userguide/update-controltower.md "../../../controltower/latest/userguide/update-controltower.md").

## Supported services

AWS Managed Services provides operational management support services for the following AWS services. Each AWS service is distinct and as a result, AMS's level of
operational management support varies depending on the nature and characteristics of the underlying AWS service. If you request that AWS Managed Services provide services
for any software or service that is not expressly identified as supported in the following list, any
AWS Managed Services provided for such customer-requested configurations will be treated as a "Beta Service" under the Service Terms.

- Incidents: All AWS services
- Service request: All AWS services
- Patching: Amazon EC2
- Backups and Restoration: All AWS services supported by AWS Backup. For a list of services
  supported by AWS Backup, see [AWS Backup supported resources](../../../aws-backup/latest/devguide/whatisbackup.md#supported-resources "../../../aws-backup/latest/devguide/whatisbackup.md#supported-resources").
- Resource Scheduler: Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Relational Database Service (Amazon RDS) and Amazon EC2 Auto Scaling groups
- Services monitored for operational events: [Supported checks](tr-supported-checks.md "tr-supported-checks.md") and Trusted Advisor, Application Load Balancer, Aurora, Amazon EC2, ELB, Amazon FSx for NetApp ONTAP, Amazon FSx
  for Windows File Server, NAT gateway (a Network Address Translation (NAT)
  service), OpenSearch, AWS Health Dashboard, Amazon Redshift, Amazon Relational Database Service (Amazon RDS),
  Site-to-Site VPN. To learn more about what AMS Accelerate is monitoring as part
  of a service, see [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md "monitoring-default-metrics.md") .
- Services monitored by security Config Rules: AWS Account, GuardDuty, Macie, Amazon API Gateway, AWS Certificate Manager, AWS Config,
  CloudTrail, CloudWatch, AWS CodeBuild, AWS Database Migration Service, Amazon DynamoDB, Amazon EC2, Amazon ElastiCache, Amazon Elastic Block Store (Amazon EBS),
  Amazon Elastic File System (Amazon EFS), Amazon Elastic Kubernetes Service (Amazon EKS), ELB, Amazon OpenSearch Service, Amazon EMR, AWS Identity and Access Management (IAM), AWS Key Management Service, AWS Lambda, Amazon Redshift, Amazon Relational Database Service,
  Amazon S3, Amazon SageMaker AI, AWS Secrets Manager , Amazon Simple Notification Service, AWS Systems Manager, Amazon VPC
  (Security group, volume, Elastic IP address, VPN connection, Internet gateways), Amazon VPC Flow Logs.
  For more details, see
  [Configuration compliance in Accelerate](acc-sec-compliance.md "acc-sec-compliance.md") and
  [Data protection in Accelerate](acc-sec-data-protect.md "acc-sec-data-protect.md"). You can find additional AMS security information
  in our private Security Guide that can be accessed through AWS Artifact, on the **Reports** tab, for AWS Managed Services.

###### Note

AMS Accelerate for the Asia Pacific (Malaysia) Region doesn't support monitoring with
Amazon Macie, monitoring and incident management for Amazon EKS, or monitoring of Amazon EFS
FileSystem, Amazon EC2 NatGateway, and Amazon EKS Cluster resources. It also doesn't support
SSM Agent automatic installation.

###### Note

AMS Accelerate for the Middle East (UAE) Region supports a set of in-scope features as described in
the following table. Access to the AMS account console and instances in this
Region is driven exclusively by inbound service request triggers. For more
information about the availability of Accelerate in the Middle East (UAE) Region,
consult your account manager or AWS Cloud Service Delivery Manager (CSDM).

| AMS Accelerate in-scope features for Middle East (UAE) Region | Feature description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Incident Management                                           | AMS provides incident response and assistance to help your team resolve issues. For AMS to<br>assist you with incident management, you need to submit a service<br>request. AMS doesn't proactively detect or respond to incidents in<br>this Region.                                                                                                                                                                                   |
| Monitoring                                                    | After recieving a service request from you, AMS can assist with resource remediation. AMS<br>uses automated remediation, people, and process to bring your<br>resources back to a healthy state. AMS doesn't configure baseline<br>CloudWatch events and alarms in this Region. If you have existing<br>monitoring tools, proactive tracking of your resources might be<br>available based on Cloud Architect (CA) and CSDM assessment. |
| Security                                                      | After recieving a service request from you, AMS can assist with security issue remediation.<br>AMS doesn't deploy security controls such as AWS Config Rules and GuardDuty<br>or monitor security findings in this Region. If you have existing<br>security tools, proactive security monitoring might be available<br>based on CA and CSDM assessment.                                                                                 |
| Patch Management                                              | AMS can apply vendor updates to Amazon EC2 instances for supported operating systems during<br>chosen maintenance windows, and create pre-patching snapshots. For<br>AMS to assist you with patch management, you need to submit a<br>service request. AMS patch notifications and reports aren't<br>available in this Region.                                                                                                          |
| Backup Management                                             | AMS can create and store snapshots for AWS services supported by AWS Backup, and assist with<br>backup remediation. For AMS to assist you with backup management,<br>you need to submit a service request. AMS doesn't track backup<br>jobs in this Region.                                                                                                                                                                             |
| Designated Experts                                            | AMS designates a Cloud Architect (CA) and a Cloud Service Delivery Manager (CSDM) to partner with customer organizations<br>and drive operational and security excellence.                                                                                                                                                                                                                                                              |
| Service Request Management                                    | To request information about your managed environment, AMS, or AWS service offerings,<br>submit service requests through the AMS Accelerate console. You can<br>submit a service request for "How to" questions about AWS services<br>and features, or to request AMS services that are available in<br>this Region, as described in this table.                                                                                        |

## Roles and responsibilities

The AMS Accelerate responsible, accountable, consulted, and informed, or RACI, matrix assigns primary responsibility either to the customer
or AMS for a variety of activities. The table describes your (the "Customer") responsibilities versus our ("AMS Accelerate") responsibilities.

The [Scope of changes performed by AMS Accelerate](#acc-scope-changes "#acc-scope-changes") section lists the specific circumstances
when AMS is authorized to make changes to your account; and some types of changes that AMS never makes.

### AMS Accelerate RACI Matrix

AMS Accelerate manages your AWS infrastructure. The following table provides an overview of the roles
and responsibilities for you and AMS Accelerate for activities in the lifecycle of an application
running within the managed environment.

- **R** stands for Responsible party that does the work to achieve
  the task.
- **C** stands for Consulted; a party whose opinions are sought,
  typically as subject matter experts; and with whom there is bilateral communication.
- **I** stands for Informed; a party who is informed on progress,
  often only on completion of the task.

###### Note

Some sections contain 'R' for both AMS and Customers. This is because, in the AWS Shared Responsibility model, both AMS and the customers take joint ownership to respond to infrastructure and application issues.

| **Activity**                                                                                                                                                                                                                                              | **Customer** | **AWS Managed Services (AMS)** |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------ |
| **AMS patterns**                                                                                                                                                                                                                                          |
| Create new patterns                                                                                                                                                                                                                                       | I            | R                              |
| Deploy and customize patterns                                                                                                                                                                                                                             | R            | C, I                           |
| Test and remove patterns                                                                                                                                                                                                                                  | R            | I                              |
| **Application lifecycle**                                                                                                                                                                                                                                 |
| Application development                                                                                                                                                                                                                                   | R            | I                              |
| Application infrastructure requirements, analysis, and design                                                                                                                                                                                             | R            | I                              |
| Application deployment                                                                                                                                                                                                                                    | R            | I                              |
| AWS resource deployment                                                                                                                                                                                                                                   | R            | I                              |
| Application monitoring                                                                                                                                                                                                                                    | R            | I                              |
| Application testing/optimization                                                                                                                                                                                                                          | R            | I                              |
| Troubleshoot and resolve application issues                                                                                                                                                                                                               | R            | I                              |
| Troubleshoot and resolve problems                                                                                                                                                                                                                         | R            | I                              |
| Monitoring supported for AWS infrastructure                                                                                                                                                                                                               | C            | R                              |
| Incident response for AWS network issues                                                                                                                                                                                                                  | C            | R                              |
| Incident response for AWS resource issues                                                                                                                                                                                                                 | C            | R                              |
| **Managed Account onboarding**                                                                                                                                                                                                                            |
| Grant access to the AWS Managed Account for the AMS team and tools                                                                                                                                                                                        | R            | C                              |
| Implement changes in the account or environment to allow the deployment of tools in the account.<br>For example, changes in Service Control Policies (SCPs)                                                                                               | R            | C                              |
| Install SSM agents in EC2 instances                                                                                                                                                                                                                       | R            | C                              |
| Install and configure tooling required to provide AMS services. For example, CloudWatch agents,<br>scripts for patching, alarms, logs, and others                                                                                                         | I            | R                              |
| Manage access and identity lifecycle for AMS engineers                                                                                                                                                                                                    | I            | R                              |
| Collect all required inputs to configure AMS services. For example, patch maintenance<br>windows duration, schedule and targets                                                                                                                           | R            | I                              |
| Request the configuration of AMS services and provide all required inputs                                                                                                                                                                                 | R            | I                              |
| Configure AMS services as requested by the customer. For example, patch maintenance windows, resource tagger, and alarm manager                                                                                                                           | C            | R                              |
| Manage the lifecycle of users and their permissions, for local directory services, used to<br>access AWS accounts and instances                                                                                                                           | R            | I                              |
| Recommend reserved instances optimization                                                                                                                                                                                                                 | I            | R                              |
| Onboard account(s) to Trusted Remediator                                                                                                                                                                                                                  | C,I          | R                              |
| **Patch management**                                                                                                                                                                                                                                      |
| Collect all required inputs to configure patch maintenance windows, patch baselines, and target                                                                                                                                                           | R            | I                              |
| Request the configuration of patch maintenance windows and baselines, and provide all required inputs                                                                                                                                                     | R            | I                              |
| Configure patch maintenance windows, patch baselines, and targets as requested by the customer                                                                                                                                                            | C            | R                              |
| Monitor for applicable updates to supported OS and software preinstalled with<br>supported OS for EC2 instances                                                                                                                                           | I            | R                              |
| Report for missing updates to supported OS and maintenance window<br>coverage                                                                                                                                                                             | I            | R                              |
| Take snapshots of instances before applying updates                                                                                                                                                                                                       | I            | R                              |
| Apply updates to EC2 instances per customer configuration                                                                                                                                                                                                 | I            | R                              |
| Investigate failed updates to EC2 instances                                                                                                                                                                                                               | C            | R                              |
| Update AMIs and stacks for Auto-Scaling groups (ASGs)                                                                                                                                                                                                     | R            | C                              |
| Patch the Windows operating system, and Microsoft packages installed on the operating system which are governed by Windows Update                                                                                                                         | I            | R                              |
| Patch installed applications, software, or application dependencies not managed by Windows Update                                                                                                                                                         | R            | I                              |
| Patch the Linux operating system and any package that is enabled for management by the operating system's native package manager (for example Yum, Apt, Zypper)                                                                                           | I            | R                              |
| Patch installed applications, software, or application dependencies not managed by the Linux operating system's native package manager                                                                                                                    | R            | I                              |
| **Backup**                                                                                                                                                                                                                                                |
| Collect all required inputs to configure backup plans and target resources                                                                                                                                                                                | R            | I                              |
| Request the configuration of Backup plans and provide all required inputs                                                                                                                                                                                 | R            | I                              |
| Configure backup plans and targets as requested by the customer                                                                                                                                                                                           | C            | R                              |
| Specify backup schedules and target resources                                                                                                                                                                                                             | R            | I                              |
| Perform backups per plan                                                                                                                                                                                                                                  | I            | R                              |
| Investigate failed backup jobs                                                                                                                                                                                                                            | I            | R                              |
| Report for backup jobs status and backup coverage                                                                                                                                                                                                         | I            | R                              |
| Validate backups                                                                                                                                                                                                                                          | R            | I                              |
| Request backup restoration for resources of supported AWS services resources as part of incident management                                                                                                                                               | R            | I                              |
| Perform backup restoration activities for resources of supported AWS services                                                                                                                                                                             | I            | R                              |
| Restore affected custom or third-party applications                                                                                                                                                                                                       | R            | I                              |
| **Networking**                                                                                                                                                                                                                                            |
| Provisioning and configuration of Managed Account VPCs, IGWs, Direct connect, and other AWS networking Services                                                                                                                                           | R            | I                              |
| Configure and operate AWS Security Groups/NAT/NACL inside the Managed account                                                                                                                                                                             | R            | I                              |
| Networking configuration and implementation within customer network (for example DirectConnect)                                                                                                                                                           | R            | I                              |
| Networking configuration and implementation within AWS network                                                                                                                                                                                            | R            | I                              |
| Monitor defined by AMS for network security, including security groups                                                                                                                                                                                    | I            | R                              |
| Network-level logging configuration and management (VPC flow logs and others)                                                                                                                                                                             | I            | R                              |
| **Logging**                                                                                                                                                                                                                                               |
| Record all application change logs                                                                                                                                                                                                                        | R            | I                              |
| Record AWS infrastructure change logs                                                                                                                                                                                                                     | I            | R                              |
| Enable and aggregate AWS audit trail                                                                                                                                                                                                                      | I            | R                              |
| Aggregate logs from AWS resources                                                                                                                                                                                                                         | I            | R                              |
| **Monitoring and Remediation**                                                                                                                                                                                                                            |
| Collect all required inputs to configure alarm manager, resource tagger, and alarm thresholds                                                                                                                                                             | R            | I                              |
| Request the configuration of alarm manager and provide all required inputs                                                                                                                                                                                | R            | I                              |
| Configure alarm manager, resource tagger, and alarm thresholds as requested by the customer.                                                                                                                                                              | C            | R                              |
| Deploy AMS CloudWatch baseline metrics and alarms per customer configuration                                                                                                                                                                              | I            | R                              |
| Monitor supported AWS resources using baseline CloudWatch metrics and<br>alarms                                                                                                                                                                           | I            | R                              |
| Investigate alerts from AWS resources                                                                                                                                                                                                                     | C            | R                              |
| Remediate alerts based on defined configuration, or create an incident                                                                                                                                                                                    | I            | R                              |
| Define, monitor, and investigate customer-specific monitors                                                                                                                                                                                               | R            | I                              |
| Investigate alerts from application monitoring                                                                                                                                                                                                            | R            | C                              |
| Configure Trusted Advisor checks for remediation                                                                                                                                                                                                          | R            | C                              |
| Automatically remediate supported Trusted Advisor checks                                                                                                                                                                                                  | I            | R                              |
| Manually remediate supported Trusted Advisor checks                                                                                                                                                                                                       | R            | C                              |
| Report remediation status                                                                                                                                                                                                                                 | I            | R                              |
| Troubleshoot remediation failures                                                                                                                                                                                                                         | R            | C                              |
| **Security Architecture**                                                                                                                                                                                                                                 |
| Review AMS resources and code for security issues and potential threats                                                                                                                                                                                   | I            | R                              |
| Implement security controls in AMS resources and code to mitigate<br>security risks                                                                                                                                                                       | I            | R                              |
| Enable supported AWS services for security management of the account and<br>its AWS resources                                                                                                                                                             | I            | R                              |
| Manage privileged credentials for account and OS access for AMS<br>engineers                                                                                                                                                                              | I            | R                              |
| **Security Risk Management**                                                                                                                                                                                                                              |
| Monitor supported AWS services for security management, like GuardDuty and Macie                                                                                                                                                                          | I            | R                              |
| Define and create AMS-defined Config Rules to detect if AWS resources<br>comply with Center for Internet Security (CIS) and NIST security best practices.                                                                                                 | I            | R                              |
| Monitor AMS-defined Config Rules                                                                                                                                                                                                                          | I            | R                              |
| Report conformance status of Config Rules                                                                                                                                                                                                                 | I            | R                              |
| Define a list of required Config Rules and remediate them                                                                                                                                                                                                 | I            | R                              |
| Evaluate the impact of remediating AMS-defined Config Rules                                                                                                                                                                                               | R            | I                              |
| Request remediation of AMS-defined Config Rules in the AWS account                                                                                                                                                                                        | R            | I                              |
| Track resources exempted from AMS-defined Config Rules                                                                                                                                                                                                    | R            | I                              |
| Remediate supported AMS-defined Config Rules in the AWS account                                                                                                                                                                                           | C            | R                              |
| Remediate non-supported AMS-defined Config Rules in the AWS account                                                                                                                                                                                       | R            | I                              |
| Define, monitor, and investigate customer-specific Config Rules                                                                                                                                                                                           | R            | I                              |
| **Incident Management**                                                                                                                                                                                                                                   |
| Notify about incidents detected by AMS in AWS resources                                                                                                                                                                                                   | I            | R                              |
| Notify about incidents in AWS resources                                                                                                                                                                                                                   | R            | I                              |
| Notify about incidents for AWS resources based on monitoring                                                                                                                                                                                              | I            | R                              |
| Handle application performance issues and outages                                                                                                                                                                                                         | R            | I                              |
| Categorize incident priority                                                                                                                                                                                                                              | I            | R                              |
| Provide incident response                                                                                                                                                                                                                                 | I            | R                              |
| Provide incident resolution or infrastructure restore for resources with<br>available backups                                                                                                                                                             | C            | R                              |
| **Security Incident Response – Prepare**                                                                                                                                                                                                                  |
| **Communications**                                                                                                                                                                                                                                        |
| Provide and update customer security contact details for AMS to use during security events notifications and security escalations                                                                                                                         | R            | I                              |
| Store and manage the supplied customer security contact details to use during security events and security escalations                                                                                                                                    | C            | R                              |
| **Training**                                                                                                                                                                                                                                              |
| Provide customer with documentation to support AMS during incident response process                                                                                                                                                                       | I            | R                              |
| Practice shared responsibility during incident response processes through security gamedays                                                                                                                                                               | R            | R                              |
| **Resource management**                                                                                                                                                                                                                                   |
| Configure supported security management AWS services for alerting, alerts correlation, noise reduction and additional rules                                                                                                                               | I            | R                              |
| Maintain a comprehensive inventory of AWS resources (Amazon EC2, Amazon S3 etc.), including details on the value and criticality of each asset to the business.<br>This information will be instrumental in determining an effective containment strategy | R            | C                              |
| Employ AWS tags to identify resources and workloads                                                                                                                                                                                                       | R            | C                              |
| Define and configure log retention and archival                                                                                                                                                                                                           | I            | R                              |
| Establish a secure baseline by defining and enforcing the organization's security policies and configurations for AWS accounts, services, and access management                                                                                           | R            | I                              |
| **Security Incident Response<br>• Detect**                                                                                                                                                                                                                |
| **Logging, indicators and monitoring**                                                                                                                                                                                                                    |
| Configure logging and monitoring to enable event management for instance and accounts                                                                                                                                                                     | I            | R                              |
| Monitor supported AWS services for security alerts                                                                                                                                                                                                        | I            | R                              |
| Deploy and manage endpoint security tools                                                                                                                                                                                                                 | R            | I                              |
| Monitor for malware on instances using endpoint security                                                                                                                                                                                                  | R            | I                              |
| Notify customer of detected events through outbound messaging                                                                                                                                                                                             | I            | R                              |
| Coordinate internal stakeholder communications and leadership updates to improve response time                                                                                                                                                            | R            | I                              |
| Define, deploy, and maintain AMS standard detection services (for example, Amazon GuardDuty and AWS Config)                                                                                                                                               | C            | R                              |
| Record AWS infrastructure change logs                                                                                                                                                                                                                     | R            | I                              |
| Enable and configure logging, monitoring to enable event management for the application                                                                                                                                                                   | R            | C                              |
| Implement and maintain an allow-list, deny-list, and custom detections on supported AWS security services (for example, Amazon GuardDuty)                                                                                                                 | R            | R                              |
| **Security event reporting**                                                                                                                                                                                                                              |
| Notify AMS of a suspicious activity or an active security investigation                                                                                                                                                                                   | R            | I                              |
| Notify detected security events and incidents to the customer                                                                                                                                                                                             | I            | R                              |
| Notify planned event that might trigger Security Incident Response process                                                                                                                                                                                | R            | I                              |
| **Security Incident Response<br>• Analyze**                                                                                                                                                                                                               |
| **Investigation and analysis**                                                                                                                                                                                                                            |
| Perform initial response for supported security alert generated by a supported detection source                                                                                                                                                           | I            | R                              |
| Assess false/true positives using the available data                                                                                                                                                                                                      | R            | R                              |
| Generate a snapshot of affected instances to be shared with the customer if needed                                                                                                                                                                        | I            | R                              |
| Perform forensics tasks such as chain of custody, file system analysis, memory forensics, and binary analysis                                                                                                                                             | R            | C                              |
| Collect application logs to aid investigation                                                                                                                                                                                                             | R            | I                              |
| Collect data and logs to aid investigation on security alerts                                                                                                                                                                                             | R            | R                              |
| Engage SMEs within AWS services on security investigations                                                                                                                                                                                                | C            | R                              |
| Share investigation logs from supported AWS services to customers during an investigation                                                                                                                                                                 | I            | R                              |
| **Communication**                                                                                                                                                                                                                                         |
| Send alert and notifications from AMS detection sources for managed resources                                                                                                                                                                             | I            | R                              |
| Manage alert and notifications for application security events                                                                                                                                                                                            | R            | I                              |
| Engage customer security point of contact during a security incident investigation                                                                                                                                                                        | R            | I                              |
| **Security Incident Response<br>• Contain**                                                                                                                                                                                                               |
| **Containment strategy and execution**                                                                                                                                                                                                                    |
| Assess risks and decide the containment strategy, acknowledging potential service impacts                                                                                                                                                                 | R            | C                              |
| Make a backup of affected systems for further analysis                                                                                                                                                                                                    | I            | R                              |
| Contain applications and workloads (through application specific configuration or response activity)                                                                                                                                                      | R            | C                              |
| Define the containment strategy based on the security incident and the affected resource                                                                                                                                                                  | I            | R                              |
| Enable encryption and secure storage of point in time backups of affected systems                                                                                                                                                                         | C            | R                              |
| Execute supported containment actions for AWS resources including EC2 instances, network, and IAM                                                                                                                                                         | I            | R                              |
| **Security Incident Response<br>• Eradicate**                                                                                                                                                                                                             |
| **Eradication strategy and execution**                                                                                                                                                                                                                    |
| Define eradication options based on the security incident and the affected resource on customer application workloads                                                                                                                                     | C            | R                              |
| Decide on the agreed eradication strategy, timing of eradication execution and the consequences                                                                                                                                                           | R            | I                              |
| Define eradication steps based on the security incident and the affected resource on AMS managed workloads                                                                                                                                                | C            | R                              |
| Eradicate threats and harden AWS resources including EC2 instances, network, and IAM<br>eradication                                                                                                                                                       | R            | C                              |
| Eradicate threats and harden applications and workloads (through application specific<br>configuration or response activity)                                                                                                                              | R            | I                              |
| **Security Incident Response<br>• Recover**                                                                                                                                                                                                               |
| **Recovery preparation and execution**                                                                                                                                                                                                                    |
| Configure backup plans and targets as requested by the customer                                                                                                                                                                                           | I            | R                              |
| Review backup plans to restore AMS managed workloads                                                                                                                                                                                                      | R            | I                              |
| Perform backup restoration activities for resources of supported AWS services                                                                                                                                                                             | I            | R                              |
| Backup customer application, APP configuration, and deployment settings, and review backup plans to restore customer applications and workloads post-incident                                                                                             | R            | I                              |
| Restore applications and customer workloads (through application specific restoration steps)                                                                                                                                                              | R            | I                              |
| **Security Incident Response – Post Incident Report**                                                                                                                                                                                                     |
| **Post incident reporting**                                                                                                                                                                                                                               |
| Share appropriate lessons learned and action items with customer post incident as required                                                                                                                                                                | I            | R                              |
| **Problem Management**                                                                                                                                                                                                                                    |
| Correlate incidents to identify problems                                                                                                                                                                                                                  | I            | R                              |
| Perform root cause analysis (RCA) for problems                                                                                                                                                                                                            | I            | R                              |
| Remediate problems                                                                                                                                                                                                                                        | I            | R                              |
| Identify and remediate application problems                                                                                                                                                                                                               | R            | I                              |
| **Service Management**                                                                                                                                                                                                                                    |
| Request information using service requests                                                                                                                                                                                                                | R            | I                              |
| Reply to service requests                                                                                                                                                                                                                                 | I            | R                              |
| Provide cost-optimization recommendations                                                                                                                                                                                                                 | I            | R                              |
| Prepare and deliver monthly service report                                                                                                                                                                                                                | I            | R                              |
| **Change Management**                                                                                                                                                                                                                                     |
| Change management processes and tooling for provisioning and updating<br>resources in the managed environment                                                                                                                                             | R            | I                              |
| Maintenance of application change calendar                                                                                                                                                                                                                | R            | I                              |
| Notice of upcoming maintenance Window                                                                                                                                                                                                                     | R            | I                              |
| Record changes made by AMS Operations                                                                                                                                                                                                                     | I            | R                              |
| **Cost Optimization**                                                                                                                                                                                                                                     |
| Collect all required inputs to configure Resource Scheduler                                                                                                                                                                                               | R            | I                              |
| Request the onboarding, configuration of Resource Scheduler and provide all required<br>inputs                                                                                                                                                            | R            | I                              |
| Deploy Resource Scheduler per customer configuration                                                                                                                                                                                                      | C, I         | R                              |
| Disable and enable the Resource Scheduler on customer account                                                                                                                                                                                             | R            | C                              |
| Create, delete, describe, and update schedules                                                                                                                                                                                                            | C            | R                              |
| Create, delete, describe, and update periods                                                                                                                                                                                                              | C            | R                              |
| Investigate and troubleshoot issues with Resource Scheduler                                                                                                                                                                                               | I            | R                              |
| Request for offboarding the Resource Scheduler                                                                                                                                                                                                            | R            | I                              |
| Offboard the Resource Scheduler from account                                                                                                                                                                                                              | C, I         | R                              |

## Scope of changes performed by AMS Accelerate

AMS Accelerate only makes changes for the specific purposes and situations
described next. AMS makes changes only at the infrastructure level, using the
console or APIs. AMS never changes your application, control, or domain layers.
You can see any changes made by AMS (or other users) using our set of pre-built
queries; to do this, see [Tracking changes in your AMS Accelerate accounts](acc-change-record.md "acc-change-record.md").

**AWS resources**

AMS Accelerate deploys or updates AWS resources only in the following situations:

- To deploy and update tools and resources required by AMS.
- As part of AMS monitoring, in response to events and alarms.
- To remediate security issues as part of [Responses to violations in Accelerate](acc-sec-compliance.md#acc-sec-compliance-responses "acc-sec-compliance.md#acc-sec-compliance-responses")
  (making noncompliant resources conform to security best practices).
- During remediation and restoration as part of an incident response.
- When responding to customer requests to configure AMS features, such as the following:
  - Alarm manager
  - Resource tagger
  - Patch baselines and maintenance windows
  - Resource scheduler
  - Backup plans

AMS Accelerate does not deploy or update resources outside of these situations. If
you need help from AMS to make changes in other situations, consider using
[Operations on Demand](https://aws.amazon.com/managed-services/features/operations-on-demand/ "https://aws.amazon.com/managed-services/features/operations-on-demand/").

**Operating system software**

AMS Accelerate can make changes to your operating system software during
unavailability situations via incident resolution as defined in our
[Service Level Agreement](samples/acc_sla.md "samples/acc_sla.md"). AMS can also make changes to your operating systems as
part of [Automated instance configuration in AMS Accelerate](acc-inst-auto-config.md "acc-inst-auto-config.md").

**Application code and configuration**

AMS Accelerate never modifies your code (for example, AWS CloudFormation
templates, other infrastructure-as-code templates, or Lambda functions), but can
guide your teams on which changes are required to follow best operational and
security practices. AMS Accelerate provides troubleshooting assistance for
infrastructure issues that impact applications, but AMS Accelerate doesn't access or
validate your application configurations.
