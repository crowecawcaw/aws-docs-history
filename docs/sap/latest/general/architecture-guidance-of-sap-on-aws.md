

# Architecture guidance for availability and reliability of SAP on AWS
<a name="architecture-guidance-of-sap-on-aws"></a>

August 2021

This guide is part of a content series that provides detailed information about hosting, configuring, and using SAP technologies in the Amazon Web Services (AWS) Cloud. For more information, see [SAP on AWS Technical Documentation](https://aws.amazon.com/sap/docs/).

## Overview
<a name="arch-guide-overview"></a>

This guide provides a set of architecture guidelines, strategies, and decisions for deploying SAP NetWeaver-based systems with a highly available and reliable configuration on AWS.

In this guide we cover:
+ Introduction to SAP high availability and reliability
+ Architecture guidelines and decision consideration
+ Architecture patterns and recommended usage

This guide is intended for users who have previous experience designing high availability and disaster recovery (HADR) architectures for SAP.

This guide does not cover the business requirements determining the need for HADR and/or the implementation details for a specific partner or customer solution.

## Prerequisites
<a name="arch-guide-prerequisites"></a>

### Specialized knowledge
<a name="arch-guide-specialized-knowledge"></a>

Before following the configuration instructions in this guide, we recommend familiarizing yourself with the following AWS services. (If you are new to AWS, see [Getting Started with AWS](https://aws.amazon.com/getting-started).)
+  [Amazon EC2](https://aws.amazon.com/ec2) 
+  [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) 
+  [Amazon VPC](https://aws.amazon.com/vpc) 
+  [Amazon EFS](https://aws.amazon.com/efs) 
+  [Amazon S3](https://aws.amazon.com/s3) 

### Recommended reading
<a name="arch-guide-recommended-reading"></a>

Before reading this document, we recommend understanding key concepts and best practices from these guides:
+  [SAP on AWS Overview and Planning](https://docs.aws.amazon.com/sap/latest/general/sap-on-aws-overview.html) 
+  [Getting Started with Architecting SAP on the AWS Cloud](https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud) 