# Guidance for Deploying Cross-Region Disaster Recovery with AWS Elastic Disaster Recovery

This user guide provides prescriptive instructions to deploy AWS Elastic Disaster Recovery for AWS customers who are looking to protect applications that currently operate within an Amazon Web Services (AWS) Region and choose to recover to another Region for disaster recovery. This guide serves to complement the publicly available [Elastic Disaster Recovery](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md") documentation, available on the [AWS documentation library](../../../index.md "../../../index.md"). It introduces important concepts, provides specific guidance on configuration of Elastic Disaster Recovery for a cross-Region need, and step-by-step instructions on how to design, deploy, and manage Elastic Disaster Recovery.

By following this guide, you will be able to:

- Familiarize yourself with the concepts of Elastic Disaster Recovery
- Learn how to think about your overall disaster recovery design, and where Elastic Disaster Recovery fits
- Deploy Elastic Disaster Recovery to protect applications across AWS Regions
- Recover source servers to a different AWS Region using best practices
- Learn how to think about your Elastic Disaster Recovery testing process
- Understand how to recover your servers during a disaster
- Understand how to failback your servers after you have alleviated the disaster in your source Availability Zone (AZ)
- If needed: properly clean-up and remove servers from Elastic Disaster Recovery

## What is AWS Elastic Disaster Recovery?

Elastic Disaster Recovery minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications running on Amazon Elastic Compute Cloud (EC2) and Amazon Elastic Block Store (EBS) using affordable storage, minimal compute, and point-in-time recovery. Elastic Disaster Recovery continuously replicates source servers to your
recovery target within AWS, allowing you to prepare your environment to recover within minutes from unexpected infrastructure or application outages, human error, data corruption, ransomware, or other disruptions.

Elastic Disaster Recovery provides a unified process to test, recover, and fail back any application running on a supported Operating Systems (OS). Elastic Disaster Recovery supports large, heterogeneous environments with mission-critical workloads, and can support recovery point objectives (RPO) of seconds, with recovery time objectives (RTO) of minutes, reducing overall disaster recovery costs.
