

# Create and attach an Elastic Fabric Adapter to an Amazon EC2 instance
<a name="create-efa"></a>

You can create an EFA and attach it to an Amazon EC2 instance much like any other elastic network interface in Amazon EC2. However, unlike elastic network interfaces, EFAs can't be attached to or detached from an instance in a `running` state.

**Considerations**
+  You can change the security group that is associated with an EFA. To enable OS-bypass functionality, the EFA must be a member of a security group that allows all inbound and outbound traffic to and from the security group itself. For more information, see [Step 1: Prepare an EFA-enabled security group](efa-start.md#efa-start-security).

  You change the security group that is associated with an EFA in the same way that you change the security group that is associated with an elastic network interface. For more information, see [Modify network interface attributes](modify-network-interface-attributes.md).
+ You assign an Elastic IP (IPv4) and IPv6 address to an EFA (EFA with ENA) network interface in the same way that you assign an IP address to an elastic network interface. For more information, see [Managing IP addresses](managing-network-interface-ip-addresses.md).

  You can't assign an IP address to an EFA-only network interface.

**Topics**
+ [Create an EFA](#efa-create)
+ [Attach an EFA to a stopped instance](#efa-attach)
+ [Attach an EFA when launching an instance](#efa-launch)
+ [Add an EFA to a launch template](#efa-launch-template)

## Create an EFA
<a name="efa-create"></a>

You can create an EFA in a subnet in a VPC. You can't move the EFA to another subnet after it's created, and you can only attach it to stopped instances in the same Availability Zone.

------
#### [ Console ]

**To create an EFA (EFA with ENA or ENA-only) network interface**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Network Interfaces** and then choose **Create network interface**.

1. For **Description**, enter a descriptive name for the EFA.

1. For **Subnet**, select the subnet in which to create the EFA.

1. **Interface type**, choose one of the following options:
   + **EFA with ENA** — To create a network interface that supports both ENA and EFA devices.
   + **EFA-only** — To create a network interface with an EFA device only.

1. (For EFA with ENA only) Configure the IP address and prefix assignment for the network interface. The type of IP addresses and prefixes you can assign depend on the selected subnet. For IPv4-only subnets, you can assign IPv4 IP addresses and prefixes only. For IPv6-only subnets, you can assign IPv6 IP addresses and prefixes only. For dual-stack subnets, you can assign both IPv4 and IPv6 IP addresses and prefixes. 
**Note**  
You can't assign IP addresses to an EFA-only network interface.

   1. For **Private IPv4 address** and/or **IPv6 address**, choose **Auto-assign** to have Amazon EC2 automatically assign an IP address from the selected subnet, or choose **Custom** to manually specify the IP address to assign.

   1. If you assign an IPv6 address, you can optionally enable **Assign primary IPv6 IP**. Doing this assigns a primary IPv6 global unicast address (GUA) to the network interface. Assigning a primary IPv6 address enables you to avoid disrupting traffic to instances or ENIs. For more information, see [IPv6 addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#vpc-ipv6-addresses).

   1. For **IPv4 prefix delegation** and/or **IPv6 prefix delegation**, choose **Auto-assign** to have Amazon EC2 automatically assign a prefix from the subnet's CIDR block, or choose **Custom** to manually specify a prefix from the subnet's CIDR block. If you specify a prefix, AWS verifies that it is not already assigned to another resource. For more information, see [Prefix delegation for Amazon EC2 network interfaces](ec2-prefix-eni.md)

   1. (Optional) Configure the **Idle connection tracking timeout** settings. For more information, see [Idle connection tracking timeout](security-group-connection-tracking.md#connection-tracking-timeouts)
      + **TCP established timeout** — The timeout period, in seconds, for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.
      + **UDP timeout** — The timeout period, in seconds, for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.
      + **UDP stream timeout** — The timeout period, in seconds, for idle UDP flows classified as streams that have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

1. For **Security groups**, select one or more security groups.

1. Choose **Create network interface**.

------
#### [ AWS CLI ]

**To create an EFA**  
Use the [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) command. For `--interface-type`, specify `efa` for an EFA network interface or `efa-only` for an EFA-only network interface.

```
aws ec2 create-network-interface \
    --subnet-id {{subnet-0abcdef1234567890}} \
    --interface-type {{efa}} \
    --description "{{my efa}}"
```

------
#### [ PowerShell ]

**To create an EFA**  
Use the [New-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2NetworkInterface.html) cmdlet. For `-InterfaceType`, specify `efa` for an EFA network interface or `efa-only` for an EFA-only network interface

```
New-EC2NetworkInterface `
    -SubnetId {{subnet-0abcdef1234567890}} `
    -InterfaceType {{efa}} `
    -Description "{{my efa}}"
```

------

## Attach an EFA to a stopped instance
<a name="efa-attach"></a>

You can attach an EFA to any supported instance that is in the `stopped` state. You cannot attach an EFA to an instance that is in the `running` state. For more information about the supported instance types, see [Supported instance types](efa.md#efa-instance-types).

You attach an EFA to an instance in the same way that you attach a network interface to an instance. For more information, see [Attach a network interface](network-interface-attachments.md#attach_eni).

## Attach an EFA when launching an instance
<a name="efa-launch"></a>

------
#### [ AWS CLI ]

**To attach an existing EFA when launching an instance**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command with the `--network-interfaces` option. For the primary network interface, specify an EFA network interface and `NetworkCardIndex=0`, `DeviceIndex=0`. To attach multiple EFA network interfaces, see [Maximize network bandwidth](efa-acc-inst-types.md).

```
--network-interfaces "NetworkCardIndex=0, \
    DeviceIndex=0, \
    NetworkInterfaceId={{eni-1234567890abcdef0}}, \
    Groups={{sg-1234567890abcdef0}}, \
    SubnetId={{subnet-0abcdef1234567890}}"
```

**To attach a new EFA when launching an instance**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command with the `--network-interfaces` option. For the primary network interface, use `NetworkCardIndex=0`, `DeviceIndex=0`, and `InterfaceType=efa`. If you are attaching multiple EFA network interfaces, see [Maximize network bandwidth](efa-acc-inst-types.md).

```
--network-interfaces "NetworkCardIndex=0, \
    DeviceIndex=0, \
    InterfaceType=efa, \
    Groups={{sg-1234567890abcdef0}}, \
    SubnetId={{subnet-0abcdef1234567890}}"
```

------
#### [ PowerShell ]

**To attach an existing EFA when launching an instance**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet with the `-NetworkInterfaces` parameter.

```
-NetworkInterface $networkInterface
```

Define the network interface as follows.

```
$networkInterface = New-Object Amazon.EC2.Model.InstanceNetworkInterfaceSpecification
$networkInterface.DeviceIndex = 0
$networkInterface.NetworkInterfaceId = "{{eni-1234567890abcdef0}}"
$networkInterface.Groups = @("{{sg-1234567890abcdef0}}")
$networkInterface.SubnetId = "{{subnet-0abcdef1234567890}}"
```

**To attach a new EFA when launching an instance**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet with the `-NetworkInterfaces` parameter.

```
-NetworkInterface $networkInterface
```

Define the network interface as follows.

```
$networkInterface = New-Object Amazon.EC2.Model.InstanceNetworkInterfaceSpecification
$networkInterface.DeviceIndex = 0
$networkInterface.InterfaceType = "efa"
$networkInterface.Groups = @("{{sg-1234567890abcdef0}}")
$networkInterface.SubnetId = "{{subnet-0abcdef1234567890}}"
```

------

## Add an EFA to a launch template
<a name="efa-launch-template"></a>

You can create a launch template that contains the configuration information needed to launch EFA-enabled instances. You can specify both EFA and EFA-only network interfaces in the launch template. To create an EFA-enabled launch template, create a new launch template and specify a supported instance type, your EFA-enabled AMI, and an EFA-enabled security group. For `NetworkInterfaces`, specify the EFA network interfaces to attach. For the primary network interface, use `NetworkCardIndex=0`, `DeviceIndex=0`, and `InterfaceType=efa`. If you are attaching multiple EFA network interfaces, see [Maximize network bandwidth on Amazon EC2 instances with multiple network cards](efa-acc-inst-types.md).

You can leverage launch templates to launch EFA-enabled instances with other AWS services, such as [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) or [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html).

For more information about creating launch templates, see [Create an Amazon EC2 launch template](create-launch-template.md).