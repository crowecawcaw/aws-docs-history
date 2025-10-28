# Architecture guidance for availability and reliability of SAP on AWS

August 2021

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the Amazon Web Services (AWS) Cloud. For more information, see [SAP on AWS Technical Documentation](https://aws.amazon.com/sap/docs/ "https://aws.amazon.com/sap/docs/").

## Overview

This guide provides a set of architecture guidelines, strategies, and decisions for deploying SAP NetWeaver-based systems with a highly available and reliable configuration on AWS.

In this guide we cover:

- Introduction to SAP high availability and reliability
- Architecture guidelines and decision consideration
- Architecture patterns and recommended usage

This guide is intended for users who have previous experience designing high availability and disaster recovery (HADR) architectures for SAP.

This guide does not cover the business requirements determining the need for HADR and/or the implementation details for a specific partner or customer solution.

## Prerequisites

### Specialized knowledge

Before following the configuration instructions in this guide, we recommend familiarizing yourself with the following AWS services. (If you are new to AWS, see [Getting Started with AWS](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started").)

- [Amazon EC2](https://aws.amazon.com/ec2 "https://aws.amazon.com/ec2")
- [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")
- [Amazon VPC](https://aws.amazon.com/vpc "https://aws.amazon.com/vpc")
- [Amazon EFS](https://aws.amazon.com/efs "https://aws.amazon.com/efs")
- [Amazon S3](https://aws.amazon.com/s3 "https://aws.amazon.com/s3")

### Recommended reading

Before reading this document, we recommend understanding key concepts and best practices from these guides:

- [SAP on AWS Overview and Planning](sap-on-aws-overview.md "sap-on-aws-overview.md")
- [Getting Started with Architecting SAP on the AWS Cloud](https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud "https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud")
