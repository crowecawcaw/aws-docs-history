# Configuring AWS DataSync transfers with an NFS file

server

With AWS DataSync, you can transfer data between your Network File System (NFS) file
server and one of the following AWS storage services:

- [Amazon S3](create-s3-location.md "create-s3-location.md")
- [Amazon EFS](create-efs-location.md "create-efs-location.md")
- [Amazon FSx for Windows File Server](create-fsx-location.md "create-fsx-location.md")
- [Amazon FSx for Lustre](create-lustre-location.md "create-lustre-location.md")
- [Amazon FSx for OpenZFS](create-openzfs-location.md "create-openzfs-location.md")
- [Amazon FSx for NetApp ONTAP](create-ontap-location.md "create-ontap-location.md")
  To set up this kind of transfer, you create a [location](how-datasync-transfer-works.md#sync-locations "how-datasync-transfer-works.md#sync-locations") for your NFS file server. You can use this location as a transfer
  source or destination.

## Providing DataSync access to NFS file servers

For DataSync to access your NFS file server, you need a DataSync [agent](how-datasync-transfer-works.md#sync-agents "how-datasync-transfer-works.md#sync-agents"). The agent mounts an export on your file
server by using the NFS protocol.

###### Topics

- [Configuring your NFS
  export](#accessing-nfs-configuring-export "#accessing-nfs-configuring-export")
- [Supported NFS versions](#supported-nfs-versions "#supported-nfs-versions")

### Configuring your NFS

export

The export that DataSync needs for your transfer depends on if your NFS file
server is a source or destination location and how your file server's
permissions are configured.

If your file server is a source location, DataSync just has to read and traverse
your files and folders. If it's a destination location, DataSync needs root access
to write to the location and set ownership, permissions, and other metadata on
the files and folders that you're copying. You can use the
`no_root_squash` option to allow root access for your
export.

The following examples describe how to configure an NFS export that provides
access to DataSync.

###### When your NFS file server is a source location (root access)

Configure your export by using the following command, which provides DataSync
read-only permissions (`ro`) and root access (
`no_root_squash`):

```
`export-path` `datasync-agent-ip-address`(ro,no_root_squash)
```

###### When your NFS file server is a destination location

Configure your export by using the following command, which provides DataSync
write permissions (`rw`) and root access (
`no_root_squash`):

```
`export-path` `datasync-agent-ip-address`(rw,no_root_squash)
```

###### When your NFS file server is a source location (no root access)

Configure your export by using the following command, which specifies the
POSIX user ID (UID) and group ID (GID) that you know would provide DataSync
read-only permissions on the export:

```
`export-path` `datasync-agent-ip-address`(ro,all_squash,anonuid=`uid`,anongid=`gid`)
```

### Supported NFS versions

By default, DataSync uses NFS version 4.1. DataSync also supports NFS 4.0 and
3.x.

## Configuring your network for NFS

transfers

For your DataSync transfer, you must configure traffic for a few network connections:

1.  Allow traffic on the following ports from your DataSync agent to your NFS
    file server:

        * For NFS version 4.1 and 4.0
         – TCP port 2049
        * For NFS version 3.x – TCP
         ports 111 and 2049

    Other NFS clients in your network should be able to mount the NFS export
    that you're using to transfer data. The export must also be accessible
    without Kerberos authentication.

2.  Configure traffic for your [service
    endpoint connection](datasync-network.md "datasync-network.md") (such as a VPC, public, or FIPS
    endpoint).
3.  Allow traffic from the DataSync service to the [AWS storage
    service](datasync-network.md#storage-service-network-requirements "datasync-network.md#storage-service-network-requirements") you're transferring to or from.

## Creating your NFS transfer

location

Before you begin, note the following:

- You need an NFS file server that you want to transfer data from.
- You need a DataSync agent that can [access your
  file server](#accessing-nfs "#accessing-nfs").
- DataSync doesn't support copying NFS version 4 access control lists
  (ACLs).

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**,
   then choose **Locations** and **Create
   location**.
3. For **Location type**, choose **Network
   File System (NFS)**.
4. For **Agents**, choose the DataSync agent that can
   connect to your NFS file server.

You can choose more than one agent. For more information, see
[Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents "do-i-need-datasync-agent.md#multiple-agents"). 5. For **NFS server**, enter the Domain Name System
(DNS) name or IP address of the NFS file server that your DataSync
agent connects to. 6. For **Mount path**, enter the NFS export path
that you want DataSync to mount.

This path (or a subdirectory of the path) is where DataSync transfers
data to or from. For more information, see [Configuring your NFS
export](#accessing-nfs-configuring-export "#accessing-nfs-configuring-export"). 7. (Optional) Expand **Additional settings** and
choose a specific **NFS version** for DataSync to use
when accessing your file server.

For more information, see [Supported NFS versions](#supported-nfs-versions "#supported-nfs-versions"). 8. (Optional) Choose **Add tag** to tag your NFS
location.

_Tags_ are key-value pairs that help you
manage, filter, and search for your locations. We recommend creating
at least a name tag for your location. 9. Choose **Create location**.

- Use the following command to create an NFS location.

```
aws datasync create-location-nfs \
    --server-hostname `nfs-server-address` \
    --on-prem-config AgentArns=`datasync-agent-arns` \
    --subdirectory `nfs-export-path`
```

For more information on creating the location, see [Providing DataSync access to NFS file servers](#accessing-nfs "#accessing-nfs").

DataSync automatically chooses the NFS version that it uses to read
from an NFS location. To specify an NFS version, use the optional
`Version` parameter in the [NfsMountOptions](API_NfsMountOptions.md "API_NfsMountOptions.md") API operation.
This command returns the Amazon Resource Name (ARN) of the NFS location,
similar to the ARN shown following.

```
{
    "LocationArn": "arn:aws:datasync:us-east-1:111222333444:location/loc-0f01451b140b2af49"
}
```

To make sure that the directory can be mounted, you can connect to any
computer that has the same network configuration as your agent and run the
following command.

```
mount -t nfs -o nfsvers=<`nfs-server-version` <`nfs-server-address`:<`nfs-export-path` <`test-folder`
```

The following is an example of the command.

```
mount -t nfs -o nfsvers=3 198.51.100.123:/path_for_sync_to_read_from /temp_folder_to_test_mount_on_local_machine
```
