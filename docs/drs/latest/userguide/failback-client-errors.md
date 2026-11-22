

# Failback Client errors

The following topics cover errors that you might encounter when you set up or connect the Failback Client in AWS Elastic Disaster Recovery (Elastic Disaster Recovery).

**Topics**
+ [DRS-FAILBACK-001: Could not associate failback client to recovery instance](#Troubleshooting-Failback-Errors-credentials)
+ [DRS-FAILBACK-002: Could not discover account ID](#Troubleshooting-Failback-discover-account)
+ [DRS-FAILBACK-003: Credential retrieval failed](#Troubleshooting-Failback-credential-retrieval)
+ [DRS-FAILBACK-004: Recovery instance not found](#Troubleshooting-Failback-recovery-instance-not-found)
+ [DRS-FAILBACK-005: Manifest download timed out](#Troubleshooting-Failback-manifest-download-timed-out)
+ [DRS-FAILBACK-006: Failback Client assets download failed](#Troubleshooting-Failback-assets-download-failed)
+ [DRS-FAILBACK-007: Failed to get recovery instance volumes](#Troubleshooting-Failback-get-volumes)
+ [DRS-FAILBACK-008: Could not verify recovery instance connectivity](#Troubleshooting-Failback-Errors-connectivity-instance)
+ [DRS-FAILBACK-009: Could not establish replication connection to recovery instance](#Troubleshooting-Failback-replication-connection)
+ [DRS-FAILBACK-010: Failed to download replication software](#Troubleshooting-Failback-download-replication-software)
+ [Failback client not seen](#Troubleshooting-Failback-client-not-seen)

## DRS-FAILBACK-001: Could not associate failback client to recovery instance
<a name="Troubleshooting-Failback-Errors-credentials"></a>

**Error message:** `Error code: DRS-FAILBACK-001 - Could not associate failback client to recovery instance`

**Cause:** The Failback Client couldn't associate the failback server with a recovery instance. This happens when:
+ The recovery instance ID is missing or doesn't match a recovery instance in the account and Region of the credentials that you entered. If you ran the Failback Client with `--no-prompt` and didn't provide an ID, the Failback Client can find the recovery instance on its own only when the failback server is the original source server.
+ The credentials don't have the permissions in the `AWSElasticDisasterRecoveryFailbackInstallationPolicy` managed policy.
+ The source server was an Amazon EC2 instance, which fails back with reverse replication instead of the Failback Client.

**Resolution:** To resolve this error, complete the following steps.

1. Copy the recovery instance ID from the **Recovery instances** page of the Elastic Disaster Recovery console in the Region that you recovered into.

1. Verify that the credentials and Region that you entered match the account and Region of that recovery instance.

1. Attach the `AWSElasticDisasterRecoveryFailbackInstallationPolicy` managed policy to your IAM user or role.

1. If the source server was an Amazon EC2 instance, fail it back with reverse replication instead of the Failback Client. For instructions on failing back an Amazon EC2 source server, see [Performing a cross-Region failback](failback-failover-region-region.md), [Performing a cross-account failback](failback-failover-cross-account.md), or [Cross Availability Zone recovery](failback-failover-cross-availability-zone-failback.md).

1. Retry the association.  
**If the Failback Client asks for a recovery instance ID**  
If the ID was wrong, enter the correct ID, or the number of the recovery instance in the list. If you attached the policy, enter the same ID again. If the credentials or Region were wrong, or the source server was an Amazon EC2 instance, stop the Failback Client and follow the preceding steps.  
**If you ran the Failback Client with `--no-prompt`**  
Run it again with `--recovery-instance-id` set to the ID, or run it without `--no-prompt`. For more information, see [Failback Client program arguments](failback-performing.md#failback-failover-program-arguments).

1. If the error continues, contact AWS Support.

For more information, see [Failback AWS credentials](failback-performing.md#failback-performing-credentials).

## DRS-FAILBACK-002: Could not discover account ID
<a name="Troubleshooting-Failback-discover-account"></a>

**Error message:** `Error code: DRS-FAILBACK-002 - Could not discover account ID`

**Cause:** The Failback Client found no source servers or recovery instances in the Region with the credentials that you entered. This happens when you choose the wrong Region or use credentials for a different AWS account.

**Resolution:** To resolve this error, complete the following steps.

1. Verify that the Region matches the Region where your recovery instances are located.

1. Verify that the credentials belong to the AWS account that contains your source servers and recovery instances.

1. Confirm the account and Region by running the following command:

   ```bash
   aws sts get-caller-identity --region {{region}}
   ```

## DRS-FAILBACK-003: Credential retrieval failed
<a name="Troubleshooting-Failback-credential-retrieval"></a>

**Error message:** `Error code: DRS-FAILBACK-003 - Credential retrieval failed`

**Cause:** This error has one of the following causes:
+ The hardware clock is set to local time instead of UTC. The Failback Client requires UTC for certificate-based authentication, so a local-time clock causes authentication to fail.
+ The trust policy of the `AWSElasticDisasterRecoveryFailbackRole` role allows the `sts:AssumeRole` action but not the `sts:SetSourceIdentity` action.
+ You entered a web proxy that the Failback Client's credentials step can't use. The credentials step requires the proxy to include the `http://` scheme, so it skips a proxy entered without a scheme (for example, `proxy.example.com:3128`). It also can't use a proxy that requires a user name and password, because it ignores proxy credentials in the URL.
+ The connection from the failback server to the Elastic Disaster Recovery endpoint on TCP port 443 dropped while the Failback Client was getting credentials.

**Resolution:** Identify which cause applies, and then complete the corresponding steps.

1. If the hardware clock is set to local time, set it to UTC:

   1. Access the BIOS or EFI Shell of the failback target server.

   1. Set the hardware clock to UTC instead of local time.

   1. Restart the Failback Client.
**Note**  
This error commonly occurs when you fail back to physical servers or hypervisors where the hardware clock is set to local time.

1. If the trust policy is missing the `sts:SetSourceIdentity` action, add it:

   1. Open the [IAM console](https://console.aws.amazon.com/iam/).

   1. In the navigation pane, choose **Roles**.

   1. Choose `AWSElasticDisasterRecoveryFailbackRole`.

   1. On the **Trust relationships** tab, choose **Edit trust policy**.

   1. Add the `sts:SetSourceIdentity` action alongside the existing `sts:AssumeRole` action. For an example trust policy, see [Initializing DRS through the API](getting-started-initializing.md#drs-initializing-manually).

   1. Save the trust policy, and then run the Failback Client again.

1. If you use a web proxy, enter it in a form that the credentials step can use:

   1. Enter the proxy as `http://{{host}}:{{port}}`, including the `http://` scheme.

   1. Use a proxy that doesn't require a user name and password.

   1. Run the Failback Client again.

1. If the connection to the Elastic Disaster Recovery endpoint dropped, check that the failback server can reach the endpoint on TCP port 443, and then run the Failback Client again.

## DRS-FAILBACK-004: Recovery instance not found
<a name="Troubleshooting-Failback-recovery-instance-not-found"></a>

**Error message:** `Error code: DRS-FAILBACK-004 - Recovery instance not found`

**Cause:** The recovery instance was deleted or terminated after the Failback Client connected to it.

**Resolution:** Confirm whether the recovery instance still exists, and then take the appropriate action.

1. In the Elastic Disaster Recovery console, check whether the recovery instance still exists in the Region.

1. If the recovery instance exists, run the Failback Client again.

1. If the recovery instance no longer exists, you can't fail back from it. Run the Failback Client again and choose a recovery instance that exists. For more information, see [Failback Client detailed walkthrough](failback-performing.md#failback-performing-performing).

## DRS-FAILBACK-005: Manifest download timed out
<a name="Troubleshooting-Failback-manifest-download-timed-out"></a>

**Error message:** `Error code: DRS-FAILBACK-005 - Manifest download timed out`

**Cause:** The server couldn't download the failback manifest and its hash file from Amazon S3 in the AWS Region that you fail back from over HTTPS (TCP port 443), or the two files didn't match. This error usually has one of the following causes:
+ A firewall, proxy, or network rule blocks some of the Elastic Disaster Recovery Amazon S3 buckets that the server needs.
+ Your DNS server can't resolve the Amazon S3 endpoint names, or DNS filtering blocks the name of one Elastic Disaster Recovery bucket.
+ You set the network with `CONFIG_NETWORK=1`, and the IP address, subnet mask, gateway, or DNS server is wrong.

If a firewall silently drops the connection instead of rejecting it, the error can take 20 minutes or longer to appear. The screen shows no progress while the server waits.

**Resolution:** To resolve this error, complete the following steps.

1. Allow outbound traffic on TCP port 443 from the server to Amazon S3 in the AWS Region that you fail back from, including every Elastic Disaster Recovery bucket. For the Amazon S3 access that failback requires, see [Failback prerequisites](failback-performing.md#failback-performing-prerequisites). For the list of Elastic Disaster Recovery buckets, see [Communication over TCP port 443](Network-Requirements.md#TCP-443).

1. If you use a web proxy, verify that it allows these connections.

1. Verify that your DNS server can resolve the Amazon S3 endpoint names.

1. If you set the network with `CONFIG_NETWORK=1`, verify the `IPADDR`, `NETMASK`, `GATEWAY`, and `DNS` values.

1. Boot the server from the Failback Client ISO again.

1. If the error continues, contact AWS Support.

## DRS-FAILBACK-006: Failback Client assets download failed
<a name="Troubleshooting-Failback-assets-download-failed"></a>

**Error message:** `Error code: DRS-FAILBACK-006 - Failback Client assets download failed`

**Cause:** The server downloaded the failback manifest from Amazon S3 but couldn't download the Failback Client package or its hash file. This error usually has one of the following causes:
+ The network connection is unstable, so the download stops responding for more than about 20 seconds or the connection drops.
+ A web proxy, firewall, or Transport Layer Security (TLS) inspection device limits the size or duration of a download, or filters by URL path, and so stops the larger package.

**Resolution:** To resolve this error, complete the following steps.

1. Check that the network link is stable and doesn't drop or pause connections.

1. Allow full downloads from Amazon S3 in the AWS Region that you fail back from through any web proxy, firewall, or TLS inspection device, with no size or time limits and no path filtering. For the Amazon S3 access that failback requires, see [Failback prerequisites](failback-performing.md#failback-performing-prerequisites). For the list of Elastic Disaster Recovery buckets, see [Communication over TCP port 443](Network-Requirements.md#TCP-443).

1. Boot the server from the Failback Client ISO again.

1. If the error continues, contact AWS Support.

## DRS-FAILBACK-007: Failed to get recovery instance volumes
<a name="Troubleshooting-Failback-get-volumes"></a>

**Error message:** `Error code: DRS-FAILBACK-007 - Failed to get recovery instance volumes`

**Cause:** The AWS Replication Agent on the recovery instance hasn't reported the instance's disks to Elastic Disaster Recovery since the instance launched. This happens when the agent isn't running, for example because SELinux in enforcing mode prevents it from starting. It also happens when the instance can't reach the Elastic Disaster Recovery endpoint on TCP port 443. If the recovery instance launched recently, the agent might not have reported the disks yet.

**Resolution:** To resolve this error, complete the following steps.

1. Verify that the recovery instance is running.

1. Verify that the AWS Replication Agent service is running:
   + **Linux:**

     ```bash
     systemctl status aws-replication-agent.service
     ```
   + **Windows (PowerShell):**

     ```powershell
     Get-Service AwsReplicationService
     ```

1. In Linux with SELinux in enforcing mode, if the service fails with permission errors, restore the SELinux labels on the agent installation folder, and then restart the service.

1. Allow outbound traffic on TCP port 443 to the Elastic Disaster Recovery endpoint in the security group and network ACLs. Verify that the recovery instance can reach the endpoint in one of these ways: a public IP address with a route to an internet gateway, a route to a NAT gateway, or a Elastic Disaster Recovery VPC endpoint. If you use a VPC endpoint, also allow the traffic in the VPC endpoint security group, and verify private DNS.

1. Keep the Failback Client running. It continues when the disks appear.

1. If the error continues, contact AWS Support.

## DRS-FAILBACK-008: Could not verify recovery instance connectivity
<a name="Troubleshooting-Failback-Errors-connectivity-instance"></a>

**Error message:** `Error code: DRS-FAILBACK-008 - Could not verify recovery instance connectivity`

**Cause:** The AWS Replication Agent on the recovery instance hasn't contacted Elastic Disaster Recovery since the Failback Client mapped the volumes. This happens when the recovery instance is stopped or terminated, or when the agent isn't running. It also happens when the instance can't reach the Elastic Disaster Recovery endpoint on TCP port 443.

**Resolution:** To resolve this error, use the console or the command line.

------
#### [ Console ]

1. If the recovery instance was terminated, launch a new recovery instance, and then restart the Failback Client.

1. Make sure the recovery instance is running.

1. Make sure the AWS Replication Agent service on the recovery instance is running.

1. Verify that the recovery instance can reach the Elastic Disaster Recovery endpoint in one of these ways: a public IP address with a route to an internet gateway, a route to a NAT gateway, or a Elastic Disaster Recovery VPC endpoint.

1. Verify that the security group attached to the recovery instance allows outbound traffic on TCP port 443.

1. Check the agent logs for connectivity errors.

1. Keep the Failback Client running. It continues when the recovery instance connects to Elastic Disaster Recovery.

------
#### [ CLI ]

1. If the recovery instance was terminated, launch a new recovery instance, and then restart the Failback Client.

1. Make sure the recovery instance is running.

1. Make sure the AWS Replication Agent service on the recovery instance is running.

1. Verify the recovery instance network configuration:

   ```bash
   aws ec2 describe-instances --instance-ids {{instance-id}} \
       --query "Reservations[*].Instances[*].[PublicIpAddress,SecurityGroups]"
   ```

1. Test connectivity from the recovery instance to the Elastic Disaster Recovery endpoint:
   + **Linux:**

     ```bash
     curl -v https://drs.{{region}}.amazonaws.com
     ```
   + **Windows (PowerShell):**

     ```powershell
     Test-NetConnection -ComputerName drs.{{region}}.amazonaws.com -Port 443
     ```

1. Check the agent logs for errors:

   ```bash
   tail /var/lib/aws-replication-agent/agent.log.0 | grep error
   ```

1. Keep the Failback Client running. It continues when the recovery instance connects to Elastic Disaster Recovery.

------

If the error continues, contact AWS Support.

If the agent log shows a "driver compiled for different kernel" error, see [Troubleshoot driver compilation errors](agent-install-linux-errors.md#error-driver-compiled).

## DRS-FAILBACK-009: Could not establish replication connection to recovery instance
<a name="Troubleshooting-Failback-replication-connection"></a>

**Error message:** `Error code: DRS-FAILBACK-009 - Could not establish replication connection to recovery instance`

**Cause:** The Failback Client opens a connection to the AWS Replication Agent on the recovery instance over TCP port 1500, and the connection can't be established. The address that the Failback Client connects to depends on the failback replication settings of the recovery instance:
+ With a public IP address for data replication, the Failback Client connects to the public IP address of the recovery instance.
+ With the **Use private IP** option, which uses a VPN, Direct Connect, or VPC peering connection, the Failback Client connects to the private IP address.
+ When the failback replication settings use IPv6, the Failback Client connects to the recovery instance's IPv6 address, whether or not **Use private IP** is selected.

The connection fails for one of the following reasons:
+ The network path to that address on TCP port 1500 is blocked.
+ A network device between the Failback Client and the recovery instance interrupts or inspects the TLS connection on port 1500.
+ The AWS Replication Agent on the recovery instance isn't running.

The Failback Client shows this error after about 10 minutes without a connection and keeps trying.

**Resolution:** To resolve this error, complete the following steps:

1. Verify that the AWS Replication Agent service on the recovery instance is running:
   + **Linux:**

     ```bash
     systemctl status aws-replication-agent.service
     ```
   + **Windows (PowerShell):**

     ```powershell
     Get-Service AwsReplicationService
     ```

1. Allow inbound TCP port 1500 to the address that matches the failback replication settings of the recovery instance:  
**Public IP**  
The recovery instance must have a public IP address. Its security group and network ACL must allow inbound TCP port 1500 from the public egress address of the Failback Client network. The Failback Client network must allow outbound TCP port 1500. Allow inbound TCP port 1500 only from the Failback Client network, not from 0.0.0.0/0. Connections from other hosts can prevent the Failback Client from connecting.  
**Use private IP**  
A network path from the Failback Client network to the VPC must exist through a VPN, Direct Connect, or VPC peering connection. The on-premises CIDR range must not overlap the subnet of the recovery instance. The Failback Client initiates the connection. The recovery instance's security group and network ACL must allow inbound TCP port 1500 from the private address range of the Failback Client network. The on-premises firewall must allow outbound TCP port 1500 to the private IP address of the recovery instance.  
**IPv6**  
The recovery instance needs an IPv6 address. Its security group and network ACL must allow inbound TCP port 1500 from the IPv6 address of the Failback Client network, and the Failback Client network must allow outbound TCP port 1500 over IPv6. You set IPv6 for failback replication with the `internetProtocol` parameter of the `UpdateFailbackReplicationConfiguration` operation.

   Network ACLs are stateless, so the network ACL must also allow the return traffic to the Failback Client network on outbound TCP ports 1024–65535.

   For more information about the setting that controls this, see [Use private IP](recovery-instances-details.md#recovery-instances-details-failback-replication-settings-private-ip). For more information about failback network requirements, see [Failback prerequisites](failback-performing.md#failback-performing-prerequisites).

1. Make sure that no firewall, proxy, or inspection device between the Failback Client network and the recovery instance decrypts, inspects, or interrupts traffic on TCP port 1500. Exclude TCP port 1500 from TLS inspection.

1. On the recovery instance, check the AWS Replication Agent log. The agent logs DRS-REPL-007 when nothing connects on TCP port 1500. It logs DRS-REPL-004 when a connection to port 1500 fails authentication, for example when a TLS inspection device is in the path or another host connects to the port. For more information, see [DRS-REPL-007: Timed out waiting for the failback connection on TCP port 1500](agent-runtime-errors.md#error-failback-listen-timed-out).

1. Keep the Failback Client running while you fix the cause. It keeps trying and continues when the connection succeeds.

1. If the Failback Client doesn't connect within 15 minutes after you fix the network path, contact AWS Support.

## DRS-FAILBACK-010: Failed to download replication software
<a name="Troubleshooting-Failback-download-replication-software"></a>

**Error message:** `Error code: DRS-FAILBACK-010 - Failed to download replication software`

**Cause:** The Failback Client couldn't download a usable copy of the replication software from Amazon S3 in the recovery AWS Region over TCP port 443. This error has one of the following causes:
+ The Failback Client couldn't download the file from Amazon S3. For example, a firewall or proxy blocked or dropped the connection, DNS resolution failed, a private network has no route or endpoint to Amazon S3, or Amazon S3 denied the request.
+ The download finished, but the file is empty, for example because a proxy returned an empty response.
+ The downloaded file failed its integrity check, for example because a proxy changed it.
+ A firewall or proxy allows the Amazon S3 hostname that the Failback Client used when it started, but not the hostname of the replication software download.

The Failback Client shows this error after repeated download attempts fail. It doesn't exit. The download starts again automatically after a few minutes, and later failures don't show the error code again.

**Resolution:** To resolve this error, complete the following steps:

1. Allow outbound TCP port 443 from the Failback Client to Amazon S3 in the recovery AWS Region. The Failback Client downloads the replication software from virtual-hosted bucket hostnames of the form `*.s3.{{region}}.amazonaws.com`. For the list of Amazon S3 bucket hostnames to allow, see [Communication over TCP port 443](Network-Requirements.md#TCP-443). When the failback replication settings set the internet protocol, the download uses the dual-stack hostnames `*.s3.dualstack.{{region}}.amazonaws.com`, so allow those too. Also allow outbound TCP port 443 to the AWS Elastic Disaster Recovery endpoint in the recovery Region.

1. The Failback Client reads the proxy when it starts. To change the proxy, restart the failback server into the Failback Client. The proxy must not alter or truncate the download.
   + With Elastic Disaster Recovery Failback Automation (DRSFA), set the `PROXY` field in the custom failback configuration file. For more information, see [Generating the configuration file](failback-failover-drsfa-custom.md#failback-failover-drsfa-custom-generating).
   + When you run the Failback Client interactively, it asks for a proxy only if it can't reach the download endpoint when it starts. If it reached Amazon S3 at startup, allow the download in your network or proxy instead. With `--no-prompt`, it exits instead of asking.

1. If you use an Amazon S3 VPC endpoint or a proxy, make sure that it doesn't block or change requests to Amazon S3.

1. If you use a private network and the Failback Client can't reach public Amazon S3, use an Amazon S3 interface endpoint with private DNS so that the bucket hostnames of the form `*.s3.{{region}}.amazonaws.com` resolve to the endpoint from your network. When the failback replication settings set the internet protocol, the download uses the dual-stack hostnames `*.s3.dualstack.{{region}}.amazonaws.com`. Verify DNS resolution for both hostname shapes from the Failback Client network.

1. Keep the Failback Client running. After you fix connectivity, the next automatic download attempt succeeds. Restart the failback server into the Failback Client only if you change its proxy or network settings.

1. If the error continues after you confirm connectivity, contact AWS Support.

## Failback client not seen
<a name="Troubleshooting-Failback-client-not-seen"></a>

**Error message:** `Failback client not seen` status in the Elastic Disaster Recovery console.

**Cause:** Communication between the Failback Client and the Elastic Disaster Recovery endpoint has been interrupted. Common causes include the following:
+ A network issue between the Failback Client and the Elastic Disaster Recovery endpoint on TCP port 443
+ A Failback Client process that was terminated or interrupted
+ A Failback Client that runs in the foreground, where closing the shell session terminates the process

**Resolution:** To resolve this error, complete the following steps.

1. Verify network connectivity to `drs.{{region}}.amazonaws.com` on TCP port 443.

1. Use `screen` or `tmux` to keep the Failback Client session alive.

1. Restart the Failback Client if needed.

**Note**  
Replication can continue in the background because the AWS Replication Agent runs independently of the Failback Client process.