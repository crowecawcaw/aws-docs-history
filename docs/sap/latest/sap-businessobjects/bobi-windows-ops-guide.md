# SAP BusinessObjects Business Intelligence Platform on AWS Deployment and Operations Guide for Windows

_SAP specialists, Amazon Web Services_

_[Last updated](bobi-windows-document-revisions.md#bobi-windows-document-revisions.title "bobi-windows-document-revisions.md#bobi-windows-document-revisions.title"): January 2023_

The purpose of this guide is to provide an overview of how to implement and operate SAP BusinessObjects (BO) Business Intelligence (BI) Platform (also referred in this document as SAP BOBI Platform) on Amazon Elastic Compute Cloud (Amazon EC2). This guide covers common AWS services and features that are relevant for SAP BusinessObjects BI platform. This guide is not an exhaustive list of all possible configuration options. It covers solutions common to typical deployment scenarios.

This guide is not intended to replace the standard SAP BOBI Platform installation and administration guides, operating system, or relational database management system (RDBMS) documentation.

## Overview

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the Amazon Web Services Cloud. For the other guides in the series, ranging from overviews to advanced topics, see [SAP on AWS Technical Documentation](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").

The purpose of this guide is to provide an overview of how to implement and operate SAP BusinessObjects (BO) Business Intelligence (BI) Platform (also referred in this document as SAP BOBI Platform) on Amazon Elastic Compute Cloud (Amazon EC2). This guide covers common AWS services and features that are relevant for SAP BusinessObjects BI platform. This guide is not an exhaustive list of all possible configuration options. It covers solutions common to typical deployment scenarios.

This guide is not intended to replace the standard SAP BOBI Platform installation and administration guides, operating system, or relational database management system (RDBMS) documentation.

## General AWS Knowledge

Before you follow the configuration instructions in this guide, we recommend that you become familiar with the following AWS services. (If you are new to AWS, see [Getting Started with AWS](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/").)

- [Amazon EC2](https://aws.amazon.com/documentation/ec2/ "https://aws.amazon.com/documentation/ec2/")
- [Amazon VPC](https://aws.amazon.com/documentation/vpc/ "https://aws.amazon.com/documentation/vpc/")
- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS CloudFormation](https://aws.amazon.com/documentation/cloudformation/ "https://aws.amazon.com/documentation/cloudformation/")
