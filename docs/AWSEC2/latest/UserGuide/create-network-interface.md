

# Create a network interface for your EC2 instance
<a name="create-network-interface"></a>

You can create a network interface for use by your EC2 instances. When you create a network interface, you specify the subnet for which it is created. You can't move a network interface to another subnet after it's created. You must attach a network interface to an instance in the same Availability Zone. You can detach a secondary network interface from an instance and then attach it to a different instance in the same Availability Zone. You can't detach a primary network interface from an instance. For more information, see [Network interface attachments for your EC2 instance](network-interface-attachments.md).

------
#### [ Console ]

**To create a network interface**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Network Interfaces**.

1. Choose **Create network interface**.

1. (Optional) For **Description**, enter a descriptive name.

1. For **Subnet**, select a subnet. The options available in the subsequent steps change depending on the type of subnet you select (IPv4-only, IPv6-only, or dual-stack (IPv4 and IPv6)).

1. For **Interface type**, choose one of the following:
   + **ENA**: A high-performance network interface designed to handle high throughput and packet-per-second rates for TCP/IP protocols while minimizing CPU usage. This is the default value. For more information about ENA, see [Elastic Network Adapter](enhanced-networking-ena.md).
   + **EFA with ENA**: A network interface that supports both ENA and EFA devices for traditional TCP/IP based transport along with SRD based transport. If you choose EFA with ENA, the instance you are attaching it to must [support EFA](efa.md#efa-instance-types). For more information about EFA, see [Elastic Fabric Adapter](efa.md).
   + **EFA-only**: A high-performance network interface designed to handle high throughput, low latency inter-node communication for SRD based transport while bypassing the operating system stack. If you choose this option, the instance you are attaching it to must [support EFA](efa.md#efa-instance-types). EFA-only network interfaces do not support IP addresses. For more information about EFA, see [Elastic Fabric Adapter](efa.md).

1. For **Private IPv4 address**, do one of the following:
   + Choose **Auto-assign** to allow Amazon EC2 to select an IPv4 address from the subnet.
   + Choose **Custom** and enter an IPv4 address that you select from the subnet.

1. (Subnets with IPv6 addresses only) For **IPv6 address**, do one of the following:
   + Choose **None** if you do not want to assign an IPv6 address to the network interface.
   + Choose **Auto-assign** to allow Amazon EC2 to select an IPv6 address from the subnet.
   + Choose **Custom** and enter an IPv6 address that you select from the subnet.

1. (Optional) If you’re creating a network interface in a dual-stack or IPv6-only subnet, you have the option to **Assign Primary IPv6 IP**. This assigns a primary IPv6 global unicast address (GUA) to the network interface. Assigning a primary IPv6 address enables you to avoid disrupting traffic to instances or ENIs. Choose **Enable** if the instance that this ENI will be attached to relies on its IPv6 address not changing. AWS will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. After you enable an IPv6 GUA address to be a primary IPv6, you can't disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.

1. (Optional) To create an Elastic Fabric Adapter, choose **Elastic Fabric Adapter**, **Enable**.

1. (Optional) Under **Advanced settings**, you can optionally set IP prefix delegation. For more information, see [Prefix delegation](ec2-prefix-eni.md).
   + **Auto-assign** — AWS chooses the prefix from the IPv4 or IPv6 CIDR blocks for the subnet, and assigns it to the network interface.
   + **Custom** — You specify the prefix from the IPv4 or IPv6 CIDR blocks for the subnet, and AWS verifies that the prefix is not already assigned to other resources before assigning it to the network interface.

1. (Optional) Under **Advanced settings**, for **Idle connection tracking timeout**, modify the default idle connection timeouts. For more information, see [Idle connection tracking timeout](security-group-connection-tracking.md#connection-tracking-timeouts).
   + **TCP established timeout**: Timeout (in seconds) for idle TCP connections in an established state.
     + Min: `60` seconds
     + Max: `432000` seconds
     + Default: `350` seconds for [Nitro v6](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) instance types (excluding P6e-GB200); `432000` seconds for all other instance types (including P6e-GB200).
     + Recommended: Less than `432000` seconds
   + **UDP timeout**: Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.
     + Min: `30` seconds
     + Max: `60` seconds
     + Default: `30` seconds
   + **UDP stream timeout**: Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.
     + Min: `60` seconds
     + Max: `180` seconds
     + Default: `180` seconds

1. For **Security groups**, select one or more security groups.

1. (Optional) For each tag, choose **Add new tag** and enter a tag key and an optional tag value.

1. Choose **Create network interface**.

------
#### [ AWS CLI ]

**Example 1: To create a network interface with IP addresses chosen by Amazon EC2**  
Use the following [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) command. This example creates a network interface with a public IPv4 address and an IPv6 address chosen by Amazon EC2.

```
aws ec2 create-network-interface \
    --subnet-id {{subnet-0abcdef1234567890}} \
    --description "{{my dual-stack network interface}}" \
    --ipv6-address-count {{1}} \
    --groups {{sg-1234567890abcdef0}}
```

**Example 2: To create a network interface with specific IP addresses**  
Use the following [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) command.

```
aws ec2 create-network-interface \
    --subnet-id {{subnet-0abcdef1234567890}} \
    --description "{{my dual-stack network interface}}" \
    --private-ip-address {{10.251.50.12}} \
    --ipv6-addresses {{2001:db8::1234:5678:1.2.3.4}} \
    --groups {{sg-1234567890abcdef0}}
```

**Example 3: To create a network interface with a count of secondary IP addresses**  
Use the following [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) command. In this example, Amazon EC2 chooses both the primary IP address and the secondary IP addresses.

```
aws ec2 create-network-interface \
    --subnet-id {{subnet-0abcdef1234567890}} \
    --description "{{my network interface}}" \
    --secondary-private-ip-address-count {{2}} \
    --groups {{sg-1234567890abcdef0}}
```

**Example 4: To create a network interface with a specific secondary IP address**  
Use the following [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) command. This example specifies a primary IP address and a secondary IP address.

```
aws ec2 create-network-interface \
    --subnet-id {{subnet-0abcdef1234567890}} \
    --description "{{my network interface}}" \
    --private-ip-addresses PrivateIpAddress={{10.0.1.30}},Primary=true \
                           PrivateIpAddress={{10.0.1.31}},Primary=false
    --groups {{sg-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**Example 1: To create a network interface with IP addresses chosen by Amazon EC2**  
Use the [New-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2NetworkInterface.html) cmdlet. This example creates a network interface with a public IPv4 address and an IPv6 address chosen by Amazon EC2.

```
New-EC2NetworkInterface `
    -SubnetId {{subnet-0abcdef1234567890}} `
    -Description "{{my dual-stack network interface}}" `
    -Ipv6AddresCount {{1}} `
    -Group {{sg-1234567890abcdef0}}
```

**Example 2: To create a network interface with specific IP addresses**  
Use the [New-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2NetworkInterface.html) cmdlet.

```
New-EC2NetworkInterface `
    -SubnetId {{subnet-0abcdef1234567890}} `
    -Description "{{my dual-stack network interface}}" `
    -PrivateIpAddress {{10.251.50.12}} `
    -Ipv6Address $ipv6addr `
    -Group {{sg-1234567890abcdef0}}
```

Define the IPv6 addresses as follows.

```
$ipv6addr = New-Object Amazon.EC2.Model.InstanceIpv6Address
$ipv6addr1.Ipv6Address = "{{2001:db8::1234:5678:1.2.3.4}}"
```

**Example 3: To create a network interface with a count of secondary IP addresses**  
Use the [New-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2NetworkInterface.html) cmdlet. In this example, Amazon EC2 chooses both the primary IP address and the secondary IP addresses.

```
New-EC2NetworkInterface `
    -SubnetId {{subnet-0abcdef1234567890}} `
    -Description "{{my network interface}}" `
    -SecondaryPrivateIpAddressCount {{2}} `
    -Group {{sg-1234567890abcdef0}}
```

**Example 4: To create a network interface with a specific secondary IP address**  
Use the [New-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2NetworkInterface.html) cmdlet. This example specifies a primary IP address and a secondary IP address.

```
New-EC2NetworkInterface `
    -SubnetId {{subnet-0abcdef1234567890}} `
    -Description "{{my network interface}}" `
    -PrivateIpAddresses @($primary, $secondary) `
    -Group {{sg-1234567890abcdef0}}
```

Define the secondary addresses as follows.

```
$primary = New-Object Amazon.EC2.Model.PrivateIpAddressSpecification
$primary.PrivateIpAddress = "{{10.0.1.30}}"
$primary.Primary = $true
$secondary = New-Object Amazon.EC2.Model.PrivateIpAddressSpecification
$secondary.PrivateIpAddress = "{{10.0.1.31}}"
$secondary.Primary = $false
```

------