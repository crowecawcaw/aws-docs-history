# Associate an Elastic IP address with an instance

After you allocate an Elastic IP address, you can associate it with an AWS resource,
such as an EC2 instance, NAT gateway, or Network Load Balancer. To associate an Elastic IP address with
a different AWS resource later on, you can disassociate it from its current resource
and then associated it with the new resource.

###### Tasks

- [Allocate an Elastic IP address](#using-instance-addressing-eips-allocating "#using-instance-addressing-eips-allocating")
- [Associate an Elastic IP address](#using-instance-addressing-eips-associating "#using-instance-addressing-eips-associating")
- [Disassociate an Elastic IP
  address](#using-instance-addressing-eips-associating-different "#using-instance-addressing-eips-associating-different")

## Allocate an Elastic IP address

You can allocate an Elastic IP address for use in a Region. There is a charge for all
Elastic IP addresses whether they are in use (associated with a resource, like an EC2 instance)
or idle (created in your account but unassociated).

Console

###### To allocate an Elastic IP address

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network & Security**,
   **Elastic IPs**.
3. Choose **Allocate Elastic IP address**.
4. (Optional) When you allocate an Elastic IP address (EIP), you
   choose the **Network border group** in which to
   allocate the EIP. A network border group is a collection of
   Availability Zones (AZs), Local Zones, or Wavelength Zones from
   which AWS advertises a public IP address. Local Zones and
   Wavelength Zones may have different network border groups than
   the AZs in a Region to ensure minimum latency or physical
   distance between the AWS network and the customers accessing
   the resources in these Zones.

###### Important

You must allocate an EIP in the same network border group
as the AWS resource that will be associated with the EIP.
An EIP in one network border group can only be advertised in
zones in that network border group and not in any other
zones represented by other network border groups.

If you have Local Zones or Wavelength Zones enabled (for more
information, see [Enable a Local Zone](../../../local-zones/latest/ug/getting-started.md#getting-started-find-local-zone "../../../local-zones/latest/ug/getting-started.md#getting-started-find-local-zone") or [Enable Wavelength Zones](../../../wavelength/latest/developerguide/get-started-wavelength.md#enable-zone-group "../../../wavelength/latest/developerguide/get-started-wavelength.md#enable-zone-group")), you can choose a network
border group for AZs, Local Zones, or Wavelength Zones. Choose
the network border group carefully as the EIP and the AWS
resource it is associated with must reside in the same network
border group. You can use the EC2 console to view the network
border group that your Availability Zones, Local Zones, or
Wavelength Zones are in. Typically, all Availability Zones in
a Region belong to the same network border group, whereas Local
Zones or Wavelength Zones belong to their own separate network
border groups.

If you don't have Local Zones or Wavelength Zones enabled,
when you allocate an EIP, the network border group that
represents all of the AZs for the Region (such as
`us-west-2`) is predefined for you and you cannot
change it. This means that the EIP that you allocate to this
network border group will be advertised in all AZs in the Region
you're in. 5. For **Public IPv4 address pool**, choose one of the
following:

    * **Amazon's pool of IPv4 addresses**—If you want an IPv4
     address to be allocated from Amazon's pool of IPv4
     addresses.
    * **Public IPv4 address that you bring to your AWS
     account**—If you want to allocate a
     non-contiguous (non-sequential) public IPv4 address from
     an IP address pool that you have brought to your AWS
     account. This option is disabled if you do not have any
     IP address pools. For more information about bringing
     your own IP address range to your AWS account, see
     [Bring your own IP addresses (BYOIP) to Amazon EC2](ec2-byoip.md "ec2-byoip.md").
    * **Customer owned pool of IPv4 addresses**—If you want to
     allocate an IPv4 address from a pool created from your
     on-premises network for use with an AWS Outpost. This
     option is disabled if you do not have an AWS
     Outpost.
    * **Allocate using an IPAM IPv4 pool**: If you want to allocate sequential Elastic IP addresses from a
     contiguous public IPv4 block in an IPAM pool. Allocating sequential
     Elastic IP addresses can significantly reduce management
     overhead for security access control lists and simplify
     IP address allocation and tracking for enterprises
     scaling on AWS. For more information, see [Allocate sequential Elastic IP addresses from an IPAM pool](../../../vpc/latest/ipam/tutorials-eip-pool.md "../../../vpc/latest/ipam/tutorials-eip-pool.md")
     in the *Amazon VPC IPAM User Guide*.

6. (Optional) To add a tag, choose **Add new tag**
   and enter a tag key and a tag value.

AWS CLI

###### To allocate an Elastic IP address

Use the [allocate-address](../../../cli/latest/reference/ec2/allocate-address.md "../../../cli/latest/reference/ec2/allocate-address.md")
AWS CLI command.

In the following example, Amazon EC2 selects an address from Amazon's address pool.

```
aws ec2 allocate-address
```

In the following example, Amazon EC2 selects an address from the specified
pool that you brought to AWS using BYOIP.

```
aws ec2 allocate-address \
    --public-ipv4-pool `ipv4pool-ec2-012345abcdef67890`
```

The following example specifies an address from the specified IPv4 IPAM pool.

```
aws ec2 allocate-address \
    --ipam-pool-id `ipam-pool-1234567890abcdef0` \
    --address `192.0.2.0`
```

PowerShell

###### To allocate an Elastic IP address

Use the [New-EC2Address](../../../powershell/latest/reference/items/New-EC2Address.md "../../../powershell/latest/reference/items/New-EC2Address.md")
cmdlet.

In the following example, Amazon EC2 selects an address from Amazon's address pool.

```
New-EC2Address
```

In the following example, Amazon EC2 selects an address from the specified
pool that you brought to AWS using BYOIP.

```
New-EC2Address \
    --PublicIpv4Pool `ipv4pool-ec2-012345abcdef67890`
```

The following example specifies an address from the specified IPv4 IPAM pool.

```
New-EC2Address \
    --IpamPoolId `ipam-pool-1234567890abcdef0` \
    --Address `192.0.2.0`
```

## Associate an Elastic IP address

If you're associating an Elastic IP address with your instance to enable
communication with the internet, you must also ensure that your instance is in a
public subnet. For more information, see [Enable internet access using an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the
_Amazon VPC User Guide_.

Console

###### To associate an Elastic IP address with an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic IPs**.
3. Select the Elastic IP address to associate and choose **Actions**,
   **Associate Elastic IP address**.
4. For **Resource type**, choose **Instance**.
5. For instance, choose the instance with which to associate the Elastic IP address. You can
   also enter text to search for a specific instance.
6. (Optional) For **Private IP address**, specify a private IP address
   with which to associate the Elastic IP address.
7. Choose **Associate**.

###### To associate an Elastic IP address with a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic IPs**.
3. Select the Elastic IP address to associate and choose **Actions**,
   **Associate Elastic IP address**.
4. For **Resource type**, choose **Network interface**.
5. For **Network interface**, choose the network interface with which to associate
   the Elastic IP address. You can also enter text to search for a specific network interface.
6. (Optional) For **Private IP address**, specify a private IP address
   with which to associate the Elastic IP address.
7. Choose **Associate**.

AWS CLI

###### To associate an Elastic IP address

Use the [associate-address](../../../cli/latest/reference/ec2/associate-address.md "../../../cli/latest/reference/ec2/associate-address.md") AWS CLI command.

```
aws ec2 associate-address \
    --instance-id `i-0b263919b6498b123` \
    --allocation-id `eipalloc-64d5890a`
```

PowerShell

###### To associate an Elastic IP address

Use the [Register-EC2Address](../../../powershell/latest/reference/items/Register-EC2Address.md "../../../powershell/latest/reference/items/Register-EC2Address.md")
cmdlet.

```
Register-EC2Address `
    -InstanceId `i-0b263919b6498b123` `
    -AllocationId `eipalloc-64d5890a`
```

## Disassociate an Elastic IP

address

You can disassociate an Elastic IP address from an instance or network interface at any time. After you disassociate the Elastic IP address,
you can associate it with another resource.

Console

###### To disassociate and reassociate an Elastic IP address

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic IPs**.
3. Select the Elastic IP address to disassociate, choose **Actions**,
   **Disassociate Elastic IP address**.
4. Choose **Disassociate**.

AWS CLI

###### To disassociate an Elastic IP address

Use the [disassociate-address](../../../cli/latest/reference/ec2/disassociate-address.md "../../../cli/latest/reference/ec2/disassociate-address.md") AWS CLI command.

```
aws ec2 disassociate-address --association-id `eipassoc-12345678`
```

PowerShell

###### To disassociate an Elastic IP address

Use the [Unregister-EC2Address](../../../powershell/latest/reference/items/Unregister-EC2Address.md "../../../powershell/latest/reference/items/Unregister-EC2Address.md")
cmdlet.

```
Unregister-EC2Address -AssociationId `eipassoc-12345678`
```
