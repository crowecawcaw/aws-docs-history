# Disaster recovery for SAP workloads on AWS using AWS Elastic Disaster Recovery

Disasters due to natural events (earthquakes, hurricanes, or floods), application failures, technical failures or human actions cause application downtime and potential data loss, impacting revenue. To mitigate such scenarios, you can create a business continuity plan with the key element of disaster recovery. Designing, implementing, and maintaining a disaster recovery plan is critical for organizations running mission-critical applications, such as SAP. For more information, see [Business Continuity Plan (BCP)](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.md").

AWS Elastic Disaster Recovery enables organizations to quickly and easily implement a new or migrate an existing disaster recovery plan to AWS. The source servers can be hosted on AWS, existing physical or virtual data centers, private cloud or with other cloud providers. We recommend using Elastic Disaster Recovery to implement a disaster recovery plan for your SAP workloads, where AWS is the disaster recovery environment, and the source environment may or may not be on AWS. You can access Elastic Disaster Recovery from the [Elastic Disaster Recovery console](https://console.aws.amazon.com/drs "https://console.aws.amazon.com/drs").

An initial setup of the AWS Replication Agent is required on the source systems for Elastic Disaster Recovery to initiate secure data replication. Your data is replicated using secure protocols, either directly over the internet, or via an encrypted and/or dedicated network connection, to any AWS Region supported by Elastic Disaster Recovery. By replicating the source systems to replication servers in a staging area, the cost of disaster recovery is optimized by using affordable storage, shared servers, and minimal compute resources to maintain ongoing replication.

You can perform non-disruptive tests, known as drills, to confirm that your Elastic Disaster Recovery implementation is ready for a disaster recovery scenario. Elastic Disaster Recovery automatically converts your servers to boot and run natively on AWS when you launch instances for drills or recovery. The service also automatically creates point in time (PIT) snapshots of your server state as it replicates. If you need to recover applications, you can launch recovery instances on AWS within minutes, using the latest snapshot or an earlier PIT snapshot. Once your applications are running on AWS, you can choose to keep them there or initiate data replication back to your primary site when the issue is resolved. You can fail back to your primary site with Elastic Disaster Recovery tools, such as Failback Client.

For more information, see [What is Elastic Disaster Recovery](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md")?

###### Topics

- [Scenarios](#scenarios-overview "#scenarios-overview")
- [References](#references "#references")
- [Service-level agreements and SAP licenses](slas-licenses.md "slas-licenses.md")
- [Network, storage, and compute](key-considerations.md "key-considerations.md")
- [Disaster recovery scenarios](scenarios.md "scenarios.md")
- [Shared storage resiliency](file-systems-storage.md "file-systems-storage.md")
- [Implementing disaster recovery on AWS cloud for SAP workloads](implementation.md "implementation.md")

## Scenarios

The following disaster recovery scenarios are covered in this document.

- in-region – source workload is running on AWS cloud and disaster recovery implementation uses a second Availability Zone in the same AWS Region.
- cross-region – source workload is running on AWS cloud and disaster recovery implementation uses a different AWS Region. The choice of another Region can be for compliance reasons.
- outside of AWS – source workload is running outside of AWS (on-premises, public or private cloud) and disaster recovery is implemented with AWS.

## References

This document does not provide detailed steps for setting up and using AWS Elastic Disaster Recovery. For more information, see [What is DRSlong;?](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md") in the AWS Elastic Disaster Recovery User Guide.

It is important to understand the key business requirements that guide a disaster recovery solution design and implementation, including recovery point objectives, recovery time objectives, along with the disaster recovery plan and disaster recovery drill. Check the following resources for concepts related to a disaster recovery implementation on AWS.

- [AWS Elastic Disaster Recovery Core concepts](https://aws.amazon.com/disaster-recovery/faqs/#Core_concepts "https://aws.amazon.com/disaster-recovery/faqs/#Core_concepts")
- [AWS Well-Architected Framework : Best Practice 10.1](../../../wellarchitected/latest/sap-lens/best-practice-10-1.md "../../../wellarchitected/latest/sap-lens/best-practice-10-1.md")
- [Architecture guidance for availability and reliability of SAP on AWS](architecture-guidance-of-sap-on-aws.md "architecture-guidance-of-sap-on-aws.md")

If you are new to AWS, see the following documents.

- [Getting started with AWS](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started")
- [What is Amazon EC2?](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md")
- [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
- [Amazon Elastic Block Store (Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")

_To use this information provided here effectively, you must have previous experience installing, migrating, and operating SAP environments and systems on AWS, along with high availability and disaster recovery solution implementation._
