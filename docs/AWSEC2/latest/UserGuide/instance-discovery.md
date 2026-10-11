

# Find an Amazon EC2 instance type
<a name="instance-discovery"></a>

Before you can launch an instance, you must select an instance type to use. The instance type that you choose might depend on the resources that your workload requires, such as compute, memory, or storage resources. It can be beneficial to identify several instance types that might suit your workload and evaluate their performance in a test environment. There is no substitute for measuring the performance of your application under load.

You can get suggestions and guidance for EC2 instance types using the EC2 instance type finder. For more information, see [Get recommendations from EC2 instance type finder](get-ec2-instance-type-recommendations.md).

If you already have running EC2 instances, you can use AWS Compute Optimizer to get recommendations about the instance types that you should use to improve performance, save money, or both. For more information, see [Get EC2 instance recommendations from Compute Optimizer](ec2-instance-recommendations.md).

**Topics**
+ [Filter instance types](#filter-instance-types)
+ [Describe an instance type using the AWS CLI](#describe-instance-type-example)

## Filter instance types
<a name="filter-instance-types"></a>

You can find an instance type that meets your requirements by filtering on whether the instance type is available in a specified Availability Zone, or by filtering on instance attributes or support for specific features. Choose the tab for the method you want to use.

------
#### [ Console ]

**To filter instance types**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar, select the Region in which to launch your instances. You can select any Region that's available to you, regardless of your location.

1. In the navigation pane, choose **Instance Types**. 

1. (Optional) Choose the preferences (gear) icon to select which instance type attributes to display, such as **On-Demand Linux pricing**, and then choose **Confirm**. Alternatively, select the name of an instance type to open its details page and view all attributes available through the console. The console does not display all the attributes available through the API or the command line.

1. Use the instance type attributes to filter the list of displayed instance types to only the instance types that meet your needs. For example, you can filter on the following attributes:
   + **Availability zones** – The name of the Availability Zone, Local Zone, or Wavelength Zone. For more information, see [Regions and Zones](using-regions-availability-zones.md).
   + **vCPUs** or **Cores** – The number of vCPUs or cores.
   + **Memory (GiB)** – The memory size, in GiB.
   + **Network performance** – The network performance, in Gigabits.
   + **Local instance storage** – Indicates whether the instance type has local instance storage (`true` \| `false`).

1. (Optional) To see a side-by-side comparison, select the checkbox for multiple instance types. The comparison is displayed at the bottom of the screen.

1. (Optional) To save the list of instance types to a comma-separated values (.csv) file for further review, choose **Actions**, **Download list CSV**. The file includes all instance types that match the filters you set.

1. (Optional) To launch instances using an instance type that meets your needs, select the checkbox for the instance type and choose **Actions**, **Launch instance**. For more information, see [Launch an EC2 instance using the launch instance wizard in the console](ec2-launch-instance-wizard.md).

------
#### [ CLI ]

You can use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) and [describe-instance-type-offerings](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-type-offerings.html) AWS Command Line Interface commands to find the instance types that meet your needs.

The following examples show how to filter instance types by Availability Zone, available memory size, available instance storage, or hibernation support.

**To filter instance types by Availability Zone**  
The following example displays only the instance types offered in the specified Availability Zone.

```
aws ec2 describe-instance-type-offerings \
    --location-type "availability-zone" \
    --filters "Name=location,Values={{us-east-2a}}" \
    --region {{us-east-2}} \
    --query "InstanceTypeOfferings[*].[InstanceType]" --output text | sort
```

The output is a list of instance types, sorted alphabetically. The following is the start of the output only.

```
a1.2xlarge
a1.4xlarge
a1.large
a1.medium
a1.metal
   ...
```

**To filter instance types by available memory size**  
The following example displays only current generation instance types with 64 GiB (65536 MiB) of memory.

```
aws ec2 describe-instance-types \
    --filters "Name=current-generation,Values=true" "Name=memory-info.size-in-mib,Values={{65536}}" \
    --region {{us-east-2}} \
    --query "InstanceTypes[*].[InstanceType]" --output text | sort
```

The output is a list of instance types, sorted alphabetically. The following is the start of the output only.

```
c5a.8xlarge
c5ad.8xlarge
c6a.8xlarge
c6g.8xlarge
c6gd.8xlarge
   ...
```

**To filter instance types by available instance storage**  
The following example displays the total size of instance storage for all R7 instances with instance store volumes.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=r7*" "Name=instance-storage-supported,Values=true" \
    --region {{us-east-2}} \
    --query "InstanceTypes[].[InstanceType, InstanceStorageInfo.TotalSizeInGB]" \
    --output table
```

The following is example output.

```
---------------------------
|  DescribeInstanceTypes  |
+----------------+--------+
|  r7gd.xlarge   |  237   |
|  r7gd.8xlarge  |  1900  |
|  r7gd.16xlarge |  3800  |
|  r7gd.medium   |  59    |
|  r7gd.4xlarge  |  950   |
|  r7gd.2xlarge  |  474   |
|  r7gd.metal    |  3800  |
|  r7gd.large    |  118   |
|  r7gd.12xlarge |  2850  |
+----------------+--------+
```

**To filter instance types by hibernation support**  
The following example displays the instance types that support hibernation.

```
aws ec2 describe-instance-types \
    --filters "Name=hibernation-supported,Values=true" \
    --region {{us-east-2}} \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

The output is a list of instance types, sorted alphabetically. The following is the start of the output only.

```
c4.2xlarge
c4.4xlarge
c4.8xlarge
c4.large
c4.xlarge
...
```

------
#### [ PowerShell ]

You can use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) and [Get-EC2InstanceTypeOffering](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTypeOffering.html) Tools for PowerShell cmdlets to find the instance types that meet your needs.

The following examples show how to filter instance types by Availability Zone, available memory size, available instance storage, or hibernation support.

**To filter instance types by Availability Zone**  
The following example displays only the instance types offered in the specified Availability Zone.

```
(Get-EC2InstanceTypeOffering `
    -LocationType "availability-zone" `
    -Region {{us-east-2}} `
    -Filter @{Name="location"; Values="{{us-east-2a}}"}).InstanceType | Sort-Object
```

**To filter instance types by available memory size**  
The following example displays only current generation instance types with 64 GiB (65536 MiB) of memory.

```
(Get-EC2InstanceType `
    -Filter @{Name="current-generation"; Values="true"}, 
            @{Name="memory-info.size-in-mib"; Values="65536"}).InstanceType | Sort-Object
```

**To filter instance types by available instance storage**  
The following example displays the total size of instance storage for all R7 instances with instance store volumes.

```
Get-EC2InstanceType `
    -Filter @{Name="instance-type"; Values="r7*"}, 
            @{Name="instance-storage-supported"; Values="true"} | `
     Select InstanceType, @{Name="TotalSizeInGB"; Expression={($_.InstanceStorageInfo.TotalSizeInGB)}}
```

The following is example output.

```
InstanceType  TotalSizeInGB
------------  -------------
r7gd.8xlarge           1900
r7gd.16xlarge          3800
r7gd.xlarge             237
r7gd.4xlarge            950
r7gd.medium              59
r7gd.2xlarge            474
r7gd.large              118
r7gd.metal             3800
r7gd.12xlarge          2850
```

**To filter instance types by hibernation support**  
The following example displays the instance types that support hibernation.

```
(Get-EC2InstanceType `
    -Filter @{Name="hibernation-supported"; Values="true"}).InstanceType | Sort-Object
```

------

## Describe an instance type using the AWS CLI
<a name="describe-instance-type-example"></a>

You can use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command to describe a specific instance type.

**To fully describe an instance type**  
The following command displays all available details for the specified instance type. The output is lengthy, so it is omitted here.

```
aws ec2 describe-instance-types \
    --instance-types {{t2.micro}} \
    --region {{us-east-2}}
```

**To describe an instance type and filter the output**  
The following command displays the networking details for the specified instance type.

```
aws ec2 describe-instance-types \
    --instance-types {{t2.micro}} \
    --region {{us-east-2}} \
    --query "InstanceTypes[].NetworkInfo"
```

The following is example output.

```
[
    {
        "NetworkPerformance": "Low to Moderate",
        "MaximumNetworkInterfaces": 2,
        "MaximumNetworkCards": 1,
        "DefaultNetworkCardIndex": 0,
        "NetworkCards": [
            {
                "NetworkCardIndex": 0,
                "NetworkPerformance": "Low to Moderate",
                "MaximumNetworkInterfaces": 2,
                "BaselineBandwidthInGbps": 0.064,
                "PeakBandwidthInGbps": 1.024
            }
        ],
        "Ipv4AddressesPerInterface": 2,
        "Ipv6AddressesPerInterface": 2,
        "Ipv6Supported": true,
        "EnaSupport": "unsupported",
        "EfaSupported": false,
        "EncryptionInTransitSupported": false,
        "EnaSrdSupported": false
    }
]
```

The following command displays the available memory for the specified instance type.

```
aws ec2 describe-instance-types \
    --instance-types {{t2.micro}} \
    --region {{us-east-2}} \
    --query "InstanceTypes[].MemoryInfo"
```

The following is example output.

```
[
    {
        "SizeInMiB": 1024
    }
]
```