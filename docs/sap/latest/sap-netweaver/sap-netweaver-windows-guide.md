# SAP NetWeaver on AWS Deployment and Operations Guide for Windows

_SAP specialists, Amazon Web Services_

_Last updated: November 2022_

This guide provides guidance on how to set up AWS resources and the Microsoft Windows Server operating system to deploy SAP NetWeaver on Amazon EC2 instances.

This guide is intended for SAP architects, SAP engineers, IT architects, and IT administrators who want to deploy SAP NetWeaver on AWS.

## About this Guide

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the AWS Cloud. For the other guides in the series, ranging from overviews to advanced topics, see the [SAP on AWS Technical Documentation home page](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").

This guide is for users who are responsible for planning, architecting, and deploying SAP NetWeaver on AWS. You should have a good understanding of AWS services, general networking concepts, Windows Server operating systems, and SAP NetWeaver administration. This document guides you through the steps required to successfully launch and configure the resources required for SAP NetWeaver on Windows.

Instructions in this document are based on the recommendations provided by SAP and Microsoft for SAP NetWeaver on Windows as described in the following OSS notes:

| SAP NetWeaver on Windows OSS Notes | SAP OSS Note                                                     | Description |
| ---------------------------------- | ---------------------------------------------------------------- | ----------- |
| 1656099                            | SAP Applications on AWS: Supported DB/OS and Amazon EC2 products |
| 1409608                            | Virtualization on Windows                                        |
| 1732161                            | SAP Systems on Windows Server 2012 (R2)                          |
| 2384179                            | SAP Systems on Windows Server 2016                               |
| 2751450                            | SAP Systems on Windows Server 2019                               |
| 1564275                            | Install SAP Systems Using Virtual Host Names on Windows          |
| 3143497                            | SAP Systems on Windows Server 2022                               |

In addition, this document also follows best practices from AWS, Microsoft, and SAP for SAP NetWeaver deployments on Windows. See the recommended reading section for more details.

This document doesn’t provide guidance on how to set up network and security constructs, such as Amazon Virtual Private Cloud (Amazon VPC), subnets, route tables, ACLs, NAT Gateway, AWS Identity and Access Management (IAM) roles, and AWS Security Groups. Instead, it focuses on how to configure and maintain the compute, storage, and operating system constructs for SAP NetWeaver deployment and operation on Windows on AWS.

SAP NetWeaver is also available to deploy on Linux. If you’re considering using Linux, see the [SAP NetWeaver Quick Start](https://aws.amazon.com/quickstart/architecture/sap-netweaver-abap/ "https://aws.amazon.com/quickstart/architecture/sap-netweaver-abap/") for Linux.
