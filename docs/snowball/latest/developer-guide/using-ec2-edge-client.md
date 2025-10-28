Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Starting EC2-compatible instances automatically

The Snowball Edge Client is a standalone command line interface (CLI) application that you can run in your environment. You can use it to perform some administrative tasks on your
Snowball Edge device or cluster of devices. For more information about how to use the
Snowball Edge client, including how to start and stop services with it, see [Configuring and using the Snowball Edge Client](using-client-commands.md "using-client-commands.md").

Following, you can find information about the Snowball Edge client commands that are
specific to compute instances, including examples of use.

For a list of Amazon EC2-compatible commands you can use on your AWS Snowball Edge device, see [Supported Amazon EC2-compatible AWS CLI commands on a Snowball Edge](using-ec2-endpoint.md#cli-support-ec2-edge "using-ec2-endpoint.md#cli-support-ec2-edge").

## Creating an EC2-compatible launch configuration on a Snowball Edge

To automatically start Amazon EC2-compatible compute instances on your AWS Snowball Edge device after it is
unlocked, you can create a launch configuration. To do so, use the
`snowballEdge create-autostart-configuration` command, as shown
following.

**Usage**

```
snowballEdge create-autostart-configuration --physical-connector-type [SFP_PLUS or RJ45 or QSFP] --ip-address-assignment [DHCP or STATIC] [--static-ip-address-configuration IpAddress=[IP address],NetMask=[Netmask]] --launch-template-id [--launch-template-version]
```

## Updating an EC2-compatible launch configuration on a Snowball Edge

To update an existing launch configuration on your Snowball Edge, use the
`snowballEdge update-autostart-configuration` command. You can find
its usage following. To enable or disable a launch configuration, specify the
`--enabled` parameter.

**Usage**

```
snowballEdge update-autostart-configuration --autostart-configuration-arn [--physical-connector-type [SFP_PLUS or RJ45 or QSFP]] [--ip-address-assignment [DHCP or STATIC]] [--static-ip-address-configuration IpAddress=[IP address],NetMask=[Netmask]][--launch-template-id] [--launch-template-version] [--enabled]
```

## Deleting an EC2-compatible launch configuration on a Snowball Edge

To delete a launch configuration that's no longer in use, use the
`snowballEdge delete-autostart-configuration` command, as
follows.

**Usage**

```
snowballEdge delete-autostart-configuration --autostart-configuration-arn
```

## Listing EC2-compatible launch configurations on a Snowball Edge

To list the launch configurations that you have created on your Snowball Edge,
use the `describe-autostart-configurations` command, as follows.

**Usage**

```
snowballEdge describe-autostart-configurations
```

## Creating a Virtual Network Interface on a Snowball Edge

To run a compute instance or start the NFS interface on
a Snowball Edge, first create a Virtual Network Interface (VNI). Each
Snowball Edge has three network interfaces (NICs), the physical network interface
controllers for the device. These are the RJ45, SFP, and QSFP ports on the back of
the device.

Each VNI is based on a physical one, and you can have any number of VNI s
associated with each NIC. To create a virtual network interface, use the
`snowballEdge create-virtual-network-interface` command.

###### Note

The `--static-ip-address-configuration` parameter is valid only
when using the `STATIC` option for the
`--ip-address-assignment` parameter.

**Usage**

You can use this command in two ways: with the Snowball Edge client configured,
or without the Snowball Edge client configured. The following usage example shows
the method with the Snowball Edge client configured.

```
snowballEdge create-virtual-network-interface --ip-address-assignment `[DHCP or STATIC]` --physical-network-interface-id `[physical network interface id]` --static-ip-address-configuration IpAddress=`[IP address]`,NetMask=`[Netmask]`
```

The following usage example shows the method without the Snowball Edge client
configured.

```
snowballEdge create-virtual-network-interface --endpoint https://`[ip address]` --manifest-file `/path/to/manifest` --unlock-code `[unlock code]` --ip-address-assignment `[DHCP or STATIC]` --physical-network-interface-id `[physical network interface id]` --static-ip-address-configuration IpAddress=`[IP address]`,NetMask=`[Netmask]`
```

###### Example: Creating VNICs (Using DHCP)

```
snowballEdge create-virtual-network-interface --ip-address-assignment dhcp --physical-network-interface-id s.ni-8EXAMPLEaEXAMPLEd
{
  "VirtualNetworkInterface" : {
    "VirtualNetworkInterfaceArn" : "arn:aws:snowball-device:::interface/s.ni-8EXAMPLE8EXAMPLEf",
    "PhysicalNetworkInterfaceId" : "s.ni-8EXAMPLEaEXAMPLEd",
    "IpAddressAssignment" : "DHCP",
    "IpAddress" : "192.0.2.0",
    "Netmask" : "255.255.255.0",
    "DefaultGateway" : "192.0.2.1",
    "MacAddress" : "EX:AM:PL:E1:23:45",
    "MtuSize" : "1500"
  }
}
```

## Describing Your Virtual Network

Interfaces

To describe the VNICs that you previously created on your device, use the
`snowballEdge describe-virtual-network-interfaces` command. You can
find its usage following.

**Usage**

You can use this command in two ways: with the Snowball Edge client configured,
or without the Snowball Edge client configured. The following usage example shows
the method with the Snowball Edge client configured.

```
snowballEdge describe-virtual-network-interfaces
```

The following usage example shows the method without the Snowball Edge client
configured.

```
snowballEdge describe-virtual-network-interfaces --endpoint https://`[ip address]` --manifest-file `/path/to/manifest` --unlock-code `[unlock code]`
```

###### Example: Describing VNICs

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
    "MacAddress" : "EX:AM:PL:E1:23:45",
    "MtuSize" : "1500"
  },{
    "VirtualNetworkInterfaceArn" : "arn:aws:snowball-device:::interface/s.ni-1EXAMPLE1EXAMPLE1",
    "PhysicalNetworkInterfaceId" : "s.ni-8EXAMPLEaEXAMPLEd",
    "IpAddressAssignment" : "DHCP",
    "IpAddress" : "192.0.2.2",
    "Netmask" : "255.255.255.0",
    "DefaultGateway" : "192.0.2.1",
    "MacAddress" : "12:34:5E:XA:MP:LE",
    "MtuSize" : "1500"
  }
]
```

## Updating a Virtual Network Interface on a Snowball Edge

After creating a virtual network interface (VNI), you can update its
configuration using the `snowballEdge update-virtual-network-interface`
command. After providing the Amazon Resource Name (ARN) for a particular VNI, you
provide values only for whatever elements you are updating.

**Usage**

You can use this command in two ways: with the Snowball Edge client configured,
or without the Snowball Edge client configured. The following usage example shows
the method with the Snowball Edge client configured.

```
snowballEdge update-virtual-network-interface --virtual-network-interface-arn `[virtual network-interface-arn]` --ip-address-assignment `[DHCP or STATIC]` --physical-network-interface-id `[physical network interface id]` --static-ip-address-configuration IpAddress=`[IP address]`,NetMask=`[Netmask]`
```

The following usage example shows the method without the Snowball Edge client
configured.

```
snowballEdge update-virtual-network-interface --endpoint https://`[ip address]` --manifest-file `/path/to/manifest` --unlock-code `[unlock code]` --virtual-network-interface-arn `[virtual network-interface-arn]` --ip-address-assignment `[DHCP or STATIC]` --physical-network-interface-id `[physical network interface id]` --static-ip-address-configuration IpAddress=`[IP address]`,NetMask=`[Netmask]`
```

###### Example: Updating a VNIC (Using DHCP)

```
snowballEdge update-virtual-network-interface --virtual-network-interface-arn arn:aws:snowball-device:::interface/s.ni-8EXAMPLEbEXAMPLEd --ip-address-assignment dhcp
```

## Deleting a Virtual Network Interface on a Snowball Edge

To delete a virtual network interface (VNI), you can use the `snowballEdge
 delete-virtual-network-interface` command.

**Usage**

You can use this command in two ways: with the Snowball Edge client configured,
or without the Snowball Edge client configured. The following usage example shows
the method with the Snowball Edge client configured.

```
snowballEdge delete-virtual-network-interface --virtual-network-interface-arn `[virtual network-interface-arn]`
```

The following usage example shows the method without the Snowball Edge client
configured.

```
snowballEdge delete-virtual-network-interface --endpoint https://`[ip address]` --manifest-file `/path/to/manifest` --unlock-code `[unlock code]` --virtual-network-interface-arn `[virtual network-interface-arn]`
```

###### Example: Deleting a VNIC

```
snowballEdge delete-virtual-network-interface --virtual-network-interface-arn arn:aws:snowball-device:::interface/s.ni-8EXAMPLEbEXAMPLEd
```
