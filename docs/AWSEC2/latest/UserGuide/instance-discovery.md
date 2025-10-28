# Find an Amazon EC2 instance type

Before you can launch an instance, you must select an instance type to use. The instance type
that you choose might depend on the resources that your workload requires, such as compute,
memory, or storage resources. It can be beneficial to identify several instance types that might
suit your workload and evaluate their performance in a test environment. There is no substitute
for measuring the performance of your application under load.

You can get suggestions and guidance for EC2 instance types using the EC2 instance type finder. For more
information, see [Get recommendations from EC2 instance type finder](get-ec2-instance-type-recommendations.md "get-ec2-instance-type-recommendations.md").

If you already have running EC2 instances, you can use AWS Compute Optimizer to get recommendations about
the instance types that you should use to improve performance, save money, or both. For more
information, see [Get EC2 instance recommendations from Compute Optimizer](ec2-instance-recommendations.md "ec2-instance-recommendations.md").

###### Tasks

- [Find an instance type using the console](#instance-discovery-console "#instance-discovery-console")
- [Describe an instance type using the AWS CLI](#describe-instance-type-example "#describe-instance-type-example")
- [Find an instance type using the AWS CLI](#instance-discovery-cli "#instance-discovery-cli")
- [Find an instance type using the Tools for PowerShell](#instance-discovery-ps "#instance-discovery-ps")

## Find an instance type using the console

You can find an instance type that meets your needs using the Amazon EC2 console.

###### To find an instance type using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select the Region in which to launch your instances. You can
   select any Region that's available to you, regardless of your location.
3. In the navigation pane, choose **Instance Types**.
4. (Optional) Choose the preferences (gear) icon to select which instance type attributes to
   display, such as **On-Demand Linux pricing**, and then choose
   **Confirm**. Alternatively, select the name of an instance type to open its
   details page and view all attributes available through the console. The console does not
   display all the attributes available through the API or the command line.
5. Use the instance type attributes to filter the list of displayed instance types to only
   the instance types that meet your needs. For example, you can filter on the following
   attributes:
   - **Availability zones** – The name of the Availability Zone,
     Local Zone, or Wavelength Zone. For more information, see [Regions and Zones](using-regions-availability-zones.md "using-regions-availability-zones.md").
   - **vCPUs** or **Cores** – The number of vCPUs or cores.
   - **Memory (GiB)** – The memory size, in GiB.
   - **Network performance** – The network performance, in Gigabits.
   - **Local instance storage** – Indicates whether the instance type
     has local instance storage (`true` | `false`).

6. (Optional) To see a side-by-side comparison, select the checkbox for multiple instance
   types. The comparison is displayed at the bottom of the screen.
7. (Optional) To save the list of instance types to a comma-separated values (.csv) file for
   further review, choose **Actions**, **Download list CSV**.
   The file includes all instance types that match the filters you set.
8. (Optional) To launch instances using an instance type that meet your needs, select the
   checkbox for the instance type and choose **Actions**, **Launch
   instance**. For more information, see [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

## Describe an instance type using the AWS CLI

You can use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md")
command to describe a specific instance type.

###### To fully describe an instance type

The following command displays all available details for the specified instance type. The output is
lengthy, so it is omitted here.

```
aws ec2 describe-instance-types \
    --instance-types `t2.micro` \
    --region `us-east-2`
```

###### The describe an instance type and filter the output

The following command displays the networking details for the specified instance type.

```
aws ec2 describe-instance-types \
    --instance-types `t2.micro` \
    --region `us-east-2` \
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
    --instance-types `t2.micro` \
    --region `us-east-2` \
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

## Find an instance type using the AWS CLI

You can use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md")
and [describe-instance-type-offerings](../../../cli/latest/reference/ec2/describe-instance-type-offerings.md "../../../cli/latest/reference/ec2/describe-instance-type-offerings.md")
commands to find the instance types that meet your needs.

###### Examples

- [Find an instance type by Availability Zone](#find-instance-type-example-1 "#find-instance-type-example-1")
- [Find an instance type by available memory size](#find-instance-type-example-2 "#find-instance-type-example-2")
- [Find an instance type by available instance storage](#find-instance-type-example-3 "#find-instance-type-example-3")
- [Find an instance type that supports hibernation](#find-instance-type-example-4 "#find-instance-type-example-4")

### Example 1: Find an instance type by Availability Zone

The following example displays only the instance types offered in the specified Availability Zone.

```
aws ec2 describe-instance-type-offerings \
    --location-type "availability-zone" \
    --filters "Name=location,Values=`us-east-2a`" \
    --region `us-east-2` \
    --query "InstanceTypeOfferings[*].[InstanceType]" --output text | sort
```

The output is a list of instance types, sorted alphabetically. The following is the start of the output
only.

```
a1.2xlarge
a1.4xlarge
a1.large
a1.medium
a1.metal
a1.xlarge
c4.2xlarge
   ...
```

### Example 2: Find an instance type by available memory size

The following example displays only current generation instance types with 64 GiB (65536 MiB) of memory.

```
aws ec2 describe-instance-types \
    --filters "Name=current-generation,Values=true" "Name=memory-info.size-in-mib,Values=`65536`" \
    --region `us-east-2` \
    --query "InstanceTypes[*].[InstanceType]" --output text | sort
```

The output is a list of instance types, sorted alphabetically. The following is the start of the output
only.

```
c5a.8xlarge
c5ad.8xlarge
c6a.8xlarge
c6g.8xlarge
c6gd.8xlarge
c6gn.8xlarge
c6i.8xlarge
c6id.8xlarge
c6in.8xlarge
   ...
```

### Example 3: Find an instance type by available instance storage

The following example displays the total size of instance storage for all R7 instances with instance store
volumes.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=r7*" "Name=instance-storage-supported,Values=true" \
    --region `us-east-2` \
    --query "InstanceTypes[].[InstanceType, InstanceStorageInfo.TotalSizeInGB]" \
    --output table
```

The following is example output.

````
---------------------------
|  DescribeInstanceTypes  | +----------------+--------+
|  r7gd.xlarge   |  237   |
|  r7gd.8xlarge  |  1900  |
|  r7gd.16xlarge |  3800  |
|  r7gd.medium   |  59    |
|  r7gd.4xlarge  |  950   |
|  r7gd.2xlarge  |  474   |
|  r7gd.metal    |  3800  |
|  r7gd.large    |  118   |
|  r7gd.12xlarge |  2850  | +----------------+--------+ ``` ### Example 4: Find an instance type that supports hibernation The following example displays the instance types that support hibernation. ``` aws ec2 describe-instance-types \ --filters "Name=hibernation-supported,Values=true" \ --region `us-east-2` \ --query "InstanceTypes[*].[InstanceType]" \ --output text | sort ``` The output is a list of instance types, sorted alphabetically. The following is the start of the output only. ``` c4.2xlarge c4.4xlarge c4.8xlarge c4.large c4.xlarge c5.12xlarge c5.18xlarge c5.2xlarge c5.4xlarge c5.9xlarge ... ``` ## Find an instance type using the Tools for PowerShell You can use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") and [Get-EC2InstanceTypeOffering](../../../powershell/latest/reference/items/Get-EC2InstanceTypeOffering.md "../../../powershell/latest/reference/items/Get-EC2InstanceTypeOffering.md") cmdlets to find the instance types that meet your needs. ###### Examples <br>• [Find an instance type by Availability Zone](#find-instance-type-by-az-ps "#find-instance-type-by-az-ps") <br>• [Find an instance type by available memory size](#find-instance-type-by-memory-ps "#find-instance-type-by-memory-ps") <br>• [Find an instance type by available instance storage](#find-instance-type-by-storage-ps "#find-instance-type-by-storage-ps") <br>• [Find an instance type that supports hibernation](#find-instance-type-hibernation-ps "#find-instance-type-hibernation-ps") ### Find an instance type by Availability Zone The following example displays only the instance types offered in the specified Availability Zone. ``` (Get-EC2InstanceTypeOffering ` -LocationType "availability-zone" ` -Region `us-east-2` ` -Filter @{Name="location"; Values="`us-east-2a`"}).InstanceType | Sort-Object ` ``` ### Find an instance type by available memory size The following example displays only current generation instance types with 64 GiB (65536 MiB) of memory. ``` (Get-EC2InstanceType ` -Filter @{Name="current-generation"; Values="true"}, @{Name="memory-info.size-in-mib"; Values="65536"}).InstanceType | Sort-Object ``` ### Find an instance type by available instance storage The following example displays the total size of instance storage for all R7 instances with instance store volumes. ``` Get-EC2InstanceType ` -Filter @{Name="instance-type"; Values="r7*"}, @{Name="instance-storage-supported"; Values="true"} | ` Select InstanceType, @{Name="TotalSizeInGB"; Expression={($_.InstanceStorageInfo.TotalSizeInGB)}} ``` The following is example output. ``` InstanceType  TotalSizeInGB ------------  ------------- r7gd.8xlarge           1900 r7gd.16xlarge          3800 r7gd.xlarge             237 r7gd.4xlarge            950 r7gd.medium              59 r7gd.2xlarge            474 r7gd.large              118 r7gd.metal             3800 r7gd.12xlarge          2850 ``` ### Find an instance type that supports hibernation The following example displays the instance types that support hibernation. ``` (Get-EC2InstanceType ` -Filter @{Name="hibernation-supported"; Values="true"}).InstanceType | Sort-Object ```
````
