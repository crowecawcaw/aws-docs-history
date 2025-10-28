# Migrating Workloads: Prerequisites for Linux and Windows

Before ingesting a copy of an on-premises instance into AWS Managed Services (AMS), certain prerequisites must be met.
These are the prerequisites, including those that differ between Windows and Linux operating systems.

###### Note

To simplify the process of determining if the instances are ready for ingestion, validation
tools for both Windows and Linux have been created. These tools can be downloaded and run
directly on your on-premises servers as well as EC2 instances in AWS.
[Linux Pre-WIGS Validation.zip](samples/linux-prewigs-validation.md "samples/linux-prewigs-validation.md"),
[Windows Pre-WIGS Validation.zip](samples/windows-prewigs-validation.md "samples/windows-prewigs-validation.md").

BEFORE YOU BEGIN, for Linux and Windows:

- Perform a full virus scan.
- The instance must have the `customer-mc-ec2-instance-profile` instance profile.
- Install the [Amazon EC2 Systems Manager (SSM) Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") and make sure that the SSM Agent is up and running.
- A minimum of 10GB of free disk space on the root volume is recommended to run AMS workload ingest (WIGS).
  Operationally, AMS recommends disk utilization less than 75% and alerts when disk utilization reaches 85%.
- Determine a time frame for the ingestion with your migration partner.
- The custom AMI exists as an EC2 instance in the target production AMS account (this is the migration partner's responsibility).

###### Important

The operating system must be supported by AMS workload ingest.

- The following operating systems are supported:
  - Microsoft Windows Server: 2008 R2, 2012, 2012 R2, 2016, 2019 and 2022
  - Linux: Amazon Linux 2023, Amazon Linux 2, and Amazon Linux, CentOS 7.x, CentOS 6.5-6.10, Oracle Linux 7: minor versions 7.5 and above,
    Oracle Linux 8: minor versions up to 8.3, RHEL 8.x, RHEL 7.x, RHEL 6.5-6.10, SUSE Linux Enterprise Server 15 SP3, SP4, and SAP specific versions,
    SUSE Linux Enterprise Server 12 SP5, Ubuntu 18.04

- The following AMIs are not supported:
  - Amazon Linux 2023 Minimal AMI.

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.
