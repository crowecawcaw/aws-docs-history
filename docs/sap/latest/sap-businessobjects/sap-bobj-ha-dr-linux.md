# SAP BusinessObjects BI Platform on AWS: HA/DR Guide for Linux

_SAP specialists, Amazon Web Services (AWS)_

_Last updated: January 2023_

The purpose of this guide is to provide an overview of how to configure high availability (HA) and disaster recovery (DR) for SAP BusinessObjects Business Intelligence (BI) Platform on AWS. This guide will explore how features native to AWS in combination with SAP BusinessObjects BI Platform installation and configuration techniques can greatly improve the availability of an SAP deployment. This guide is not an exhaustive list of all possible configuration options, but covers solutions common to typical deployment scenarios.

This guide isn’t intended to replace the SAP BusinessObjects BI Platform installation and administration guides, operating system documentation, or RDBMS documentation.

The procedures and examples in this guide are based on the following:

- A typical, large-scale deployment on AWS that includes two Availability Zones and three subnets in each Availability Zone. You can change this configuration to support your own requirements for SAP BusinessObjects BI Platform servers and tiers.
- An internal Application Load Balancer in front of the web servers, but you can use another internal or internet-facing load balancer.
- Amazon Relational Database Service (Amazon RDS) for MySQL as an example Central Management Server (CMS) and auditing database for SAP BusinessObjects BI Platform. However, you can use any of the [databases supported by SAP](https://support.sap.com/pam "https://support.sap.com/pam"). HA configuration instructions for other databases aren’t included in this guide; see the database-specific documentation on the SAP website.
- Amazon Elastic File System (Amazon EFS) for input and output filestores.

###### Note

You must have SAP portal access to view the SAP Notes. For more information, see the [SAP Support website](https://support.sap.com/en/my-support/knowledge-base.html "https://support.sap.com/en/my-support/knowledge-base.html").

## About this Guide

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the AWS Cloud. For the other guides in the series, ranging from overviews to advanced topics, see the [SAP on AWS Technical Documentation home page](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").
