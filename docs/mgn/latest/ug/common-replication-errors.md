NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Common replication errors

This section describes common replication errors, possible explanations, and potential mitigations.

###### Replication errors

- [Agent not seen](#common-agent-not-seen "#common-agent-not-seen")
- [Not converging](#common-not-converging "#common-not-converging")
- [Snapshot failure](#common-snapshot-failure "#common-snapshot-failure")
- [Unstable network](#common-unstable-network "#common-unstable-network")
- [Failed to connect AWS replication Agent to replication software](#common-connection-agent-replication-software "#common-connection-agent-replication-software")
- [Failed to establish communication with replication software](#common-establish-communication-replication-software "#common-establish-communication-replication-software")
- [Failed to create firewall rules](#common-failed-create-firewall "#common-failed-create-firewall")
- [Failed to authenticate with service](#common-failed-authenticate-service "#common-failed-authenticate-service")
- [Failed to create staging disks](#common-failed-create-staging-disks "#common-failed-create-staging-disks")
- [Failed to pair the replication agent with replication server](#common-pair-replication-agent-server "#common-pair-replication-agent-server")
- [Stalled replication when replicating a source volume smaller than 1MiB](#stalled-replication-for-source-disk-under-1MiB "#stalled-replication-for-source-disk-under-1MiB")
- [Unknown data replication error](#common-unknown-data-replication-error "#common-unknown-data-replication-error")

## Agent not seen

- If you see this message, ensure that:

      + The source Server has access to the AWS Application Migration Service service.
      + The replication agent is in running state. For Windows, use Windows services management console (services.msc) or command line (for example, get-services PowerShell). For Linux, use the command `systemctl status aws-replication`.

  If the agent is indeed in running state, verify that the connectivity to the Regional
  AWS MGN endpoint on TCP Port 443. [Learn more about
  verifying connectivity to AWS MGN regional endpoints.](../../../general/latest/gr/mgn.md "../../../general/latest/gr/mgn.md")

## Not converging

This error message (NOT_CONVERGING) could indicate an inadequate replication
speed.

Not converging error implies that there is a backlog, but the transfer of data in comparison to the growth of the data on the source server is slower. If the source server is writing more to the disk as compared to the speed at which its sending the data then we get the not converging error.

- Follow the instructions on [calculating the required bandwidth](Troubleshooting-Communication-Errors.md#Calculating-Bandwidth "Troubleshooting-Communication-Errors.md#Calculating-Bandwidth").
- [Verify network bandwidth](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test "Replication-Related-FAQ.md#perform-connectivity-bandwidth-test").
- Verify replicator Amazon EBS volumes (associated with the source server) performance. If
  required, modify EBS volume type from the AWS MGN console: Go to the specific source server
  page and select the **Disk settings** tab.
- Verify the source server performance. For example CPU and Memory utilization.

## Snapshot failure

This error message (SNAPSHOTS_FAILURE) indicates that the service is unable to take a consistent snapshot.

This can be caused by:

- Inadequate IAM permissions – Check your CloudTrail logs for any errors in the CreateSnapshot API call. Ensure that you have the required IAM permissions
  (attached to the required IAM roles).

Restrictive Service Control Policies – Check if your AWS Organization has a Service Control Policy (SCP) that is preventing the snapshot creation.

- API throttling – Check your CloudTrail logs for API throttling errors.

## Unstable network

This error message (UNSTABLE_NETWORK) may indicate that there are network issues.
Check your connectivity, then [run the network bandwidth test](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test "Replication-Related-FAQ.md#perform-connectivity-bandwidth-test").

## Failed to connect AWS replication Agent to replication software

This error message (FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE) may indicate a pairing
issue. AWS MGN needs to provide the replication server and agent with information to allow
them to communicate. Make sure there is network connectivity between the agent, migration
server, and the AWS MGN endpoint.

If the issue persists, contact support.

## Failed to establish communication with replication software

This error message (FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION) may
suggest that there are network connectivity issues. Make sure you have network connectivity
between the agent, replication server and the AWS MGN endpoint.

## Failed to create firewall rules

This error message (Firewall rules creation failed) can be caused by several reasons.

1. Ensure that the IAM permission prerequisites are met.
2. Review the replication settings of the associated source server.

## Failed to authenticate with service

This error message (Failed to authenticate the replication server with the
service) may indicate a communication issue between the replication server and the
AWS MGN endpoint on TCP Port 443. Check the subnet you selected and ensure that TCP Port
443 is open from your replication server.

To verify the connection:

- Launch a test Amazon Linux 2 EC2 instance in the same subnet that was selected in the
  replication settings.
- On the server, run the following command:

```
wget <enter_MGN_regional_endpoint>
```

- If the command fails, there is a connectivity problem.

## Failed to create staging disks

This error message (Failed to create staging disks) may indicate that your AWS account is configured to use encrypted EBS disks, but the IAM user does not have the required permissions to encrypt using the selected KMS key.

Check your CloudTrail logs for any errors in the CreateVolume API call. Then ensure that you have the required IAM permissions attached to the specified IAM role. If the issue persists, also check your KMS Key Policy for any statements that may prevent AWS MGN from using the selected KMS key.

## Failed to pair the replication agent with replication server

This error message (Failed to pair replication agent with replication server) may be caused by multiple reasons. Make sure that you have connectivity between the replication agent, the replication server, and the AWS MGN endpoint. If the issue persists, contact Support.

## Stalled replication when replicating a source volume smaller than 1MiB

Replication is stalled which point to a common network, however in this edge case it indicates you are trying to replicate a disk on source server which is smaller than 1MiB. This is not supported. To mitigate, a. [Reinstall](reinstalling-agent.md "reinstalling-agent.md") the agent with manually identifying disks to replication, and not include the disk with size under 1MiB. b. Expand the volume and reinstall the agent.

## Unknown data replication error

Unknown errors (unknown_error) can occur for any number of reasons. There are several steps you can take to attempt to mitigate the issue:

- Check connectivity.
- Check throttling.
- Check performance issue on the replication server.
- Check the [network bandwidth](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test "Replication-Related-FAQ.md#perform-connectivity-bandwidth-test") between the agent and the replication
  server.
- [Check the replication agent logs.](Troubleshooting-Agent-Issues.md#MGN-Agent-Log "Troubleshooting-Agent-Issues.md#MGN-Agent-Log")
