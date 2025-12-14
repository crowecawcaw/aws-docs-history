# AWS Managed Services (AMS) AMS Advanced operation plan features

AMS Advanced offers the following features for supported AWS services:

- **Logging, Monitoring, Guardrails, and Event Management**:

AMS configures and monitors your managed environment for logging activity and defines
alerts based on a variety of health checks. Alerts are investigated by AMS for applicable
AWS services, and those that negatively impact your usage of those services result in the creation
of incidents. AMS aggregates and stores all logs generated as a result of all operations
in CloudWatch, CloudTrail, and system logs in Amazon S3. You can ask for additional alerts
to be put in place. In addition to AMS’ preventative controls, AMS
deploys configuration guardrails and detective controls to provide ongoing protection for you from
misconfigurations that could reduce the operational and security integrity of the managed accounts,
to enforce your controls such as tagging and compliance. When a monitored control is detected an alarm
is generated that results in notification, modification, or termination of resources based on predefined
AMS defaults that can be modified by you.

- **Continuity management** (Backup and Restore):

AMS provides backups of resources using standard, existing AWS Backup functionality on a
scheduled interval determined by you. Restore actions from specific snapshots can be performed by
AMS with your RFC. Data changes that occur between snapshot intervals are the
responsibility of you to backup. You can submit an RFC for backup or snapshot requests outside
of scheduled intervals. In the case of Availability Zone (AZ) unavailability in an AWS Region, with
your permission, AMS restores the managed environment by recreating new stack(s)
based on templates and available EBS snapshots of the impacted Stacks.

- **Security and access management**:

AMS provides endpoint security (EPS) such as configuring anti-virus and anti-malware
protection. You can also use your own EPS tool and processes and not use AMS for EPS using a feature called
bring your own EPS (BYOEPS). AMS also configures default
AWS security capabilities that are approved by you during onboarding, such as AWS Identity and Access Management (IAM) roles and Amazon EC2 security groups, and uses standard AWS tools (e.g. AWS Security Hub CSPM,
Amazon Macie, Amazon GuardDuty) to monitor and respond to security issues. You manage your users through an
approved directory service provided by you. For a list of approved directory services,
see [Supported configurations](supported-configs.md "supported-configs.md").

AMS includes endpoint security (EPS), which is inclusive of antivirus (AV), and anti-malware protection,
malware and intrusion detection (Trend Micro). Security groups are defined per stack
template and are modified at launch depending on the visibility of the application
(public/private) security groups.

Access to systems is requested through change management requests for change (RFCs). Access management
provides access to distinct resources, such as Amazon EC2 instances, the AWS Management Console, and
APIs. After establishing a one-way trust with an AMS Microsoft Active Directory
deployment during onboarding and federating to AWS, you can use your existing
corporate credentials for all interactions.

- **Patch management**:

AMS applies and installs updates to EC2 instances for supported operating systems (OSs) and
software pre-installed with supported operating systems. For a list of supported operating systems,
see [Supported configurations](supported-configs.md "supported-configs.md").

AMS offers two models for patching:

    + AMS standard patch for traditional account-based patching, and
    + AMS Patch Orchestrator, for tag-based patching.

In AMS standard patch, a monthly maintenance window is chosen by you
for AMS to perform most patching activities. AMS applies _critical security updates_ outside of the
selected maintenance window (with appropriate notifications) and _important updates_ during the selected
maintenance window. AMS additionally applies updates to infrastructure management
tools during the selected maintenance window. You can exclude stacks from patch management or reject
updates, if you want.

With AMS Patch Orchestrator, a default maintenance window per account, is defined by you
for AMS to perform patching activities. You can schedule additional custom
maintenance windows for AMS to patch a specific set of instances defined by you
with tags. AMS applies all available updates, but you can filter or reject
updates by creating a custom patch baseline. For both models, if you approve or reject an
update provided under patch management but later change your mind, you are responsible for
initiating the update via an RFC. AMS tracks the patch status of resources and highlights
systems that aren’t current in the monthly business review. Patch management is limited to stacks in the
managed environment, including all AMS managed applications and supported AWS services
with patching capabilities (for example, RDS). In order to support all types of infrastructure configurations
when an update is released, AMS a) updates the EC2 instance and b) provides an updated
AMS AMI for you to use. It is your responsibility to install, configure,
patch, and monitor any additional applications not specifically covered above.

- **Change management**:

AMS change management is the mechanism for you to control changes in your managed environment. AMS uses a combination of preventative
and detective controls to facilitate this process and provides different level of control and associated risk depending on the
AMS mode selected.

All actions in your AMS environment are logged in AWS CloudTrail.

For more information about AMS Change Management and different modes, see
[AMS Change Management guide](../ctref/index.md "../ctref/index.md") and
[AMS Modes](ams-modes-ug.md "ams-modes-ug.md").

- **Automated and self-service provisioning management**:

You can provision AWS resources on AMS Advanced in several ways:

    + Submit provisioning and configuration Requests for Change (RFCs)
    + Deploy through AWS Service Catalog
    + Deploy through [Direct Change mode](direct-change-mode.md "direct-change-mode.md")
    + Deploy through [Developer mode](developer-mode.md "developer-mode.md"). Remember that the resources
     created through the Developer mode are not managed by AMS.
    + Configure AWS services directly using self-service provisioning for select AWS services
     (see [Supported AWS services](supported-services.md "supported-services.md")).

- **Incident management**:

AMS proactively notifies you of incidents detected by AMS.
AMS responds to both customer-submitted and AMS-generated incidents and resolves incidents
based on the incident priority. Unless otherwise instructed by you, incidents
that are determined by AMS to be a risk to the security of your managed environment, and incidents
relating to the availability of AMS and other AWS services, are proactively actioned.
AMS takes action on all other incidents once your authorization is received. Recurring
incidents are addressed by the problem management process.

- **Problem management**:

AMS performs trend analysis to identify and investigate problems and to identify the root
cause. Problems are remediated either with a workaround or a permanent solution that prevents recurrence of
similar future service impact. A post incident report (PIR) may be requested for any "High" incident,
upon resolution. The PIR captures the root cause and preventative actions taken, including implementation
of preventative measures.

- **Reporting**:

AMS provides you with a monthly service report that summarizes key performance metrics
of AMS, including an executive summary and insights, operational metrics, managed resources,
AMS service level agreement (SLA) adherence, and financial metrics around spending, savings, and cost
optimization. Reports are delivered by the AMS cloud service delivery manager (CSDM)
assigned to you.

- **Service request management** :

To request information about your managed environment, AMS, or AWS service offerings, submit service requests using the AMS console. You can submit a service request for "How to" questions about AWS services and features or to request additional AMS services.

- **Service Desk** :

AMS staffs engineering operations with full-time Amazon employees to fulfill non-automated
requests including incident management, service request management, and change management. The Service Desk
operates 24 x 7 365 days a year.

- **Designated resources**:

Each customer is assigned a Cloud Service Delivery Manager (CSDM) and a Cloud Architect (CA).

    + CSDMs can be contacted directly. They perform service reviews, and delivery reporting and
     insights through all phases of the implementation, migration and operational life cycle. CSDMs conduct
     monthly business reviews and detail items such as financial spend, cost-saving recommendations, service
     utilization, and risk reporting. They dive deep into operational performance statistics and provide
     recommendations of areas of improvements.
    + CAs can be contacted directly and provide technical expertise to help you optimize
     your use of the AWS cloud. Example CA activities include, selecting workloads for migration, assisting
     with the onboarding additional accounts and workloads, acting as the technical lead in operational
     activities such as game days, disaster recovery testing, problem management, and technical advice to
     get the most out of AMS and AWS. CAs drive technical discussions at all levels of your organization
     and assist with incident management, making trade-offs, establishing best practices, and technical
     risk mitigation.

- **Developer mode** :

This feature enables you to iterate infrastructure designs and deployments quickly within
AMS-configured accounts[1] by allowing direct access to AWS service APIs and the
AWS console in addition to access to the AMS change management process. Resources provisioned or
configured with developer mode permissions outside of the change management process are your responsibility
to manage (See "Automated and Self-Service Provisioning Management"). Resources provisioned
through the AMS change management process are supported like other change management-provisioned workloads
on AMS.

- **AWS support**:

AMS customers can choose the level of AWS Support they require to complement their AMS Operations plan.
Accounts enrolled in AMS can be subscribed to either Business Support or Enterprise Support. To
learn about the differences in Support Plans, see
[AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

- **Customer-managed account**:

This feature enables you to request AWS accounts within the same managed environment but the ongoing
operations of workloads and AWS resources within those accounts are your responsibility. AMS
provisions customer-managed accounts, but once the accounts are created, no other AMS features or services
are provided to those accounts. AWS will not enroll customer-managed accounts in enterprise-level
premium support. It will be your responsibility to enroll customer-managed accounts in AWS support at
the support rate you choose.

- **Firewall management**:

AMS provides an optional managed firewall solution for Supported Firewall Services, which enables
internet-bound egress traffic filtering for networks in your managed environment. This excludes public-facing services
that do not use the AWS network infrastructure and whose traffic goes directly to the internet. The solution combines
industry-leading firewall technology with AMS infrastructure management capabilities to deploy, monitor, manage, scale, and
restore the firewall infrastructure.
When you onboard AMS, you receive a complete list of your AMS network infrastructure.
To get an updated list of services running in support of your AMS infrastructure at any
time, file a service request with specifics about the information you want. To request a
change to your network design, create a service request describing the changes you want to
make—for example, adding a VPC or requesting a security group rule change.
