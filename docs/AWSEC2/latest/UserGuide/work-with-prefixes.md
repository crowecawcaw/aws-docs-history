# Manage prefixes for your network interfaces

When you assign prefixes to a network interface, you can choose whether to let us automatically
assign the prefixes or you can specify custom prefixes. If you let us automatically assign prefixes
and the subnet for the network interface has a subnet CIDR reservation of type `prefix`,
we select the prefixes from the subnet CIDR reservation. Otherwise, we select them from the
subnet CIDR range.

###### Tasks

- [Assign prefixes during network interface creation](#assign-auto-creation "#assign-auto-creation")
- [Assign prefixes to an existing network interface](#assign-auto-existing "#assign-auto-existing")
- [Remove prefixes from your network interfaces](#unassign-prefix "#unassign-prefix")

## Assign prefixes during network interface creation

You can assign automatic or custom prefixes when you create a network interface.

Console

###### To assign automatic prefixes during network interface creation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Choose **Create network interface**.
4. Enter a description for the network interface, select the subnet in
   which to create the network interface, and configure the private IPv4 and
   IPv6 addresses.
5. Expand **Advanced settings**.
6. For **IPv4 prefix delegation** do one of the following:
   - To automatically assign an IPv4 prefix, choose **Auto-assign**.
     For **Number of IPv4 prefixes**, enter the number
     of prefixes to assign.
   - To assign a specific IPv4 prefix, choose **Custom**.
     Choose **Add new prefix** and enter the prefix.

7. For **IPv6 prefix delegation** do one of
   the following:
   - To automatically assign an IPv6 prefix, choose **Auto-assign**.
     For **Number of IPv6 prefixes**, enter the number
     of prefixes to assign.
   - To assign a specific IPv6 prefix, choose **Custom**.
     Choose **Add new prefix** and enter the prefix.###### Note

**IPv6 prefix delegation** appears only if
the selected subnet is enabled for IPv6. 8. Select the security groups to associate with the network interface and
assign resource tags if needed. 9. Choose **Create network interface**.

AWS CLI

###### To assign automatic IPv4 prefixes during network interface creation

Use the [create-network-interface](../../../cli/latest/reference/ec2/create-network-interface.md "../../../cli/latest/reference/ec2/create-network-interface.md") command and set `--ipv4-prefix-count` to the number of
IPv4 prefixes for AWS to assign. In the following example, AWS assigns one
IPv4 prefix.

```
aws ec2 create-network-interface \
    --subnet-id `subnet-047cfed18eEXAMPLE` \
    --description "`IPv4 automatic example`" \
    --ipv4-prefix-count `1`
```

###### To assign specific IPv4 prefixes during network interface creation

Use the [create-network-interface](../../../cli/latest/reference/ec2/create-network-interface.md "../../../cli/latest/reference/ec2/create-network-interface.md") command and set `--ipv4-prefixes` to the prefixes. AWS
selects IPv4 addresses from this range. In the following example, the prefix CIDR is 10.0.0.208/28.

```
aws ec2 create-network-interface \
    --subnet-id `subnet-047cfed18eEXAMPLE` \
    --description "`IPv4 manual example`" \
    --ipv4-prefixes Ipv4Prefix=`10.0.0.208/28`
```

###### To assign automatic IPv6 prefixes during network interface creation

Use the [create-network-interface](../../../cli/latest/reference/ec2/create-network-interface.md "../../../cli/latest/reference/ec2/create-network-interface.md") command and set `--ipv6-prefix-count` to the number of
IPv6 prefixes for AWS to assign. In the following example, AWS assigns one
IPv6 prefix.

```
aws ec2 create-network-interface \
    --subnet-id `subnet-047cfed18eEXAMPLE` \
    --description "`IPv6 automatic example`" \
    --ipv6-prefix-count `1`
```

###### To assign specific IPv6 prefixes during network interface creation

Use the [create-network-interface](../../../cli/latest/reference/ec2/create-network-interface.md "../../../cli/latest/reference/ec2/create-network-interface.md") command and set `--ipv6-prefixes` to the prefixes. AWS
selects IPv6 addresses from this range. In the following example, the prefix CIDR is
2600:1f13:fc2:a700:1768::/80.

```
aws ec2 create-network-interface \
    --subnet-id `subnet-047cfed18eEXAMPLE` \
    --description "`IPv6 manual example`" \
    --ipv6-prefixes Ipv6Prefix=`2600:1f13:fc2:a700:1768::/80`
```

PowerShell

###### To assign automatic IPv4 prefixes during network interface creation

Use the [New-EC2NetworkInterface](../../../powershell/latest/reference/items/New-EC2NetworkInterface.md "../../../powershell/latest/reference/items/New-EC2NetworkInterface.md")
cmdlet and set `Ipv4PrefixCount` to the number of IPv4 prefixes for
AWS to assign. In the following example, AWS assigns one IPv4 prefix.

```
New-EC2NetworkInterface `
    -SubnetId '`subnet-047cfed18eEXAMPLE`' `
    -Description '`IPv4 automatic example`' `
    -Ipv4PrefixCount `1`
```

###### To assign specific IPv4 prefixes during network interface creation

Use the [New-EC2NetworkInterface](../../../powershell/latest/reference/items/New-EC2NetworkInterface.md "../../../powershell/latest/reference/items/New-EC2NetworkInterface.md")
cmdlet and set `Ipv4Prefix` to the prefixes. AWS selects
IPv4 addresses from this range. In the following example, the prefix CIDR
is 10.0.0.208/28.

```
Import-Module AWS.Tools.EC2
New-EC2NetworkInterface `
    -SubnetId '`subnet-047cfed18eEXAMPLE`' `
    -Description '`IPv4 manual example`' `
    -Ipv4Prefix (New-Object `
        -TypeName Amazon.EC2.Model.Ipv4PrefixSpecificationRequest `
        -Property @{Ipv4Prefix = '`10.0.0.208/28`'})
```

###### To assign automatic IPv6 prefixes during network interface creation

Use the [New-EC2NetworkInterface](../../../powershell/latest/reference/items/New-EC2NetworkInterface.md "../../../powershell/latest/reference/items/New-EC2NetworkInterface.md")
cmdlet and set `Ipv6PrefixCount` to the number of IPv6 prefixes for
AWS to assign. In the following example, AWS assigns one IPv6 prefix.

```
New-EC2NetworkInterface `
    -SubnetId '`subnet-047cfed18eEXAMPLE`' `
    -Description '`IPv6 automatic example`' `
    -Ipv6PrefixCount `1`
```

###### To assign specific IPv6 prefixes during network interface creation

Use the [New-EC2NetworkInterface](../../../powershell/latest/reference/items/New-EC2NetworkInterface.md "../../../powershell/latest/reference/items/New-EC2NetworkInterface.md")
cmdlet and set `Ipv6Prefixes` to the prefixes. AWS selects
IPv6 addresses from this range. In the following example, the prefix CIDR
is 2600:1f13:fc2:a700:1768::/80.

```
Import-Module AWS.Tools.EC2
New-EC2NetworkInterface `
    -SubnetId '`subnet-047cfed18eEXAMPLE`' `
    -Description '`IPv6 manual example`' `
    -Ipv6Prefix (New-Object `
        -TypeName Amazon.EC2.Model.Ipv6PrefixSpecificationRequest `
        -Property @{Ipv6Prefix = '`2600:1f13:fc2:a700:1768::/80`'})
```

## Assign prefixes to an existing network interface

You can assign automatic or custom prefixes to an existing network interface.

Console

###### To assign automatic prefixes to an existing network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Select the network interface to which to assign the
   prefixes, and choose **Actions**,
   **Manage prefixes**.
4. For **IPv4 prefix delegation** do one of the following:
   - To automatically assign an IPv4 prefix, choose **Auto-assign**.
     For **Number of IPv4 prefixes**, enter the number
     of prefixes to assign.
   - To assign a specific IPv4 prefix, choose **Custom**.
     Choose **Add new prefix** and enter the prefix.

5. For **IPv6 prefix delegation** do one of the following:
   - To automatically assign an IPv6 prefix, choose **Auto-assign**.
     For **Number of IPv6 prefixes**, enter the number
     of prefixes to assign.
   - To assign a specific IPv6 prefix, choose **Custom**.
     Choose **Add new prefix** and enter the prefix.###### Note

**IPv6 prefix delegation** appears only if
the selected subnet is enabled for IPv6. 6. Choose **Save**.

AWS CLI
Use the [assign-ipv6-addresses](../../../cli/latest/reference/ec2/assign-ipv6-addresses.md "../../../cli/latest/reference/ec2/assign-ipv6-addresses.md") command to assign IPv6 prefixes and the
[assign-private-ip-addresses](../../../cli/latest/reference/ec2/assign-private-ip-addresses.md "../../../cli/latest/reference/ec2/assign-private-ip-addresses.md") command to assign IPv4 prefixes
to existing network interfaces.

###### To assign automatic IPv4 prefixes to an existing network interface

Use the [assign-private-ip-addresses](../../../cli/latest/reference/ec2/assign-private-ip-addresses.md "../../../cli/latest/reference/ec2/assign-private-ip-addresses.md") command and set `--ipv4-prefix-count` to the number of
IPv4 prefixes for AWS to assign. In the following example, AWS assigns one IPv4
prefix.

```
aws ec2 assign-private-ip-addresses \
    --network-interface-id `eni-081fbb4095EXAMPLE` \
    --ipv4-prefix-count `1`
```

###### To assign specific IPv4 prefixes to an existing network interface

Use the [assign-private-ip-addresses](../../../cli/latest/reference/ec2/assign-private-ip-addresses.md "../../../cli/latest/reference/ec2/assign-private-ip-addresses.md") command and set `--ipv4-prefixes` to the prefix. AWS
selects IPv4 addresses from this range. In the following example, the prefix CIDR is
10.0.0.208/28.

```
aws ec2 assign-private-ip-addresses \
    --network-interface-id `eni-081fbb4095EXAMPLE` \
    --ipv4-prefixes `10.0.0.208/28`
```

###### To assign automatic IPv6 prefixes to an existing network interface

Use the [assign-ipv6-addresses](../../../cli/latest/reference/ec2/assign-ipv6-addresses.md "../../../cli/latest/reference/ec2/assign-ipv6-addresses.md") command and set `--ipv6-prefix-count` to the number of
IPv6 prefixes for AWS to assign. In the following example, AWS assigns one IPv6 prefix.

```
aws ec2 assign-ipv6-addresses \
    --network-interface-id `eni-00d577338cEXAMPLE` \
    --ipv6-prefix-count `1`
```

###### To assign specific IPv6 prefixes to an existing network interface

Use the [assign-ipv6-addresses](../../../cli/latest/reference/ec2/assign-ipv6-addresses.md "../../../cli/latest/reference/ec2/assign-ipv6-addresses.md") command and set `--ipv6-prefixes` to the prefix. AWS selects
IPv6 addresses from this range. In the following example, the prefix CIDR is
2600:1f13:fc2:a700:18bb::/80.

```
aws ec2 assign-ipv6-addresses \
    --network-interface-id `eni-00d577338cEXAMPLE` \
    --ipv6-prefixes `2600:1f13:fc2:a700:18bb::/80`
```

PowerShell

###### To assign automatic IPv4 prefixes to an existing network interface

Use the [Register-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md")
cmdlet and set `Ipv4PrefixCount` to the number of IPv4 prefixes
for AWS to assign. In the following example, AWS assigns one IPv4 prefix.

```
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId '`eni-00d577338cEXAMPLE`' `
    -Ipv4PrefixCount `1`
```

###### To assign specific IPv4 prefixes to an existing network interface

Use the [Register-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md")
cmdlet and set `Ipv4Prefix` to the prefix. AWS selects IPv4 addresses
from this range. In the following example, the prefix CIDR is 10.0.0.208/28.

```
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId '`eni-00d577338cEXAMPLE`' `
    -Ipv4Prefix '`10.0.0.208/28`'
```

###### To assign automatic IPv6 prefixes to an existing network interface

Use the [Register-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md")
cmdlet and set `Ipv6PrefixCount` to the number of IPv4 prefixes
for AWS to assign. In the following example, AWS assigns one IPv6 prefix.

```
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId '`eni-00d577338cEXAMPLE`' `
    -Ipv6PrefixCount `1`
```

###### To assign specific IPv6 prefixes to an existing network interface

Use the [Register-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md")
cmdlet and set `Ipv6Prefix` to the prefix. AWS selects IPv6 addresses
from this range. In the following example, the prefix CIDR is 2600:1f13:fc2:a700:18bb::/80.

```
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId '`eni-00d577338cEXAMPLE`' `
    -Ipv6Prefix '`2600:1f13:fc2:a700:18bb::/80`'
```

## Remove prefixes from your network interfaces

You can remove prefixes from an existing network interface.

Console

###### To remove the prefixes from a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Select the network interface.
4. Choose **Actions**, **Manage prefixes**.
5. For **IPv4 prefix delegation**, to remove specific prefixes, choose
   **Unassign** next to the prefixes to remove. To remove all prefixes,
   choose **Do not assign**.
6. For **IPv6 prefix delegation**, to remove specific prefixes, choose
   **Unassign** next to the prefixes to remove. To remove all prefixes,
   choose **Do not assign**.

###### Note

**IPv6 prefix delegation** appears only if
the selected subnet is enabled for IPv6. 7. Choose **Save**.

AWS CLI
You can use the [unassign-ipv6-addresses](../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md "../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md") command to remove IPv6 prefixes and the [unassign-private-ip-addresses](../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md "../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md")
commands to remove IPv4 prefixes from your existing network interfaces.

###### To remove IPv4 prefixes from a network interface

Use the [unassign-private-ip-addresses](../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md "../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md") command
and set `--ipv4-prefix` to the prefix CIDR to remove.

```
aws ec2 unassign-private-ip-addresses \
    --network-interface-id `eni-081fbb4095EXAMPLE` \
    --ipv4-prefixes `10.0.0.176/28`
```

###### To remove IPv6 prefixes from a network interface

Use the [unassign-ipv6-addresses](../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md "../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md")
command and set `--ipv6-prefix` to the prefix CIDR to remove.

```
aws ec2 unassign-ipv6-addresses \
    --network-interface-id `eni-00d577338cEXAMPLE` \
    --ipv6-prefix `2600:1f13:fc2:a700:18bb::/80`
```

PowerShell

###### To remove IPv4 prefixes from a network interface

Use the [Unregister-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Unregister-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Unregister-EC2PrivateIpAddress.md")
cmdlet and set `Ipv4Prefix` to the prefix CIDR to remove.

```
Unregister-EC2PrivateIpAddress `
    -NetworkInterfaceId '`eni-00d577338cEXAMPLE`' `
    -Ipv4Prefix '`10.0.0.208/28`'
```

###### To remove IPv6 prefixes from a network interface

Use the [Unregister-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Unregister-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Unregister-EC2Ipv6AddressList.md")
cmdlet and set `Ipv6Prefix` to the prefix CIDR to remove.

```
Unregister-EC2Ipv6AddressList `
    -NetworkInterfaceId '`eni-00d577338cEXAMPLE`' `
    -Ipv6Prefix '`2600:1f13:fc2:a700:18bb::/80`'
```
