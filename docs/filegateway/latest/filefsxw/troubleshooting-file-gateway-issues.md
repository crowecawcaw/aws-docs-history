Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Troubleshooting: File Gateway

issues

You can configure your File Gateway to write log entries to a Amazon CloudWatch log group. If you
do, you receive notifications about gateway health status and about any errors that the
gateway encounters. You can find information about these error and health notifications in
CloudWatch Logs.

In the following sections, you can find information that can help you understand the cause
of each error and health notification and how to fix issues.

###### Topics

- [Error: FileMissing](#troubleshoot-logging-errors-filemissing "#troubleshoot-logging-errors-filemissing")
- [Error:
  FsxFileSystemAuthenticationFailure](#troubleshoot-logging-errors-fsxfilesystemauthenticationfailure "#troubleshoot-logging-errors-fsxfilesystemauthenticationfailure")
- [Error:
  FsxFileSystemConnectionFailure](#troubleshoot-logging-errors-fsxfilesystemconnectionfailure "#troubleshoot-logging-errors-fsxfilesystemconnectionfailure")
- [Error:
  FsxFileSystemFull](#troubleshoot-logging-errors-fsxfilesystemfull "#troubleshoot-logging-errors-fsxfilesystemfull")
- [Error:
  GatewayClockOutOfSync](#troubleshoot-logging-errors-gatewayclockoutofsync "#troubleshoot-logging-errors-gatewayclockoutofsync")
- [Error:
  InvalidFileState](#troubleshoot-logging-errors-invalidfilestate "#troubleshoot-logging-errors-invalidfilestate")
- [Error: ObjectMissing](#troubleshoot-logging-errors-objectmissing "#troubleshoot-logging-errors-objectmissing")
- [Error:
  DroppedNotifications](#troubleshoot-logging-errors-droppednotifications "#troubleshoot-logging-errors-droppednotifications")
- [Notification: HardReboot](#troubleshoot-hardreboot-notification "#troubleshoot-hardreboot-notification")
- [Notification: Reboot](#troubleshoot-reboot-notification "#troubleshoot-reboot-notification")
- [Troubleshooting: Active Directory domain
  issues](#troubleshooting-ad-domain "#troubleshooting-ad-domain")
- [Troubleshooting: Using CloudWatch
  metrics](#troubleshooting-with-cw-metrics "#troubleshooting-with-cw-metrics")

## Error: FileMissing

The `FileMissing` error is similar to the `ObjectMissing` error,
and the steps to resolve it are identical. You can get a `FileMissing` error
when a writer other than the specified File Gateway deletes the specified file from the
Amazon FSx. Any subsequent uploads to Amazon FSx or retrievals from Amazon FSx for the object
fail.

###### To resolve a FileMissing error

1. Save the latest copy of the file to the local file system of your SMB client
   (you need this file copy in step 3).
2. Delete the file from the File Gateway using your SMB client.
3. Copy the latest version of the file that you saved in step 1 Amazon FSx using your
   SMB client. Do this through your File Gateway.

## Error:

FsxFileSystemAuthenticationFailure

You can get an `FsxFileSystemAuthenticationFailure` error when the
credentials provided while attaching the filesystem expired or, its privileges have been
revoked.

###### To resolve an FsxFileSystemAuthenticationFailure error

1. Ensure that the credentials provided at the time of attaching the Amazon FSx file
   system are still valid.
2. Ensure that the user has all necessary permissions as described in [Attach an
   Amazon FSx for Windows File Server file system](attach-fsxw-filesystem.md "attach-fsxw-filesystem.md").

## Error:

FsxFileSystemConnectionFailure

You can get an `FsxFileSystemConnectionFailure` error when the Amazon FSx server
is inaccessible from the gateway machine.

###### To resolve an FsxFileSystemConnectionFailure error

1. Ensure that all the firewall and VPC rules are allowing the connection between
   the gateway machine and the Amazon FSx server.
2. Ensure that the Amazon FSx server is running.

## Error:

FsxFileSystemFull

You can get an `FsxFileSystemFull` error when there is not enough free disk
space in the Amazon FSx file system.

###### To resolve an FsxFileSystemFull error

- Increase the storage space for the Amazon FSx file system.

## Error:

GatewayClockOutOfSync

You can get a `GatewayClockOutOfSync` error when the gateway detects a
difference of 5 minutes or more between the local system time and the time reported by
the AWS Storage Gateway servers. Clock synchronization issues can negatively impact
connectivity between the gateway and AWS. If the gateway clock is out of sync, I/O
errors might occur for NFS and SMB connections, and SMB users might experience
authentication errors.

###### To resolve a GatewayClockOutOfSync error

- Check the network configuration between the gateway and the NTP server. For
  more information about synchronizing the gateway VM time and updating the NTP
  server configuration, see [Configuring a Network Time Protocol (NTP) server for your
  gateway](manage-on-premises-fgw.md#MaintenanceTimeSync-fgw "manage-on-premises-fgw.md#MaintenanceTimeSync-fgw").

## Error:

InvalidFileState

You can get an `InvalidFileState` error when a writer other than the
specified gateway modifies the specified file in the specified file share. As a result,
the state of the file on the gateway doesn’t match its state in Amazon FSx. Any subsequent
uploads or retrievals of the file from Amazon FSx could fail.

###### To resolve an InvalidFileState error

1. Save the latest copy of the file to the local file system of your SMB client
   (you need this file to copy in step 4). If the version of the file in Amazon FSx is
   the latest, download that version. You can do this by directly accessing the
   Amazon FSx share using any SMB client.
2. Delete the file in Amazon FSx directly.
3. Delete the file from the gateway using your SMB client.
4. Using your SMB client, copy the latest version of the file that you saved in
   step 1, _through your File Gateway_,to Amazon FSx.

## Error: ObjectMissing

You can get an `ObjectMissing` error when a writer other than the specified
File Gateway deletes the specified file from the Amazon FSx. Any subsequent uploads to Amazon FSx
or retrievals from Amazon FSx for the object fail.

###### To resolve an ObjectMissing error

1. Save the latest copy of the file to the local file system of your SMB client
   (you need this file copy in step 3).
2. Delete the file from the File Gateway using your SMB client.
3. Copy the latest version of the file that you saved in step 1 Amazon FSx using your
   SMB client. Do this through your File Gateway.

## Error:

DroppedNotifications

You might see a `DroppedNotifications` error instead of other expected
types of CloudWatch log entries when free storage space on your gateway's root disk is less
than 1 GB, or if more than 100 health notifications are generated within a 1 minute
interval. In these circumstances, the gateway stops generating detailed CloudWatch log
notifications as a precautionary measure.

**To resolve a DroppedNotifications error**

1. Check the `Root Disk Usage` metric on the
   **Monitoring** tab for your gateway in the Storage Gateway console
   to determine whether available root disk space is running low.
2. Increase the size of the gateway's root storage disk if available space is
   less than 1 GB. Refer to your virtual machine hypervisor's documentation for
   instructions.

To increase root disk size for Amazon EC2 gateways, see [Request modifications to your EBS volumes](../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md "../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md") in the
_Amazon Elastic Compute Cloud User Guide_.

###### Note

It is not possible to increase the root disk size for the
AWS Storage Gateway Hardware Appliance. 3. Restart your gateway.

## Notification: HardReboot

You can get a `HardReboot` notification when the gateway VM is restarted
unexpectedly. Such a restart can be due to loss of power, a hardware failure, or another
event. For VMware gateways, a reset by vSphere High Availability Application Monitoring
can cause this event.

When your gateway runs in such an environment, check for the presence of the
`HealthCheckFailure` notification and consult the VMware events log for
the VM.

## Notification: Reboot

You can get a reboot notification when the gateway VM is restarted. You can restart a
gateway VM by using the VM Hypervisor Management console or the Storage Gateway console.
You can also restart by using the gateway software during the gateway's maintenance
cycle.

If the time of the reboot is within 10 minutes of the gateway's configured [maintenance start time](MaintenanceManagingUpdate-common.md "MaintenanceManagingUpdate-common.md"), this
reboot is probably a normal occurrence and not a sign of any problem. If the reboot
occurred significantly outside the maintenance window, check whether the gateway was
restarted manually.

## Troubleshooting: Active Directory domain

issues

FSx File Gateway doesn't generate specific log messages for Active Directory domain issues.
If you have trouble joining your gateway to your Active Directory domain, do the
following:

- Verify that the gateway is not attempting to use a read-only domain controller
  (RODC) to join the domain.
- Verify that the gateway is configured to use the correct DNS servers.

For example, if you are trying to join an Amazon EC2 gateway instance to an
AWS-managed Active Directory, verify that the DHCP option set for your EC2 VPC
specifies the AWS-managed Active Directory DNS servers.

DNS servers that you configure through the VPC DHCP options set are provided
to the all EC2 instances in the VPC. If you want to specify a DNS server for an
individual gateway, you can do so using that gateway's EC2 local console.

For on-premises gateways, you specify a DNS server using the VM local
console.

- Verify gateway network connectivity by running the following commands from the
  command prompt in the gateway's local console. Replace the highlighted variables
  with the actual domain name and IP addresses from your deployment.

```
dig -d `ExampleDomainName`
ncport -d `ExampleDomainControllerIPAddress` -p 445
ncport -d `ExampleDomainControllerIPAddress` -p 389

```

- Verify that your Active Directory service account has the requisite
  permissions. For more information, see [Active
  Directory service account permission requirements](ad-serviceaccount-permissions.md "ad-serviceaccount-permissions.md").
- Verify that the gateway joins the correct Organizational Unit (OU).

Joining a domain creates an Active Directory computer account in the default
computers container (which is not an OU), using the gateway's **Gateway
ID** as the account name (for example, SGW-1234ADE). It is not
possible to customize the name of this account.

If your Active Directory environment has a designated OU for new computer
objects, you must specify that OU when joining the domain.

If you encounter access denied errors when attempting to join the designated
OU, check with your Active Directory domain administrator. The administrator may
need to pre-stage the gateway's computer account before it can join the domain.
For more information, see [How can I troubleshoot issues with joining my Storage Gateway file gateway to a
domain for Microsoft Active Directory authentication?](https://aws.amazon.com/premiumsupport/knowledge-center/storage-gateway-domain-join-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/storage-gateway-domain-join-error/").

- Verify that your gateway's hostname is resolvable in DNS by running the
  following command from the command prompt in the gateway's local console.
  Replace the highlighted variable with the actual hostname for your
  gateway.

```
dig -d `ExampleHostName` -r A
```

If you configured a custom hostname for your gateway, you must manually add a
DNS A-record that points to its IP address.

- Verify that network latency between the gateway and the domain controller is
  reasonably low. The query to join a domain can time out if the gateway does not
  receive a response from the domain controller within 20 seconds.

If you join the gateway to the domain using the [JoinDomain](../../../storagegateway/latest/APIReference/API_JoinDomain.md "../../../storagegateway/latest/APIReference/API_JoinDomain.md") CLI command, you can can add the
`--timeout-in-seconds` flag to increase the timeout to a maximum
of 3,600 seconds.

- Verify that the Active Directory user you are using to join the gateway to the
  domain has the privileges required to do so.

## Troubleshooting: Using CloudWatch

metrics

You can find information following about actions to address issues using Amazon CloudWatch
metrics with Storage Gateway.

###### Topics

- [Your gateway reacts slowly when browsing
  directories](#slow-gateway "#slow-gateway")
- [Your gateway isn't responding](#gateway-not-responding "#gateway-not-responding")
- [You do not see files in your Amazon FSx file
  system](#files-missing-fsx "#files-missing-fsx")
- [You do not see older snapshots in your Amazon FSx
  file system](#snapshots-missing-fsx "#snapshots-missing-fsx")
- [Your gateway is slow transferring data
  to Amazon FSx](#slow-data-transfer-to-fsx "#slow-data-transfer-to-fsx")
- [Your gateway backup job fails or there are errors
  when writing to your gateway](#backup-job-fails "#backup-job-fails")

### Your gateway reacts slowly when browsing

directories

If your File Gateway reacts slowly when you run the **ls** command
or browse directories, check the `IndexFetch` and
`IndexEviction` CloudWatch metrics:

- If the `IndexFetch` metric is greater than 0 when you run an
  `ls` command or browse directories, your File Gateway
  started without information on the contents of the directory affected and
  had to access FSx for Windows File Server. Subsequent efforts to list
  the contents of that directory should go faster.
- If the `IndexEviction` metric is greater than 0, it means that
  your File Gateway has reached the limit of what it can manage in its cache
  at that time. In this case, your File Gateway has to free some storage
  space from the least recently accessed directory to list a new directory. If
  this occurs frequently and there is a performance impact, contact Support.

Discuss with Support the contents of the related Amazon FSx
file system and recommendations to improve performance based on your use
case.

### Your gateway isn't responding

If your File Gateway isn't responding, do the following:

- If there was a recent reboot or software update, then check the
  `IOWaitPercent` metric. This metric shows the percentage of
  time that the CPU is idle when there is an outstanding disk I/O request. In
  some cases, this might be high (10 or greater) and might have risen after
  the server was rebooted or updated. In these cases, then your File Gateway
  might be bottlenecked by a slow root disk as it rebuilds the index cache to
  RAM. You can address this issue by using a faster physical disk for the root
  disk.
- If the `MemUsedBytes` metric is at or nearly the same as the
  `MemTotalBytes` metric, then your File Gateway is running
  out of available RAM. Make sure that your File Gateway has at least the
  minimum required RAM. If it already does, consider adding more RAM to your
  File Gateway based on your workload and use case.

If the file share is SMB, the issue might also be due to the number of SMB
clients connected to the file share. To see the number of clients connected
at any given time, check the `SMBV(1/2/3)Sessions` metric. If
there are many clients connected, you might need to add more RAM to your
File Gateway.

### You do not see files in your Amazon FSx file

system

If you notice that files on the gateway are not reflected in the Amazon FSx file
system, check the `FilesFailingUpload` metric. If the metric reports that
some files are failing upload, check your health notifications. When files fail to
upload, the gateway generates a health notification containing more details on the
issue.

### You do not see older snapshots in your Amazon FSx

file system

Some file operations on the FSx File Gateway, such as top-level folder renames or permission changes, can result in multiple file operations that lead to a high I/O load on your FSx for Windows File Server file system. If your file system doesn't have enough performance resources for your workload, the file system might delete [shadow copies](../../../fsx/latest/WindowsGuide/shadow-copies-fsxW.md "../../../fsx/latest/WindowsGuide/shadow-copies-fsxW.md") because it prioritizes availability for ongoing I/O over historical shadow copy retention.

In the Amazon FSx console, check the **Monitoring and performance** page to see if your file system is under-provisioned. If it is, you can switch to SSD storage, increase throughput capacity, or increase SSD IOPS to handle your workload.

### Your gateway is slow transferring data

to Amazon FSx

If your File Gateway is slow transferring data to Amazon FSx for Windows File Server, do the
following:

- If the `CachePercentDirty` metric is 80 or greater, your
  File Gateway is writing data faster to disk than it can upload the data to
  Amazon FSx for Windows File Server. Consider increasing the bandwidth for upload from your
  File Gateway, adding one or more cache disks, or slowing down client
  writes, or increase the throughput capacity for associated
  Amazon FSx for Windows File Server.
- If the `CachePercentDirty` metric is low, check the
  `IoWaitPercent` metric. If `IoWaitPercent` is
  greater than 10, your File Gateway might be bottlenecked by the speed of
  the local cache disk. We recommend local solid state drive (SSD) disks for
  your cache, preferably NVM Express (NVMe). If such disks aren't
  available, try using multiple cache disks from separate physical disks for a
  performance improvement.

### Your gateway backup job fails or there are errors

when writing to your gateway

If your File Gateway backup job fails or there are errors when writing to your
File Gateway, do the following:

- If the `CachePercentDirty` metric is 90 percent or greater,
  your File Gateway can't accept new writes to disk because there is not
  enough available space on the cache disk. To see how fast your File Gateway
  is uploading to FSx for Windows File Server, view the
  `CloudBytesUploaded` metric. Compare that metric with the
  `WriteBytes` metric, which shows how fast the client is
  writing files to your File Gateway. If the SMB client is writing to your
  File Gateway faster than it can upload to FSx for Windows File Server, add
  more cache disks to cover the size of the backup job at a minimum. Or,
  increase the upload bandwidth.
- If a large file copy such as backup job fails but the
  `CachePercentDirty` metric is less than 80 percent, your
  File Gateway might be hitting a client-side session timeout. For SMB, you
  can increase this timeout using the PowerShell command
  `Set-SmbClientConfiguration -SessionTimeout 300`. Running
  this command sets the timeout to 300 seconds.
