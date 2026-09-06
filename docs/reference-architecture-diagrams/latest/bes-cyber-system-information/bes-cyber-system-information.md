

# BES Cyber System Information on AWS
<a name="bes-cyber-system-information"></a>

Publication date: **May 18, 2022 ([Diagram history](#bcsi-history))**

With this architecture, you can build a secure extension of an Operations Technology (OT) data center into AWS. This extension supports ingestion of data from Bulk Electric System (BES) assets. The solution uses an AWS Amazon VPC for inherent security and isolation. Compute, analytics, and AI/ML services operate on a data lake to conduct contingency analysis, incident response, and advanced analytics. The architecture also demonstrates North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) compliance for BES Cyber System Information (BCSI).

## BES Cyber System Information diagram
<a name="bcsi-diagram"></a>

![Reference architecture diagram showing how to extend OT data centers into AWS securely for BCSI analytics by using Amazon VPC, Amazon EC2, SageMaker AI, and Amazon S3.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/bes-cyber-system-information/images/bes-cyber-system-information.png)


The following steps describe the security, networking, and analytics components for this architecture:

1. Connect your utility OT network (generation facilities, remote substations, data centers, and customer locations) to AWS.

1. Establish secure and highly reliable networking to AWS over VPN. For guaranteed bandwidth, use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) with IEEE 802.1AE (MACSec) encryption. (Relates to CIP 11.)

1. 3A. Manage and govern cloud resources at scale from a centralized location by using services such as [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/), [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/), and AWS Systems Manager. Log all account activity with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/). Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/) to assess all cloud configurations and any changes. (Relates to CIP 11.)

   3B. Control access with [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) and [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/). Monitor network traffic for malicious activity by using [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/). Encrypt and protect data by using [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/). (Relates to CIP 4 and CIP 11.)

1. Ingest data by using services such as [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/), [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/), [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), or [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/). Route data flows to Amazon VPC through Amazon VPC endpoints. (Relates to CIP 11.)

1. Use Amazon VPC with its inherent security and isolation for hosting compute and database resources. (Relates to CIP 11.)

   5A. Run analysis and simulations by using compute options including [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/), [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/), and [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) for containerized applications, and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/). Encrypt all compute resources with AWS KMS. (Relates to CIP 11.)

   5B. Store data securely in highly available relational databases by using [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) and [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/). Encrypt data at rest with AWS KMS. (Relates to CIP 11.)

   5C. Use AI/ML services such as [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for analysis and assessment of BCSI.

1. Create the OT data lake on [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Perform ETL and build the data catalog with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Archive data in Amazon S3 Glacier. Encrypt data by using AWS KMS. Restrict data access to the Amazon VPC by using Amazon VPC endpoints. (Relates to CIP 11.)

## Further reading
<a name="bcsi-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="bcsi-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#bcsi-history) | Reference architecture diagram first published. | May 18, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.