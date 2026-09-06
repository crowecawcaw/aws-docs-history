

# Maximum IP addresses per network interface
<a name="AvailableIpPerENI"></a>

Each instance type supports a maximum number of network interfaces, maximum number of private IPv4 addresses per network interface, and maximum number of IPv6 addresses per network interface. The limit for IPv6 addresses is separate from the limit for private IPv4 addresses per network interface. Note that all instance types support IPv6 addressing except for the following: C1, M1, M2, M3, and T1.

**Available network interfaces**

The *Amazon EC2 Instance Types Guide* provides the information about the network interfaces available for each instance type. For more information, see the following:
+ [Network specifications – General purpose](https://docs.aws.amazon.com/ec2/latest/instancetypes/gp.html#gp_network)
+ [Network specifications – Compute optimized](https://docs.aws.amazon.com/ec2/latest/instancetypes/co.html#co_network)
+ [Network specifications – Memory optimized](https://docs.aws.amazon.com/ec2/latest/instancetypes/mo.html#mo_network)
+ [Network specifications – Storage optimized](https://docs.aws.amazon.com/ec2/latest/instancetypes/so.html#so_network)
+ [Network specifications – Accelerated computing](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html#ac_network)
+ [Network specifications – High-performance computing](https://docs.aws.amazon.com/ec2/latest/instancetypes/hpc.html#hpc_network)
+ [Network specifications – Previous generation](https://docs.aws.amazon.com/ec2/latest/instancetypes/pg.html#pg_network)

------
#### [ Console ]

**To retrieve the maximum network interfaces**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instance Types**.

1. Add a filter to specify the instance type (**Instance type=c5.12xlarge**) or instance family (**Instance family=c5**).

1. (Optional) Choose the **Preferences** icon and then turn on **Maximum number of network interfaces**. This column indicates the maximum number of network interfaces for each instance type.

1. (Optional) Select the instance type. On the **Networking** tab, find **Maximum number of network interfaces**.

------
#### [ AWS CLI ]

**To retrieve the maximum network interfaces**  
You can use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command to display information about an instance type, such as its supported network interfaces and IP addresses per interface. The following example displays this information for all C8i instances.

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

------
#### [ PowerShell ]

**To retrieve the maximum network interfaces**  
You can use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) PowerShell command to display information about an instance type, such as its supported network interfaces and IP addresses per interface. The following example displays this information for all C8i instances.

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

------