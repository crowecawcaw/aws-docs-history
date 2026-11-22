

# Common replication errors

This section describes common replication errors, possible explanations, and potential mitigations.

**Topics**
+ [Agent not seen](#common-agent-not-seen)
+ [Not converging](#common-not-converging)
+ [Snapshot failure](#common-snapshot-failure)
+ [Unstable network](#common-unstable-network)
+ [Failed to connect AWS replication Agent to replication software](#common-connection-agent-replication-software)
+ [Failed to establish communication with replication software](#common-establish-communication-replication-software)
+ [Failed to create firewall rules](#common-failed-create-firewall)
+ [Failed to create security groups](#common-failed-create-security-groups)
+ [Failed to authenticate with service](#common-failed-authenticate-service)
+ [Failed to create staging disks](#common-failed-create-staging-disks)
+ [Replication stuck at Attach Staging Disks](#common-stuck-attach-staging-disks)
+ [Failed to pair the replication agent with replication server](#common-pair-replication-agent-server)
+ [Stalled replication when replicating a source volume smaller than 1MiB](#stalled-replication-for-source-disk-under-1MiB)
+ [Data replication takes a long time](#common-slow-data-replication)
+ [Unknown data replication error](#common-unknown-data-replication-error)

## Agent not seen
<a name="common-agent-not-seen"></a>
+ If you see this message, ensure that:
  + The source Server has access to the AWS Transform MGN service.
  + The replication agent is in running state. For Windows, use Windows services management console (services.msc) or command line (for example, get-services PowerShell). For Linux, use the command `systemctl status aws-replication`.

  If the agent is indeed in running state, verify that the connectivity to the Regional MGN endpoint on TCP Port 443. [Learn more about verifying connectivity to MGN regional endpoints.](https://docs.aws.amazon.com/general/latest/gr/mgn.html)

## Not converging
<a name="common-not-converging"></a>

This error message (NOT\_CONVERGING) could indicate an inadequate replication speed.

Not converging error implies that there is a backlog, but the transfer of data in comparison to the growth of the data on the source server is slower. If the source server is writing more to the disk as compared to the speed at which its sending the data then we get the not converging error.
+ Follow the instructions on [calculating the required bandwidth](Troubleshooting-Communication-Errors.md#Calculating-Bandwidth).
+ [Verify network bandwidth](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test).
+ Verify replicator Amazon EBS volumes (associated with the source server) performance. If required, modify EBS volume type from the MGN console: Go to the specific source server page and select the **Disk settings** tab.
+ Verify the source server performance. For example CPU and Memory utilization.

## Snapshot failure
<a name="common-snapshot-failure"></a>

This error message (SNAPSHOTS\_FAILURE) indicates that the service is unable to take a consistent snapshot.

This can be caused by:
+ Inadequate IAM permissions – Check your CloudTrail logs for any errors in the CreateSnapshot API call. Ensure that you have the required IAM permissions (attached to the required IAM roles).

  Restrictive Service Control Policies – Check if your AWS Organization has a Service Control Policy (SCP) that is preventing the snapshot creation.
+ API throttling – Check your CloudTrail logs for API throttling errors.

## Unstable network
<a name="common-unstable-network"></a>

This error message (UNSTABLE\_NETWORK) may indicate that there are network issues. Check your connectivity, then [run the network bandwidth test](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test).

## Failed to connect AWS replication Agent to replication software
<a name="common-connection-agent-replication-software"></a>

This error message (FAILED\_TO\_PAIR\_AGENT\_WITH\_REPLICATION\_SOFTWARE) may indicate a pairing issue. AWS MGN needs to provide the replication server and agent with information to allow them to communicate. Make sure there is network connectivity between the agent, migration server, and the MGN endpoint. 

If the issue persists, contact support.

## Failed to establish communication with replication software
<a name="common-establish-communication-replication-software"></a>

This error message (FAILED\_TO\_ESTABLISH\_AGENT\_REPLICATOR\_SOFTWARE\_COMMUNICATION) may suggest that there are network connectivity issues. Make sure you have network connectivity between the agent, replication server and the MGN endpoint.

## Failed to create firewall rules
<a name="common-failed-create-firewall"></a>

This error message (Firewall rules creation failed) can be caused by several reasons. 

1. Ensure that the IAM permission prerequisites are met.

1. Review the replication settings of the associated source server.

## Failed to create security groups
<a name="common-failed-create-security-groups"></a>

AWS MGN could not create or update the security group for the replication server. This is usually one of the following:
+ A Service Control Policy (SCP) or permissions boundary in your AWS Organization is blocking the MGN service-linked role from modifying security groups.
+ A security group named **AWS Application Migration Service default Replication Server Security Group** already exists in the staging area VPC but was not created by MGN. Remove or rename it so MGN can create and manage its own.

## Failed to authenticate with service
<a name="common-failed-authenticate-service"></a>

This error message (Failed to authenticate the replication server with the service) may indicate a communication issue between the replication server and the MGN endpoint on TCP Port 443. Check the subnet you selected and ensure that TCP Port 443 is open from your replication server. 

To verify the connection:
+ Launch a test Amazon Linux 2 EC2 instance in the same subnet that was selected in the replication settings.
+ On the server, run the following command: 

  ```
  wget <enter_MGN_regional_endpoint>
  ```
+ If the command fails, there is a connectivity problem.

## Failed to create staging disks
<a name="common-failed-create-staging-disks"></a>

This error message (Failed to create staging disks) may indicate that your AWS account is configured to use encrypted EBS disks, but the IAM user does not have the required permissions to encrypt using the selected KMS key.

Check your CloudTrail logs for any errors in the CreateVolume API call. Then ensure that you have the required IAM permissions attached to the specified IAM role. If the issue persists, also check your KMS Key Policy for any statements that may prevent MGN from using the selected KMS key.

This error can also mean that the staging disk type cannot hold the disk. In that case, the replication status of the server shows the reason from Amazon EC2, for example: `Volume of 61440GiB is too large for volume type gp2; maximum is 16384GiB`. This happens when a disk is larger than 16 TiB but its staging disk type stops at 16 TiB (gp2, io1, st1, or sc1), whether you chose that type or AUTO did. It can also happen later, if a disk grows past 16 TiB after the agent is installed. To fix it, change the staging disk type of the disk to gp3 or io2. If the disk is on AUTO, you can instead choose the **Faster, General Purpose SSD (gp3)** option as the [Amazon EBS volume type](ebs-storage.md#ebs-volume-type) for large disks. For the size that each type supports, see [Disk size by staging disk type](ebs-storage.md#staging-disk-size).

## Replication stuck at Attach Staging Disks
<a name="common-stuck-attach-staging-disks"></a>

If replication is stuck at the "Attach Staging Disks" stage during initial sync, the replication server may have reached the maximum number of Amazon EBS volumes that can be attached to the instance type.

**Cause:** By default, MGN uses a single replication server per 15 source disks. If the total number of disks across source servers sharing a replication server exceeds the Amazon EBS volume attachment limit of the replication server instance type, the attach operation will stall.

**Resolution:**
+ Use a replication server instance type that supports more Amazon EBS volume attachments. For a list of instance types and their supported volume counts, see [General purpose instances – EBS specifications](https://docs.aws.amazon.com/ec2/latest/instancetypes/gp.html#gp_storage-ebs).
+ Use [dedicated replication servers](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html#dedicated-replication-server) to reduce the number of disks per replication server.
+ Reduce the number of disks being replicated per source server by excluding unnecessary volumes during agent installation.

## Failed to pair the replication agent with replication server
<a name="common-pair-replication-agent-server"></a>

This error message (Failed to pair replication agent with replication server) may be caused by multiple reasons. Make sure that you have connectivity between the replication agent, the replication server, and the MGN endpoint. If the issue persists, contact Support.

## Stalled replication when replicating a source volume smaller than 1MiB
<a name="stalled-replication-for-source-disk-under-1MiB"></a>

Replication is stalled which point to a common network, however in this edge case it indicates you are trying to replicate a disk on source server which is smaller than 1MiB. This is not supported. To mitigate, a. [Reinstall](https://docs.aws.amazon.com/mgn/latest/ug/reinstalling-agent.html) the agent with manually identifying disks to replication, and not include the disk with size under 1MiB. b. Expand the volume and reinstall the agent.

## Data replication takes a long time
<a name="common-slow-data-replication"></a>

The initial sync or a rescan of a source server takes a long time.

**Cause:** The initial sync and a rescan read and write every block of the source disks, regardless of how much of each disk is in use, so they take longer the larger the disks are. Their speed depends on the replication server instance type and on the throughput of the Amazon EBS staging disks or of the FSx for ONTAP file system.

**Resolution:**
+ Choose a replication server instance type with more bandwidth, such as c6in.xlarge or larger, in the replication template or in the replication settings of the source server. For more information, see [Replication server instance type](replication-server-settings.md#instance-type).
+ Set the Amazon EBS staging disks to General Purpose SSD (gp3) and increase their throughput. For more information, see [Change staging disk type](ebs-storage.md#staging-disk).
+ If the source server stages on FSx for ONTAP, increase the throughput capacity of the file system. For more information, see [Step 2: Create FSx for ONTAP file system](fsx-ontap.md#fsx-ontap-step2-create-filesystem).
+ If replication is still slow, [verify the network bandwidth](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test) between the source server and the replication server.

For more information, see [Replicating large disks](ebs-storage.md#large-disks).

## Unknown data replication error
<a name="common-unknown-data-replication-error"></a>

Unknown errors (unknown\_error) can occur for any number of reasons. There are several steps you can take to attempt to mitigate the issue: 
+ Check connectivity.
+ Check throttling.
+ Check performance issue on the replication server.
+ Check the [network bandwidth](https://docs.aws.amazon.com/mgn/latest/ug/Replication-Related-FAQ.html#perform-connectivity-bandwidth-test) between the agent and the replication server.
+ [Check the replication agent logs.](Troubleshooting-Agent-Issues.md#MGN-Agent-Log)