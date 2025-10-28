# Microsoft SQL Server for SAP NetWeaver on AWS Deployment and Operations Guide

_SAP specialists, Amazon Web Services_

_[Last updated](document-revisions-sap-sql.md#document-revisions-sap-sql.title "document-revisions-sap-sql.md#document-revisions-sap-sql.title"): December 2020_

This guide provides guidance on how to set up AWS resources and the Microsoft Windows Server operating system to deploy Microsoft SQL Server for SAP NetWeaver on Amazon EC2 instances.

This guide is for users who are responsible for planning, architecting, and deploying SQL Server on AWS for SAP NetWeaver based applications. You should have a good understanding of AWS services, general networking concepts, Windows Server operating systems, and SQL Server administration.

## Overview

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the Amazon Web Services Cloud. For the other guides in the series, ranging from overviews to advanced topics, see [SAP on AWS Technical Documentation home page](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").

This guide provides guidance on how to set up AWS resources and the Microsoft Windows Server operating system to deploy Microsoft SQL Server for SAP NetWeaver on Amazon EC2 instances.

Instructions in this document are based on recommendations provided by SAP and Microsoft for SQL Server deployment on Windows via the below SAP notes or KB articles:

| Table 1 - SAP NetWeaver on Windows OSS Notes | SAP OSS Note                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1656099                                      | SAP Applications on AWS: Supported DB/OS and Amazon EC2 products |
| 1409608                                      | Virtualization on Windows                                        |
| 1732161                                      | SAP Systems on Windows Server 2012 (R2)                          |
| 2384179                                      | SAP Systems on Windows Server 2016                               |
| 2751450                                      | SAP Systems on Windows Server 2019                               |
| 1564275                                      | Install SAP Systems Using Virtual Host Names on Windows          |
| 1772688                                      | SQL Server AlwaysOn and SAP applications                         | In addition, this document also follows best practices from AWS, Microsoft, and SAP for SAP NetWeaver deployments on Windows. This guide is for users who are responsible for planning, architecting, and deploying SQL Server on AWS for SAP NetWeaver based applications. You should have a good understanding of AWS services, general networking concepts, Windows Server operating systems, and SQL Server administration. This document doesn’t provide guidance on how to set up network and security constructs like Amazon Virtual Private Cloud (Amazon VPC), subnets, route tables, ACLs, NAT Gateway, IAM Roles, AWS Security Groups, and so on. This document focuses on configuring and maintaining compute, storage, and operating system for Microsoft SQL Server for SAP NetWeaver based applications. |
