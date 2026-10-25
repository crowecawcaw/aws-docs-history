

# Replication errors: agent runtime errors
<a name="agent-runtime-errors"></a>

This topic covers messages that the AWS Replication Agent writes to its own log on the source server or recovery instance. The other topics in this section cover replication errors that AWS Elastic Disaster Recovery reports in the console. Use this topic when the console shows no specific error, or to find the cause behind one. To find the agent log, see [Check agent status and logs](agent-diagnostics.md#agent-log-locations).

For each error in this topic, the agent logs a line that starts with Error code: DRS-REPL- and a three-digit number. The line also includes a short summary and a *For troubleshooting, see* link to the matching section.

**Topics**
+ [DRS-REPL-001: Server identity changed and no matching recovery instance was found](#error-agent-identity-changed)
+ [DRS-REPL-002: Replication driver failed to load at agent startup](#error-driver-load-failed-startup)
+ [DRS-REPL-003: Cannot connect to the replication server on TCP port 1500](#error-replication-server-connect-failed)
+ [DRS-REPL-004: Authentication with the replication server failed](#error-replication-auth-message-failed)
+ [DRS-REPL-005: Cannot reach AWS Elastic Disaster Recovery or load agent credentials](#error-management-transport-failed)
+ [DRS-REPL-006: AWS Elastic Disaster Recovery rejected the agent credentials](#error-management-auth-rejected)
+ [DRS-REPL-007: Timed out waiting for the failback connection on TCP port 1500](#error-failback-listen-timed-out)
+ [DRS-REPL-008: Handshake with the replication server failed](#error-replication-handshake-failed)
+ [DRS-REPL-009: Agent ran out of memory and restarted](#error-agent-out-of-memory)

## DRS-REPL-001: Server identity changed and no matching recovery instance was found
<a name="error-agent-identity-changed"></a>

**Error message:** Error code: DRS-REPL-001 - Server identity changed and no matching recovery instance was found

**Cause:** At startup, the agent detected that the server identity changed and found no matching recovery instance. This happens when:
+ A disk with the agent installed was cloned, migrated, or restored onto a different server.
+ On the same server, the agent cannot detect or read the identifier that it recorded at installation: the MAC address, the VMware UUID, or the Google Cloud instance ID. For example, it cannot read the VMware UUID from the system BIOS information or reach the Google Cloud metadata server.
+ On a recovery instance, the agent could not confirm with AWS Elastic Disaster Recovery that the instance is a recovery instance. For example, the instance has no instance profile with the required permissions, cannot reach AWS Elastic Disaster Recovery over TCP port 443, or is not a recovery instance in this AWS account and Region.

The process exits after 60 seconds, and the service manager restarts it. Replication does not start.

**Resolution:**
+ On a recovery instance, verify the instance profile policy and TCP port 443 access to AWS Elastic Disaster Recovery. See [AWS managed policy: AWSElasticDisasterRecoveryRecoveryInstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.md). The agent checks again after it restarts. If the error persists, reinstall the agent as a recovery instance. This procedure first disconnects the instance from AWS. See [Reinstalling the agent on a recovery instance](reinstalling-agent.md#reinstalling-agent-recovery-instance).
+ On a server that was cloned, migrated, or restored, or whose identifier changed, reinstall the agent so that it registers as its own source server. See [Reinstalling the agent](reinstalling-agent.md).
+ If the identity changed unexpectedly, contact AWS Support.

## DRS-REPL-002: Replication driver failed to load at agent startup
<a name="error-driver-load-failed-startup"></a>

**Error message:** Error code: DRS-REPL-002 - Replication driver failed to load at agent startup

**Cause:** At startup, the agent could not load the replication driver or set up the driver device. The process exits, and the service manager restarts it. Common causes include the following:
+ On Linux, the agent could not rebuild the driver after a kernel upgrade. The agent rebuilds it automatically, which requires kernel headers that match the new kernel and access to download the driver sources from AWS.
+ On Linux, kernel headers that do not match the running kernel
+ On Linux, Secure Boot or SELinux settings that block the driver
+ Endpoint protection software that blocks the driver

**Resolution:**

1. On Linux, install kernel headers that match the running kernel, and then reinstall the agent to rebuild the driver. See [Error: Kernel headers version mismatch](agent-install-linux-errors.md#error-kernel-headers-mismatch).

1. On Linux, resolve Secure Boot, SELinux, or endpoint protection settings that block the driver. See [Error: Permission denied when loading kernel driver](agent-install-linux-errors.md#error-selinux-secure-boot).

1. On Windows, check the driver service with `sc query AwsReplicationDriver`, confirm that endpoint protection software is not blocking the driver, and then restart the agent.

1. If the driver still fails to load, collect diagnostic information and contact AWS Support. See [Gather diagnostic information for support](agent-diagnostics.md#agent-diagnostic-tools).

## DRS-REPL-003: Cannot connect to the replication server on TCP port 1500
<a name="error-replication-server-connect-failed"></a>

**Error message:** Error code: DRS-REPL-003 - Cannot connect to the replication server on TCP port 1500

**Cause:** The agent could not connect to the replication server on TCP port 1500 because the connection was refused, timed out, or had no route. The agent retries every 30 seconds until it connects.

**Resolution:**

1. Verify that the firewall, route table, and network ACL that you manage allow outbound TCP traffic on port 1500 from the source server to the replication server. See [Verifying TCP port 1500](verifying-network-connectivity.md#comm-1500-verify).

1. AWS Elastic Disaster Recovery opens inbound TCP port 1500 on the security group that it creates for the replication server. If you replaced that security group, verify that your security group allows inbound TCP traffic on port 1500. See [Resolving port 1500 issues](verifying-network-connectivity.md#comm-1500-resolve).

1. If the error persists, contact AWS Support.

## DRS-REPL-004: Authentication with the replication server failed
<a name="error-replication-auth-message-failed"></a>

**Error message:** Error code: DRS-REPL-004 - Authentication with the replication server failed

**Cause:** The agent connected to the replication server on TCP port 1500, but the connection failed while the agent sent or received the authentication message. For example, a firewall, proxy, or other network device between the source server and the replication server interrupted or inspected the TLS connection. The agent retries every 30 seconds.

**Resolution:**

1. Make sure that no firewall, proxy, or inspection device decrypts or interrupts TCP port 1500 traffic between the source server and the replication server. To verify connectivity, see [Verifying TCP port 1500](verifying-network-connectivity.md#comm-1500-verify).

1. If the log shows No available tokens for peer, earlier connection attempts in the same session failed. Fix the network issues first. If this is the only error in the log, contact AWS Support.

1. If authentication still fails, reinstall the agent. If the error returns, contact AWS Support.

## DRS-REPL-005: Cannot reach AWS Elastic Disaster Recovery or load agent credentials
<a name="error-management-transport-failed"></a>

**Error message:** Error code: DRS-REPL-005 - Cannot reach AWS Elastic Disaster Recovery or load agent credentials

**Cause:** A request to AWS Elastic Disaster Recovery failed before the service responded, because the agent could not reach the endpoint or load its credentials. Common causes are DNS resolution failures, blocked outbound TCP port 443, incorrect proxy settings, or an unavailable credential source. The agent keeps running and retries.

**Resolution:**

1. Verify DNS resolution and outbound TCP port 443 connectivity from the source server to the AWS Elastic Disaster Recovery endpoint for the target Region. See [Solving communication problems over TCP port 443 between the source servers and AWS Elastic Disaster Recovery](Network-Requirements.md#Solving-Problems-TCP-443).

1. If the source server uses a proxy, verify the proxy settings.

1. If the agent uses an instance profile, confirm that an instance profile with the required IAM policy is attached. For an agent that you installed with an instance profile, see [Using an instance profile for agent installation in AWS](agent-installations-in-aws.md). For a recovery instance, see [AWS managed policy: AWSElasticDisasterRecoveryRecoveryInstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.md).

1. If the error persists, contact AWS Support.

## DRS-REPL-006: AWS Elastic Disaster Recovery rejected the agent credentials
<a name="error-management-auth-rejected"></a>

**Error message:** Error code: DRS-REPL-006 - AWS Elastic Disaster Recovery rejected the agent credentials

**Cause:** AWS Elastic Disaster Recovery does not recognize the agent's credentials. For example, AWS access keys stored in the agent configuration were deleted or deactivated. Agents installed with the current installer use a certificate instead of stored access keys. After seven days of rejected requests, the agent stops its regular requests and checks the credentials once every 24 hours until they work.

**Resolution:**

1. Reinstall the agent to configure new credentials. See [Reinstalling the agent](reinstalling-agent.md).

1. Confirm that the agent log no longer shows the invalid security token warning and that replication resumes.

**Note**  
With cross-account roles, a missing or misconfigured `DRSCrossAccountAgentAuthorizedRole` role in the account where the instance runs, or `DRSCrossAccountAgentRole` role in the account that the agent replicates to, causes an AWS STS error for the `AssumeRole` request instead of this message. See [Creating the Failback and in-AWS right-sizing roles](adding-trusted-account.md#trusted-accounts-failback-role).

## DRS-REPL-007: Timed out waiting for the failback connection on TCP port 1500
<a name="error-failback-listen-timed-out"></a>

**Error message:** Error code: DRS-REPL-007 - Timed out waiting for the failback connection on TCP port 1500

**Cause:** During failback, the agent on the recovery instance listens on TCP port 1500 for the Failback Client. The agent starts to listen only after the Failback Client finishes configuring the replication software. The Failback Client did not connect within 5 minutes, so the wait timed out. The agent waits 30 seconds and then listens again.

**Resolution:**

1. On the computer that runs the Failback Client, confirm that the Failback Client is still running and check its status. While it connects, it shows Establishing a connection between the Failback Client and the AWS Replication Agent running on the Recovery Instance over port 1500.... When it succeeds, it shows Connection established. Replication in progress.... If it reports a failure, follow the message and see [Failback Client errors](failback-client-errors.md).

1. Confirm that the Failback Client can reach the recovery instance on TCP port 1500. The Failback Client connects to the private IP address of the recovery instance when you choose **Use private IP** in the failback replication settings. Otherwise, it connects to the public IP address. See [Use private IP](recovery-instances-details.md#recovery-instances-details-failback-replication-settings-private-ip). From the Failback Client network, test the connection to that address on TCP port 1500. On Linux:

   ```
   nc -zv {{recovery-instance-ip}} 1500
   ```

   On Windows:

   ```
   Test-NetConnection -ComputerName {{recovery-instance-ip}} -Port 1500
   ```

   If the test connects, the agent can log the DRS-REPL-004 error once. You can ignore that entry. If the test fails, continue with the next step.

1. Confirm that the security group and network ACL for the recovery instance allow inbound TCP traffic on port 1500 from the Failback Client. See [Error: Failed to get recovery instance volumes](failback-client-errors.md#Troubleshooting-Failback-get-volumes). Also verify that your environment meets the requirements in [Failback prerequisites](failback-performing.md#failback-performing-prerequisites).

1. If the error persists, contact AWS Support.

## DRS-REPL-008: Handshake with the replication server failed
<a name="error-replication-handshake-failed"></a>

**Error message:** Error code: DRS-REPL-008 - Handshake with the replication server failed

**Cause:** The TCP port 1500 connection opened and the authentication message was sent. While the agent exchanged version, session, and volume information, the connection closed or reset, or returned no response for 5 minutes. A firewall, proxy, or other network device can reset or drop the connection during this exchange. The replication server can also end the session when AWS Elastic Disaster Recovery does not accept the agent or its replication session. During failback, this error can also occur between a recovery instance and the Failback Client. The agent retries every 30 seconds.

On Windows, this error also occurs if the agent cannot map a replicated volume to a local disk. The log then shows runWindowsDeviceMappingCommand failed.

**Resolution:**

1. If the connection keeps dropping and reconnecting, the agent can log this error repeatedly. First, check whether replication is affected. For a source server, open the **Source servers** page and confirm that **Data replication status** is **Healthy** and that lag is not growing. See [Interacting with the Source Servers page](interracting.md). For failback, open the recovery instance details page and check the **Data replication status** panel. See [Data replication status](recovery-instances-details.md#recovery-instances-details-failback-dashboard-data-replication). You can also search the agent log for Connected to replicator after the error. If replication is healthy and lag is not growing, no action is needed.

1. This error happens after the TCP port 1500 connection opens, so a test that only checks whether the port is reachable passes. Instead, check your firewall, proxy, and intrusion prevention logs for TCP port 1500 connections that were reset or dropped after they opened. Exclude TCP port 1500 traffic from deep packet inspection on those devices.

1. If the replication server ended the session, the agent gets new connection details from AWS Elastic Disaster Recovery on its next attempt. If the error continues and replication does not resume, contact AWS Support.

1. On Windows, if the log shows runWindowsDeviceMappingCommand failed, the agent could not map a replicated volume to a local disk. Collect diagnostic information and contact AWS Support. See [Gather diagnostic information for support](agent-diagnostics.md#agent-diagnostic-tools).

## DRS-REPL-009: Agent ran out of memory and restarted
<a name="error-agent-out-of-memory"></a>

**Error message:** Error code: DRS-REPL-009 - Agent ran out of memory and restarted

**Cause:** The agent process ran out of memory and exited. The service manager restarts the agent after 30 seconds, and replication resumes. The agent sets its maximum memory based on the memory of the server. On some out-of-memory errors, the Java runtime can write a `client.hprof` file to the agent directory. This file contains a copy of the agent memory and can include sensitive data.

**Resolution:**

1. The agent restarts after this error, and replication resumes. To count how many times the error occurred, search the agent log for the error code. On Linux:

   ```
   sudo grep "DRS-REPL-009" /var/lib/aws-replication-agent/agent.log.0
   ```

   On Windows, in PowerShell run as an administrator:

   ```
   Select-String -Pattern "DRS-REPL-009" -Path "C:\Program Files (x86)\AWS Replication Agent\agent.log.0"
   ```

   If the agent does not log error codes, search for OutOfMemoryError instead. On Linux, you can also run `systemctl status aws-replication-agent` to see when the agent last started. If the error appears once and the console shows replication as **Healthy**, no action is needed.

1. If the error appears more than once, collect diagnostic information and contact AWS Support. See [Gather diagnostic information for support](agent-diagnostics.md#agent-diagnostic-tools). In your case, include the kind of OutOfMemoryError from the agent log, for example Java heap space or unable to create new native thread.

1. If a `client.hprof` file is present, tell AWS Support in your case and wait for instructions on how to share it. The file is at `/var/lib/aws-replication-agent/client.hprof` on Linux and `C:\Program Files (x86)\AWS Replication Agent\client.hprof` on Windows, in the same folder as `agent.log.0`. The Java runtime does not overwrite an existing `client.hprof` file, so check the file timestamp to confirm that it is from the latest error. Because this file can include sensitive data, delete it after you share it.