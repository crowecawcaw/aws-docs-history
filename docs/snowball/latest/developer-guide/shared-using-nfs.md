AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Managing the NFS interface on Snowball Edge

Use the Network File System (NFS) interface to upload files to the Snowball Edge as if the device is local storage to your operating system. This allows for a more user-friendly approach to transferring data because you can use features of your operating system, like copying files, dragging and dropping them, or other graphical user interface features. Each S3 bucket on the device is available as an NFS interface endpoint and can be mounted to copy data to. The NFS interface is available for import jobs.

You can use the NFS interface if the Snowball Edge device was configured to include it when the job to order the device was created. If the device is not configured to include the NFS interface, use the S3 adapter or Amazon S3 compatible storage on Snowball Edge to transfer data. For more information about the S3 adapter, see [Managing Amazon S3 adapter storage with AWS OpsHub](manage-s3.md "manage-s3.md"). For more information about Amazon S3 compatible storage on Snowball Edge, see [Set up Amazon S3 compatible storage on Snowball Edge with AWS OpsHub](s3-edge-snow-opshub.md "s3-edge-snow-opshub.md").

When started, the NFS interface uses 1 GB of memory and 1 CPU. This may limit the number of other services running on the Snowball Edge or the number of EC2-compatible instances that can run.

Data transferred through the NFS interface is not encrypted in transit. When configuring the NFS interface, you can provide CIDR blocks and the Snowball Edge will restrict access to the NFS interface from client computers with addresses in those blocks.

Files on the device will be transferred to Amazon S3 when it is returned to AWS. For more information, see [Importing Jobs into Amazon S3](importtype.md "importtype.md").

For more information about using NFS with your computer operating system, see the documentation for your operating system.

Keep the following details in mind when using the NFS interface.

- The NFS interface provides a local bucket for data storage on the device. For import jobs, no data from the local bucket will be imported to Amazon S3.
- File names are object keys in your local S3 bucket on the Snowball Edge. The key name is a sequence of Unicode
  characters whose UTF-8 encoding is at most 1,024 bytes long. We recommend
  using NFSv4.1 where possible and encode file names with Unicode UTF-8 to ensure a
  successful data import. File names that are not encoded with UTF-8 might not be uploaded
  to S3 or might be uploaded to S3 with a different file name depending on the NFS
  encoding you use.
- Ensure that the maximum length of your file path is less than 1024 characters. Snowball Edge
  do not support file paths that are greater that 1024 characters. Exceeding this file
  path length will result in file import errors.
- For more information, see [Object keys](../../../AmazonS3/latest/userguide/UsingMetadata.md "../../../AmazonS3/latest/userguide/UsingMetadata.md")
  in the Amazon Simple Storage Service User Guide.
- For NFS based transfers, standard POSIX style metadata will be added to your
  objects as they get imported to Amazon S3 from Snowball Edge. In addition, you will
  see meta-data "x-amz-meta-user-agent aws-datasync" as we currently use AWS DataSync
  as part of the internal import mechanism to Amazon S3 for Snowball Edge import with
  NFS option.
- You can transfer up to 40M files using a single Snowball Edge device. If you require to transfer more
  than 40M files in a single job, please batch the files in order to reduce the
  file numbers per each transfer. Individual files can be of any size with a
  maximum file size of 5 TB for Snowball Edge devices with the enhanced NFS interface or the S3 interface.
  You can also configure and manage the NFS interface with AWS OpsHub, a GUI tool. For more information, see [Managing the NFS interface](manage-nfs.md "manage-nfs.md").

## NFS configuration for

Snowball Edge

The NFS interface is not running on the Snowball Edge device by default, so you need
to start it to enable data transfer to the device. You can configure the NFS interface by providing the IP address of a Virtual Network Interface (VNI) running on the Snowball Edge and restricting
access to your file share, if required. Before configuring the NFS interface, set up a virtual network interface (VNI) on your Snowball Edge. For more information, see [Network Configuration for Compute Instances](network-config-ec2.md "network-config-ec2.md").

### Configure

Snowball Edge for the NFS interface

- Use the `describe-service` command to determine if the NFS interface is active.

```

snowballEdge describe-service --service-id `nfs`

```

The command will return the state of the NFS service, `ACTIVE` or `INACTIVE`.

```

{
  "ServiceId" : "nfs",
  "Status" : {
  "State" : "ACTIVE"
  }
}

```

If the value of the `State` name is `ACTIVE`, the NFS interface service is active and you can mount the Snowball Edge NFS volume. For more information, see . If the value is `INACTIVE`, you have to
start the service.

### Starting the NFS service on the Snowball Edge

Start a virtual network interface (VNI), if necessary, then start the NFS service on the Snowball Edge. If necessary, when starting the NFS service, provide a block of allowed network addresses. If you don't provide any addresses, access to the NFS endpoints will be unrestricted.

1. Use the `describe-virtual-network-interface` command to see the VNIs available on the Snowball Edge.

```

snowballEdge describe-virtual-network-interfaces

```

If one or more VNIs are active on the Snowball Edge, the command returns the following.

```

snowballEdge describe-virtual-network-interfaces
[
  {
    "VirtualNetworkInterfaceArn" : "arn:aws:snowball-device:::interface/s.ni-8EXAMPLE8EXAMPLE8",
    "PhysicalNetworkInterfaceId" : "s.ni-8EXAMPLEaEXAMPLEd",
    "IpAddressAssignment" : "DHCP",
    "IpAddress" : "192.0.2.0",
    "Netmask" : "255.255.255.0",
    "DefaultGateway" : "192.0.2.1",
    "MacAddress" : "EX:AM:PL:E1:23:45"
  },{
    "VirtualNetworkInterfaceArn" : "arn:aws:snowball-device:::interface/s.ni-1EXAMPLE1EXAMPLE1",
    "PhysicalNetworkInterfaceId" : "s.ni-8EXAMPLEaEXAMPLEd",
    "IpAddressAssignment" : "DHCP",
    "IpAddress" : "192.0.2.2",
    "Netmask" : "255.255.255.0",
    "DefaultGateway" : "192.0.2.1",
    "MacAddress" : "12:34:5E:XA:MP:LE"
  }
]

```

Note the value of the `VirtualNetworkInterfaceArn` name of the VNI to use with the NFS interface. 2. If no VNIs are available, use the `create-virtual-network-interface` command to create a VNI for the NFS interface. For more information, see [Setting up a Virtual Network Interface (VNI)](network-config-ec2.md#snowcone-setup-vni "network-config-ec2.md#snowcone-setup-vni"). 3. Use the `start-service` command to start the NFS service and associate it with the VNI. To restrict access to the NFS interface, include the `service-configuration` and `AllowedHosts` parameters in the command.

```

snowballEdge start-service --virtual-network-interface-arns `arn-of-vni` --service-id nfs `--service-configuration AllowedHosts=CIDR-address-range`

```

4. Use the `describe-service` command to check the service status. It is running when the value of the `State` name is `ACTIVE`.

```

snowballEdge describe-service --service-id nfs

```

The command returns the service state, as well as the IP address and port number of the NFS endpoint and the CIDR ranges allowed to access the endpoint.

```

{
 "ServiceId" : "nfs",
 "Status" : {
 "State" : "ACTIVE"
 },
 "Endpoints" : [ {
 "Protocol" : "nfs",
 "Port" : 2049,
 "Host" : "192.0.2.0"
 } ],
 "ServiceConfiguration" : {
 "AllowedHosts" : [ "10.24.34.0/23", "198.51.100.0/24" ]
 }
}

```

### Mounting NFS endpoints on client computers

After the NFS interface is started, mount the endpoint as local storage on client computers.

The following are the default mount commands for Windows, Linux, and macOS operating systems.

- Windows:

```

mount -o nolock rsize=128 wsize=128 mtype=hard `nfs-interface-ip-address`:/buckets/`BucketName` *
```

- Linux:

```

mount -t nfs `nfs-interface-ip-address`:/buckets/`BucketName` mount_point
```

- macOS:

```

mount -t nfs -o vers=3,rsize=131072,wsize=131072,nolocks,hard,retrans=2 `nfs-interface-ip-address`:/buckets/$`bucketname` mount_point
```

### Stopping the NFS interface on Snowball Edge

When you are finished transferring files through the NFS interface and before powering off the Snowball Edge, use the `stop-service` command to stop the NFS service.

```

snowballEdge stop-service --service-id nfs
```
