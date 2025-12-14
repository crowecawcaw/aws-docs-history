# Planning and Prerequisites

###### Topics

- [SAP Landscape Assessment](#sap-nw-dep-planning-and-prereqs-assess "#sap-nw-dep-planning-and-prereqs-assess")
- [Shared Resources](#sap-nw-dep-planning-and-prereqs-resource "#sap-nw-dep-planning-and-prereqs-resource")
- [Prerequisites](#sap-nw-dep-planning-and-prereqs-list "#sap-nw-dep-planning-and-prereqs-list")
- [Deployment Methods](#sap-nw-dep-planning-and-prereqs-dep "#sap-nw-dep-planning-and-prereqs-dep")

## SAP Landscape Assessment

Before deploying SAP NetWeaver on AWS, document your existing SAP landscape to inform architecture decisions. This assessment determines landing zone
requirements including account and subnet allocation, as well as patterns for infrastructure selection and shared services.

By considering the complete set of requirements, you can optimize resource allocation and plan for deployment automation where applicable. For comprehensive guidance on SAP workload design principles, refer to the [SAP Lens of the AWS Well-Architected Framework](../../../wellarchitected/latest/sap-lens/sap-lens.md "../../../wellarchitected/latest/sap-lens/sap-lens.md").

Review resilience, performance, and connectivity requirements to determine deployment pattern selection (single instance, distributed, or highly available) as well as requirements for web dispatchers and load balancers. Establish non-functional requirements for:

- Maximum tolerable downtime (RTO - Recovery Time Objective)
- Maximum acceptable data loss (RPO - Recovery Point Objective)
- Maintenance window constraints
- Geographic distribution requirements for disaster recovery

Consider sizing and cost implications for infrastructure selection, including Reserved Instances, operating system selection, and requirements for operational consistency and support.

## Shared Resources

Before deploying individual EC2 instances, consider resource dependencies and establish reusable patterns.

Shared resources may include:

- AWS accounts
- Target AWS Region and Availability Zones
- VPC ID and subnet configurations
- Databases (for example, tenant databases hosting multiple NetWeaver stacks)
- Security groups
- IAM roles
- Shared storage (transport directories, EFS file systems)
- S3 buckets for backups, software distribution, and logging
- Load balancers
- Encryption keys and secrets
- Instance type and Reserved Instance requirements
- AMI selection (SLES for SAP or RHEL for SAP)
- Required AWS service quotas and limits

For each resource type, establish patterns based on organizational boundaries: business unit, environment criticality (production/non-production), specific environments (development, test, sandbox), application type (BW, ECC), host type (ASCS, web dispatcher, application server), SAP System ID (SID), individual hosts, or AWS service boundaries.

These design standards directly impact naming conventions, shareable resources, tagging strategies, and automation patterns.

### Information gathering

As you work through the deployment process, consider how to populate your design and identify patterns for resource sharing. The following information will help you make consistent decisions across your SAP landscape.

| Information          | Description                                                                                                                                               | Your Value |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Region ID            | Region where you want to deploy your AWS resources                                                                                                        |            |
| Availability Zone    | Availability Zone within your target region where you want to deploy your resources. For High Availability installations, you need two Availability Zones |            |
| Amazon VPC ID        | Amazon VPC where you want to deploy your Amazon EC2 instance for SAP installation                                                                         |            |
| Subnet ID            | Subnet where you want to deploy your Amazon EC2 instance                                                                                                  |            |
| Key pair             | Key pair generated in your target region with access to the private key                                                                                   |            |
| Security group ID    | Security group that you want to assign to your Amazon EC2 instance                                                                                        |            |
| IAM instance profile | IAM instance profile with necessary permissions for SAP operations and AWS service access                                                                 |            |

Use this table to document your decisions and establish consistent patterns that can be reused across similar deployments in your SAP landscape.

## Prerequisites

### Design Scope

This guide provides technical implementation guidance for SAP NetWeaver infrastructure deployment. It is not a replacement for a comprehensive High Level Design (HLD). Work with your SAP Basis experts or Systems Integration partner to complete a full architectural design that addresses your specific business requirements, integration patterns, and operational procedures.

### Specialized Knowledge

This guide assumes familiarity with AWS services including Amazon VPC, Amazon EC2, Amazon EBS, Amazon EFS, and security groups. SAP NetWeaver architecture knowledge is required, including understanding of ASCS instances, application servers, and database connectivity patterns.

### SAP Documentation

[SAP Note 1656099 - SAP Applications on AWS: Supported DB/OS and AWS EC2 products](https://me.sap.com/notes/1656099 "https://me.sap.com/notes/1656099")

[SAP Note 1588667 - SAP on AWS: Overview of related SAP Notes and Web-Links](https://me.sap.com/notes/1588667 "https://me.sap.com/notes/1588667")

[SAP Note 1588896 - Linux: Support Statement for SLES on Amazon Web Services](https://me.sap.com/notes/1588896 "https://me.sap.com/notes/1588896")

[SAP Note 1618572 - Linux: Support Statement for RHEL on Amazon Web Services](https://me.sap.com/notes/1618572 "https://me.sap.com/notes/1618572")

[SAP Note 2369910 - SAP Software on Linux: General information](https://me.sap.com/notes/2369910 "https://me.sap.com/notes/2369910")

[SAP Note 1827960 - Adjusting operating system limits for SAP instances](https://me.sap.com/notes/1827960 "https://me.sap.com/notes/1827960")

## Deployment Methods

### AWS Launch Wizard for SAP

AWS Launch Wizard provides a guided deployment experience for SAP workloads, automatically provisioning and configuring AWS resources based on SAP best practices. Launch Wizard simplifies the deployment process by:

- Automatically sizing compute and storage resources based on SAP requirements
- Configuring networking and security groups according to SAP communication patterns
- Setting up monitoring and backup solutions
- Providing cost estimates before deployment

For detailed information about Launch Wizard for SAP, see [AWS Launch Wizard for SAP User Guide](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md").

When designing systems deployed through Launch Wizard, understand the underlying architecture and resource relationships. For comprehensive design considerations, see [How AWS Launch Wizard for SAP works](../../../launchwizard/latest/userguide/how-launch-wizard-sap-works.md "../../../launchwizard/latest/userguide/how-launch-wizard-sap-works.md").

### Infrastructure as Code

For repeatable deployments and standardization across environments, consider Infrastructure as Code approaches such as AWS CloudFormation.

### Manual Deployment using AWS Console or AWS CLI

Install and configure the AWS CLI with appropriate credentials and target region. Ensure IAM permissions include EC2, EBS, EFS, and Systems Manager access as required for the deployment.
