# Introduction

This guide provides best practices for operating SAP HANA systems that have been deployed on AWS. This guide is not intended to replace any of the standard SAP documentation. See the following SAP guides and notes:

- [SAP Library (help.sap.com) - SAP HANA Administration Guide](https://help.sap.com/hana/SAP_HANA_Administration_Guide_en.pdf "https://help.sap.com/hana/SAP_HANA_Administration_Guide_en.pdf")
- [SAP installation guides](https://service.sap.com/instguides "https://service.sap.com/instguides") (SAP portal access required)
- [SAP notes](https://service.sap.com/notes "https://service.sap.com/notes") (SAP portal access required)
  This guide assumes that you have a basic knowledge of AWS. If you are new to AWS, see the following on the AWS website before continuing:

- [AWS Getting Started Resource Center](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/")
- [What is Amazon EC2?](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md")
  In addition, see the following SAP on AWS guides:

- [https://d0.awsstatic.com/enterprise-marketing/SAP/SAP_on\_](https://d0.awsstatic.com/enterprise-marketing/SAP/SAP_on_ "https://d0.awsstatic.com/enterprise-marketing/SAP/SAP_on_")
  AWS_Implementation_Guide.pdf[SAP on AWS Implementation and Operations Guide] provides best practices for achieving optimal performance, availability, and reliability, and lower total cost of ownership (TCO) while running SAP solutions on AWS.
- [https://d0.awsstatic.com/enterprise-marketing/SAP/SAP_on\_](https://d0.awsstatic.com/enterprise-marketing/SAP/SAP_on_ "https://d0.awsstatic.com/enterprise-marketing/SAP/SAP_on_")
  AWS_High_Availability_Guide_v3.2.pdf[SAP on AWS High Availability Guide] explains how to configure SAP systems on Amazon Elastic Compute Cloud (Amazon EC2) to protect your application from various single points of failure.
- [SAP on AWS Backup and Recovery Guide](https://d0.awsstatic.com/enterprise-marketing/SAP/sap-hana-on-aws-high-availability-disaster-recovery-guide.pdf "https://d0.awsstatic.com/enterprise-marketing/SAP/sap-hana-on-aws-high-availability-disaster-recovery-guide.pdf") explains how to back up SAP systems running on AWS, in contrast to backing up SAP systems on traditional infrastructure.
