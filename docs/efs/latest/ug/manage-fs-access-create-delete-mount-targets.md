# Creating mount targets

To access an EFS file system in a VPC, you need to create mount targets for
the file system.

For an EFS file system, the following is true:

- You can create mount targets for the file system in one VPC at a time. If you want
  to access the file system from another VPC, you need to delete the mount targets from
  the current VPC and then create new mount targets in the other VPC. For more
  information, see [Changing the mount target VPC](manage-fs-access-change-vpc.md "manage-fs-access-change-vpc.md").
- If the VPC has multiple subnets in an Availability Zone, you can create a mount target
  in only one of those subnets. All EC2 instances in the Availability Zone can share
  the single mount target.
- At a minimum, you should create a mount target in each Availability Zone from which you
  want to access the file system.

###### Note

There are cost considerations for mounting a file system on an EC2 instance
in an Availability Zone through a mount target created in another Availability Zone. For more
information, see [Amazon EFS Pricing](https://aws.amazon.com/efs/pricing "https://aws.amazon.com/efs/pricing"). In
addition, by always using a mount target local to the instance's Availability Zone, you remove a
partial failure scenario. If the mount target's zone goes down, you can't access your
file system through that mount target.

You can create mount targets for a file system by using the AWS Management Console, AWS CLI, or
programmatically by using the AWS SDKs. In the console, you can create mount targets when
you create the file system or after the file system is created. For instructions on creating
mount targets when creating a file system, see [Custom create using the console](creating-using-create-fs.md#creating-using-fs-part1-console "creating-using-create-fs.md#creating-using-fs-part1-console").

Use the following procedure to add mount targets to an existing EFS file
system.

###### To create a mount target on an EFS file system

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. In the left navigation pane, choose **File systems**, and
   then select the file system for which you want to change the VPC.
3. Choose **Network** and then choose
   **Manage** to display the mount targets for the file
   system.
4. Choose the file system that you want to add mount targets for by choosing
   its **Name** or the **File system ID**.

###### Note

For One Zone file systems, you can only create a single mount
target that is in the same Availability Zone as the file system. 5. For file systems that use EFS Regional storage classes,
choose **Add mount target** for each mount target you want to
create for the file system. 6. Define the mount target settings:

    1. Choose the Availability Zone and subnet ID for the mount target.
    2. For **IP address type**, choose **IPv4 only** to support IPv4 addresses only, **IPv6 only** to support IPv6 addresses only, or **Dual-stack** to support both IPv4 and IPv6
     addresses.


    ###### Note

    The IP address type must match the IP type of the subnet. Additionally,
     the IP address type overrides the IP addressing attribute of your subnet. For
     example, if the IP address type is IPv4-only and the IPv6 addressing attribute
     is enabled for your subnet, network interfaces created in the subnet receive
     an IPv4 address from the range of the subnet. For more information, see [Modify
     the IP addressing attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md").
    3. If you know the IP address where you want to place the mount target, then
     enter it in the IP address box that matches the **IP
     address type**. If you don't specify a value, Amazon EFS selects an unused
     IP address from the specified subnet.


    ###### Note

    You can't change the IP address of a mount target after it's created. To
     change an IP address, you need to delete the mount target and create a new one
     with the new address.

7. Choose at least one security group to associate with the mount target. You can
   [modify the security
   groups](manage-fs-access-update-mount-target-config-sg.md "manage-fs-access-update-mount-target-config-sg.md") later.
8. Choose **Save**.
   This section provide examples for creating a mount target in the AWS CLI
   using the `create-mount-target` command. The equivalent API command is
   [CreateMountTarget](API_CreateMountTarget.md "API_CreateMountTarget.md").

- If you don't specify an IP address type for the mount target, then IPv4-only
  is used.
- If you don't specify an IP address for the mount target, then Amazon EFS assigns an
  available address on the specified subnet.
- The IP address type overrides the IP addressing attribute of your subnet.
  For example, if the IP address type is IPv4-only and the IPv6 addressing
  attribute is enabled for your subnet, network interfaces created in the subnet
  receive an IPv4 address from the range of the subnet. For more information,
  see [Modify the IP addressing attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md").

###### Note

For One Zone file systems, you can only create a single mount target that is in the
same Availability Zone as the file system.

The following command specifies the file system, subnet, and security group for the mount target.
The target is created at an available IPv4 address on the specified subnet.

```
`$` aws efs create-mount-target \
--file-system-id `file-system-id` \
--subnet-id  `subnet-id` \
--security-group `ID-of-the-security-group-created-for-mount-target` \
--region `aws-region` \
```

The following example shows the command with sample data.

```
`$` aws efs create-mount-target \
--file-system-id fs-0123456789abcdef1 \
--subnet-id  subnet-b3983dc4 \
--security-group sg-01234567 \
--region us-east-2 \
```

After successfully creating the mount target, Amazon EFS returns the mount target
description as JSON as shown in the following example.

```
{
    "OwnerID": "111122223333"
    "MountTargetId": "fsmt-f9a14450",
    "FileSystemId": "fs-0123456789abcdef1",
    "SubnetId": "subnet-b3983dc4",
    "LifeCycleState": "available",
    "IpAddress": "10.0.1.24",
    "NetworkInterfaceId": "eni-3851ec4e",
    "AvailabilityZoneId": "use2-az1",
    "AvailabilityZoneName": "us-east-2a",
    "VpcId": "vpc-3c39ef57"
}
```

The following command specifies the file system, subnet, security group,
and IPv4 address to use for the mount target. The target is created at the
specified IPv4 address on the specified subnet.

```
`$` aws efs create-mount-target \
--file-system-id `file-system-id` \
--subnet-id  `subnet-id` \
--security-group `ID-of-the-security-group-created-for-mount-target` \
--ip-address `IPv4-address`
--region `aws-region` \
```

The following example shows the command with sample data.

```
`$` aws efs create-mount-target \
--file-system-id fs-0123456789abcdef1 \
--subnet-id  subnet-b3983dc4 \
--security-group sg-01234567 \
--ip-address 10.0.1.24 \
--region us-east-2 \
```

After successfully creating the mount target, Amazon EFS returns the mount target
description as JSON as shown in the following example.

```
{
    "OwnerID": "111122223333"
    "MountTargetId": "fsmt-f9a14450",
    "FileSystemId": "fs-0123456789abcdef1",
    "SubnetId": "subnet-b3983dc4",
    "LifeCycleState": "available",
    "IpAddress": "10.0.1.24",
    "NetworkInterfaceId": "eni-3851ec4e",
    "AvailabilityZoneId": "use2-az1",
    "AvailabilityZoneName": "us-east-2a",
    "VpcId": "vpc-3c39ef57"
}
```

The following command specifies the file system, subnet, security group, and
IPv6 address to use for the mount target. The target is created at the specified
IPv6 address on the specified subnet.

```
`$` aws efs create-mount-target \
--file-system-id `file-system-id` \
--subnet-id  `subnet-id` \
--security-group `ID-of-the-security-group-created-for-mount-target` \
--ip-address-type `IP-address-type` \
--ipv6-address `IPv6-address` \
--region `aws-region` \
```

The following example shows the command with sample data.

```
`$` aws efs create-mount-target \
--file-system-id fs-0123456789abcdef1 \
--subnet-id  subnet-b3983dc4 \
--security-group sg-01234567 \
--ip-address-type IPV6_ONLY \
--ipv6-address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 \
--region us-east-2 \
```

After successfully creating the mount target, Amazon EFS returns the mount target
description as JSON as shown in the following example.

```
{
    "OwnerID": "111122223333"
    "MountTargetId": "fsmt-f9a14450",
    "FileSystemId": "fs-0123456789abcdef1",
    "SubnetId": "subnet-b3983dc4",
    "LifeCycleState": "available",
    "Ipv6Address": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "NetworkInterfaceId": "eni-3851ec4e",
    "AvailabilityZoneId": "use2-az1",
    "AvailabilityZoneName": "us-east-2a",
    "VpcId": "vpc-3c39ef57"
}
```

The command specifies the file system, subnet, security group, dual-stack IP
address type, and IPv6 address for the mount target. The target is created at an
available IPv4 address and the specified IPv6 address on the dual-stack
subnet.

```
`$` aws efs create-mount-target \
--file-system-id `file-system-id` \
--subnet-id  `subnet-id` \
--security-group `ID-of-the-security-group-created-for-mount-target` \
--ip-address-type `IP-address-type`
--ipv6-address `IPv6-address` \
--region `aws-region` \
```

The following example shows the command with sample data.

```
`$` aws efs create-mount-target \
--file-system-id fs-0123456789abcdef1 \
--subnet-id  subnet-b3983dc4 \
--security-group sg-01234567 \
--ip-address-type DUAL_STACK \
--ipv6-address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 \
--region us-east-2 \
```

After successfully creating the mount target, Amazon EFS returns the mount target
description as JSON as shown in the following example.

```
{
    "OwnerID": "111122223333"
    "MountTargetId": "fsmt-f9a14450",
    "FileSystemId": "fs-0123456789abcdef1",
    "SubnetId": "subnet-b3983dc4",
    "LifeCycleState": "available",
    "IpAddress": "10.0.1.24",
    "Ipv6Address": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "NetworkInterfaceId": "eni-3851ec4e",
    "AvailabilityZoneId": "use2-az1",
    "AvailabilityZoneName": "us-east-2a",
    "VpcId": "vpc-3c39ef57"
}
```
