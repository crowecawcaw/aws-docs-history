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
4. (Optional) Click the **Preferences** icon and then turn on
   **Maximum number of network interfaces**. This column indicates
   the maximum number of network interfaces for each instance type.
5. (Optional) Select the instance type. On the **Networking**
   tab, find **Maximum number of network interfaces**.

AWS CLI

###### To retrieve the maximum network interfaces

You can use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command to display information about an
instance type, such as its supported network interfaces and IP addresses per interface.
The following example displays this information for all C5 instances.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=c5.*" \
    --query "InstanceTypes[].{ \
        Type: InstanceType, \
        MaxENI: NetworkInfo.MaximumNetworkInterfaces, \
        IPv4addr: NetworkInfo.Ipv4AddressesPerInterface}" \
    --output table
```

The following is example output.

````
---------------------------------------
|        DescribeInstanceTypes        | +----------+----------+---------------+
| IPv4addr | MaxENI   |     Type      | +----------+----------+---------------+
|  30      |  8       |  c5.4xlarge   |
|  50      |  15      |  c5.24xlarge  |
|  15      |  4       |  c5.xlarge    |
|  30      |  8       |  c5.12xlarge  |
|  10      |  3       |  c5.large     |
|  15      |  4       |  c5.2xlarge   |
|  50      |  15      |  c5.metal     |
|  30      |  8       |  c5.9xlarge   |
|  50      |  15      |  c5.18xlarge  | +----------+----------+---------------+ ``` PowerShell ###### To retrieve the maximum network interfaces You can use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") PowerShell command to display information about an instance type, such as its supported network interfaces and IP addresses per interface. The following example displays this information for all C5 instances. ``` Get-EC2InstanceType -Filter @{Name="instance-type"; Values="c5.*"} | ` Select-Object ` @{Name='Ipv4AddressesPerInterface'; Expression={($_.Networkinfo.Ipv4AddressesPerInterface)}}, @{Name='MaximumNetworkInterfaces'; Expression={($_.Networkinfo.MaximumNetworkInterfaces)}}, InstanceType | ` Format-Table -AutoSize ``` The following is example output. ``` Ipv4AddressesPerInterface MaximumNetworkInterfaces InstanceType ------------------------- ------------------------ ------------ 30                        8 c5.4xlarge 15                        4 c5.xlarge 30                        8 c5.12xlarge 50                       15 c5.24xlarge 30                        8 c5.9xlarge 50                       15 c5.metal 15                        4 c5.2xlarge 10                        3 c5.large 50                       15 c5.18xlarge ```
````
