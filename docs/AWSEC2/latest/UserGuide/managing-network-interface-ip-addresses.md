# Manage the IP addresses for your network interface

You can manage the following IP addresses for your network interfaces:

- Elastic IP addresses (one per private IPv4 address)
- IPv4 addresses
- IPv6 addresses

Console

###### To manage the IP addresses of a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Select the checkbox for the network interface.
4. To manage the IPv4 and IPv6 addresses, do the following:
   1. Choose **Actions**, **Manage IP addresses**.
   2. Expand the network interface.
   3. For **IPv4 addresses**, edit the IP addresses as needed. To assign
      an additional IPv4 address, choose **Assign new IP
      address** and then specify an IPv4 address from
      the subnet range or let AWS choose one for you.
   4. (Dual stack or IPv6 only) For **IPv6 addresses**, edit the IP
      addresses as needed. To assign an additional IPv6 address,
      choose **Assign new IP address** and then
      specify an IPv6 address from the subnet range or let AWS
      choose one for you.
   5. To assign or unassign a public IPv4 address to a network interface, choose
      **Auto-assign public IP**. You can
      enable or disable this for any network interface, but it
      only affects the primary network interface.
   6. (Dual stack or IPv6-only) For **Assign primary IPv6
      IP**, choose **Enable** to
      assign a primary IPv6 address. The first GUA associated with
      the network interface is chosen as the primary IPv6 address.
      After you assign a primary IPv6 address, you can't change
      it. This address is the primary IPv6 address until the
      instance is terminated or the network interface is
      detached.
   7. Choose **Save**.

5. To associate an Elastic IP address, do the following:
   1. Choose **Actions**, **Associate address**.
   2. For **Elastic IP address**, select the Elastic IP address.
   3. For **Private IPv4 address**, select the private IPv4
      address to associate with the Elastic IP address.
   4. (Optional) Choose **Allow the Elastic IP address to be reassociated**
      if the network interface is currently associated with another instance or network
      interface.
   5. Choose **Associate**.

6. To disassociate an Elastic IP address, do the following:
   1. Choose **Actions**, **Disassociate address**.
   2. For **Public IP address**, select the Elastic IP address.
   3. Choose **Disassociate**.

AWS CLI

###### To manage the IPv4 addresses

Use the following [assign-private-ip-addresses](../../../cli/latest/reference/ec2/assign-private-ip-addresses.md "../../../cli/latest/reference/ec2/assign-private-ip-addresses.md")
command to assign an IPv4 address.

```
aws ec2 assign-private-ip-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --private-ip-addresses `10.0.0.82`
```

Use the following [unassign-private-ip-addresses](../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md "../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md")
command to unassign an IPv4 address.

```
aws ec2 unassign-private-ip-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --private-ip-addresses `10.0.0.82`
```

###### To manage the IPv6 addresses

Use the following [assign-ipv6-addresses](../../../cli/latest/reference/ec2/assign-ipv6-addresses.md "../../../cli/latest/reference/ec2/assign-ipv6-addresses.md")
command to assign an IPv6 address.

```
aws ec2 assign-ipv6-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --ipv6-addresses `2001:db8:1234:1a00:9691:9503:25ad:1761`
```

Use the following [unassign-ipv6-addresses](../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md "../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md")
command to unassign an IPv6 address.

```
aws ec2 unassign-ipv6-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --ipv6-addresses `2001:db8:1234:1a00:9691:9503:25ad:1761`
```

###### To manage the Elastic IP address for the primary private IPv4 address

Use the following [associate-address](../../../cli/latest/reference/ec2/associate-address.md "../../../cli/latest/reference/ec2/associate-address.md")
command to associate an Elastic IP address with the primary private IPv4 address.

```
aws ec2 associate-address \
    --allocation-id `eipalloc-0b263919b6EXAMPLE` \
    --network-interface-id `eni-1234567890abcdef0`
```

Use the following [disassociate-address](../../../cli/latest/reference/ec2/disassociate-address.md "../../../cli/latest/reference/ec2/disassociate-address.md")
command to disassociate an Elastic IP address from the primary private IPv4 address.

```
aws ec2 disassociate-address --association-id `eipassoc-2bebb745a1EXAMPLE`
```

PowerShell

###### To manage the IPv4 addresses

Use the [Register-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md")
cmdlet to assign an IPv4 address.

```
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -PrivateIpAddress `10.0.0.82`
```

Use the [Unregister-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Unregister-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Unregister-EC2PrivateIpAddress.md")
cmdlet to unassign an IPv4 address.

```
Unregister-EC2PrivateIpAddress `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -PrivateIpAddress `10.0.0.82`
```

###### To manage the IPv6 addresses

Use the [Register-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md")
cmdlet to assign an IPv6 address.

```
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Ipv6Address `2001:db8:1234:1a00:9691:9503:25ad:1761`
```

Use the [Unregister-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Unregister-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Unregister-EC2Ipv6AddressList.md")
cmdlet to unassign an IPv6 address.

```
Unregister-EC2Ipv6AddressList `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Ipv6Address `2001:db8:1234:1a00:9691:9503:25ad:1761`
```

###### To manage the Elastic IP address for the primary private IPv4 address

Use the [Register-EC2Address](../../../powershell/latest/reference/items/Register-EC2Address.md "../../../powershell/latest/reference/items/Register-EC2Address.md")
cmdlet to associate an Elastic IP address with the primary private IPv4 address.

```
Register-EC2Address `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -AllocationId `eipalloc-0b263919b6EXAMPLE`
```

Use the [Unregister-EC2Address](../../../powershell/latest/reference/items/Unregister-EC2Address.md "../../../powershell/latest/reference/items/Unregister-EC2Address.md")
cmdlet to disassociate an Elastic IP address from the primary private IPv4 address.

```
Unregister-EC2Address -AssociationId `eipassoc-2bebb745a1EXAMPLE`
```
