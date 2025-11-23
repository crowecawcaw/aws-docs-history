# AWS DRS individual replication

settings

AWS Elastic Disaster Recovery attempts to reduce costs by consolidating the replication of as many source
servers as possible onto the same Replication Server based on the individual Source
Server **Replication Settings**. Source Servers must
have identical **Replication Settings** to be
considered for consolidation, and must not have [Use dedicated replication instance](#dedicated-replication-server "#dedicated-replication-server")
enabled. For example, DRS does not consolidate Source Servers that have a different
**Staging area subnet** specified in their
**Replication Settings**. To reduce EC2 usage, we
recommend having as many as possible Source Servers have identical **Replication Settings** to one another.

Modifying the **Replication Settings** of an existing Source Server can impact existing replication,
depending on the settings configured. Additionally, most **Replication Settings** options
can be modified in bulk for multiple Source Servers through the AWS Elastic Disaster Recovery Console:

| Replication Setting                       | Impact                                                                                                                                                | Bulk Editing |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Staging area subnet                       | Small pause while reconnecting Source Server to new Replicator.                                                                                       | Supported    |
| Replication server instance type          | Small pause while reconnecting Source Server to new Replicator.                                                                                       | Supported    |
| Dedicated instance for replication server | Small pause while reconnecting Source Server to new Replicator.                                                                                       | Supported    |
| EBS encryption                            | Full Sync may be required.                                                                                                                            | Supported    |
| Data Routing (Private IP)                 | No impact.                                                                                                                                            | Supported    |
| Network Bandwidth Throttling              | No impact.                                                                                                                                            | Supported    |
| Point in time (PIT) policy                | Replication server is disconnected as a safety measure. This ensures proper handling of retention policy changes that might affect replication state. | Supported    |
| MAP program tagging                       | No impact.                                                                                                                                            | Supported    |
| Tags                                      | No impact.                                                                                                                                            | Supported    |

## Replication server configuration

Replication Servers are AWS EC2 Instances automatically launched by AWS Elastic Disaster Recovery to support Continuous Data Replication from Source Servers.

### Staging area subnet

The **Staging area subnet** setting defines which
VPC Subnet that the a Replication Server for a Source Server uses. A Source
Server must be able to successfully initialize connections to the subnet
configured within its **Staging area subnet**
setting. The best practice is to create a single dedicated, separate subnet
for recovery in your AWS Account. Learn more about creating subnets in
[this AWS VPC article](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md"). Unless [Use private ip](../../../index.md "../../../index.md") is enabled and valid
routing within the VPC exists, Replication Servers must be in a [Public
subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types"). By default, a Replication Servers assigns itself a
[Public IPv4](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses") without any additional configuration needed.

DRS Console

###### Updating the Staging area subnet

1. Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane, select **Source Servers**.
2. Select one or more source servers, then select **Replication**.
3. Select **Edit replication settings**.
4. Navigate to **Replication server configuration**, then select the drop down box under
   **Staging area subnet**.
5. Select a new VPC Subnet from the drop down box.
6. Save settings by selecting **Save replication settings**.

Command Line

###### Updating the Staging area subnet

- Updating the Staging area subnet via commandline
  - [describe-recovery-instances](../../../cli/latest/reference/drs/describe-recovery-instances.md "../../../cli/latest/reference/drs/describe-recovery-instances.md") (AWS CLI)

  ```
  aws drs describe-recovery-instances --source-server-id `s-123456789abcdefgh` --staging-area-subnet-id `subnet-123456789abcd`
  ```

  - [Update-EDRSReplicationConfiguration](../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md "../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md") (DRS Tools for Windows PowerShell)

  ```
  Update-EDRSReplicationConfiguration -SourceServerID `s-123456789abcdefgh` -StagingAreaSubnetId `subnet-123456789abcd`
  ```

### Replication server instance type

The **Replication server instance type**
determines the EC2 Instance type and size that is used for the launch of a
source server's replication server. DRS Replicators only support EC2
Instances with x86_64 CPU architecture.

By default, AWS Elastic Disaster Recovery utilizes the t3.small instance type, and should work well
for most common workloads. We recommend monitoring the Cloudwatch metrics of a replication server,
if your Source Server is experiencing frequent Lag or Backlog. Metrics to monitor include
EBSWriteBytes or EBSWriteOps, which may indicate the
**Replication server instance type** is improperly sized to protect your source server.

AWS Elastic Disaster Recovery supports replicating Source Servers with up to 60 volumes, however the
**Replication server instance type** must also support and equal or greater
number of EBS Volume attachements. We recommend reviewing the
[Dedicated Amazon EBS volume limit Documentation](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit") to ensure an appropriately sized EC2 Instance Type is selected.

DRS Console

###### Updating the Replication server instance type

1. Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane, select **Source Servers**.
2. Select one or more source servers, then select **Replication**.
3. Select **Edit replication settings**.
4. Navigate to **Replication server configuration**, then select the drop down box under
   **Dedicated instance for replication server**.
5. Select **Replication server instance** from the drop down box.
6. Save settings by selecting **Save replication settings**.

Command Line

###### Modifying Dedicated instance for replication server

- Updating the Replication server instance type via commandline
  - [update-replication-configuration](../../../cli/latest/reference/drs/update-replication-configuration.md "../../../cli/latest/reference/drs/update-replication-configuration.md") (AWS CLI)

  ```
  aws drs update-replication-configuration --source-server-id `s-123456789abcdefgh` --replication-server-instance-type `m5.large`
  ```

  - [Update-EDRSReplicationConfiguration](../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md "../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md") (DRS Tools for Windows PowerShell)

  ```
  Update-EDRSReplicationConfiguration -SourceServerID `s-123456789abcdefgh` -ReplicationServerInstanceType  `m5.large`
  ```

### Dedicated instance for replication

server

The **Dedicated instance for replication server**
setting specifies whether or not the Source Server's can use to a
Replication Server shared with other Source Servers. By default, AWS Elastic Disaster Recovery
attempts to consolidate as many Source Servers as possible onto a single
Replication Server, based on a variety of factors. Setting **Dedicated instance for replication server** to
**use dedicated replication instance**
ensures that only this Source Server replicates data to the Replication
Server.

We recommend leaving **Dedicated instance for
replication server** as **do not use dedicated replication instance** unless the Source Server
is experiencing frequent Lag or Backlog due to sharing a Replication Server with other Source Servers. Using a dedicated replication
server may increase EC2 costs associated with protecting a Source Server.

DRS Console

###### Enabling Dedicated instance for replication server

1. Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane, select **Source Servers**.
2. Select one or more source servers, then select **Replication**.
3. Select **Edit replication settings**.
4. Navigate to **Replication server configuration**, then select the drop down box under
   **Dedicated instance for replication server**.
5. Select **use dedicated replication instance** from the drop down box.
6. Save settings by selecting **Save replication settings**.

Command Line

###### Modifying Dedicated instance for replication server

1. Enabling Dedicated instance for replication server via commandline
   - [update-replication-configuration](../../../cli/latest/reference/drs/update-replication-configuration.md "../../../cli/latest/reference/drs/update-replication-configuration.md") (AWS CLI)

   ```
   aws drs update-replication-configuration --source-server-id `s-123456789abcdefgh` --use-dedicated-replication-server
   ```

   - [Update-EDRSReplicationConfiguration](../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md "../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md") (DRS Tools for Windows PowerShell)

   ```
   Update-EDRSReplicationConfiguration -SourceServerID `s-123456789abcdefgh` -UseDedicatedReplicationServer `$true`
   ```

2. Disabling Dedicated instance for replication server via commandline
   - [update-replication-configuration](../../../cli/latest/reference/drs/update-replication-configuration.md "../../../cli/latest/reference/drs/update-replication-configuration.md") (AWS CLI)

   ```
   aws drs update-replication-configuration --source-server-id `s-123456789abcdefgh` --no-use-dedicated-replication-server
   ```

   - [Update-EDRSReplicationConfiguration](../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md "../../../powershell/latest/reference/items/Update-EDRSReplicationConfiguration.md") (DRS Tools for Windows PowerShell)

   ```
   Update-EDRSReplicationConfiguration -SourceServerID `s-123456789abcdefgh` -UseDedicatedReplicationServer `$false`
   ```
