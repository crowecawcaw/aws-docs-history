Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Best practices for File Gateway

This section contains the following topics, which provide information about the best
practices for working with gateways, file shares, buckets, and data. We recommend that you
familiarize yourself with the information outlined in this section, and attempt to follow these
guidelines in order to avoid problems with your AWS Storage Gateway. For additional guidance on diagnosing
and solving common issues you might encounter with your deployment, see [Troubleshooting problems with your Storage Gateway
deployment](troubleshooting-gateway-issues.md "troubleshooting-gateway-issues.md").

###### Topics

- [Best practices: recovering your data](#recover-data-from-gateway "#recover-data-from-gateway")
- [Restoring from backups or
  snapshots directly on Amazon FSx](#bestpractice-restore-snapshot-backup-fsx-fgw "#bestpractice-restore-snapshot-backup-fsx-fgw")
- [Clean up unnecessary resources](#cleanup-file "#cleanup-file")

## Best practices: recovering your data

Although it is rare, your gateway might encounter an unrecoverable failure. Such a failure
can occur in your virtual machine (VM), the gateway itself, the local storage, or elsewhere.
If a failure occurs, we recommend that you follow the instructions in the appropriate
section following to recover your data.

###### Important

Storage Gateway doesn’t support recovering a gateway VM from a snapshot that is created by
your hypervisor or from your Amazon EC2 Amazon Machine Image (AMI). If your gateway VM
malfunctions, activate a new gateway and recover your data to that gateway using the
instructions following.

### Recovering from an unexpected virtual

machine shutdown

If your VM shuts down unexpectedly, for example during a power outage, your gateway
becomes unreachable. When power and network connectivity are restored, your gateway
becomes reachable and starts to function normally. Following are some steps you can take
at that point to help recover your data:

- If an outage causes network connectivity issues, you can troubleshoot the
  issue. For information about how to test network connectivity, see [Testing your gateway's network
  connectivity](MaintenanceTestGatewayConnectivity-fgw.md "MaintenanceTestGatewayConnectivity-fgw.md").

### Recovering your data from a malfunctioning

cache disk

If your cache disk encounters a failure, we recommend you use the following steps to
recover your data depending on your situation:

- If the malfunction occurred because a cache disk was removed from your host,
  shut down the gateway, re-add the disk, and restart the gateway.

### Recovering your data from an inaccessible data

center

If your gateway or data center becomes inaccessible for some reason, you can recover
your data to another gateway in a different data center or recover to a gateway hosted
on an Amazon EC2 instance. If you don't have access to another data center, we recommend
creating the gateway on an Amazon EC2 instance. The steps you follow depends on the gateway
type you are covering the data from.

###### To recover data from a File Gateway in an inaccessible data center

For File Gateway, you map a new file system to the FSx for Windows File Server that contains the data you want to recover.

1. Create and activate a new File Gateway on an Amazon EC2 host. For more
   information, see [Deploy a default Amazon EC2 host for
   FSx File Gateway](ec2-gateway-file.md "ec2-gateway-file.md").
2. Create a new file system on the EC2 gateway you created.
   For more information, see [Create an
   FSx for Windows File Server file system](create-file-system.md "create-file-system.md").
3. Mount your file system on your client and map it to the
   FSx for Windows File Server that contains the data that you want to recover. For
   more information, see [Mount and use your
   file share](use-fsxw-gateway.md "use-fsxw-gateway.md").

## Restoring from backups or

snapshots directly on Amazon FSx

In some cases, you might need to restore data on your Amazon FSx file system directly, using a
backup or snapshot from an earlier point in time. In these instances, there is a risk of creating
a dual-writer scenario between the backup application and the FSx File Gateway, which can result in
stuck or mis-matched files. To avoid problems when restoring your Amazon FSx file system from backups
or snapshots, use the following procedure.

###### Note

Any cached data currently stored on your FSx File Gateway will not be valid after you restore
your Amazon FSx file system from a backup or snapshot using this procedure.

###### To avoid problems when restoring your Amazon FSx file system from backups or snapshots

1. Detach the Amazon FSx file system from the FSx File Gateway using the Storage Gateway console.
2. Restore the backup or snapshot directly on your Amazon FSx file system.
3. Reattach the Amazon FSx file system to the FSx File Gateway using the Storage Gateway console.

## Clean up unnecessary resources

As a best practice, we recommend cleaning up Storage Gateway resources to avoid unexpected or
unnecessary charges. For example, if you created a gateway as a demonstration exercise or a test,
consider deleting it and its virtual appliance from your deployment. Use the following procedure
to clean up resources.

###### To clean up resources you don't need

1. If you no longer plan to continue using a gateway, delete it. For more information, see
   [Deleting your gateway and removing associated
   resources](deleting-gateway-common.md "deleting-gateway-common.md").
2. Delete the Storage Gateway VM from your on-premises host. If you created your gateway on an Amazon EC2
   instance, terminate the instance.
