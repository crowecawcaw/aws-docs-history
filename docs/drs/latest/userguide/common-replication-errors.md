# Common replication errors

This section describes common replication errors and possible explanations and potential mitigations.

###### Replication errors

- [Agent not seen](#common-agent-not-seen "#common-agent-not-seen")
- [Not converging](#common-not-converging "#common-not-converging")
- [Failback client not seen](#common-failback-not-seen "#common-failback-not-seen")
- [Snapshot failure](#common-snapshot-failure "#common-snapshot-failure")
- [Unstable network](#common-unstable-network "#common-unstable-network")
- [Failed to download replication software to failback client](#common-download-replication-software "#common-download-replication-software")
- [Failed to configure replication software](#common-configure-replication-software "#common-configure-replication-software")
- [Failed to establish communication with recovery instance](#common-communication-recovery-instance "#common-communication-recovery-instance")
- [Failed to connect AWS replication Agent to replication software](#common-connection-agent-replication-software "#common-connection-agent-replication-software")
- [Failed to establish communication with replication software](#common-establish-communication-replication-software "#common-establish-communication-replication-software")
- [Failed to create firewall rules](#common-failed-create-firewall "#common-failed-create-firewall")
- [Failed to authenticate with service](#common-failed-authenticate-service "#common-failed-authenticate-service")
- [Failed to create staging disks](#common-failed-create-staging-disks "#common-failed-create-staging-disks")
- [Failed to pair the replication agent with replication server](#common-pair-replication-agent-server "#common-pair-replication-agent-server")
- [Failed to launch replication server](#common-failed-launch-replication-server "#common-failed-launch-replication-server")
- [Failed to boot replication server](#common-failed-boot-replication-server "#common-failed-boot-replication-server")
- [Failed to attach staging disks](#common-failed-attach-staging-disks "#common-failed-attach-staging-disks")
- [Failed to connect AWS Replication Agent to replication server](#common-failed-connect-agent-replication-server "#common-failed-connect-agent-replication-server")
- [Failed to start data transfer](#common-failed-start-data-transfer "#common-failed-start-data-transfer")
- [Unknown data replication error](#common-unknown-data-replication-error "#common-unknown-data-replication-error")
- [Replication lag issues](#Replication-Lag-Issues "#Replication-Lag-Issues")

## Agent not seen

This error indicates that the AWS Elastic Disaster Recovery service has lost communication with the
AWS Replication Agent. Use the following steps to diagnose the issue.

Console

###### Verify agent and replication status

1. Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane,
   select **Source servers**.
2. Select the affected source server and check the
   **Data replication status** field.
3. If the status shows **Disconnected**,
   verify that the agent is running on the source server:

   - **Linux:** Run
     `sudo systemctl status aws-replication-agent`
   - **Windows:** Open
     `services.msc` and check the status of
     **AwsReplicationService**.

4. Verify connectivity to the Regional AWS DRS endpoint on TCP Port 443.
   [Learn
   more about verifying connectivity to AWS DRS regional endpoints.](../../../general/latest/gr/drs.md#drs-region "../../../general/latest/gr/drs.md#drs-region")

If this message appears on your **recovery dashboard**,
also ensure that the
[AWSElasticDisasterRecoveryRecoveryInstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.md")
required EC2 instance profile is associated with the recovery instance.

CLI

###### Verify agent and replication status

1. Check the replication state of the source server:

```
aws drs describe-source-servers \
  --filters sourceServerIDs=`s-1234567890abcdefg` \
  --query 'items[0].{State:dataReplicationInfo.dataReplicationState,Error:dataReplicationInfo.dataReplicationError,LastSeen:lifeCycle.lastSeenByServiceDateTime}'
```

If the state is `DISCONNECTED`, the agent is not communicating
with the service. 2. Verify the agent is running on the source server:

    * **Linux:**



    ```
    sudo systemctl status aws-replication-agent
    ```
    * **Windows (PowerShell):**



    ```
    Get-Service -Name AwsReplicationService
    ```

3. Test connectivity to the DRS endpoint:

   - **Linux:**

   ```
   curl -v https://drs.`region`.amazonaws.com 2>&1 | head -20
   ```
   - **Windows (PowerShell):**

   ```
   Test-NetConnection -ComputerName drs.`region`.amazonaws.com -Port 443
   ```

For recovery instances, also verify the instance profile:

```
aws ec2 describe-instances \
  --instance-ids `i-1234567890abcdefg` \
  --query 'Reservations[0].Instances[0].IamInstanceProfile.Arn'
```

## Not converging

This error message (NOT_CONVERGING) could indicate an inadequate replication
speed.

- Follow the instructions on [calculating the required bandwidth](Troubleshooting-Communication-Errors.md#Calculating-Bandwidth "Troubleshooting-Communication-Errors.md#Calculating-Bandwidth").
- [Verify network bandwidth](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test "Replication-Related-FAQ.md#perform-connectivity-bandwidth-test").

Console

###### Check replication lag and disk settings

1. Navigate to the AWS Elastic Disaster Recovery Console. Select the affected source
   server.
2. Check the **Replication lag**
   value and **ETA**.
3. Select the **Disk settings** tab.
   If required, modify the EBS volume type to improve replication
   performance (for example, change from `gp2` to
   `gp3` with higher throughput).

###### Note

Changing the staging disk type may affect replication
costs. Review [EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/") before making
changes.

CLI

###### Check replication lag and disk settings

1. Check the replication lag and state:

```
aws drs describe-source-servers \
  --filters sourceServerIDs=`s-1234567890abcdefg` \
  --query 'items[0].dataReplicationInfo.{State:dataReplicationState,Lag:lagDuration,ETA:etaDateTime}'
```

2. Check the current replication disk settings:

```
aws drs get-replication-configuration \
  --source-server-id `s-1234567890abcdefg` \
  --query 'replicatedDisks[*].{Device:deviceName,StagingType:stagingDiskType,IOPS:iops,Throughput:throughput}'
```

## Failback client not seen

This error message (FAILBACK_CLIENT_NOT_SEEN) could indicate that there’s a
network connectivity issue and that the Failback Client is unable to communicate
with the AWS DRS endpoint. Check network connectivity.

## Snapshot failure

This error message (SNAPSHOTS_FAILURE) indicates that the service is unable to take a consistent snapshot.

This can be caused by:

- Inadequate IAM permissions – Ensure that you have the required IAM
  permissions (attached to the required IAM roles).
- API throttling – [Check if you have activated throttling](data-routing.md#route-control "data-routing.md#route-control"). If throttling is not
  activated, check your CloudTrail logs for throttling errors.

## Unstable network

This error message (UNSTABLE_NETWORK) may indicate that there are network issues.
Check your connectivity, then [run the network bandwidth test](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test "Replication-Related-FAQ.md#perform-connectivity-bandwidth-test").

## Failed to download replication software to failback client

This error message (FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT)
may indicate that there are connectivity issues. [Check your connectivity to the S3
endpoint](Network-Requirements.md#TCP-443 "Network-Requirements.md#TCP-443") and try again.

If the issue persists, you might have a proxy or a network security appliance filtering your traffic and blocking the software download.

## Failed to configure replication software

This error message (FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE) may appear for
multiple reasons. Try again and if the issue persists, contact AWS support.

## Failed to establish communication with recovery instance

This message (FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION) could indicate communication issues. Ensure that the Failback Client is
able to communicate with the recovery instance.

If you are utilizing public network, (no VPN, no direct connect, and more), ensure that your recovery instance has a public IP. By default, AWS DRS launch template deactivates public IP,
and recovery instances are only launched with private IPs.

## Failed to connect AWS replication Agent to replication software

This error message (FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE) may indicate a pairing issue. AWS DRS needs to provide the replication
server and agent with information to allow them to communicate. Make sure there is network connectivity between the agent, replication server, and the AWS DRS endpoint.

If the issue persists, contact support.

## Failed to establish communication with replication software

This error message (FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION) may suggest that there are network connectivity issues. Make sure you have network connectivity between the agent, replication server and the AWS DRS endpoint.

If this message appears during failback, ensure that TCP port 1500 is opened inbound on the recovery instance.

## Failed to create firewall rules

This error message (Firewall rules creation failed) can be caused by several reasons.

1. Ensure that the IAM permission prerequisites are met.
2. Review the replication settings of the associated source server.

## Failed to authenticate with service

This error message (FAILED_TO_AUTHENTICATE_WITH_SERVICE) may indicate a
communication issue between the replication server and the DRS endpoint on TCP
Port 443. Check the subnet you selected and ensure that TCP Port 443 is open from
your replication server.

Console

###### Verify staging area connectivity

1. Navigate to the AWS Elastic Disaster Recovery Console. Select the affected source
   server and check the **Replication
   settings** to identify the staging area subnet.
2. In the Amazon EC2 Console, launch a test instance in the same
   staging area subnet.
3. From the test instance, verify connectivity to the DRS
   endpoint by navigating to
   `https://drs.`region`.amazonaws.com`
   in a browser or using `wget`.
4. If the connection fails, check the security group, network
   ACL, and route table associated with the staging area
   subnet.

CLI

###### Verify staging area connectivity

1. Identify the staging area subnet from the replication
   configuration:

```
aws drs get-replication-configuration \
  --source-server-id `s-1234567890abcdefg` \
  --query '{Subnet:stagingAreaSubnetId,SecurityGroup:replicationServersSecurityGroupsIDs}'
```

2. Test connectivity from a machine in the staging area
   subnet:

   - **Linux:**

   ```
   curl -v https://drs.`region`.amazonaws.com 2>&1 | head -20
   ```
   - **Windows (PowerShell):**

   ```
   Test-NetConnection -ComputerName drs.`region`.amazonaws.com -Port 443
   ```

## Failed to create staging disks

This error message (Failed to create staging disks) may indicate that your AWS
account is configured to encrypt EBS disks but the IAM user does not have the
required permissions to encrypt using the selected KMS key. Ensure that the IAM
prerequisites are met.

## Failed to pair the replication agent with replication server

This error message (Failed to pair replication agent with replication server) may
be caused by multiple reasons. Make sure that you have connectivity between the
replication agent, the replication server, and the DRS endpoint. If the issue
persists, contact Support.

## Failed to launch replication server

This error message (FAILED_TO_LAUNCH_REPLICATION_SERVER) indicates that AWS Elastic Disaster Recovery
was unable to launch a replication server in the staging area.

Console

###### Verify replication server launch prerequisites

1. Navigate to the AWS Elastic Disaster Recovery Console. Select the affected source
   server and check the **Replication
   settings** to identify the staging area subnet and
   replication server instance type.
2. In the Amazon EC2 Console, navigate to **Service
   Quotas** and verify that you have not reached the limit
   for the replication server instance type.
3. Verify that the IAM permissions prerequisites are met.

CLI

###### Verify replication server launch prerequisites

1. Check the replication configuration for the instance type and
   subnet:

```
aws drs get-replication-configuration \
  --source-server-id `s-1234567890abcdefg` \
  --query '{InstanceType:replicationServerInstanceType,Subnet:stagingAreaSubnetId}'
```

2. Check your EC2 running instances quota:

```
aws service-quotas get-service-quota \
  --service-code ec2 \
  --quota-code L-1216C47A
```

Compare the quota value against your current running instance
count in the staging area Region.

## Failed to boot replication server

This error message (FAILED_TO_BOOT_REPLICATION_SERVER) indicates that the
replication server was launched but failed to boot successfully.

- Verify that the staging area subnet has outbound connectivity on
  TCP port 443 to the AWS Elastic Disaster Recovery regional endpoint.
- Check the staging area security group and network ACL settings.
- If the issue persists, contact AWS Support.

## Failed to attach staging disks

This error message (FAILED_TO_ATTACH_STAGING_DISKS) indicates that AWS Elastic Disaster Recovery
was unable to attach the staging disks to the replication server.

- Verify that the IAM permissions prerequisites are met, including
  permissions for Amazon EC2 volume operations.
- Check your EBS volume limits in the staging area Region.
- If the issue persists, contact AWS Support.

## Failed to connect AWS Replication Agent to replication server

This error message (FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER) indicates that
the agent on the source server was unable to establish a data replication connection
with the replication server over TCP port 1500.

Console

###### Verify port 1500 connectivity

1. Navigate to the AWS Elastic Disaster Recovery Console. Select the affected source
   server and check the **Replication
   settings** to identify the staging area subnet.
2. In the Amazon EC2 Console, check the security group associated with
   the staging area to ensure TCP port 1500 is allowed inbound.
3. Check the network ACL on the staging area subnet to ensure it
   allows inbound TCP port 1500.

CLI

###### Verify port 1500 connectivity

1. Identify the staging area security group:

```
aws drs get-replication-configuration \
  --source-server-id `s-1234567890abcdefg` \
  --query 'replicationServersSecurityGroupsIDs'
```

2. Check that the security group allows inbound TCP 1500:

```
aws ec2 describe-security-groups \
  --group-ids `sg-1234567890abcdefg` \
  --query 'SecurityGroups[0].IpPermissions[?ToPort==`1500`]'
```

3. Test port 1500 from the source server:

   - **Linux:**

   ```
   nc -zv `replication-server-ip` 1500
   ```
   - **Windows:**

   ```
   Test-NetConnection -ComputerName `replication-server-ip` -Port 1500
   ```

## Failed to start data transfer

This error message (FAILED_TO_START_DATA_TRANSFER) indicates that the replication
agent and replication server were paired but data transfer could not begin.

- Check network connectivity and bandwidth between the source server
  and the replication server.
- [Check the replication agent
  logs](troubleshooting-agent-issues.md#agent-log-locations "troubleshooting-agent-issues.md#agent-log-locations") for additional details.
- If the issue persists, contact AWS Support.

## Unknown data replication error

Unknown errors (unknown_error) can occur for any number of reasons. There are
several steps you can take to attempt to mitigate the issue:

- Check connectivity.
- Check throttling.
- Check for performance issues on the replication server.
- Check the network bandwidth between the agent and the replication
  server.
- [Check the replication agent
  logs.](Agent-Related-FAQ.md#agent-logs-location "Agent-Related-FAQ.md#agent-logs-location")

## Replication lag issues

Potential solutions:

- Make sure that the source server is up and running.
- Make sure that AWS Elastic Disaster Recovery services are up and running.
- Make sure that TCP Port 1500 is not blocked outbound from the Source
  server to the replication server.
- If the MAC address of the Source had changed, that would require a reinstallation of the
  AWS Replication Agent.
- If the source machine was rebooted recently or the AWS Elastic Disaster Recovery services were
  restarted, the disks are reread after this and until it’s finished, the lag
  will grow.
- If the source machine had a spike of write operations, the lag will grow
  until AWS Elastic Disaster Recovery service manages to flush all the written data to the drill
  or recovery instance replication server.
