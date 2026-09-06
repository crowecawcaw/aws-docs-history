

# Failback Client errors
<a name="failback-client-errors"></a>

The following topics cover errors that you might encounter when you set up or connect the Failback Client in AWS Elastic Disaster Recovery (Elastic Disaster Recovery).

**Topics**
+ [Error: Could not associate failback client to recovery instances](#Troubleshooting-Failback-Errors-credentials)
+ [Error: Could not discover account ID](#Troubleshooting-Failback-discover-account)
+ [Error: Failed to get recovery instance volumes](#Troubleshooting-Failback-get-volumes)
+ [Error: Failback client not seen](#Troubleshooting-Failback-client-not-seen)
+ [Error: Could not verify recovery instance connectivity to DRS](#Troubleshooting-Failback-Errors-connectivity-instance)

## Error: Could not associate failback client to recovery instances
<a name="Troubleshooting-Failback-Errors-credentials"></a>

**Error message:** Could not associate failback client to recovery instances

**Cause:** The IAM credentials used for the Failback Client do not have the required failback policy attached.

**Resolution:**

**To resolve this error**

1. Attach the `AWSElasticDisasterRecoveryFailbackInstallationPolicy` managed policy to the IAM user or role.

1. Restart the failback process.

For more information, see [Learn more about Failback Client credentials](failback-performing.md#failback-performing-credentials).

## Error: Could not discover account ID
<a name="Troubleshooting-Failback-discover-account"></a>

**Error message:** Could not discover account id from describe

**Cause:** The AWS credentials or Region entered into the Failback Client are incorrect.

**Resolution:**

**To resolve this error**

1. Verify that the AWS Access Key ID and Secret Access Key are correct and active.

1. Verify that the Region matches the Region where Elastic Disaster Recovery is configured.

1. Test the credentials by running the following command:

   ```
   aws sts get-caller-identity --region {{region}}
   ```

## Error: Failed to get recovery instance volumes
<a name="Troubleshooting-Failback-get-volumes"></a>

**Error message:** Failed to get recovery instance volumes, please check the network configuration of your recovery instance

**Cause:** The Failback Client cannot communicate with the recovery instance on TCP port 1500.

**Resolution:**

**To resolve this error**

1. Verify that TCP port 1500 is open between the failback server and the recovery instance.

1. If you are not using a private route (VPN or ), verify that the recovery instance has a public IP address.

1. Test connectivity to the recovery instance on port 1500:
   + **Linux:**

     ```
     nc -zv {{recovery-instance-ip}} 1500
     ```
   + **Windows (PowerShell):**

     ```
     Test-NetConnection -ComputerName {{recovery-instance-ip}} -Port 1500
     ```

## Error: Failback client not seen
<a name="Troubleshooting-Failback-client-not-seen"></a>

**Error message:** Failback client not seen status in the Elastic Disaster Recovery console.

**Cause:** Communication between the Failback Client and the Elastic Disaster Recovery endpoint has been interrupted. Common causes include:
+ Network issues between the Failback Client and the Elastic Disaster Recovery endpoint (TCP 443)
+ The Failback Client process was terminated or interrupted
+ The Failback Client runs in the foreground — closing the shell session terminates the process

**Resolution:**

**To resolve this error**

1. Verify network connectivity to `drs.{{region}}.amazonaws.com` on port 443.

1. Use `screen` or `tmux` to keep the Failback Client session alive.

1. Restart the Failback Client if needed.

**Note**  
Replication might continue in the background because the AWS Replication Agent runs independently of the Failback Client process.

## Error: Could not verify recovery instance connectivity to DRS
<a name="Troubleshooting-Failback-Errors-connectivity-instance"></a>

**Error message:** Could not verify recovery instance connectivity to Elastic Disaster Recovery

**Cause:** The recovery instance cannot communicate with the AWS Elastic Disaster Recovery endpoint on TCP port 443.

**Resolution:**

------
#### [ Console ]

**To resolve this error (console)**

1. Verify that the recovery instance has a public IP address. If you use a VPN or , a public IP is not required.

1. Verify that the security group attached to the recovery instance allows outbound traffic on TCP port 443.

1. Check the agent logs for connectivity errors.

------
#### [ CLI ]

**To resolve this error (CLI)**

1. Verify the recovery instance network configuration:

   ```
   aws ec2 describe-instances --instance-ids {{instance-id}} \
       --query "Reservations[*].Instances[*].[PublicIpAddress,SecurityGroups]"
   ```

1. Test connectivity from the recovery instance to the Elastic Disaster Recovery endpoint:
   + **Linux:**

     ```
     curl -v https://drs.{{region}}.amazonaws.com
     ```
   + **Windows (PowerShell):**

     ```
     Test-NetConnection -ComputerName drs.{{region}}.amazonaws.com -Port 443
     ```

1. Check the agent logs for errors:

   ```
   tail /var/lib/aws-replication-agent/agent.log.0 | grep error
   ```

------

If the agent log shows a "driver compiled for different kernel" error, see [Troubleshoot driver compilation errors](agent-install-linux-errors.md#error-driver-compiled).