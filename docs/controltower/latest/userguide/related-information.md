# Additional information and links

This topic includes links to relevant blog posts, technical documentation, and related
information that can help you as you work with AWS Control Tower. The sources cover some common use
cases and best practices for AWS Control Tower capabilities, and some additional enhancements.

## Tutorials and labs

- [AWS Control Tower
  lab](https://catalog.workshops.aws/control-tower/en-US "https://catalog.workshops.aws/control-tower/en-US") – These labs provide a high-level overview of common
  tasks related to AWS Control Tower.
- On the AWS Control Tower dashboard, choose **Get
  personalized guidance** if you have a use case in mind but you're
  not sure where to start.
- Try visiting this [AWS Cloud Operations YouTube playlist](https://www.youtube.com/playlist?list=PLhr1KZpdzukdbisTs-Eskg4xsfLFOki1T "https://www.youtube.com/playlist?list=PLhr1KZpdzukdbisTs-Eskg4xsfLFOki1T") and search AWS Control Tower to find
  videos that explain more about how to use AWS Control Tower functionality.

## Networking

Set up repeatable and manageable patterns for networks in AWS. Learn more about
design, automation, and appliances that are commonly used by
customers.

- [AWS Quick Start
  VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/")– This Quick Start guide provides a
  networking foundation based on AWS best practices for your AWS Cloud
  infrastructure. It builds an AWS Virtual Private Network environment with public and
  private subnets where you can launch AWS services and other resources.
- [Self-service VPCs in AWS Control Tower using AWS Service Catalog](https://aws.amazon.com/blogs/mt/self-service-vpcs-in-aws-control-tower-using-aws-service-catalog/ "https://aws.amazon.com/blogs/mt/self-service-vpcs-in-aws-control-tower-using-aws-service-catalog/")–
  This blog post describes a way to set up Account Factory so you can provision
  accounts with customized VPCs.
- [Implementing Serverless Transit Network Orchestrator (STNO) in
  AWS Control Tower](https://aws.amazon.com/blogs/mt/serverless-transit-network-orchestrator-stno-in-control-tower/ "https://aws.amazon.com/blogs/mt/serverless-transit-network-orchestrator-stno-in-control-tower/") – This blog post demonstrates how to automate
  network connectivity access across accounts. This blog is intended for AWS Control Tower
  administrators, or those responsible for managing networks within their AWS
  environment.

## Security, identity, and logging

Extend your security posture, integrate with external or existing identity providers,
and centralize logging systems.

_Security_

- [Automating AWS Security Hub Alerts with AWS Control Tower lifecycle events](https://aws.amazon.com/blogs/mt/automating-aws-security-hub-alerts-with-aws-control-tower-lifecycle-events/ "https://aws.amazon.com/blogs/mt/automating-aws-security-hub-alerts-with-aws-control-tower-lifecycle-events/") –
  This blog post describes how to automate Security Hub enablement and configuration in
  an AWS Control Tower multi-account environment on existing and new accounts.
- [Enabling AWS Identity and Access Management](https://aws.amazon.com/blogs/mt/enabling-aws-identity-and-access-analyzer-on-aws-control-tower-accounts "https://aws.amazon.com/blogs/mt/enabling-aws-identity-and-access-analyzer-on-aws-control-tower-accounts") – This blog post describes how to enhance
  your organizational security visibility by enabling and centralizing IAM
  Access Analyzer findings.
- [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") provides
  secure, hierarchical storage for configuration data management and secrets
  management. You can use it to share configuration information in a secure
  location, for use by AWS Systems Manager and by AWS CloudFormation. For example,
  you can store a list of Regions in which you want to deploy conformance packs.

_Identity_

- [Link
  Azure AD user identity into AWS accounts and applications for single
  sign-on](https://aws.amazon.com/blogs/aws/the-next-evolution-in-aws-single-sign-on/ "https://aws.amazon.com/blogs/aws/the-next-evolution-in-aws-single-sign-on/") – This blog post describes how to use Azure AD with
  IAM Identity Center and AWS Control Tower.
- [Manage access to AWS centrally for Okta users with AWS IAM Identity Center](https://aws.amazon.com/about-aws/whats-new/2020/05/manage-access-to-aws-centrally-for-okta-users-with-aws-single-sign-on/ "https://aws.amazon.com/about-aws/whats-new/2020/05/manage-access-to-aws-centrally-for-okta-users-with-aws-single-sign-on/")
  – This blog post describes how to use Okta with IAM Identity Center and AWS Control Tower.

_Logging_

- [AWS Centralized Logging Solution](https://aws.amazon.com/solutions/implementations/centralized-logging/ "https://aws.amazon.com/solutions/implementations/centralized-logging/") – This solutions post
  describes the Centralized Logging solution which enables organizations to
  collect, analyze, and display logs on AWS across multiple accounts and AWS
  Regions.
- For information about viewing your AWS Config resources, see the [Config Resource Compliance Dashboard](https://catalog.workshops.aws/awscid/en-US/dashboards/additional/config-resource-compliance-dashboard "https://catalog.workshops.aws/awscid/en-US/dashboards/additional/config-resource-compliance-dashboard").

## Deploying resources and managing workloads

Deploy and manage resources and workloads.

- [Getting Started Library integration](https://aws.amazon.com/about-aws/whats-new/2020/04/aws-service-catalog-adds-three-new-getting-started-portfolios/ "https://aws.amazon.com/about-aws/whats-new/2020/04/aws-service-catalog-adds-three-new-getting-started-portfolios/") – This blog post
  describes Getting Started portfolios you can use.
- [Continuous deployment of Cloud Custodian to AWS Control Tower](https://aws.amazon.com/blogs/opensource/continuous-deployment-of-cloud-custodian-to-aws-control-tower/ "https://aws.amazon.com/blogs/opensource/continuous-deployment-of-cloud-custodian-to-aws-control-tower/")

## Working with existing organizations and

accounts

Work with existing AWS organizations and accounts.

- [Enroll an account](enroll-account.md "enroll-account.md") – This user guide topic describes how to
  enroll an existing AWS account in AWS Control Tower.
- [Bring an account under AWS Control Tower](https://aws.amazon.com/blogs//architecture/field-notes-enroll-existing-aws-accounts-into-aws-control-tower/ "https://aws.amazon.com/blogs//architecture/field-notes-enroll-existing-aws-accounts-into-aws-control-tower/") – This blog post describes
  how to deploy AWS Control Tower into your existing AWS organizations.
- [Extend AWS Control Tower governance using AWS Config conformance
  packs](https://aws.amazon.com/blogs//mt/extend-aws-control-tower-governance-using-aws-config-conformance-packs/ "https://aws.amazon.com/blogs//mt/extend-aws-control-tower-governance-using-aws-config-conformance-packs/") – This blog post describes how to deploy AWS Config
  conformance packs to assist with bringing existing accounts and organizations
  into governance by AWS Control Tower.
- [How to Detect and Mitigate Guardrail Violation with AWS Control Tower](https://aws.amazon.com/blogs/mt/how-to-detect-and-mitigate-guardrail-violation-with-aws-control-tower/ "https://aws.amazon.com/blogs/mt/how-to-detect-and-mitigate-guardrail-violation-with-aws-control-tower/")
  – This blog post describes how to add controls and how to subscribe to
  SNS notifications so that you can be notified by email of control compliance
  violations.

## Automation and integration

Automate account creation and integrate lifecycle events with AWS Control Tower.

- [Lifecycle events](https://aws.amazon.com/blogs/mt/using-lifecycle-events-to-track-aws-control-tower-actions-and-trigger-automated-workflows "https://aws.amazon.com/blogs/mt/using-lifecycle-events-to-track-aws-control-tower-actions-and-trigger-automated-workflows") – This blog post describes how to use
  lifecycle events with AWS Control Tower.
- [Automate account creation](https://aws.amazon.com/blogs/mt/how-to-automate-the-creation-of-multiple-accounts-in-aws-control-tower/ "https://aws.amazon.com/blogs/mt/how-to-automate-the-creation-of-multiple-accounts-in-aws-control-tower/") – This blog post describes how to
  set up automated account creation in AWS Control Tower.
- [Amazon VPC flow log automation](https://aws.amazon.com/blogs/mt/vpc-flow-log-with-aws-control-tower-lifecycle "https://aws.amazon.com/blogs/mt/vpc-flow-log-with-aws-control-tower-lifecycle") – This blog post describes how to
  automate and centralize Amazon VPC Flow Logs in a multi-account environment.
- [Automate VPC tagging with AWS Control Tower lifecycle events](https://aws.amazon.com/blogs//infrastructure-and-automation/automate-vpc-tagging-with-aws-control-tower-lifecycle-events/ "https://aws.amazon.com/blogs//infrastructure-and-automation/automate-vpc-tagging-with-aws-control-tower-lifecycle-events/")– This
  blog post describes how to automate resource tagging for VPCs, by means of
  lifecycle events in AWS Control Tower.
- [Automated account management](https://aws.amazon.com/blogs/mt/using-aws-control-tower-and-aws-service-catalog-to-automate-control-tower-lifecycle-events/ "https://aws.amazon.com/blogs/mt/using-aws-control-tower-and-aws-service-catalog-to-automate-control-tower-lifecycle-events/") – This blog post describes how
  to automate account management tasks after your AWS Control Tower environment is set
  up.

## Migrating workloads

Use other AWS services with AWS Control Tower to assist in workload migration.

- [CloudEndure migration](https://aws.amazon.com/blogs/mt/how-to-take-advantage-of-aws-control-tower-and-cloudendure-to-migrate-workloads-to-aws/ "https://aws.amazon.com/blogs/mt/how-to-take-advantage-of-aws-control-tower-and-cloudendure-to-migrate-workloads-to-aws/") – This blog post describes how to
  combine CloudEndure and other AWS services with AWS Control Tower to assist in workload
  migration.

## Related AWS services

AWS Control Tower acts as an orchestration layer for AWS Organizations. Therefore, by means of the AWS
Organizations console and APIs, you have access to over 20 other AWS services that work
with AWS Control Tower. These additional services are not accessible directly through the
AWS Control Tower console.

- For a full list of services available to AWS Control Tower by means of AWS
  Organizations, see [AWS
  services that you can use with AWS Organizations](../../../organizations/latest/userguide/orgs_integrate_services_list.md "../../../organizations/latest/userguide/orgs_integrate_services_list.md").
- To enable multi-account capabilities for these related AWS services, you must
  enable trusted access. For more information, see [Using AWS
  Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md").

###### Note

Remember that AWS IAM Identity Center, AWS Config, and AWS CloudTrail are set up for you in
AWS Control Tower and fully integrated. You do not need to modify your trusted access
or delegated administration settings for these services.

- Some AWS services available through AWS Organizations can use delegated
  administration, including AWS Systems Manager and AWS Firewall Manager. For more
  information, see [Configuring a Delegated Administrator](../../../systems-manager/latest/userguide/Explorer-setup-delegated-administrator.md "../../../systems-manager/latest/userguide/Explorer-setup-delegated-administrator.md"), and [Enabling a delegated administrator account for Firewall Manager](../../../organizations/latest/userguide/services-that-can-integrate-fms.md#integrate-enable-da-fms "../../../organizations/latest/userguide/services-that-can-integrate-fms.md#integrate-enable-da-fms").
  Also see this video, [Set up
  security groups with AWS Firewall Manager](firewall-setup-walkthrough.md "firewall-setup-walkthrough.md").

## AWS Marketplace solutions

Discover solutions from AWS Marketplace.

- [AWS Control Tower
  Marketplace](https://aws.amazon.com/marketplace/solutions/control-tower "https://aws.amazon.com/marketplace/solutions/control-tower") – AWS Marketplace offers a broad range of solutions for
  AWS Control Tower to help you integrate third-party software. These solutions help solve
  key infrastructure and operational use cases including identity management,
  security for a multi-account environment, centralized networking, operational
  intelligence, and security information and event management (SIEM).
