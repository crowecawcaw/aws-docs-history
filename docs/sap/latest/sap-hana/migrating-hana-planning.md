

# Planning
<a name="migrating-hana-planning"></a>

Before you start migrating your SAP environment to AWS, there are some prerequisites that we recommend you go over, to ensure minimal interruptions or delays. For details, see the [SAP on AWS overview](https://docs.aws.amazon.com/sap/latest/general/sap-on-aws-overview.html). The following sections discuss additional considerations for planning your migration.

## Understanding On-Premises Resource Utilization
<a name="migrating-hana-resource-utilization"></a>

If you are planning to rehost your on-premises SAP HANA environment on AWS, [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/) can help you understand the utilization of resources as well as hardware configuration, performance data, and network connections in your on-premises SAP HANA environment. You can use this information to ensure that appropriate communication ports are enabled between SAP HANA and other systems in the security groups or virtual private clouds (VPCs) on AWS.

Application Discovery Service can be deployed in an agentless mode (for VMware environments) or with an agent-based mode (all VMs and physical servers). We recommend that you run Application Discovery Service for a few weeks to get a complete, initial assessment of how your on-premises environment is utilized, before you migrate to AWS.

## Reviewing AWS Automation Tools for SAP
<a name="migrating-hana-automation"></a>

It is a good idea to review AWS automation tools and services that can help you migrate your SAP environment to AWS. For example, AWS Launch Wizard for SAP helps you deploy workloads, such as SAP HANA and SAP NetWeaver application servers. For details, see the [Migration Tools and Methodologies](migrating-hana-tools.md) section later in this guide.

## Prerequisites
<a name="migrating-hana-prerequisites"></a>

SAP HANA system migration requires a moderate to high-level knowledge of the source and target IT technologies and environments. We recommend that you familiarize yourself with the following information:

 AWS Cloud architecture and migration:
+  [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) 
+  [An Overview of the AWS Cloud Adoption Framework](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf) 
+  [Architecting for the Cloud: Best Practices](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf) 
+  [Migrating Your Existing Applications to the AWS Cloud](https://d1.awsstatic.com/whitepapers/cloud-migration-main.pdf) 

 AWS services:
+  [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) 
+  [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) 
+  [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) 
+  [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) 

SAP on AWS:
+  [AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html) 
+  [SAP HANA Environment Setup on AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/std-sap-hana-environment-setup.html) 