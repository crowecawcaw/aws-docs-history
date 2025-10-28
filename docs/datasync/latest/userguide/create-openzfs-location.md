# Configuring DataSync transfers with

Amazon FSx for OpenZFS

To transfer data to or from your Amazon FSx for OpenZFS file system, you must create an
AWS DataSync transfer _location_. DataSync can use this
location as a source or destination for transferring data.

## Providing DataSync access to FSx for OpenZFS file

systems

DataSync mounts your FSx for OpenZFS file system from your virtual private cloud (VPC)
using [network interfaces](required-network-interfaces.md "required-network-interfaces.md"). DataSync
fully manages the creation, the use, and the deletion of these network interfaces on
your behalf.

###### Note

VPCs that you use with DataSync must have default tenancy. VPCs with dedicated tenancy
aren't supported.

## Configuring FSx for OpenZFS file

system authorization

DataSync accesses your FSx for OpenZFS file system as an NFS client, mounting the file
system as a root user with a user ID (UID) and group ID (GID) of
`0`.

For DataSync to copy all of your file metadata, you must configure the NFS export
settings on your file system volumes using `no_root_squash`. However, you
can limit this level of access to only a specific DataSync task.

For more information, see [Volume
properties](../../../fsx/latest/OpenZFSGuide/managing-volumes.md#volume-properties "../../../fsx/latest/OpenZFSGuide/managing-volumes.md#volume-properties") in the _Amazon FSx for OpenZFS User
Guide_.

### Configuring NFS exports

specific to DataSync (recommended)

You can configure an NFS export specific to each volume that’s accessed only
by your DataSync task. Do this for the most recent ancestor volume of the mount
path that you specify when creating your FSx for OpenZFS location.

###### To configure an NFS export specific to DataSync

1. Create your [DataSync
   task](create-task-how-to.md "create-task-how-to.md").

This creates the task’s network interfaces that you specify in your
NFS export settings. 2. Locate the private IP addresses of the task's network interfaces by
using the Amazon EC2 console or AWS CLI. 3. For your FSx for OpenZFS file system volume, configure the following NFS
export settings for each of the task’s network interfaces:

    * Client address: Enter the
     network interface’s private IP address (for example,
     ``10.24.34.0``).
    * NFS options: Enter
     `rw,no_root_squash`.

### Configuring NFS exports for all

clients

You can specify an NFS export that allows root access to all clients.

###### To configure an NFS export for all clients

- For your FSx for OpenZFS file system volume, configure the following NFS
  export settings:
  - Client address: Enter
    `*`.
  - NFS options: Enter
    `rw,no_root_squash`.

## Creating your FSx for OpenZFS transfer

location

To create the location, you need an existing FSx for OpenZFS file system. If you
don't have one, see [Getting started with
Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/getting-started.md "../../../fsx/latest/OpenZFSGuide/getting-started.md") in the _Amazon FSx for OpenZFS User
Guide_.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, choose
   **Locations**, and then choose **Create
   location**.
3. For **Location type**, choose
   **Amazon FSx**.

You configure this location as a source or destination
later. 4. For **FSx file system**, choose the FSx for OpenZFS
file system that you want to use as a location. 5. For **Mount path**, enter the mount path for your
FSx for OpenZFS file system.

The path must begin with `/fsx` and can be any existing
directory path in the file system. When the location is used as a
source, DataSync reads data from the mount path. When the location is
used as a destination, DataSync writes all data to the mount path. If a
subdirectory isn't provided, DataSync uses the root volume directory
(for example, `/fsx`). 6. For **Security groups**, choose up to five
security groups that provide network access to your FSx for OpenZFS
file system.

The security groups must provide access to the network ports that
are used by the FSx for OpenZFS file system. The file system must allow
network access from the security groups.

For more information about security groups, see [File system access control with Amazon VPC](../../../fsx/latest/OpenZFSGuide/limit-access-security-groups.md "../../../fsx/latest/OpenZFSGuide/limit-access-security-groups.md") in the
_Amazon FSx for OpenZFS User Guide_. 7. (Optional) Expand **Additional settings** and for
**NFS version** choose the NFS version that
DataSync uses to access your file system.

By default, DataSync uses NFS version 4.1. 8. (Optional) Enter values for the **Key** and
**Value** fields to tag the FSx for OpenZFS file
system.

Tags help you manage, filter, and search for your location. We
recommend creating at least a name tag for your location. 9. Choose **Create location**.

###### To create an FSx for OpenZFS location by using the AWS CLI

1. Copy the following `create-location-fsx-open-zfs`
   command:

```
aws datasync create-location-fsx-open-zfs \
   --fsx-filesystem-arn arn:aws:fsx:`region`:`account-id`:file-system/`filesystem-id` \
   --security-group-arns arn:aws:ec2:`region`:`account-id`:security-group/`group-id` \
   --protocol NFS={}
```

2. Specify the following required options in the command:
   - For `fsx-filesystem-arn`, specify the location
     file system's fully qualified Amazon Resource Name (ARN).
     This includes the AWS Region where your file system
     resides, your AWS account, and the file system ID.
   - For `security-group-arns`, specify the ARN of
     the Amazon EC2 security group that provides access to the [network
     interfaces](required-network-interfaces.md "required-network-interfaces.md") of your FSx for OpenZFS file system's
     preferred subnet. This includes the AWS Region where your
     Amazon EC2 instance resides, your AWS account, and the security
     group ID.

   For more information about security groups, see [File System Access Control with Amazon VPC](../../../fsx/latest/OpenZFSGuide/limit-access-security-groups.md "../../../fsx/latest/OpenZFSGuide/limit-access-security-groups.md") in the
   _Amazon FSx for OpenZFS User Guide_.
   - For `protocol`, specify the protocol that DataSync
     uses to access your file system. (DataSync currently supports
     only NFS.)

3. Run the command. You get a response showing the location that you
   just created.

```
{
    "LocationArn": "arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890"
}
```
