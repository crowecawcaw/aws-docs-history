

# Failback replication errors
<a name="failback-replication-errors"></a>

The following errors can occur during reverse replication (failback data sync) in AWS Elastic Disaster Recovery. Each section describes the error message, its cause, and the resolution steps.

**Topics**
+ [Error: AWS Replication Agent is not connected to DRS](#failback-error-agent-not-connected)
+ [Error: Credential retrieval failed (clock skew)](#failback-error-credential-retrieval)
+ [Error: Some recovery instances could not be processed](#failback-error-recovery-instances-not-processed)

## Error: AWS Replication Agent is not connected to DRS
<a name="failback-error-agent-not-connected"></a>

**Error message**

AWS Replication agent is not connected to DRS. Verify the agent is installed and running, and that it has connectivity to the service

**Cause**

After you initiate reverse replication, the agent on the recovery instance cannot communicate with the AWS Elastic Disaster Recovery service.

**Resolution**

To resolve this error, complete the following steps:

1. Verify that the agent is installed and running on the recovery instance. Run the following command for your operating system:
   + Linux:

     ```
     systemctl status aws-replication-agent
     ```
   + Windows:

     ```
     Get-Service AwsReplicationService
     ```

1. Verify that the recovery instance has internet connectivity or a NAT gateway connection.

1. If both the agent and connectivity are confirmed working, reinstall the agent as a recovery instance and retry reverse replication.

## Error: Credential retrieval failed (clock skew)
<a name="failback-error-credential-retrieval"></a>

**Error message**

botocore.exceptions.CredentialRetrievalError: Error when retrieving credentials from cert

**Cause**

The Failback Client uses Amazon Linux 2 and certificate-based authentication. Amazon Linux 2 assumes the hardware clock is set to UTC. If the BIOS or EFI clock is set to local time instead of UTC, authentication fails because of time skew.

**Resolution**

To resolve this error, complete the following steps:

1. Access the BIOS or EFI Shell of the failback target server.

1. Set the hardware clock to UTC (not local time).

1. Restart the Failback Client.

**Note**  
This error commonly occurs when failing back to physical servers or hypervisors where the hardware clock was configured for local time.

## Error: Some recovery instances could not be processed
<a name="failback-error-recovery-instances-not-processed"></a>

**Error message**

Some Recovery instances could not be processed: {{recovery-instance-id}}

**Cause**

This error occurs during reverse replication when both of the following conditions are true:
+ The **Launch into source instance** setting is enabled in the source Region's default launch settings.
+ The source Amazon EC2 instance is missing the required tag `AWSDRS:AllowLaunchingIntoThisInstance`.

**Resolution**

To resolve this error, use one of the following options:
+ **Option 1** – Disable the **Launch into source instance** setting in the source Region's default launch settings.
+ **Option 2** – Add the tag `AWSDRS:AllowLaunchingIntoThisInstance` to the source Amazon EC2 instance.

**Note**  
Review the impact before you disable **Launch into source instance**. This setting affects all future recovery launches for the account in this Region.