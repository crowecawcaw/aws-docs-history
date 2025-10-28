# SAP HANA Environment Setup on AWS

_Last updated: December 2022_

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the AWS Cloud. For the other guides in the series, ranging from overviews to advanced topics, see the [SAP on AWS Technical Documentation home page](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").

This document provides guidance on how to set up AWS resources and configure SUSE Linux Enterprise Server (SLES) and Red Hat Enterprise Linux (RHEL) operating systems to deploy SAP HANA on Amazon Elastic Compute Cloud (Amazon EC2) instances in an existing virtual private cloud (VPC). It includes instructions for configuring storage for scale-up and scale-out workloads with Amazon Elastic Block Store (Amazon EBS), Amazon Elastic File System (Amazon EFS), and Amazon FSx for NetApp ONTAP (FSx for ONTAP).

This document follows AWS best practices to ensure that your system meets all key performance indicators (KPIs) that are required for Tailored Data Center Integration (TDI)–based SAP HANA implementations on AWS. In addition, this document also follows recommendations provided by SAP, SUSE, and Red Hat for SAP HANA in the following SAP OSS Notes (requires SAP portal access).

- [1944799 - SAP HANA Guidelines for SLES Operating System Installation](https://launchpad.support.sap.com/#/notes/1944799 "https://launchpad.support.sap.com/#/notes/1944799")
- [2205917 - SAP HANA DB: Recommended OS settings for SLES 12 / SLES for SAP Applications 12](https://launchpad.support.sap.com/#/notes/2205917 "https://launchpad.support.sap.com/#/notes/2205917")
- [2684254 - SAP HANA DB: Recommended OS settings for SLES 15 / SLES for SAP Applications 15](https://launchpad.support.sap.com/#/notes/2684254 "https://launchpad.support.sap.com/#/notes/2684254")
- [2009879 - SAP HANA Guidelines for Red Hat Enterprise Linux (RHEL) Operating System](https://launchpad.support.sap.com/#/notes/2009879 "https://launchpad.support.sap.com/#/notes/2009879")
- [2292690 - SAP HANA DB: Recommended OS settings for RHEL 7](https://launchpad.support.sap.com/#/notes/2292690 "https://launchpad.support.sap.com/#/notes/2292690")
- [2777782 - SAP HANA DB: Recommended OS Settings for RHEL 8](https://launchpad.support.sap.com/#/notes/2777782 "https://launchpad.support.sap.com/#/notes/2777782")

###### Note

SAP, SUSE, and Red Hat regularly updates these OSS notes. Review the latest version of the OSS notes for up-to-date information before proceeding.

This guide is intended for users with a good understanding of AWS services, network concepts, the Linux operating system and SAP HANA administration to successfully launch and configure the resources that are required for SAP HANA.

AWS Launch Wizard for SAP is a service that guides you through the sizing, configuration and deployment of SAP HANA based applications on AWS, and follows the best practices from AWS, SAP, and operating system vendors, including SUSE and Red Hat. AWS Launch Wizard for SAP supports a wide range of deployment models, including SAP HANA database in a scale-up and scale-out mode with cross-Availability Zone high availability. AWS Launch Wizard for SAP enables you to setup your SAP HANA based systems in a few hours with minimal manual intervention. For more information, see [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md").

If your organization can’t use AWS Launch Wizard for SAP for the deployment and you require additional customization to meet internal policies, you can follow the steps in this document to manually set up AWS resources such as Amazon EC2, Amazon EBS, Amazon EFS, and FSx for ONTAP by using the AWS Command Line Interface (AWS CLI) or the AWS Management Console.

This document doesn’t provide guidance on how to set up network and security constructs such as Amazon VPC, subnets, route tables, access control lists (ACLs), NAT Gateway, AWS Identity and Access Management (IAM) roles, security groups, etc. Instead, this document focuses on configuring compute, storage, and operating system resources for SAP HANA deployment on AWS.
