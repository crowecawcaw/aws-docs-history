AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Troubleshooting compute instances on

Snowball Edge

Following, you can find troubleshooting tips for computer instances on Snowball Edge devices.

###### Topics

- [Virtual Network Interface has an IP
  Address of 0.0.0.0](#troubleshoot-vnic-ipaddress "#troubleshoot-vnic-ipaddress")
- [Snowball Edge device stops responding when launching a
  large compute instance](#ec2-edge-launch-stopped "#ec2-edge-launch-stopped")
- [My instance on the Snowball Edge has one root volume](#multiple-root-volume "#multiple-root-volume")
- [Unprotected private key file error](#pem-key-perms-ec2-edge "#pem-key-perms-ec2-edge")

## Virtual Network Interface has an IP

Address of 0.0.0.0

This issue can occur if the physical network interface (NIC) you associated with
your virtual network interface (VNIC) also has an IP address of 0.0.0.0. This effect
can happen if the NIC wasn't configured with an IP address (for instance, if
you've just powered on the device). It can also happen if you're using the
wrong interface. For example, you might be trying to get the IP address of the SFP+
interface, but it's the RJ45 interface that's connected to your network.

###### Action to Take

If this occurs, you can do the following:

- Create a new VNI associated with a NIC that has an IP address. For more
  information, see [Network configurations for compute instances on Snowball Edge](network-config-ec2.md "network-config-ec2.md").
- Update an existing VNI. For more information, see [Updating a Virtual Network Interface on a Snowball Edge](using-ec2-edge-client.md#ec2-edge-update-vnic "using-ec2-edge-client.md#ec2-edge-update-vnic").

## Snowball Edge device stops responding when launching a

large compute instance

It can appear that your Snowball Edge has stopped launching an instance. This is
generally not the case. However, it can take an hour or more for the largest compute
instances to launch.

To check the status of your instances, use the AWS CLI command `aws ec2
 describe-instances` run against the HTTP or HTTPS Amazon EC2-compatible endpoint on the
Snowball Edge.

## My instance on the Snowball Edge has one root volume

Instances have one root volume by design. All `sbe` instances have a
single root volume, but on a Snowball Edge device, you can add or remove block storage
based on the needs of your applications. For more information, see [Using block storage with Amazon EC2-compatible instances on Snowball Edge](edge-ebs.md "edge-ebs.md").

## Unprotected private key file error

This error can occur if your `.h` file on your compute instance has insufficient
read/write permissions.

###### Action to Take

You can resolve this by changing the permissions for the file with the following
procedure:

1. Open a terminal and navigate to the location where you saved your `.pem` file.
2. Enter the following command.

```
chmod 400 `filename.pem`
```
