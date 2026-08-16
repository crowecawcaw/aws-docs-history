# Maximum IP addresses per network interface

Each instance type supports a maximum number of network interfaces, maximum number of private IPv4
addresses per network interface, and maximum number of IPv6 addresses per network interface.
The limit for IPv6 addresses is separate from the limit for private IPv4 addresses per
network interface. Note that all instance types support IPv6 addressing except for the
following: C1, M1, M2, M3, and T1.

###### Available network interfaces

The _Amazon EC2 Instance Types Guide_ provides the information about the network interfaces
available for each instance type. For more information, see the following:

- [Network specifications – General purpose](../../../ec2/latest/instancetypes/gp.md#gp_network "../../../ec2/latest/instancetypes/gp.md#gp_network")
- [Network specifications – Compute optimized](../../../ec2/latest/instancetypes/co.md#co_network "../../../ec2/latest/instancetypes/co.md#co_network")
- [Network specifications – Memory optimized](../../../ec2/latest/instancetypes/mo.md#mo_network "../../../ec2/latest/instancetypes/mo.md#mo_network")
- [Network specifications – Storage optimized](../../../ec2/latest/instancetypes/so.md#so_network "../../../ec2/latest/instancetypes/so.md#so_network")
- [Network specifications – Accelerated computing](../../../ec2/latest/instancetypes/ac.md#ac_network "../../../ec2/latest/instancetypes/ac.md#ac_network")
- [Network specifications – High-performance computing](../../../ec2/latest/instancetypes/hpc.md#hpc_network "../../../ec2/latest/instancetypes/hpc.md#hpc_network")
- [Network specifications – Previous generation](../../../ec2/latest/instancetypes/pg.md#pg_network "../../../ec2/latest/instancetypes/pg.md#pg_network")

Console

###### To retrieve the maximum network interfaces

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instance Types**.
3. Add a filter to specify the instance type (**Instance type=c5.12xlarge**)
   or instance family (**Instance family=c5**).
4. (Optional) Choose the **Preferences** icon and then turn on
   **Maximum number of network interfaces**. This column indicates
   the maximum number of network interfaces for each instance type.
5. (Optional) Select the instance type. On the **Networking**
   tab, find **Maximum number of network interfaces**.

AWS CLI

###### To retrieve the maximum network interfaces

You can use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command to display information about an
instance type, such as its supported network interfaces and IP addresses per interface.
The following example displays this information for all C8i instances.

```
{ echo -e "InstanceType\tMaximumNetworkInterfaces\tIpv4AddressesPerInterface"; \
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=c8i.*" \
    --query 'InstanceTypes[*].[InstanceType, NetworkInfo.MaximumNetworkInterfaces, NetworkInfo.Ipv4AddressesPerInterface]' \
    --output text | sort -k2 -n; } | column -t
```

The following is example output.

```
InstanceType    MaximumNetworkInterfaces  Ipv4AddressesPerInterface
c8i.large       3                         20
c8i.2xlarge     4                         30
c8i.xlarge      4                         30
c8i.4xlarge     8                         50
c8i.8xlarge     10                        50
c8i.12xlarge    12                        50
c8i.16xlarge    16                        64
c8i.24xlarge    16                        64
c8i.32xlarge    24                        64
c8i.48xlarge    24                        64
c8i.96xlarge    24                        64
c8i.metal-48xl  24                        64
c8i.metal-96xl  24                        64
```

PowerShell

###### To retrieve the maximum network interfaces

You can use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") PowerShell command to display information about an
instance type, such as its supported network interfaces and IP addresses per interface.
The following example displays this information for all C8i instances.

```
Get-EC2InstanceType -Filter @{Name="instance-type"; Values="c8i.*"} |
Select-Object `
    InstanceType,
    @{Name='MaximumNetworkInterfaces'; Expression={$_.NetworkInfo.MaximumNetworkInterfaces}},
    @{Name='Ipv4AddressesPerInterface'; Expression={$_.NetworkInfo.Ipv4AddressesPerInterface}} |
Sort-Object MaximumNetworkInterfaces |
Format-Table -AutoSize
```

The following is example output.

```
InstanceType   MaximumNetworkInterfaces Ipv4AddressesPerInterface
------------   ------------------------ -------------------------
c8i.large                             3                        20
c8i.xlarge                            4                        30
c8i.2xlarge                           4                        30
c8i.4xlarge                           8                        50
c8i.8xlarge                          10                        50
c8i.12xlarge                         12                        50
c8i.24xlarge                         16                        64
c8i.16xlarge                         16                        64
c8i.96xlarge                         24                        64
c8i.48xlarge                         24                        64
c8i.metal-96xl                       24                        64
c8i.32xlarge                         24                        64
c8i.metal-48xl                       24                        64
```
