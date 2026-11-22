

# Failback replication errors

The following errors can occur during reverse replication (failback data sync) in AWS Elastic Disaster Recovery. Each section describes the error message, its cause, and the resolution steps.

For more information about the `DRS-FAILBACK-003` error (credential retrieval failed), see [DRS-FAILBACK-003: Credential retrieval failed](failback-client-errors.md#Troubleshooting-Failback-credential-retrieval).

**Topics**
+ [AWS Replication Agent is not connected to DRS](#failback-error-agent-not-connected)
+ [Some recovery instances could not be processed](#failback-error-recovery-instances-not-processed)

## AWS Replication Agent is not connected to DRS
<a name="failback-error-agent-not-connected"></a>

**Error message:** `AWS Replication agent is not connected to DRS. Verify the agent is installed and running, and that it has connectivity to the service`

**Cause:** After you initiate reverse replication, the agent on the recovery instance cannot communicate with the AWS Elastic Disaster Recovery service.

**Resolution:** To resolve this error, complete the following steps.

1. Verify that the agent is installed and running on the recovery instance. Run the following command for your operating system:
   + Linux:

     ```bash
     systemctl status aws-replication-agent
     ```
   + Windows:

     ```powershell
     Get-Service AwsReplicationService
     ```

1. Verify that the recovery instance has internet connectivity or a NAT gateway connection.

1. If both the agent and connectivity are confirmed working, reinstall the agent as a recovery instance, and then retry reverse replication.

## Some recovery instances could not be processed
<a name="failback-error-recovery-instances-not-processed"></a>

**Error message:** `Some Recovery instances could not be processed: {{recovery-instance-id}}`

**Cause:** This error occurs during reverse replication when both of the following conditions are true:
+ The **Launch into source instance** setting is enabled in the source Region's default launch settings.
+ The source Amazon EC2 instance is missing the required tag `AWSDRS:AllowLaunchingIntoThisInstance`.

**Resolution:** To resolve this error, use one of the following options.
+ Disabling **Launch into source instance** affects all future recovery launches for the account in this Region. Use Option 1 only if that outcome is acceptable.

  **Option 1**: Disable the **Launch into source instance** setting in the source Region's default launch settings.
+ **Option 2**: Add the tag `AWSDRS:AllowLaunchingIntoThisInstance` to the source Amazon EC2 instance.