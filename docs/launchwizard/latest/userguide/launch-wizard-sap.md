# AWS Launch Wizard for SAP

AWS Launch Wizard for SAP is a service that guides you through the sizing, configuration, and
deployment of SAP applications on AWS, and follows [AWS cloud application best
practices](../../../wellarchitected/latest/framework/welcome.md "../../../wellarchitected/latest/framework/welcome.md").

AWS Launch Wizard reduces the time it takes to deploy SAP applications on AWS. You input your
application requirements, including the database (SAP HANA or SAP ASE) settings, SAP
landscape settings, and deployment details on the service console, and Launch Wizard identifies the
appropriate AWS resources to deploy and run your SAP application. Launch Wizard provides an
estimated cost of deployment, which allows you to modify your resources and instantly view
the updated cost. When you finalize your settings, Launch Wizard provisions and configures the
selected resources. It then optionally installs SAP application/database software using
customer-provided software.

You can create deployments from the Launch Wizard console or AWS Launch Wizard APIs. For more information,
see [Get started with AWS Launch Wizard for
SAP](launch-wizard-sap-getting-started.md "launch-wizard-sap-getting-started.md").

After you deploy an SAP application, you can access it from the Amazon EC2 console. You can
manage your SAP applications with [AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md").

## Supported deployments and features of

AWS Launch Wizard

###### Supported deployments

AWS Launch Wizard currently supports the deployment of AWS resources for the following
SAP systems and patterns. SAP HANA database software and supported SAP application
software are optionally installed and provided by the customer.

- **SAP HANA database on a single Amazon EC2 instance.**
  Deploy SAP HANA in a single-node, scale-up architecture, with up to 24TB of
  memory.
- **SAP NetWeaver on SAP HANA system on a single Amazon EC2
  instance.** Deploy an SAP application on the same Amazon EC2 instance as
  your SAP HANA database.
- **SAP NetWeaver on SAP ASE database on a single Amazon EC2
  instance.** Deploy an SAP application on the same Amazon EC2 instance as
  your SAP ASE database.
- **SAP HANA database on multiple EC2 instances.**
  Deploy SAP HANA in a multi-node, scale-out architecture.
- **SAP NetWeaver on SAP HANA system on multiple EC2
  instances.** Deploy an SAP NetWeaver system using a distributed
  deployment model, which includes an ASCS/PAS server, single/multiple SAP HANA
  servers running SAP HANA databases, and multiple application servers.
- **SAP NetWeaver on SAP ASE system on multiple EC2
  instances.** Deploy an SAP NetWeaver system using a distributed
  deployment model, which includes an ASCS/PAS server, multiple application
  servers, and single SAP ASE database server.
- **Cross-AZ SAP HANA database high availability
  setup.** Deploy SAP HANA with high availability configured across
  two Availability Zones.
- **Cross-AZ SAP NetWeaver system setup.** Deploy
  Amazon EC2 instances for ASCS/ERS and SAP HANA databases across two Availability
  Zones, and spread the deployment of application servers across them.
- **SUSE/RHEL cluster setup** For SAP HANA and
  NetWeaver on HANA high availability deployments, Launch Wizard for SAP
  configures SUSE/RHEL clustering when you provide SAP software and specify the
  deployment of SAP database or application software. For SAP HANA databases,
  clustering is enabled between the ASCS and ERS nodes.

###### AWS Launch Wizard provides the following features:

- [Instance selection and
  configuration](#launch-wizard-sap-features-app-deployment "#launch-wizard-sap-features-app-deployment")
- [AWS resource
  selection](#launch-wizard-sap-features-resource-selection "#launch-wizard-sap-features-resource-selection")
- [Cost estimation](#launch-wizard-sap-features-cost "#launch-wizard-sap-features-cost")
- [Reusable infrastructure
  settings](#launch-wizard-sap-features-code-templates "#launch-wizard-sap-features-code-templates")
- [SNS notification](#launch-wizard-sap-features-sns "#launch-wizard-sap-features-sns")
- [Application resource
  groups](#launch-wizard-sap-features-resource-groups "#launch-wizard-sap-features-resource-groups")
- [AWS Data Provider for
  SAP](#launch-wizard-sap-features-data-provider "#launch-wizard-sap-features-data-provider")
- [AWS Backint Agent for SAP
  HANA](#launch-wizard-sap-features-backint "#launch-wizard-sap-features-backint")
- [Custom deployment configuration
  scripts](#launch-wizard-sap-features-scripts "#launch-wizard-sap-features-scripts")
- [Application software
  installation](#launch-wizard-sap-features-software-install "#launch-wizard-sap-features-software-install")
- [Creation of
  AWS Service Catalog products](#launch-wizard-features-service-catalog "#launch-wizard-features-service-catalog")
- [AWS Systems Manager for
  SAP](#launch-wizard-features-systems-manager-for-sap "#launch-wizard-features-systems-manager-for-sap")
- [AWS Regions](#launch-wizard-sap-regions "#launch-wizard-sap-regions")

### Instance selection and

configuration

When you input the application requirements, Launch Wizard deploys the necessary AWS
resources for a production-ready application. This means that you do not have to
figure out how to select the right instances and configure them to run supported SAP
applications.

### AWS resource

selection

Launch Wizard considers CPU/Memory or SAPS requirements that you provide to determine the
most appropriate instance types and other resources for your SAP application. You
can modify the recommended defaults.

### Cost estimation

Launch Wizard provides a cost estimate for the complete deployment that is itemized for
each individual resource being deployed. The estimated cost automatically updates
each time you change a resource type configuration in the wizard. The provided
estimates are only for general comparisons. They are based on On-Demand Instance
costs. Actual costs may be lower.

### Reusable infrastructure

settings

You can save the settings for your AWS infrastructure for the SAP landscape to
reuse when you want to deploy SAP systems that function similarly within a
landscape. For example, a development configuration can be created for the first
development instance, which can later be reused to deploy other development
systems.

Some example scenarios for which DevOps and SAP architecture teams can create
templates include:

- Organize the SAP systems within a landscape.
- Save infrastructure settings, including VPC, subnets, key pairs, and
  security groups to ensure that systems that must be deployed with the same
  settings are correctly deployed.
- Set up connectivity between the systems using the same configuration
  template so they can communicate with each other when security groups are
  created with Launch Wizard.
- Use the same GID for SAPSYS group across different configuration templates
  to ensure that SAP transport files systems are mounted properly.

### SNS notification

You can provide an [SNS
topic](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") so that Launch Wizard will send you notifications and alerts about the
status of a deployment.

### Application resource

groups

Launch Wizard creates a resource group for all of the AWS resources created for your SAP
system. You can manage the resources through the Amazon EC2 console or by using Systems
Manager.

### AWS Data Provider for

SAP

Deploying and running the Amazon Web Services (AWS) Data Provider for SAP is a
prerequisite for running SAP systems on AWS. Launch Wizard automatically deploys AWS Data
Provider for SAP on every Amazon EC2 instance that it launches. AWS Data Provider for
SAP is a tool that collects performance-related data from AWS services. It makes
this data available to SAP applications to help monitor and improve the performance
of business transactions. AWS Data Provider for SAP uses operating system,
network, and storage data that is most relevant to the operation of the SAP
infrastructure. Its data sources include Amazon EC2 and Amazon CloudWatch.

### AWS Backint Agent for SAP

HANA

Launch Wizard deploys and configures AWS Backint Agent for SAP HANA, an SAP-certified
backup and restore application for SAP HANA workloads running on Amazon EC2 instances in
the cloud. Launch Wizard supports the deployment and configuration of Backint Agent
for single-node, multi-node, and high availability deployments for supported SAP
HANA and SAP NetWeaver on SAP HANA applications.

You have the option to choose fully-managed backup or self-managed backup when
deploying SAP applications using Launch Wizard for SAP workflow. Launch Wizard for SAP deploys AWS
Backint agent for AWS Backup if fully-managed backup is selected or AWS Backint agent
for Amazon S3 if self-managed backup is selected as your backup method.

Once the deployment is complete, you must maintain AWS Backint Agent for SAP
HANA with latest releases and updated configurations. For more information, see
[AWS Backint Agent
for SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md "../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md").

### Custom deployment configuration

scripts

You can provide custom pre-deployment and post-deployment configuration scripts
that can run on various instance tiers, such as SAP HANA Database, Primary
Application Server, and Enqueue Replication Server during the pre-deployment and
post-deployment configuration phases. Launch Wizard uses a standalone component manager
application (AWSTOE) to run the scripts. For more information, see [Custom deployment configuration
scripts](how-launch-wizard-sap-works.md#launch-wizard-sap-how-it-works-scripts "how-launch-wizard-sap-works.md#launch-wizard-sap-how-it-works-scripts").

### Application software

installation

Launch Wizard can install SAP application software that you have made available on Amazon S3,
including SAP NetWeaver ABAP on SAP HANA and SAP ASE databases, SAP NetWeaver JAVA
on SAP HANA and SAP ASE databases, SAP Solution Manager on SAP HANA and SAP ASE
databases, SAP S/4HANA, and SAP BW/4HANA. For more details about which operating
systems and database versions are supported for each deployment pattern, see [SAP applications](launch-wizard-sap-versions.md#launch-wizard-sap-versions-application "launch-wizard-sap-versions.md#launch-wizard-sap-versions-application"). For supported software
versions and installation details, see [Make SAP application software
available for AWS Launch Wizard to deploy SAP](launch-wizard-sap-software-install-details.md "launch-wizard-sap-software-install-details.md").

### Creation of

AWS Service Catalog products

AWS Launch Wizard can create AWS Service Catalog products from successful
deployments. The AWS Service Catalog products contain AWS CloudFormation templates and
associated application configuration scripts, which are stored in Amazon S3. You can use
the AWS Service Catalog products, along with integrations offered by
AWS Service Catalog, with third-party products, such as ServiceNow, Jira, or Terraform. Or, you
can use the AWS CloudFormation templates and application configuration scripts saved in Amazon S3 to
deploy SAP applications that meet the requirements of organizational deployment and
governance policies.

In addition to supporting deployments using AWS CloudFormation templates,
AWS Service Catalog, and multiple deployment tools supported by
AWS Service Catalog, AWS Launch Wizard creates a point-in-time snapshot of the code
used to deploy and configure SAP applications at the time of the deployment. You can
use the code in its current form for consistent repeated deployments, or you can use
the code as a baseline and update it to meet specific application
requirements.

### AWS Systems Manager for

SAP

You can register SAP HANA databases and SAP applications based on SAP HANA
database with AWS Systems Manager for SAP. It enables you to configure managed backups with
AWS Backup for SAP HANA at the time of deployment with AWS Launch Wizard for SAP. These newly
deployed applications have access to the management and operational capability that
offered by AWS Systems Manager for SAP.

- SAP HANA single-node, SAP HANA high availability, and SAP NetWeaver on SAP
  HANA are supported. For more information, see [Supported
  versions for SAP deployments](../../../ssm-sap/latest/userguide/supported-versions.md "../../../ssm-sap/latest/userguide/supported-versions.md").
- S/4HANA, S/4HANA Foundation, NetWeaver 7.5X, and BW/4HANA are the
  supported software stacks for SAP NetWeaver on SAP HANA deployments.
- This feature is available in all commercial regions where AWS Launch Wizard for SAP
  and AWS Systems Manager for SAP supported backup for SAP HANA with AWS Backup is available.
  For more information, see [Supported Regions](../../../ssm-sap/latest/userguide/what-is-ssm-for-sap.md#supported-regions "../../../ssm-sap/latest/userguide/what-is-ssm-for-sap.md#supported-regions").

### AWS Regions

Launch Wizard uses various AWS services during the provisioning of the application's
environment. Not every workload is supported in all AWS Regions. For a current
list of Regions where the workload can be provisioned, see [AWS Launch Wizard workload availability](launch-wizard-workload-availability.md "launch-wizard-workload-availability.md").

## Components

An SAP application deployed with Launch Wizard includes the following components.

###### SAP applications:

- **SAP HANA Database** supports the
  following:
  - Single instance deployment
  - Distributed instance deployment in a single Availability Zone
  - Cross-Availability Zone, high-availability deployment

- **SAP applications based on SAP NetWeaver on SAP HANA
  database** supports the following:
  - Single instance deployment
  - Distributed instance deployment
  - cross-Availability Zone, high-availability deployment

- **SAP applications based on SAP NetWeaver on SAP ASE
  database** supports the following:
  - Single instance deployment
  - Distributed instance deployment in a single Availability Zone

- **SAP Web Dispatcher** supports the
  following:
  - All SAP deployment patterns, including with other SAP
    applications

###### Security groups

Launch Wizard creates optional security groups to ensure that all of the systems sharing
the same configuration template can communicate with each other and with systems and
end users who access the SAP systems from an IP CIDR range, an external IP address,
or security groups. For more information about how Launch Wizard creates security groups and
how they are configured, see [Security groups in AWS Launch Wizard for
SAP](launch-wizard-sap-security-groups.md "launch-wizard-sap-security-groups.md").

###### SAP transport group configuration

You can create an SAP transport file system, or attach an existing transport file
system that was created as part of a previous deployment with AWS Launch Wizard. Transport
file systems are created with Amazon Elastic File System. For more information, see [Amazon Elastic File System setup for transport directory](how-launch-wizard-sap-works.md#launch-wizard-sap-efs "how-launch-wizard-sap-works.md#launch-wizard-sap-efs").

## Related services

The following AWS services are used when you deploy an SAP application with
AWS Launch Wizard.

###### Services

- [AWS CloudFormation](#launch-wizard-sap-related-services-cloudformation "#launch-wizard-sap-related-services-cloudformation")
- [Amazon Virtual Private Cloud security
  groups](#launch-wizard-sap-related-services-vpc "#launch-wizard-sap-related-services-vpc")
- [Amazon Elastic File System](#launch-wizard-sap-related-services-efs "#launch-wizard-sap-related-services-efs")
- [AWS Systems Manager](#launch-wizard-sap-related-services-SSM "#launch-wizard-sap-related-services-SSM")
- [Amazon Simple Notification
  Service (SNS)](#launch-wizard-related-services-sns "#launch-wizard-related-services-sns")
- [Amazon Route 53](#launch-wizard-related-services-route53 "#launch-wizard-related-services-route53")
- [AWS Backint Agent for SAP
  HANA](#launch-wizard-related-services-backint "#launch-wizard-related-services-backint")
- [AWS Task Orchestrator and Executor](#launch-wizard-related-services-ec2toe "#launch-wizard-related-services-ec2toe")
- [Amazon FSx for NetApp ONTAP](#launch-wizard-sap-related-services-fsx "#launch-wizard-sap-related-services-fsx")
- [Elastic Load Balancing](#launch-wizard-sap-related-services-alb "#launch-wizard-sap-related-services-alb")
- [AWS Systems Manager for SAP](#launch-wizard-sap-related-services-ssm "#launch-wizard-sap-related-services-ssm")

### AWS CloudFormation

[AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") is a service that helps you model and set up your AWS
resources, and lets you spend more time focusing on your applications that run in
AWS. You create a template that describes all of the AWS resources that you want
(for example, Amazon EC2 instances or Amazon RDS DB instances), and AWS CloudFormation takes care of
provisioning and configuring those resources for you. With AWS Launch Wizard for SAP, you
don’t need to build AWS CloudFormation templates to deploy your application. Instead, AWS Launch Wizard
combines infrastructure provisioning and application configuration (code that runs
on EC2 instances to configure the application) into a unified AWS CloudFormation template. The
AWS CloudFormation template is then invoked by AWS Launch Wizard’s backend service to provision an
application in your account.

### Amazon Virtual Private Cloud security

groups

[Amazon Virtual Private Cloud security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") act as a virtual firewall for your instance
to control inbound and outbound traffic. When you launch an instance in a VPC, you
can assign up to five security groups to the instances. AWS Launch Wizard displays the
security groups that will be assigned to the EC2 instances that run the SAP
applications. This allows the components to communicate.

### Amazon Elastic File System

[Amazon EFS](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") provides
file storage in the AWS Cloud. With Amazon EFS, you can create a file system,
mount the file system on an Amazon EC2 instance, and then read and write data to and from
your file system. For more information, see [Amazon Elastic File System setup for transport directory](how-launch-wizard-sap-works.md#launch-wizard-sap-efs "how-launch-wizard-sap-works.md#launch-wizard-sap-efs").

### AWS Systems Manager

[AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") is an AWS service that you can use to view and control your
infrastructure on AWS. Using the AWS Systems Manager console, you can view operational data
from multiple AWS services and automate operational tasks across your AWS
resources. Systems Manager helps you maintain security and compliance by scanning your managed
instances and reporting on, or taking corrective action on, any policy violations
that it detects.

### Amazon Simple Notification

Service (SNS)

[Amazon Simple Notification
Service (SNS)](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") is a highly available, durable, secure, fully managed
pub/sub messaging service that provides topics for high-throughput, push-based,
many-to-many messaging. Using Amazon SNS topics, your publisher systems can fan out
messages to a large number of subscriber endpoints and send notifications to end
users using mobile push, SMS, and email. You can use SNS topics for your Launch Wizard
deployments to stay up-to-date on deployment progress. For more information, see the
[_Amazon Simple Notification Service Developer Guide_](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").

### Amazon Route 53

[Amazon Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md") is a highly available and scalable Domain Name System (DNS)
web service. You can use Route 53 to perform three main functions in any combination:
domain registration, DNS routing, and health checking. Launch Wizard integrates with Route 53
hosted zones, which are containers for records. The records contain information
about how you want to route traffic for a specific domain, such as example.com, and
its subdomains (acme.example.com, zenith.example.com). There are two types of hosted
zones: public and private hosted zones. We recommend that you use private hosted
zones for SAP applications unless an application must be directly accessible from
the internet.

### AWS Backint Agent for SAP

HANA

[AWS Backint Agent for
SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-what-is.md "../../../sap/latest/sap-hana/aws-backint-agent-what-is.md") is an SAP-certified backup and restore application for SAP HANA
workloads running on Amazon EC2 instances in the cloud. AWS Backint Agent runs as
a standalone application that integrates with your existing workflows to back up
your SAP HANA database to Amazon S3 and to restore it using SAP HANA Cockpit, SAP
HANA Studio, and SQL commands. AWS Backint Agent supports full, incremental, and
differential backup of SAP HANA databases. Additionally, you can back up log files
and catalogs to Amazon S3. AWS Backint Agent runs on an SAP HANA database server,
where backups and catalogs are transferred from the SAP HANA database to the AWS
Backint Agent. The AWS Backint Agent stores your files in the S3 bucket that is
specified in the agent configuration file. To restore your SAP HANA database server,
SAP HANA reads the catalog files stored in your S3 bucket using the AWS Backint
Agent. It then initiates a request to restore the required files from S3.

### AWS Task Orchestrator and Executor

[AWS Task Orchestrator and Executor](../../../imagebuilder/latest/userguide/image-builder-component-manager.md "../../../imagebuilder/latest/userguide/image-builder-component-manager.md") is component management application used to orchestrate
complex workflows, modify system configurations, and test your systems without
writing code. This application uses a declarative document schema. As a standalone
application it does not require additional server setup. It can run on any cloud
infrastructure and on premises. AWS Launch Wizard uses this application to orchestrate the
download of the pre- and post-configuration scripts, and to run them.

### Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable,
scalable, high-performing, and feature-rich file storage built on NetApp's popular
ONTAP file system. You can now deploy and operate SAP HANA on AWS with Amazon FSx for
NetApp ONTAP. For more information, see [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/ "https://aws.amazon.com/fsx/netapp-ontap/").

### Elastic Load Balancing

Elastic Load Balancing can be deployed as an optional component to load balance internet or
intranet traffic between one or more SAP Web Dispatcher instances. Launch Wizard for SAP
supports both Application Load Balancer and Network Load Balancer resources. For more information, see [What is
Elastic Load Balancing?](../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md "../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md") in the Elastic Load Balancing User Guide.

### AWS Systems Manager for SAP

AWS Systems Manager for SAP is a secure end-to-end management solution for resources on
AWS. It provides automation capabilities to help you manage and operate your SAP
applications on AWS more efficiently with features such as as managed backups with
AWS Backup for SAP HANA and graceful start/stop of SAP HANA.
