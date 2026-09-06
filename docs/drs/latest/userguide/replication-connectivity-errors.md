

# Replication errors: agent communication
<a name="replication-connectivity-errors"></a>

The following errors occur when network connectivity issues prevent communication between the AWS Replication Agent, replication server, and AWS Elastic Disaster Recovery service endpoints. Each section describes the error, its cause, and resolution steps.

**Topics**
+ [Error: Agent not seen](#common-agent-not-seen)
+ [Error: Failed to authenticate with service](#common-failed-authenticate-service)
+ [Error: Failed to connect agent to replication software](#common-connection-agent-replication-software)
+ [Error: Failed to establish communication with replication software](#common-establish-communication-replication-software)
+ [Error: Failed to connect agent to replication server](#common-failed-connect-agent-replication-server)
+ [Error: Unstable network](#common-unstable-network)
+ [Error: Failback client not seen (replication)](#common-failback-not-seen)

## Error: Agent not seen
<a name="common-agent-not-seen"></a>

**Error code:** AGENT\_NOT\_SEEN

The source server shows a **Disconnected** status in the AWS Elastic Disaster Recovery console.

**Cause:** The AWS Elastic Disaster Recovery service has lost communication with the AWS Replication Agent on the source server.

**Resolution:**

------
#### [ Console ]

**To resolve agent not seen errors (console)**

1. Open the AWS Elastic Disaster Recovery console and check the source server status.

1. Verify that the AWS Replication Agent is running on the source server.
   + **Linux:** Run `systemctl status aws-replication-agent`.
   + **Windows:** Open Services and verify that the **AWS Replication Agent** service is running.

1. Verify that the source server can reach the AWS Elastic Disaster Recovery endpoint on TCP port 443.

------
#### [ CLI ]

**To resolve agent not seen errors (CLI)**

1. Run the following command to check the source server state:

   ```
   aws drs describe-source-servers \
       --filters sourceServerIDs={{source-server-id}} \
       --query "items[0].{State:dataReplicationInfo.dataReplicationState,Error:dataReplicationInfo.dataReplicationError.error,LastSeen:lastLaunchedInstance}"
   ```

1. Verify that the agent is running on the source server.
   + **Linux:**

     ```
     systemctl status aws-replication-agent
     ```
   + **Windows:**

     ```
     Get-Service -Name AwsReplicationService
     ```

1. Test TCP 443 connectivity to the AWS Elastic Disaster Recovery endpoint.
   + **Linux:**

     ```
     curl -v https://drs.{{region}}.amazonaws.com
     ```
   + **Windows:**

     ```
     Test-NetConnection -ComputerName drs.{{region}}.amazonaws.com -Port 443
     ```

------

**Note**  
If this error appears on the recovery dashboard, verify that the `AWSElasticDisasterRecoveryRecoveryInstancePolicy` managed policy is associated with the recovery instance IAM role.

## Error: Failed to authenticate with service
<a name="common-failed-authenticate-service"></a>

**Error code:** FAILED\_TO\_AUTHENTICATE\_WITH\_SERVICE

**Cause:** The replication server cannot reach the AWS Elastic Disaster Recovery endpoint on TCP port 443. This is a staging area network issue.

**Resolution:**

------
#### [ Console ]

**To resolve authentication errors (console)**

1. Open the AWS Elastic Disaster Recovery console and check the staging area subnet configuration for the affected source server.

1. Launch a test Amazon EC2 instance in the staging area subnet.

1. From the test instance, verify TCP 443 connectivity to the AWS Elastic Disaster Recovery endpoint (`drs.{{region}}.amazonaws.com`).

------
#### [ CLI ]

**To resolve authentication errors (CLI)**

1. Run the following command to retrieve the staging area network configuration:

   ```
   aws drs get-replication-configuration \
       --source-server-id {{source-server-id}} \
       --query "{Subnet:stagingAreaSubnetId,SGs:stagingAreaTags}"
   ```

1. Launch a test instance in the staging area subnet and verify TCP 443 connectivity to `drs.{{region}}.amazonaws.com`.

------

## Error: Failed to connect agent to replication software
<a name="common-connection-agent-replication-software"></a>

**Error code:** FAILED\_TO\_PAIR\_AGENT\_WITH\_REPLICATION\_SOFTWARE

**Cause:** AWS Elastic Disaster Recovery cannot provide the replication server and agent with the information they need to communicate. This indicates a network connectivity issue between the agent, replication server, and the AWS Elastic Disaster Recovery endpoint.

**Resolution:**

**To resolve agent pairing errors**

1. Verify network connectivity between the source server (where the agent runs) and the replication server in the staging area.

1. Verify that both the source server and the replication server can reach the AWS Elastic Disaster Recovery endpoint on TCP port 443.

1. If the issue persists, contact AWS Support.

## Error: Failed to establish communication with replication software
<a name="common-establish-communication-replication-software"></a>

**Error code:** FAILED\_TO\_ESTABLISH\_AGENT\_REPLICATOR\_SOFTWARE\_COMMUNICATION

**Cause:** Network connectivity issues exist between the agent and the replication server.

**Resolution:**

**To resolve communication errors**

1. Verify network connectivity between the agent on the source server, the replication server in the staging area, and the AWS Elastic Disaster Recovery endpoint.

1. Verify that TCP port 1500 is open between the source server and the replication server.

**Important**  
During failback, verify that TCP port 1500 is open for inbound traffic on the recovery instance security group.

## Error: Failed to connect agent to replication server
<a name="common-failed-connect-agent-replication-server"></a>

**Error code:** FAILED\_TO\_CONNECT\_AGENT\_TO\_REPLICATION\_SERVER

**Cause:** The agent cannot establish a data replication connection with the replication server over TCP port 1500.

**Resolution:**

------
#### [ Console ]

**To resolve replication server connection errors (console)**

1. Open the Amazon EC2 console and locate the security group associated with the staging area replication server.

1. Verify that the security group allows inbound TCP traffic on port 1500.

1. Check the network ACL for the staging area subnet to confirm it allows inbound TCP traffic on port 1500.

------
#### [ CLI ]

**To resolve replication server connection errors (CLI)**

1. Retrieve the security group IDs for the replication configuration:

   ```
   aws drs get-replication-configuration \
       --source-server-id {{source-server-id}} \
       --query "replicationServersSecurityGroupsIDs"
   ```

1. Verify that the security group allows inbound TCP port 1500:

   ```
   aws ec2 describe-security-groups \
       --group-ids {{sg-id}} \
       --query "SecurityGroups[].IpPermissions[?FromPort==`1500`]"
   ```

1. Test connectivity to the replication server on port 1500.
   + **Linux:**

     ```
     nc -zv {{replication-server-ip}} 1500
     ```
   + **Windows:**

     ```
     Test-NetConnection -ComputerName {{replication-server-ip}} -Port 1500
     ```

------

## Error: Unstable network
<a name="common-unstable-network"></a>

**Error code:** UNSTABLE\_NETWORK

**Cause:** Network connectivity between the source server and the replication server is intermittent.

**Resolution:**

**To resolve unstable network errors**

1. Verify that network connectivity between the source server and replication server is stable.

1. Run the [network bandwidth test](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test) to identify bandwidth or latency issues.

## Error: Failback client not seen (replication)
<a name="common-failback-not-seen"></a>

**Error code:** FAILBACK\_CLIENT\_NOT\_SEEN

**Cause:** A network connectivity issue is preventing the Failback Client from communicating with the AWS Elastic Disaster Recovery endpoint.

**Resolution:**

**To resolve Failback Client connectivity errors**

1. Verify that the Failback Client can reach the AWS Elastic Disaster Recovery endpoint on TCP port 443 (`drs.{{region}}.amazonaws.com`).

1. Check security group rules and network ACLs to confirm outbound TCP 443 traffic is allowed.

For more information, see [Failback Client troubleshooting](failback-client-errors.md#Troubleshooting-Failback-client-not-seen).