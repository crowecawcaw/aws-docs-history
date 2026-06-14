# Troubleshooting Failback Errors

###### Topics

- [Error – Could not associate failback client to recovery instances](#Troubleshooting-Failback-Errors-credentials "#Troubleshooting-Failback-Errors-credentials")
- [Error – Could not verify recovery instance connectivity to DRS](#Troubleshooting-Failback-Errors-connectivity-instance "#Troubleshooting-Failback-Errors-connectivity-instance")
- [Error message: AWS Replication agent is not connected to DRS. Verify the agent is installed and running, and that it has connectivity to the service](#w2aac39c17b9 "#w2aac39c17b9")
- [Error message: botocore.exceptions.CredentialRetrievalError: Error when retrieving credentials from cert](#w2aac39c17c11 "#w2aac39c17c11")
- [Error message: Some Recovery instances could not be processed: recovery-instance-id](#w2aac39c17c13 "#w2aac39c17c13")
- [Error: Could not discover account id from describe](#Troubleshooting-Failback-discover-account "#Troubleshooting-Failback-discover-account")
- [Error: Failed to get recovery instance volumes](#Troubleshooting-Failback-get-volumes "#Troubleshooting-Failback-get-volumes")
- [Failback client not seen](#Troubleshooting-Failback-client-not-seen "#Troubleshooting-Failback-client-not-seen")

## Error – Could not associate failback client to recovery instances

If you see the "Could not associate failback client to recovery instances" error
when using the Failback Client, that may mean that you associated the incorrect
credentials with your User. Ensure that you attach the **AWSElasticDisasterRecoveryFailbackInstallationPolicy** policy to the
user or role and restart the failback process. [Learn more about Failback Client
credentials.](failback-performing.md#failback-performing-credentials "failback-performing.md#failback-performing-credentials")

## Error – Could not verify recovery instance connectivity to DRS

If you see the "Could not verify recovery instance connectivity to Elastic
Disaster Recovery" error when using the Failback Client, you should troubleshoot
potential connectivity issues:

1. Make sure that the agent on the recovery instance is activated and
   running.
2. If not using a private route (VPN or Direct Connect), ensure that a
   public IP is set on the recovery instance in Amazon EC2.
3. TCP Port 443 outbound must be open on the recovery instance for the
   pairing to succeed.
4. Make sure that you don't have this error in your agent logs: [Error – driver was compiled for a
   different kernel not loading](troubleshooting-agent-issues.md#error-driver-compiled "troubleshooting-agent-issues.md#error-driver-compiled").

Console

###### Verify recovery instance connectivity

1. In the Amazon EC2 Console, select the recovery instance. If you are
   not using a private route (VPN or Direct Connect), verify that
   the instance has a public IP assigned.
2. Check the security group associated with the recovery instance
   to ensure outbound TCP 443 is allowed to the AWS Elastic Disaster Recovery regional
   endpoint.
3. Connect to the recovery instance and check the agent logs for
   connectivity errors:

   - **Linux:**
     `/var/lib/aws-replication-agent/agent.log.0`
   - **Windows:**
     `C:\Program Files (x86)\AWS Replication Agent\agent.log.0`

CLI

###### Verify recovery instance connectivity

1. Check the recovery instance network configuration and security
   groups:

```
aws ec2 describe-instances \
  --instance-ids `i-1234567890abcdefg` \
  --query 'Reservations[0].Instances[0].{PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress,SubnetId:SubnetId,SecurityGroups:SecurityGroups[*].GroupId}'
```

If you are not using a private route, verify that
`PublicIP` is not null. 2. From the recovery instance, test port 443 connectivity to the
DRS endpoint:

    * **Linux:**



    ```
    curl -v https://drs.`region`.amazonaws.com 2>&1 | head -20
    ```
    * **Windows (PowerShell):**



    ```
    Test-NetConnection -ComputerName drs.`region`.amazonaws.com -Port 443
    ```

3. Check the agent logs on the recovery instance for errors:

   - **Linux:**

   ```
   tail -100 /var/lib/aws-replication-agent/agent.log.0 | grep -i "error\|fail\|connect"
   ```
   - **Windows (PowerShell):**

   ```
   Select-String -Path "C:\Program Files (x86)\AWS Replication Agent\agent.log.0" -Pattern "error|fail|connect" -CaseSensitive:$false | Select-Object -Last 100
   ```

## Error message: AWS Replication agent is not connected to DRS. Verify the agent is installed and running, and that it has connectivity to the service

In certain cases, following an attempt to perform a reverse replication action,
you will receive an error message indicating that the AWS Replication agent is not
connected to AWS Elastic Disaster Recovery. In this case, verify that:

1. The agent is installed and running
2. The server is connected to the internet or the NAT gateway

If after performing the steps above you did not identify any agent or connectivity issues,
reinstall the agent as a recovery instance and try again.

## Error message: botocore.exceptions.CredentialRetrievalError: Error when retrieving credentials from cert

The Failback Client uses Amazon Linux 2 (AL2) and leverages certificate-based authentication to AWS Elastic Disaster Recovery endpoints for
certain actions. AL2 assumes that the hardware clock time provided from the underlying hardware or hypervisor is UTC, which can
result in time skew if it is not. Ensure that the time configured within the BIOS or EFI Shell of the
failback target is set to UTC, and not LocalTime.

## Error message: Some Recovery instances could not be processed: `recovery-instance-id`

You may receive this error when attempting to start reverse replication in Elastic Disaster Recovery. The error occurs when:

- The **Launch into source instance** setting is enabled in the source Region's default launch settings.
- Source Amazon EC2 instance/A1 is missing the required tag `AWSDRS:AllowLaunchingIntoThisInstance`.

Resolve this issue by:

###### Note

Review the impact of these changes on your launch configuration before
proceeding. Disabling **Launch into source instance** affects
all future recovery launches for the account in this Region.

- Disabling the **Launch into source instance** in the source Region's default launch settings.
- Adding the `AWSDRS:AllowLaunchingIntoThisInstance` tag to the source Amazon EC2 instance/A1.

## Error: Could not discover account id from describe

If you see this error when using the Failback Client:

- Verify that the AWS Access Key ID and AWS Secret Access Key are correct.
- Verify that you are entering the correct AWS Region when prompted.

## Error: Failed to get recovery instance volumes

If you see "Failed to get recovery instance volumes, please check the network
configuration of your recovery instance":

- Verify that the Failback Client can communicate with the Recovery Instance
  on TCP port 1500, either via a private route (VPN/Direct Connect) or a public route
  (public IP on the Recovery Instance).
- Test connectivity between the failback server and the Recovery Instance.

## Failback client not seen

This error in the AWS Elastic Disaster Recovery console indicates that communication between the
Failback Client and the AWS Elastic Disaster Recovery endpoint has been interrupted. Possible causes:

- Network issues between the Failback Client and the AWS Elastic Disaster Recovery endpoint.
- The Failback Client process was interrupted or terminated.
- The Failback Client runs in the foreground. If the shell session is closed,
  the process will be interrupted. Use tools like `screen` or `tmux`
  to keep the session active.

###### Note

Replication may continue in the background since the AWS Replication Agent
runs independently of the Failback Client process.
