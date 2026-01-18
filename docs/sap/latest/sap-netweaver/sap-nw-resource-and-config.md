# AWS Resource Selection and Configuration

###### Topics

- [EC2 Instance Selection](#sap-nw-resource-and-config-ec2 "#sap-nw-resource-and-config-ec2")
- [Storage Selection](#sap-nw-resource-and-config-storage "#sap-nw-resource-and-config-storage")
- [SAP Netweaver IAM Requirements](#sap-nw-resource-and-config-iam "#sap-nw-resource-and-config-iam")
- [SAP NetWeaver Security Groups](#sap-netweaver-security-groups "#sap-netweaver-security-groups")

## EC2 Instance Selection

### SAP Certified

AWS provides SAP-certified instance types that meet SAP’s performance and reliability requirements. Current generation instances offer improved price-performance ratios and enhanced networking capabilities compared to previous generations.

For SAP NetWeaver deployments, consider these certified instance families:

- Memory-optimized (R-series) - for memory-intensive SAP applications
- Compute-optimized (C-series) - for CPU-intensive workloads
- General purpose (M-series) - balanced compute, memory, and networking

Refer to the current [SAP NetWeaver supported instances](../general/sap-netweaver-aws-ec2.md "../general/sap-netweaver-aws-ec2.md") for the latest certifications and SAPS ratings.

###### Important

Use only supported operating system versions for SAP NetWeaver deployments. Avoid using OS versions that have reached End-of-Life (EOL), as OS vendors typically do not provide security patches or updates for EOL versions. Using EOL systems increases security risks and may prevent you from applying critical updates. Verify current support status with your OS vendor and SAP before deployment.

### AMI Selection

Choose appropriate Amazon Machine Images (AMIs) for your SAP deployment:

- SUSE Linux Enterprise Server (SLES)
- Red Hat Enterprise Linux (RHEL)

AWS Marketplace provides pre-configured AMIs from SUSE and Red Hat specifically optimized for SAP workloads. These images include:

- SAP-required kernel parameters and system settings
- Pre-installed SAP prerequisites and libraries
- Optimized storage and network configurations
- Regular security updates and patches

Search for:

- [SUSE Linux Enterprise Server for SAP Applications](https://aws.amazon.com/marketplace/search?prevFilters=%257B%2522category%2522%3A%2522c3bc6a75-0c3a-46ce-8fdd-498b6fd88577%2522%257D&searchTerms=SUSE+Linux+Enterprise+Server+for+SAP+Applications&sort=LAST_MODIFIED_TIME-DESCENDING "https://aws.amazon.com/marketplace/search?prevFilters=%257B%2522category%2522%3A%2522c3bc6a75-0c3a-46ce-8fdd-498b6fd88577%2522%257D&searchTerms=SUSE+Linux+Enterprise+Server+for+SAP+Applications&sort=LAST_MODIFIED_TIME-DESCENDING")
- [Red Hat Enterprise Linux for SAP with HA and Update Services](https://aws.amazon.com/marketplace/search?prevFilters=%257B%2522sort%2522%3A%2522LAST_MODIFIED_TIME-DESCENDING%2522%257D&searchTerms=Red+Hat+Enterprise+Linux+for+SAP+with+HA+and+Update+Services&sort=LAST_MODIFIED_TIME-DESCENDING "https://aws.amazon.com/marketplace/search?prevFilters=%257B%2522sort%2522%3A%2522LAST_MODIFIED_TIME-DESCENDING%2522%257D&searchTerms=Red+Hat+Enterprise+Linux+for+SAP+with+HA+and+Update+Services&sort=LAST_MODIFIED_TIME-DESCENDING")

### Instance Characteristics

Select instances based on your workload requirements:

- **Enhanced networking**: Verify and enable enhanced networking for improved network performance

```
 $ aws ec2 describe-instances --instance-ids i-1234567890abcdef0 --query 'Reservations[].Instances[].EnaSupport'
```

```
 $ aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --ena-support
```

- **EBS optimization**: Enable EBS optimization for consistent storage performance

```
 $ aws ec2 describe-instances --instance-ids i-1234567890abcdef0 --query 'Reservations[].Instances[].EbsOptimized'
```

```
 $ aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --ebs-optimized
```

- **Nitro System**: Current generation instances run on the AWS Nitro System, providing consistent performance and security

## Storage Selection

### Storage Configuration Matrix

The following table provides a reference configuration for SAP NetWeaver file systems:

| Mount Point                            | Ownership             | Local/Shared         | Type | EFS Ref       | Storage Class | Encrypted | Snapshots | Device (example) | Suggested Size (GB) |
| -------------------------------------- | --------------------- | -------------------- | ---- | ------------- | ------------- | --------- | --------- | ---------------- | ------------------- |
| **`/`**                                | root                  | Local                | EBS  | -             | gp3           | Y         | Y         | /dev/xvda1       | > 20 GB             |
| \*_`/tmp`_<br>• (1)                    | root                  | Local                | EBS  | -             | gp3           | N         | N         |                  |                     |
| **`swap`**                             | root                  | Local                | EBS  | -             | gp3           | N         | N         | /dev/xvdb        | See SAP Guidance    |
| **`/usr/sap`**                         | <sid>adm:sapsys (755) | Local                | EBS  | -             | gp3           | Y         | Y         | /dev/xvdc        | > 20 GB             |
| \*_`/usr/sap/<SID>/ASCS<nn>`_<br>• (2) | <sid>adm:sapsys (755) | Shared (SID)         | NFS  | SHARED\_<SID> | -             | Y         | N/A       | -                | -                   |
| \*_`/usr/sap/<SID>/ERS<nn>`_<br>• (2)  | <sid>adm:sapsys (755) | Shared (SID)         | NFS  | SHARED\_<SID> | -             | Y         | N/A       | -                | -                   |
| **`/sapmnt/<SID>`**                    | <sid>adm:sapsys (755) | Shared (SID)         | NFS  | SHARED\_<SID> | -             | Y         | N/A       | -                | -                   |
| **`/usr/sap/trans`**                   | <sid>adm:sapsys (755) | Shared (Landscape)   | NFS  | SHARED_TRANS  | -             | Y         | N/A       | -                | -                   |
| **`/software`**                        | root:root (755)       | Shared (Environment) | NFS  | SHARED_COMMON | -             | Y         | N/A       | -                | -                   |
| **`/interfaces`**                      | <sid>adm:sapsys (755) | Shared (Environment) | NFS  | SHARED_COMMON | -             | Y         | N/A       | -                | -                   |

Notes:

1. Consider separating /tmp from your root filesystem
2. Only required if configuring a highly available ASCS Cluster
3. For single systems, or systems entirely in a single AZ, EBS can be used for shared directories and exported from the instance where the ASCS resides.

General:

- Replace `<SID>` with your SAP System ID (e.g., PRD, DEV, QAS)
- Replace `<sid>` with lowercase system ID (e.g., prd, dev, qas)
- Replace `<nn>` with instance numbers (e.g., 00, 01, 10)
- EFS references represent logical groupings - actual EFS file system names should follow your naming conventions
- Sizes shown are minimum recommendations - adjust based on your specific requirements
- See [SAP Note 1597355 - Swap-space recommendation for Linux](https://me.sap.com/notes/1597355 "https://me.sap.com/notes/1597355")

### Local SAP Storage (EBS)

For SAP ABAP/NetWeaver applications, gp3 is the recommended storage type, providing suitable performance characteristics for most deployments. For critical workloads requiring increased durability, consider using io2 volumes. You can modify IOPS and throughput based on specific workload demands.

We recommend using XFS as your file system - a stable journaling filesystem well-suited for SAP NetWeaver workloads.

Use the following mount options:

For XFS: `noatime,nofail,logbsize=256k`
For EXT4: `noatime,nofail,nodiratime`

We suggest encrypting all local EBS volumes and backing up key volumes using snapshots on a regular basis.

### Shared SAP Storage

For SAP shared directories requiring concurrent access from multiple instances, AWS provides several NFS storage options:

- **Amazon EFS**: Serverless, fully elastic NFS storage with automatic scaling
- **Amazon FSx for NetApp ONTAP**: High-performance NFS with advanced data management features
- **Exported EBS**: EBS volumes exported via NFS from a dedicated instance (single AZ deployments)

#### Amazon EFS

Amazon EFS provides serverless, fully elastic NFS storage that scales automatically without disrupting applications. EFS supports NFSv4.1 and NFSv4.0 protocols, making it suitable for SAP shared directories that require concurrent access from multiple instances.

##### EFS Configuration for SAP

- **File System Type**: Regional (recommended) - stores data redundantly across multiple Availability Zones for high availability
- **Performance Mode**: General Purpose (default) - provides the lowest latency per operation, suitable for SAP workloads
- **Throughput Mode**: Choose based on workload patterns:
  - `Elastic`: Automatically scales 1 MiB/s to 3 GiB/s based on activity. Recommended if sharing one EFS system across multiple instances.
  - `Bursting`: 100 MiB/s minimum with burst capability. More cost-effective for periodic access patterns like SAP media storage or low usage systems.

- **Storage Classes**: Standard for frequently accessed SAP data, Infrequent Access (IA) for archival content

##### EFS Security and Encryption

- Encryption at rest: Enable during EFS creation using AWS managed keys or customer managed KMS keys
- Encryption in transit: Use the amazon-efs-utils package (efs-utils) for TLS encryption during mount operations. See [Installing the Amazon EFS client](../../../efs/latest/ug/using-amazon-efs-utils.md "../../../efs/latest/ug/using-amazon-efs-utils.md")
- Access control: Combine IAM policies, security groups, and POSIX permissions for comprehensive access management

##### EFS Creation Example

1. **Create an encrypted EFS file system with recommended settings**

```
 $ aws efs create-file-system \
--creation-token SAP-TRANS-PROD \
--backup \
--encrypted \
--performance-mode generalPurpose \
--throughput-mode elastic \
--region us-west-2 \
--tags Key=Name,Value="SAP Transport Directory" Key=Environment,Value=Production
```

Parameter Explanations:

    * `--backup`: Enables automatic daily backups with 35-day retention using AWS Backup service (recommended)
    * `--encrypted`: Enables encryption at rest using AWS managed keys (data stored on EFS is encrypted)
    * `--throughput-mode` elastic: Automatically scales throughput based on workload (consider bursting for sandbox environments or infrequently accessed filesystems like a locally available media directory)

2. **Create Mount Targets**

Create mount targets in each subnet where your SAP instances will access EFS:

```
 $ aws efs create-mount-target \
--file-system-id fs-12345678 \
--subnet-id subnet-12345678 \
--security-groups sg-12345678 \
--region us-west-2
```

3. **Retrieve File System Information**

Get the DNS name needed for mounting:

```
 $ aws efs describe-file-systems --creation-token SAP-TRANS-PROD --region us-west-2
```

4. **Allocate Directories (optional)**

Based on the storage configuration matrix, organize which directories will be hosted in which Elastic File System according to usage and connectivity, consider whether consolidating EFS file systems may reduce the cost and management overhead - for example using a single mount point for shared administrative file systems. For more critical file systems, consider the resilience and performance scope of impact.

    * SID-Specific EFS (EFS\_<SID>)




    	+ `/usr/sap/<SID>/ASCS<nn>` - ASCS instance directory (optional for HA setups)
    	+ `/usr/sap/<SID>/ERS<nn>` - ERS instance directory (optional for HA setups)
    	+ `/sapmnt/<SID>` - SAP mount directory for the specific system
    * Landscape-Wide EFS (EFS\_TRANS)




    	+ `/usr/sap/trans` - Transport directory shared across all SAP systems in the landscape
    * Environment-Wide EFS (EFS\_COMMON)




    	+ `/software` - Software distribution directory (SAP media, installation files)
    	+ `/interfaces` - Interface files and configurations

For detailed EFS creation and configuration options, refer to the [Amazon EFS User Guide](../../../efs/latest/ug/creating-using-create-fs.md "../../../efs/latest/ug/creating-using-create-fs.md").

#### Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP provides high-performance NFS storage with advanced data management capabilities. FSx for ONTAP offers:

FSx for ONTAP is particularly suitable for SAP environments requiring advanced storage features or migrating from on-premises NetApp systems. For detailed configuration guidance, refer to the [Amazon FSx for NetApp ONTAP User Guide](../../../fsx/latest/ONTAPGuide.md "../../../fsx/latest/ONTAPGuide.md").

## SAP Netweaver IAM Requirements

| Policy Area                                      | Purpose                                            | Reference                                                                                                                                                                           | Custom Policy Required           | Managed Policy                                                                    |
| ------------------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- |
| **AWS Systems Manager Access**                   | Patch management, parameter store, session manager | [Policy Documentation](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") | No                               | `AmazonSSMManagedInstanceCore`                                                    |
| **Amazon EFS Access**                            | Shared file system mounting                        | [AWS managed policies for Amazon EFS](../../../efs/latest/ug/security-iam-awsmanpol.md "../../../efs/latest/ug/security-iam-awsmanpol.md")                                          | Optional (for restricted access) | `AmazonElasticFileSystemClientFullAccess`                                         |
| **Amazon S3 Bucket Access**                      | Installation media, backups, file sync             | [AWS managed policies for Amazon S3](../../../AmazonS3/latest/userguide/security-iam-awsmanpol.md "../../../AmazonS3/latest/userguide/security-iam-awsmanpol.md")                   | Yes                              | N/A                                                                               |
| **SAP NetWeaver Pacemaker Cluster Requirements** | Instance start/stop, route table updates           | [SAP NetWeaver on AWS: high availability configuration for Netweaver (ASCS)](netweaver-ha-ascs.md "netweaver-ha-ascs.md")                                                           | Yes                              | N/A                                                                               |
| **SAP AWS Data Provider**                        | AWS Data Provider integration                      | [AWS Data Provider IAM Roles](../general/data-provider-req.md#data-provider-iam-roles "../general/data-provider-req.md#data-provider-iam-roles")                                    | Yes                              | N/A                                                                               |
| **AWS Systems Manager for SAP**                  | SAP-specific monitoring and management             | [SSM for SAP Policies](../../../ssm-sap/latest/userguide/iam-policies.md "../../../ssm-sap/latest/userguide/iam-policies.md")                                                       | No                               | `AWSSystemsManagerForSAPReadOnlyAccess` or<br>`AWSSystemsManagerForSAPFullAccess` |
| **Amazon CloudWatch**                            | Monitoring and logging                             |                                                                                                                                                                                     | No                               | `CloudWatchAgentServerPolicy`                                                     |

**Implementation Notes**

- IAM Policy Creation: [Creating IAM Policies Guide](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md")
- Best Practices: Follow the principle of least privilege when creating custom policies
- Alternative: Use [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap-setting-up.md "../../../launchwizard/latest/userguide/launch-wizard-sap-setting-up.md") for automated policy configuration

## SAP NetWeaver Security Groups

Design security groups following the principle of least privilege, allowing only necessary communication between SAP components.

Implement separate security groups for different functional tiers:

- **SAP Application Security Group**: Communication between SAP application servers and ASCS instances
- **SAP Database Security Group**: Database access restricted to authorized SAP instances only
- **SAP Web Security Group**: External access control for web-based SAP components
- **Management Security Group**: Administrative access for Systems Manager, monitoring, and backup operations

**Required ports**

For SAP application ports, refer to [TCP/IP Ports of All SAP Products](https://help.sap.com/docs/Security/575a9f0e56f34c6e8138439eefc32b16/616a3c0b1cc748238de9c0341b15c63c.html?locale=en-US&version=LATEST "https://help.sap.com/docs/Security/575a9f0e56f34c6e8138439eefc32b16/616a3c0b1cc748238de9c0341b15c63c.html?locale=en-US&version=LATEST") and filter on Product Name `Application Server ABAP`.

Administrative ports:

- Port 2049: NFS for Amazon EFS access
- Port 22: SSH access (consider restricting to AWS Systems Manager Session Manager)

**Security group best practices**

- Reference other security groups rather than IP ranges where possible
- Use descriptive names and descriptions for operational clarity
- Implement separate security groups for different tiers (application, database, web)
- Regularly review and audit security group rules
