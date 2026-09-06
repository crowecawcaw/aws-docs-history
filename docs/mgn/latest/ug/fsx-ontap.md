NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# FSx for ONTAP configuration

## Overview

This page provides step-by-step instructions for configuring Amazon FSx for NetApp ONTAP
(FSx for ONTAP) as a storage migration target for AWS Transform MGN (MGN) when migrating to AWS. With
this setup, you can use the enterprise file storage capabilities of FSx for ONTAP for your
migrated workloads. This page assumes that you are familiar with FSx for ONTAP. For detailed FSx for ONTAP
setup instructions, see the
[FSx for ONTAP Getting Started Guide](../../../fsx/latest/ONTAPGuide/getting-started.md "../../../fsx/latest/ONTAPGuide/getting-started.md").

FSx for ONTAP as a target storage type is available in all AWS Regions where
both MGN and FSx for ONTAP are available. This storage type is not available in
Local Zones. For supported regions, see
[MGN
supported regions](what-is-mgn.md#supported-regions "what-is-mgn.md#supported-regions") and
[FSx for ONTAP
availability by Region](../../../fsx/latest/ONTAPGuide/available-aws-regions.md "../../../fsx/latest/ONTAPGuide/available-aws-regions.md").

###### Important

Do not rename or modify MGN-managed FSx for ONTAP resources (LUNs, igroups, snapshots).
Changes to these resources disrupt migration and require restarting the migration from
the beginning.

### Known limitations

- **FSx for ONTAP backups can block volume cleanup**.
  FSx for ONTAP file systems have automatic backups enabled by default. Backups taken on
  target volumes can prevent MGN from deleting replication volumes on Finalize
  cutover/Disconnect from service migration stage. See
  [Troubleshooting replication volume not
  deleted after Finalize cutover](fsx-ontap-troubleshooting.md#fsx-flexclone-split-blocked "fsx-ontap-troubleshooting.md#fsx-flexclone-split-blocked").
- **Multiple LUNs per volume**. MGN creates one
  volume per source server on the FSx for ONTAP file system and places each disk as a separate LUN within that volume. For
  example, a source server with 3 disks results in one volume with 3 LUNs. The ONTAP best
  practice is a 1:1 relationship (one volume per LUN), which allows per-volume features such
  as snapshots, tiering policies, and storage efficiency to be configured independently per
  disk. As a workaround, you can use the ONTAP
  [`lun move start`](https://docs.netapp.com/us-en/ontap-cli/lun-move-start.html "https://docs.netapp.com/us-en/ontap-cli/lun-move-start.html")
  command to relocate LUNs into dedicated volumes after migration. This operation is non-disruptive
  and does not require iSCSI reconfiguration on the host.
- **Agent-based replication only**. MGN supports
  FSx for ONTAP as a target storage type only with agent-based replication.
- **Up to 5 file systems per account**. MGN supports
  migrating data into up to 5 FSx for ONTAP file systems concurrently per account. If you have
  more file systems, migrate in phases.
  For more information about FSx for ONTAP quotas, see
  [FSx for ONTAP
  quotas](../../../fsx/latest/ONTAPGuide/limits.md "../../../fsx/latest/ONTAPGuide/limits.md"). For MGN service quotas, see
  [MGN
  endpoints and quotas](../../../general/latest/gr/mgn.md "../../../general/latest/gr/mgn.md").
- **igroup limits per file system**. MGN creates one
  igroup per source server during replication and one per target instance at launch.
  FSx for ONTAP supports up to 256 igroups (Single-AZ) or 512 igroups (Multi-AZ). Plan the
  number of source servers per file system accordingly.
- **ONTAP configurations not migrated**. If you are
  migrating from an existing ONTAP storage system, source ONTAP configurations (such as
  access permissions, quotas, snapshot policies, and schedules) are not migrated
  automatically. You must reconfigure these settings on the target FSx for ONTAP file system
  after migration.
- **No mixed storage per server**.
  All data volumes from a source server use the same
  storage type (either Amazon EBS or FSx for ONTAP). You cannot mix storage types for different
  disks on the same server. The boot volume is always stored on Amazon EBS.

## Prerequisites

Before integrating FSx for ONTAP with MGN, ensure the following:

- **MGN Setup**: MGN initialized in your AWS
  account with agent-based replication.

###### Important

If you initialized MGN before FSx for ONTAP support was available, you must
reinitialize the service to create the required AWS managed roles.
In the MGN console, navigate to **Settings → Replication
template** and choose
**Reinitialize Service Permissions**. For details on these roles and their
managed policies, see
[AWS Transform MGN managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

- **VPC Configuration**: FSx for ONTAP and MGN instances must be in
  the same AWS account and Region. They can use the same VPC or different VPCs in which
  both the source and target are routable. IPv4 connectivity is required. As a best practice, use a Multi-AZ FSx for ONTAP file system
  when your applications require resiliency across Availability Zones. Deploy your target
  EC2 instances in the same AZ as the file system's preferred file server to minimize
  latency. If your applications do not require cross-AZ resiliency, you can use a Single-AZ
  FSx for ONTAP file system. Deploy your target EC2 instances in the same AZ as the file system
  to minimize latencies and avoid cross-AZ data transfer charges.
- **OS package repository access**: MGN automatically
  installs iSCSI initiator and multipath packages on replication servers and launched
  instances. Ensure that both the staging area subnet and the launch subnet have outbound
  access to OS package repositories (for example, through a NAT gateway or internet
  gateway). For the full list of required URLs, see
  [Network requirements for FSx for ONTAP](preparing-environments.md#fsx-ontap-network-requirements "preparing-environments.md#fsx-ontap-network-requirements").

## Step 1: Configure security groups

To enable MGN to work with FSx for ONTAP, you must create two security groups that
cross-reference each other:

- **MGN-Instances-SG**. Attached to the EC2 instances
  that MGN launches (test and cutover).
- **FSx-ONTAP-SG**. Attached to the FSx for ONTAP file
  system. Controls inbound traffic from MGN-launched instances.

Because `FSx-ONTAP-SG` references `MGN-Instances-SG` as the
source in its inbound rules, only MGN-launched instances can reach the file system. All
other traffic is denied by default.

### 1.1 MGN instances security group

Create this security group in the VPC where MGN will launch target instances.

###### Important

If you use different VPCs for replication and launch, create two security groups with
distinct names for clarity. For example, use `MGN-Replication-SG` (in the staging VPC) and
`MGN-Launch-SG` (in the launch VPC).

**Steps to create**

1. Navigate to the **Amazon VPC Console → Security Groups →
   Create security group**.
2. Configure the following settings:

   - Security group name: `MGN-Instances-SG`
   - Description: `Security group for instances launched by MGN to allow communication
  with FSx for ONTAP`
   - VPC: Choose the target VPC where MGN will launch instances.

3. **Inbound Rules:** The only required inbound rule is
   port 1500 for MGN data replication from source servers. You can optionally add rules
   for administrative access to your instances (for example, SSH on port 22 or RDP on port
   3389 from your corporate network).

| Type       | Protocol | Port Range | Source               | Description                          |
| ---------- | -------- | ---------- | -------------------- | ------------------------------------ |
| Custom TCP | TCP      | 1500       | `Source server CIDR` | Data replication from source servers |

4. **Outbound Rules:** The default outbound rule (All traffic
   → 0.0.0.0/0) is sufficient. If you restrict outbound rules, add at minimum the
   following rules. Reference the FSx for ONTAP security group (created in the next
   step) as the destination:

| Type  | Protocol | Port Range | Destination    | Description                   |
| ----- | -------- | ---------- | -------------- | ----------------------------- |
| iSCSI | TCP      | 3260       | `FSx-ONTAP-SG` | iSCSI access to FSx for ONTAP |
| HTTPS | TCP      | 443        | `FSx-ONTAP-SG` | ONTAP REST API / Management   |

5. Choose **Create security group**.

### 1.2 FSx for ONTAP security group

You associate this security group with the FSx for ONTAP file system. Use this security group to control
which resources can communicate with the file system and to ensure that MGN-launched
instances have the necessary access.

**Steps to create**

1. Navigate to the **Amazon VPC Console → Security Groups →
   Create security group**.
2. Configure the following settings:

   - Security group name: `FSx-ONTAP-SG`
   - Description: `Security group for FSx for ONTAP file system to allow inbound
  access from MGN-launched instances`
   - VPC: Choose the target VPC used for the FSx for ONTAP file system.

3. **Inbound Rules:** Add the following rules. The table is
   organized into two groups:

   - **Migration traffic (iSCSI)**. Required for
     MGN data replication and launch. Reference `MGN-Instances-SG` as the
     source.
   - **Management access (SSH, HTTPS)**. Optional
     rules for ONTAP CLI and REST API access from MGN-launched instances (for example,
     for troubleshooting or manual configuration). Reference `MGN-Instances-SG`
     as the source.
   - **MGN service traffic (HTTPS)**. Required
     for MGN to access the FSx for ONTAP REST API during replication and launch. Use the
     CIDR blocks of the preferred and standby subnets where the file system is deployed.
     You can find these CIDRs in the
     **FSx for ONTAP Console** under your file system's
     **Network & security** tab, or in the
     **VPC Console → Subnets** by looking up the subnet
     IDs. You can narrow this scope after the initial setup is complete.

| Type                             | Protocol | Port Range | Source                      | Description                                  |
| -------------------------------- | -------- | ---------- | --------------------------- | -------------------------------------------- |
| **Migration traffic**            |
| iSCSI                            | TCP      | 3260       | `MGN-Instances-SG`          | Allow iSCSI from MGN instances               |
| **Management access (optional)** |
| SSH                              | TCP      | 22         | `MGN-Instances-SG`          | ONTAP CLI management from MGN instances      |
| HTTPS                            | TCP      | 443        | `MGN-Instances-SG`          | ONTAP REST API management from MGN instances |
| **MGN service traffic**          |
| HTTPS                            | TCP      | 443        | `FSx preferred subnet CIDR` | MGN access to ONTAP REST API                 |
| HTTPS                            | TCP      | 443        | `FSx standby subnet CIDR`   | MGN access to ONTAP REST API                 |

4. **Outbound Rules:** The default outbound rule (All traffic
   → 0.0.0.0/0) is sufficient.
5. Choose **Create security group**.

## Step 2: Create FSx for ONTAP file system

MGN can work with an existing FSx for ONTAP file system or a new one. If you do not already
have an FSx for ONTAP file system, create one in the same AWS account and Region where MGN
will launch target instances.

### High-level steps

1. Navigate to the Amazon FSx for NetApp ONTAP Console and create a new FSx for ONTAP file system.
2. Choose **Standard create** option.
3. Choose deployment type (Multi-AZ or Single-AZ).
4. Configure storage capacity and throughput based on your workload requirements.
5. Choose the VPC and subnets for FSx for ONTAP deployment.
6. Choose `FSx-ONTAP-SG` security group created in
   [1.2 FSx for ONTAP security group](#fsx-ontap-fsx-sg "#fsx-ontap-fsx-sg").
7. Configure FSx for ONTAP admin account and password.
8. Configure a Storage Virtual Machine (SVM).
9. Wait for the file system to reach **Available** status
   (approximately 30-45 minutes).

###### Important for MGN integration

- **For Multi-AZ deployments**: you must specify an Endpoint
  IPv4 address range (not unallocated or floating) that is outside your VPC CIDR. Use the
  "Enter an IPv4 address range" option and provide a specific range within RFC 1918 private
  address space (for example, `192.168.1.0/24`). This is required for MGN
  integration to ensure consistent endpoint addressing.
- **Storage capacity**: MGN uses FSx for ONTAP storage for
  replication, conversion, and cutover. These processes require temporary storage on the file
  system. Ensure that sufficient space is available on the FSx for ONTAP file system and increase
  capacity if needed. As a guideline, provision 3x the size of the planned migration
  data. The 3x factor accounts for three concurrent storage consumers during migration: the
  replicated data, the converted volumes used for launch, and the original volumes pending
  deletion. Volume deletion in FSx for ONTAP is a background operation, so freed capacity is not
  available immediately after deletion, so headroom must be provisioned upfront. As a best
  practice, keep the file system at or below 80% SSD capacity utilization throughout the
  migration. For second-generation file systems
  ([Single-AZ 2
  and Multi-AZ 2](../../../fsx/latest/ONTAPGuide/high-availability-AZ.md "../../../fsx/latest/ONTAPGuide/high-availability-AZ.md") deployment types), you can decrease storage capacity after
  migration is complete. For more
  information, see
  [Managing
  storage capacity and provisioned IOPS](../../../fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.md "../../../fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.md").
- **Throughput capacity**: Higher throughput capacity
  reduces migration time. Throughput is selected from supported values and is a billable
  dimension. To size throughput for migration, sum the average read throughput and
  write throughput across all source servers being migrated to the file system, add 15%
  headroom, and round up to the next supported value. Plan your throughput capacity before
  starting migration, as changes take time to take effect. You can reduce throughput after
  migration is complete. For more information, see
  [Managing
  throughput capacity](../../../fsx/latest/ONTAPGuide/managing-throughput-capacity.md "../../../fsx/latest/ONTAPGuide/managing-throughput-capacity.md") and
  [FSx for ONTAP
  performance](../../../fsx/latest/ONTAPGuide/performance.md "../../../fsx/latest/ONTAPGuide/performance.md").

###### Disable Autonomous Ransomware Protection (ARP)

If ONTAP ARP is enabled on the file system, disable it before migration. ARP can
prevent MGN from deleting replication volumes on Finalize cutover/Disconnect from service
migration stage. For more information, see
[Enabling
Autonomous Ransomware Protection](../../../fsx/latest/ONTAPGuide/enable-ARP.md "../../../fsx/latest/ONTAPGuide/enable-ARP.md").

For detailed instructions on creating and configuring FSx for ONTAP file systems, see
[Creating
FSx for ONTAP file systems](../../../fsx/latest/ONTAPGuide/creating-file-systems.md "../../../fsx/latest/ONTAPGuide/creating-file-systems.md").

## Step 3: Configure certificate-based authentication

**Certificate-based authentication is required for MGN to access the
ONTAP REST API and iSCSI targets.** MGN handles TLS validation internally using AWS Certificate
Authorities.

###### Note

MGN does not use CHAP for iSCSI. iSCSI access is controlled via security groups, and
MGN authenticates to the ONTAP management API using client certificates as described in
this section.

### Create client certificate for API authentication

Generate a client certificate that FSx for ONTAP will require and MGN will use to
authenticate to the ONTAP REST API. You have several options:

Certificate options| Option | Use Case | Documentation |
| --- | --- | --- |
| **Self-Signed Certificate** | Testing/Development | [Generating a self-signed certificate<br>for FSx for ONTAP](fsx-ontap-generate-certs.md "fsx-ontap-generate-certs.md") |
| **AWS Private Certificate Authority** | Production (Recommended) | [AWS Private Certificate Authority](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md") |
| **External Certificate Authority** | Production (Enterprise PKI) | Use your organization's CA process |

###### Note

The private key must be in PKCS#8 format
(`-----BEGIN PRIVATE KEY-----`).
If your key starts with `-----BEGIN RSA PRIVATE KEY-----` (PKCS#1), convert
it:

```
`[~]$` `openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
 -in fsx-mgn-client.key -out fsx-mgn-client.key`
```

### Install client certificate on FSx for ONTAP

Install the client certificate on the FSx for ONTAP to enable certificate-based
authentication. In the following commands, replace `vserver_name`
with your file system ID (e.g., `FsxId08f0e724d292c729c`). You can find this in
the FSx for ONTAP console under your file system's details.

1. Connect to the file system's management endpoint. Log in to an EC2 instance in the
   same VPC as the FSx for ONTAP file system, then use the `fsxadmin` user to SSH
   into the file system's management endpoint IP address or DNS name:

```
`[~]$` `ssh fsxadmin@`file-system-management-endpoint-ip-address``
```

For more information, see
[Managing
file systems with the ONTAP CLI](../../../fsx/latest/ONTAPGuide/managing-resources-ontap-apps.md#fsxadmin-ontap-cli "../../../fsx/latest/ONTAPGuide/managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Install the client CA certificate:

```
`FsxId0123456::>` `security certificate install -type client-ca \
 -vserver `vserver_name` -cert-name my-client-ca`

# Paste the contents of ca.crt when prompted
# Press Enter when done
```

Verify the certificate was installed:

```
`FsxId0123456::>` `security certificate show -vserver `vserver_name` -type client-ca`
```

3. Create the user with certificate authentication. For more information, see
   [Creating
   ONTAP users](../../../fsx/latest/ONTAPGuide/create-new-ontap-users.md "../../../fsx/latest/ONTAPGuide/create-new-ontap-users.md").

```
`FsxId0123456::>` `security login create -vserver `vserver_name` \
 -user-or-group-name cert_usr -application http \
 -authentication-method cert -role fsxadmin`
```

Verify the login was created:

```
`FsxId0123456::>` `security login show -vserver `vserver_name` \
 -user-or-group-name cert_usr`
```

### Test certificate-based authentication

Log in to an EC2 instance in the same VPC as the FSx for ONTAP file system, then
run the following command to test certificate authentication:

Download the FSx for ONTAP certificate bundle (change the region in the URL):

```
`[~]$` `curl https://fsx-aws-certificates.s3.amazonaws.com/bundle-`region`.pem \
 -o bundle-`region`.pem`
```

Test authentication using the certificate:

```
`[~]$` `curl -sS --cacert bundle-`region`.pem \
 --cert fsx-mgn-client.crt \
 --key fsx-mgn-client.key \
 https://management.`fs-xxxxx`.fsx.`region`.amazonaws.com/api/cluster`
```

**Expected:** JSON response with cluster information. If you
see 401 Unauthorized, verify certificate installation and login creation.

## Step 4: Store certificates in AWS Secrets Manager

Store the client certificate and private key in AWS Secrets Manager (Secrets Manager). MGN will retrieve these
credentials using the Secret ARN.

**Required secret format:**

MGN expects the secret to contain exactly two keys:

- `cert`: The client certificate content
  (`fsx-mgn-client.crt`)
- `key`: The private key content (`fsx-mgn-client.key`)

**Store using AWS Console:**

1. Navigate to **Secrets Manager** in the AWS Console.
2. Choose **Store a new secret**.
3. Choose **Other type of secret**.
4. Add key-value pairs with exact key names as key/value (not plain text):

   - `cert` – content of your `fsx-mgn-client.crt`
   - `key` – content of your `fsx-mgn-client.key`

5. Choose **Next**.
6. On the **Configure secret** page, under
   **Tags**, add a tag with key
   `AWSApplicationMigrationServiceManaged` and value `True`.
7. Choose **Next** →
   **Store**.
8. **Copy the Secret ARN**. You need this for MGN
   configuration.

###### Important

- Use `cert` (not `certificate`).
- Use `key` (not `private_key`).
- Do NOT include a `username` field.

**Example Secret ARN:**

```
arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:mgn/fsx/ontap-api-certificate-`AbCdEf`
```

## Step 5: Configure MGN replication settings

Configure MGN to use the FSx for ONTAP REST API certificate stored in Secrets Manager.

### Configure replication template by using the AWS Console

###### Important

Changing the storage provider for a source server that is already replicating terminates
current replication and restarts the replication process from the beginning.

1. Navigate to **MGN** console.
2. Under **Settings**, choose
   **Replication template**.
3. Choose **Edit**.
4. Choose the required target subnet (subnet that can communicate with FSx for ONTAP and has outbound access to OS package repositories).
5. Choose **FSx for ONTAP configuration**.
6. Enter the following configuration:

   - Choose **AWS FSx for ONTAP** as a default storage
     type.
   - **Storage Virtual Machine (SVM) ID**: choose from the list.
   - **FSx Storage Secret ARN**: enter the Secret ARN
     you copied in [Step 4: Store certificates in AWS Secrets Manager](#fsx-ontap-step4-store-certs "#fsx-ontap-step4-store-certs").

7. Choose the `MGN-Instances-SG` security group (created in
   [1.1 MGN instances security group](#fsx-ontap-mgn-instances-sg "#fsx-ontap-mgn-instances-sg")) to allow iSCSI traffic to FSx for ONTAP.
8. Choose **Save changes**.

###### Note

Migration Acceleration Program (MAP) 2.0 tags are applied to the FSx for ONTAP file
system but not to individual FSx for ONTAP volumes.

## Step 6: Configure launch template and launch settings

The target instance must establish iSCSI connectivity to the FSx for ONTAP SVM over the network.

**Requirements:**

- Choose the required target subnet. This subnet must have network connectivity to the
  FSx for ONTAP file system (ports 3260 and 443) and outbound access to OS package repositories.
  For connectivity details, see
  [Network requirements for
  FSx for ONTAP](preparing-environments.md#fsx-ontap-network-requirements "preparing-environments.md#fsx-ontap-network-requirements").
- Modify the source server's launch template to include the
  `MGN-Instances-SG` security group (see
  [Step 1: Configure security groups](#fsx-ontap-step1-security-groups "#fsx-ontap-step1-security-groups")).

## Step 7: Enable volume integrity validation (recommended)

Enable the [Volume integrity
validation](predefined-post-launch-actions.md#predefined-volume-integrity-validation "predefined-post-launch-actions.md#predefined-volume-integrity-validation") post-launch action to automatically verify iSCSI connectivity and multipath
mount configuration after each test or cutover launch. For FSx for ONTAP migrations, this action
validates that all expected iSCSI volumes are connected, mounted, and accessible through
multipath.

To enable this action, see
[Post-launch settings](post-launch-settings.md "post-launch-settings.md").

## Post-migration optimization

After successful cutover, optimize your FSx for ONTAP deployment for ongoing operations.

### Configure backup strategy

After migration, verify that your FSx for ONTAP backup strategy covers the migrated data.
Review automatic backup settings and retention policies for your file system, and confirm
that migrated volumes are included in your backup schedule. For more information, see
[Working
with backups](../../../fsx/latest/ONTAPGuide/using-backups.md "../../../fsx/latest/ONTAPGuide/using-backups.md").

### Re-enable Autonomous Ransomware Protection (ARP)

If you disabled ONTAP ARP before migration, re-enable it after cutover is complete.
For more information, see
[Enabling
Autonomous Ransomware Protection](../../../fsx/latest/ONTAPGuide/enable-ARP.md "../../../fsx/latest/ONTAPGuide/enable-ARP.md").
