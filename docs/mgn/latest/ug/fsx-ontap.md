

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# FSx for ONTAP configuration
<a name="fsx-ontap"></a>

## Overview
<a name="fsx-ontap-overview"></a>

This page provides step-by-step instructions for configuring Amazon FSx for NetApp ONTAP (FSx for ONTAP) as a storage migration target for AWS Transform MGN (MGN) when migrating to AWS. With this setup, you can use the enterprise file storage capabilities of FSx for ONTAP for your migrated workloads. This page assumes that you are familiar with FSx for ONTAP. For detailed FSx for ONTAP setup instructions, see the [FSx for ONTAP Getting Started Guide](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/getting-started.html).

FSx for ONTAP as a target storage type is available in all AWS Regions where both MGN and FSx for ONTAP are available. This storage type is not available in Local Zones. For supported regions, see [MGN supported regions](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html#supported-regions) and [FSx for ONTAP availability by Region](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/available-aws-regions.html).

**Important**  
Do not rename or modify MGN-managed FSx for ONTAP resources (LUNs, igroups, snapshots). Changes to these resources disrupt migration and require restarting the migration from the beginning.

### Known limitations
<a name="fsx-ontap-known-limitations"></a>
+ **FSx for ONTAP backups can block volume cleanup**. FSx for ONTAP file systems have automatic backups enabled by default. Backups taken on target volumes can prevent MGN from deleting replication volumes on Finalize cutover/Disconnect from service migration stage. See [Troubleshooting replication volume not deleted after Finalize cutover](fsx-ontap-troubleshooting.md#fsx-flexclone-split-blocked).
+ **Multiple LUNs per volume**. MGN creates one volume per source server on the FSx for ONTAP file system and places each disk as a separate LUN within that volume. For example, a source server with 3 disks results in one volume with 3 LUNs. The ONTAP best practice is a 1:1 relationship (one volume per LUN), which allows per-volume features such as snapshots, tiering policies, and storage efficiency to be configured independently per disk. As a workaround, you can use the ONTAP [`lun move start`](https://docs.netapp.com/us-en/ontap-cli/lun-move-start.html) command to relocate LUNs into dedicated volumes after migration. This operation is non-disruptive and does not require iSCSI reconfiguration on the host.
+ **Agent-based replication only**. MGN supports FSx for ONTAP as a target storage type only with agent-based replication.
+ **Up to 5 file systems per account**. MGN supports migrating data into up to 5 FSx for ONTAP file systems concurrently per account. If you have more file systems, migrate in phases. For more information about FSx for ONTAP quotas, see [FSx for ONTAP quotas](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limits.html). For MGN service quotas, see [MGN endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mgn.html).
+ **igroup limits per file system**. MGN creates one igroup per source server during replication and one per target instance at launch. FSx for ONTAP supports up to 256 igroups (Single-AZ) or 512 igroups (Multi-AZ). Plan the number of source servers per file system accordingly.
+ **ONTAP configurations not migrated**. If you are migrating from an existing ONTAP storage system, source ONTAP configurations (such as access permissions, quotas, snapshot policies, and schedules) are not migrated automatically. You must reconfigure these settings on the target FSx for ONTAP file system after migration.
+ **No mixed storage per server**. All data volumes from a source server use the same storage type (either Amazon EBS or FSx for ONTAP). You cannot mix storage types for different disks on the same server. The boot volume is always stored on Amazon EBS.

## Prerequisites
<a name="fsx-ontap-prerequisites"></a>

Before integrating FSx for ONTAP with MGN, ensure the following:
+ **MGN Setup**: MGN initialized in your AWS account with agent-based replication.
**Important**  
If you initialized MGN before FSx for ONTAP support was available, you must reinitialize the service to create the required AWS managed roles. In the MGN console, navigate to **Settings → Replication template** and choose **Reinitialize Service Permissions**. For details on these roles and their managed policies, see [AWS Transform MGN managed policies](security-iam-awsmanpol.md).
+ **VPC Configuration**: FSx for ONTAP and MGN instances must be in the same AWS account and Region. They can use the same VPC or different VPCs in which both the source and target are routable. IPv4 connectivity is required. As a best practice, use a Multi-AZ FSx for ONTAP file system when your applications require resiliency across Availability Zones. Deploy your target EC2 instances in the same AZ as the file system's preferred file server to minimize latency. If your applications do not require cross-AZ resiliency, you can use a Single-AZ FSx for ONTAP file system. Deploy your target EC2 instances in the same AZ as the file system to minimize latencies and avoid cross-AZ data transfer charges.
+ **OS package repository access**: MGN automatically installs iSCSI initiator and multipath packages on replication servers and launched instances. Ensure that both the staging area subnet and the launch subnet have outbound access to OS package repositories (for example, through a NAT gateway or internet gateway). For the full list of required URLs, see [Network requirements for FSx for ONTAP](preparing-environments.md#fsx-ontap-network-requirements).

## Step 1: Configure security groups
<a name="fsx-ontap-step1-security-groups"></a>

To enable MGN to work with FSx for ONTAP, you must create two security groups that cross-reference each other:
+ **MGN-Instances-SG**. Attached to the EC2 instances that MGN launches (test and cutover).
+ **FSx-ONTAP-SG**. Attached to the FSx for ONTAP file system. Controls inbound traffic from MGN-launched instances.

Because `FSx-ONTAP-SG` references `MGN-Instances-SG` as the source in its inbound rules, only MGN-launched instances can reach the file system. All other traffic is denied by default.

### 1.1 MGN instances security group
<a name="fsx-ontap-mgn-instances-sg"></a>

Create this security group in the VPC where MGN will launch target instances.

**Important**  
If you use different VPCs for replication and launch, create two security groups with distinct names for clarity. For example, use `MGN-Replication-SG` (in the staging VPC) and `MGN-Launch-SG` (in the launch VPC).

**Steps to create**

1. Navigate to the **Amazon VPC Console → Security Groups → Create security group**.

1. Configure the following settings:
   + Security group name: `MGN-Instances-SG`
   + Description: `Security group for instances launched by MGN to allow communication with FSx for ONTAP`
   + VPC: Choose the target VPC where MGN will launch instances.

1. **Inbound Rules:** The only required inbound rule is port 1500 for MGN data replication from source servers. You can optionally add rules for administrative access to your instances (for example, SSH on port 22 or RDP on port 3389 from your corporate network).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/fsx-ontap.html)

1. **Outbound Rules:** The default outbound rule (All traffic → 0.0.0.0/0) is sufficient. If you restrict outbound rules, add at minimum the following rules. Reference the FSx for ONTAP security group (created in the next step) as the destination:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/fsx-ontap.html)

1. Choose **Create security group**.

### 1.2 FSx for ONTAP security group
<a name="fsx-ontap-fsx-sg"></a>

You associate this security group with the FSx for ONTAP file system. Use this security group to control which resources can communicate with the file system and to ensure that MGN-launched instances have the necessary access.

**Steps to create**

1. Navigate to the **Amazon VPC Console → Security Groups → Create security group**.

1. Configure the following settings:
   + Security group name: `FSx-ONTAP-SG`
   + Description: `Security group for FSx for ONTAP file system to allow inbound access from MGN-launched instances`
   + VPC: Choose the target VPC used for the FSx for ONTAP file system.

1. **Inbound Rules:** Add the following rules. The table is organized into two groups:
   + **Migration traffic (iSCSI)**. Required for MGN data replication and launch. Reference `MGN-Instances-SG` as the source.
   + **Management access (SSH, HTTPS)**. Optional rules for ONTAP CLI and REST API access from MGN-launched instances (for example, for troubleshooting or manual configuration). Reference `MGN-Instances-SG` as the source.
   + **MGN service traffic (HTTPS)**. Required for MGN to access the FSx for ONTAP REST API during replication and launch. Use the CIDR blocks of the preferred and standby subnets where the file system is deployed. You can find these CIDRs in the **FSx for ONTAP Console** under your file system's **Network & security** tab, or in the **VPC Console → Subnets** by looking up the subnet IDs. You can narrow this scope after the initial setup is complete.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/fsx-ontap.html)

1. **Outbound Rules:** The default outbound rule (All traffic → 0.0.0.0/0) is sufficient.

1. Choose **Create security group**.

## Step 2: Create FSx for ONTAP file system
<a name="fsx-ontap-step2-create-filesystem"></a>

MGN can work with an existing FSx for ONTAP file system or a new one. If you do not already have an FSx for ONTAP file system, create one in the same AWS account and Region where MGN will launch target instances.

### High-level steps
<a name="fsx-ontap-create-high-level"></a>

1. Navigate to the Amazon FSx for NetApp ONTAP Console and create a new FSx for ONTAP file system.

1. Choose **Standard create** option.

1. Choose deployment type (Multi-AZ or Single-AZ).

1. Configure storage capacity and throughput based on your workload requirements.

1. Choose the VPC and subnets for FSx for ONTAP deployment.

1. Choose `FSx-ONTAP-SG` security group created in [1.2 FSx for ONTAP security group](#fsx-ontap-fsx-sg).

1. Configure FSx for ONTAP admin account and password.

1. Configure a Storage Virtual Machine (SVM).

1. Wait for the file system to reach **Available** status (approximately 30-45 minutes).

**Important for MGN integration**  
**For Multi-AZ deployments**: you must specify an Endpoint IPv4 address range (not unallocated or floating) that is outside your VPC CIDR. Use the "Enter an IPv4 address range" option and provide a specific range within RFC 1918 private address space (for example, `192.168.1.0/24`). This is required for MGN integration to ensure consistent endpoint addressing.
**Storage capacity**: MGN uses FSx for ONTAP storage for replication, conversion, and cutover. These processes require temporary storage on the file system. Ensure that sufficient space is available on the FSx for ONTAP file system and increase capacity if needed. As a guideline, provision 3x the size of the planned migration data. The 3x factor accounts for three concurrent storage consumers during migration: the replicated data, the converted volumes used for launch, and the original volumes pending deletion. Volume deletion in FSx for ONTAP is a background operation, so freed capacity is not available immediately after deletion, so headroom must be provisioned upfront. As a best practice, keep the file system at or below 80% SSD capacity utilization throughout the migration. For second-generation file systems ([Single-AZ 2 and Multi-AZ 2](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html) deployment types), you can decrease storage capacity after migration is complete. For more information, see [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html).
**Throughput capacity**: Higher throughput capacity reduces migration time. Throughput is selected from supported values and is a billable dimension. To size throughput for migration, sum the average read throughput and write throughput across all source servers being migrated to the file system, add 15% headroom, and round up to the next supported value. Plan your throughput capacity before starting migration, as changes take time to take effect. You can reduce throughput after migration is complete. For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html) and [FSx for ONTAP performance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html).

**Disable Autonomous Ransomware Protection (ARP)**  
If ONTAP ARP is enabled on the file system, disable it before migration. ARP can prevent MGN from deleting replication volumes on Finalize cutover/Disconnect from service migration stage. For more information, see [Enabling Autonomous Ransomware Protection](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/enable-ARP.html).

For detailed instructions on creating and configuring FSx for ONTAP file systems, see [Creating FSx for ONTAP file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html).

## Step 3: Configure certificate-based authentication
<a name="fsx-ontap-step3-certificate-auth"></a>

**Certificate-based authentication is required for MGN to access the ONTAP REST API and iSCSI targets.** MGN handles TLS validation internally using AWS Certificate Authorities.

**Note**  
MGN does not use CHAP for iSCSI. iSCSI access is controlled via security groups, and MGN authenticates to the ONTAP management API using client certificates as described in this section.

### Create client certificate for API authentication
<a name="fsx-ontap-create-client-cert"></a>

Generate a client certificate that FSx for ONTAP will require and MGN will use to authenticate to the ONTAP REST API. You have several options:


**Certificate options**  

| Option | Use Case | Documentation | 
| --- | --- | --- | 
| Self-Signed Certificate | Testing/Development | [Generating a self-signed certificate for FSx for ONTAP](fsx-ontap-generate-certs.md) | 
| AWS Private Certificate Authority | Production (Recommended) | [AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) | 
| External Certificate Authority | Production (Enterprise PKI) | Use your organization's CA process | 

**Note**  
The private key must be in PKCS\#8 format (`-----BEGIN PRIVATE KEY-----`). If your key starts with `-----BEGIN RSA PRIVATE KEY-----` (PKCS\#1), convert it:  

```
[~]$ openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
  -in fsx-mgn-client.key -out fsx-mgn-client.key
```

### Install client certificate on FSx for ONTAP
<a name="fsx-ontap-install-cert"></a>

Install the client certificate on the FSx for ONTAP to enable certificate-based authentication. In the following commands, replace {{vserver\_name}} with your file system ID (e.g., `FsxId08f0e724d292c729c`). You can find this in the FSx for ONTAP console under your file system's details.

1. Connect to the file system's management endpoint. Log in to an EC2 instance in the same VPC as the FSx for ONTAP file system, then use the `fsxadmin` user to SSH into the file system's management endpoint IP address or DNS name:

   ```
   [~]$ ssh fsxadmin@{{file-system-management-endpoint-ip-address}}
   ```

   For more information, see [Managing file systems with the ONTAP CLI](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html#fsxadmin-ontap-cli).

1. Install the client CA certificate:

   ```
   FsxId0123456::> security certificate install -type client-ca \
     -vserver {{vserver_name}} -cert-name my-client-ca
   
   # Paste the contents of ca.crt when prompted
   # Press Enter when done
   ```

   Verify the certificate was installed:

   ```
   FsxId0123456::> security certificate show -vserver {{vserver_name}} -type client-ca
   ```

1. Create the user with certificate authentication. For more information, see [Creating ONTAP users](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-new-ontap-users.html).

   ```
   FsxId0123456::> security login create -vserver {{vserver_name}} \
     -user-or-group-name cert_usr -application http \
     -authentication-method cert -role fsxadmin
   ```

   Verify the login was created:

   ```
   FsxId0123456::> security login show -vserver {{vserver_name}} \
     -user-or-group-name cert_usr
   ```

### Test certificate-based authentication
<a name="fsx-ontap-test-cert"></a>

Log in to an EC2 instance in the same VPC as the FSx for ONTAP file system, then run the following command to test certificate authentication:

Download the FSx for ONTAP certificate bundle (change the region in the URL):

```
[~]$ curl https://fsx-aws-certificates.s3.amazonaws.com/bundle-{{region}}.pem \
  -o bundle-{{region}}.pem
```

Test authentication using the certificate:

```
[~]$ curl -sS --cacert bundle-{{region}}.pem \
     --cert fsx-mgn-client.crt \
     --key fsx-mgn-client.key \
     https://management.{{fs-xxxxx}}.fsx.{{region}}.amazonaws.com/api/cluster
```

**Expected:** JSON response with cluster information. If you see 401 Unauthorized, verify certificate installation and login creation.

## Step 4: Store certificates in AWS Secrets Manager
<a name="fsx-ontap-step4-store-certs"></a>

Store the client certificate and private key in AWS Secrets Manager (Secrets Manager). MGN will retrieve these credentials using the Secret ARN.

**Required secret format:**

MGN expects the secret to contain exactly two keys:
+ `cert`: The client certificate content (`fsx-mgn-client.crt`)
+ `key`: The private key content (`fsx-mgn-client.key`)

**Store using AWS Console:**

1. Navigate to **Secrets Manager** in the AWS Console.

1. Choose **Store a new secret**.

1. Choose **Other type of secret**.

1. Add key-value pairs with exact key names as key/value (not plain text):
   + `cert` – content of your `fsx-mgn-client.crt`
   + `key` – content of your `fsx-mgn-client.key`

1. Choose **Next**.

1. On the **Configure secret** page, under **Tags**, add a tag with key `AWSApplicationMigrationServiceManaged` and value `True`.

1. Choose **Next** → **Store**.

1. **Copy the Secret ARN**. You need this for MGN configuration.

**Important**  
Use `cert` (not `certificate`).
Use `key` (not `private_key`).
Do NOT include a `username` field.

**Example Secret ARN:**

```
arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:mgn/fsx/ontap-api-certificate-{{AbCdEf}}
```

## Step 5: Configure MGN replication settings
<a name="fsx-ontap-step5-mgn-replication"></a>

Configure MGN to use the FSx for ONTAP REST API certificate stored in Secrets Manager.

### Configure replication template by using the AWS Console
<a name="fsx-ontap-replication-template"></a>

**Important**  
Changing the storage provider for a source server that is already replicating terminates current replication and restarts the replication process from the beginning.

1. Navigate to **MGN** console.

1. Under **Settings**, choose **Replication template**.

1. Choose **Edit**.

1. Choose the required target subnet (subnet that can communicate with FSx for ONTAP and has outbound access to OS package repositories).

1. Choose **FSx for ONTAP configuration**.

1. Enter the following configuration:
   + Choose **AWS FSx for ONTAP** as a default storage type.
   + **Storage Virtual Machine (SVM) ID**: choose from the list.
   + **FSx Storage Secret ARN**: enter the Secret ARN you copied in [Step 4: Store certificates in AWS Secrets Manager](#fsx-ontap-step4-store-certs).

1. Choose the `MGN-Instances-SG` security group (created in [1.1 MGN instances security group](#fsx-ontap-mgn-instances-sg)) to allow iSCSI traffic to FSx for ONTAP.

1. Choose **Save changes**.

**Note**  
Migration Acceleration Program (MAP) 2.0 tags are applied to the FSx for ONTAP file system but not to individual FSx for ONTAP volumes.

## Step 6: Configure launch template and launch settings
<a name="fsx-ontap-step6-launch-settings"></a>

The target instance must establish iSCSI connectivity to the FSx for ONTAP SVM over the network.

**Requirements:**
+ Choose the required target subnet. This subnet must have network connectivity to the FSx for ONTAP file system (ports 3260 and 443) and outbound access to OS package repositories. For connectivity details, see [Network requirements for FSx for ONTAP](preparing-environments.md#fsx-ontap-network-requirements).
+ Modify the source server's launch template to include the `MGN-Instances-SG` security group (see [Step 1: Configure security groups](#fsx-ontap-step1-security-groups)).

## Step 7: Enable volume integrity validation (recommended)
<a name="fsx-ontap-step7-post-launch-validation"></a>

Enable the [Volume integrity validation](predefined-post-launch-actions.md#predefined-volume-integrity-validation) post-launch action to automatically verify iSCSI connectivity and multipath mount configuration after each test or cutover launch. For FSx for ONTAP migrations, this action validates that all expected iSCSI volumes are connected, mounted, and accessible through multipath.

To enable this action, see [Post-launch settings](post-launch-settings.md).

## Post-migration optimization
<a name="fsx-ontap-post-migration"></a>

After successful cutover, optimize your FSx for ONTAP deployment for ongoing operations.

### Configure backup strategy
<a name="fsx-ontap-configure-backups"></a>

After migration, verify that your FSx for ONTAP backup strategy covers the migrated data. Review automatic backup settings and retention policies for your file system, and confirm that migrated volumes are included in your backup schedule. For more information, see [Working with backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html).

### Re-enable Autonomous Ransomware Protection (ARP)
<a name="fsx-ontap-enable-arp"></a>

If you disabled ONTAP ARP before migration, re-enable it after cutover is complete. For more information, see [Enabling Autonomous Ransomware Protection](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/enable-ARP.html).