

# Replication errors: agent log messages
<a name="agent-runtime-errors"></a>

This topic covers messages that the AWS Replication Agent writes to its own log on the source server. The other topics in this section cover replication errors that AWS Elastic Disaster Recovery reports in the console. Use this topic when the console shows no specific error, or to find the cause behind one. To find the agent log, see [Check agent status and logs](agent-diagnostics.md#agent-log-locations).

**Topics**
+ [Error: Server identity changed and no matching recovery instance was found](#error-agent-identity-changed)
+ [Error: Replication driver failed to load at agent startup](#error-driver-load-failed-startup)
+ [Error: Cannot connect to the replication server on TCP port 1500](#error-replication-server-connect-failed)
+ [Error: Authentication with the replication server failed](#error-replication-auth-message-failed)
+ [Error: Cannot reach AWS Elastic Disaster Recovery or load agent credentials](#error-management-transport-failed)
+ [Error: AWS Elastic Disaster Recovery rejected the agent credentials](#error-management-auth-rejected)

## Error: Server identity changed and no matching recovery instance was found
<a name="error-agent-identity-changed"></a>

**Error message:** A message that starts with Server identity changed from and ends with and didn't find a Recovery Instance id - Exiting

**Cause:** At startup, the agent detected that the server identity changed and found no matching recovery instance. This happens when:
+ A disk with the agent installed was cloned, migrated, or restored onto a different server.
+ On the same server, the agent cannot detect or read the identifier that it recorded at installation: the MAC address, the VMware UUID, or the Google Cloud instance ID. For example, it cannot read the VMware UUID from the system BIOS information or reach the Google Cloud metadata server.
+ On a recovery instance, the agent could not confirm with AWS Elastic Disaster Recovery that the instance is a recovery instance. For example, the instance has no instance profile with the required permissions, cannot reach AWS Elastic Disaster Recovery over TCP port 443, or is not a recovery instance in this AWS account and Region.

The process exits after 60 seconds, and the service manager restarts it. Replication does not start.

**Resolution:**
+ On a recovery instance, verify the instance profile policy and TCP port 443 access to AWS Elastic Disaster Recovery. See [AWS managed policy: AWSElasticDisasterRecoveryRecoveryInstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.md). The agent checks again after it restarts. If the error persists, reinstall the agent as a recovery instance. This procedure first disconnects the instance from AWS. See [Reinstalling the agent on a recovery instance](reinstalling-agent.md#reinstalling-agent-recovery-instance).
+ On a server that was cloned, migrated, or restored, or whose identifier changed, reinstall the agent so that it registers as its own source server. See [Reinstalling the agent](reinstalling-agent.md).
+ If the identity changed unexpectedly, contact AWS Support.

## Error: Replication driver failed to load at agent startup
<a name="error-driver-load-failed-startup"></a>

**Error message:** Load module failed

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

## Error: Cannot connect to the replication server on TCP port 1500
<a name="error-replication-server-connect-failed"></a>

**Error message:** Error creating connection or Connecting to replicator, together with a network message such as Connection refused, connect timed out, or No route to host.

**Cause:** The agent could not connect to the replication server on TCP port 1500 because the connection was refused, timed out, or had no route. The agent retries every 30 seconds until it connects.

**Resolution:**

1. Verify that the firewall, route table, and network ACL that you manage allow outbound TCP traffic on port 1500 from the source server to the replication server. See [Verifying TCP port 1500](verifying-network-connectivity.md#comm-1500-verify).

1. AWS Elastic Disaster Recovery opens inbound TCP port 1500 on the security group that it creates for the replication server. If you replaced that security group, verify that your security group allows inbound TCP traffic on port 1500. See [Resolving port 1500 issues](verifying-network-connectivity.md#comm-1500-resolve).

1. If the error persists, contact AWS Support.

## Error: Authentication with the replication server failed
<a name="error-replication-auth-message-failed"></a>

**Error message:** Error creating connection, followed by a stack trace that mentions sending or receiving the authentication message.

**Cause:** The agent connected to the replication server on TCP port 1500, but the connection failed while the agent sent or received the authentication message. For example, a firewall, proxy, or other network device between the source server and the replication server interrupted or inspected the TLS connection. The agent retries every 30 seconds.

**Resolution:**

1. Make sure that no firewall, proxy, or inspection device decrypts or interrupts TCP port 1500 traffic between the source server and the replication server. To verify connectivity, see [Verifying TCP port 1500](verifying-network-connectivity.md#comm-1500-verify).

1. If the log shows No available tokens for peer, earlier connection attempts in the same session failed. Fix the network issues first. If this is the only error in the log, contact AWS Support.

1. If authentication still fails, reinstall the agent. If the error returns, contact AWS Support.

## Error: Cannot reach AWS Elastic Disaster Recovery or load agent credentials
<a name="error-management-transport-failed"></a>

**Error message:** Exception was thrown by the client when trying to ...

**Cause:** A request to AWS Elastic Disaster Recovery failed before the service responded, because the agent could not reach the endpoint or load its credentials. Common causes are DNS resolution failures, blocked outbound TCP port 443, incorrect proxy settings, or an unavailable credential source. The agent keeps running and retries.

**Resolution:**

1. Verify DNS resolution and outbound TCP port 443 connectivity from the source server to the AWS Elastic Disaster Recovery endpoint for the target Region. See [Solving communication problems over TCP port 443 between the source servers and AWS Elastic Disaster Recovery](Network-Requirements.md#Solving-Problems-TCP-443).

1. If the source server uses a proxy, verify the proxy settings.

1. If the agent uses an instance profile, confirm that an instance profile with the required IAM policy is attached. For an agent that you installed with an instance profile, see [Using an instance profile for agent installation in AWS](agent-installations-in-aws.md). For a recovery instance, see [AWS managed policy: AWSElasticDisasterRecoveryRecoveryInstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.md).

1. If the error persists, contact AWS Support.

## Error: AWS Elastic Disaster Recovery rejected the agent credentials
<a name="error-management-auth-rejected"></a>

**Error message:** A message that starts with Request to and includes The security token included in the request is invalid.

**Cause:** AWS Elastic Disaster Recovery does not recognize the agent's credentials. For example, AWS access keys stored in the agent configuration were deleted or deactivated. Agents installed with the current installer use a certificate instead of stored access keys. After seven days of rejected requests, the agent stops its regular requests and checks the credentials once every 24 hours until they work.

**Resolution:**

1. Reinstall the agent to configure new credentials. See [Reinstalling the agent](reinstalling-agent.md).

1. Confirm that the agent log no longer shows the invalid security token warning and that replication resumes.

**Note**  
With cross-account roles, a missing or misconfigured `DRSCrossAccountAgentAuthorizedRole` role in the account where the instance runs, or `DRSCrossAccountAgentRole` role in the account that the agent replicates to, causes an AWS STS error for the `AssumeRole` request instead of this message. See [Creating the Failback and in-AWS right-sizing roles](adding-trusted-account.md#trusted-accounts-failback-role).