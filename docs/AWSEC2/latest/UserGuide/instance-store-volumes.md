

# Instance store volume limits for EC2 instances
<a name="instance-store-volumes"></a>

The number, size, and type of instance store volumes are determined by the instance type. Some instance types, such as C8i, M8i, and R8i, do not support instance store volumes, while other instance types, such as C8id, M8id, and R8id, do support instance store volumes. You can’t attach more instance store volumes to an instance than is supported by its instance type. For the instance types that do support instance store volumes, the number and size of the instance store volumes vary by instance size. For example, `r8id.large` supports 1 x 118 GB instance store volume, while `r8id.32xlarge` supports 2 x 3800 GB instance store volumes.

For instance types with **NVMe instance store volumes**, all of the supported instance store volumes are automatically attached to the instance at launch. For instance types with **non-NVMe instance store volumes**, such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must manually specify the block device mappings for the instance store volumes that you want to attach at launch. Then, after the instance has launched, you must [ format and mount the attached instance store volumes](making-instance-stores-available-on-your-instances.md) before you can use them. You can't attach an instance store volume after you launch the instance.

Some instance types use NVMe or SATA-based solid state drives (SSD), while others use SATA-based hard disk drives (HDD). SSDs deliver high random I/O performance with very low latency, but you don't need the data to persist when the instance terminates or you can take advantage of fault-tolerant architectures. For more information, see [SSD instance store volumes for EC2 instances](ssd-instance-store.md).

The data on NVMe instance store volumes and some HDD instance store volumes is encrypted at rest. For more information, see [Data protection in Amazon EC2](data-protection.md).

## Available instance store volumes
<a name="available-instance-store-volumes"></a>

The *Amazon EC2 Instance Types Guide* provides the quantity, size, type, and performance optimizations of instance store volumes available on each supported instance type. For more information, see the following:
+ [Instance store specifications – General purpose](https://docs.aws.amazon.com/ec2/latest/instancetypes/gp.html#gp_instance-store)
+ [Instance store specifications – Compute optimized](https://docs.aws.amazon.com/ec2/latest/instancetypes/co.html#co_instance-store)
+ [Instance store specifications – Memory optimized](https://docs.aws.amazon.com/ec2/latest/instancetypes/mo.html#mo_instance-store)
+ [Instance store specifications – Storage optimized](https://docs.aws.amazon.com/ec2/latest/instancetypes/so.html#so_instance-store)
+ [Instance store specifications – Accelerated computing](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html#ac_instance-store)
+ [Instance store specifications – High-performance computing](https://docs.aws.amazon.com/ec2/latest/instancetypes/hpc.html#hpc_instance-store)
+ [Instance store specifications – Previous generation](https://docs.aws.amazon.com/ec2/latest/instancetypes/pg.html#pg_instance-store)

------
#### [ Console ]

**To retrieve instance store volume information**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instance Types**.

1. Add the filter **Local instance storage = true**. The **Storage** column indicates the total size of the instance storage for the instance type.

1. (Optional) Choose the **Preferences** icon and then turn on **Storage disk count**. This column indicates the number of instance store volumes.

1. (Optional) Add filters to further scope to specific instance types of interest.

------
#### [ AWS CLI ]

**To retrieve instance store volume information**  
Use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command. The following example displays the total size of the instance storage for each instance type in the R8i instance families with instance store volumes.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=r8i*" "Name=instance-storage-supported,Values=true" \
    --query 'sort_by(InstanceTypes, &InstanceStorageInfo.TotalSizeInGB)[].{InstanceType:InstanceType,TotalSizeInGB:InstanceStorageInfo.TotalSizeInGB}' \
    --output table
```

The following is example output.

```
--------------------------------------
|        DescribeInstanceTypes       |
+------------------+-----------------+
|   InstanceType   |  TotalSizeInGB  |
+------------------+-----------------+
|  r8id.large      |  118            |
|  r8id.xlarge     |  237            |
|  r8id.2xlarge    |  474            |
|  r8id.4xlarge    |  950            |
|  r8id.8xlarge    |  1900           |
|  r8id.12xlarge   |  2850           |
|  r8id.16xlarge   |  3800           |
|  r8id.24xlarge   |  5700           |
|  r8id.32xlarge   |  7600           |
|  r8id.48xlarge   |  11400          |
|  r8id.metal-48xl |  11400          |
|  r8id.96xlarge   |  22800          |
|  r8id.metal-96xl |  22800          |
+------------------+-----------------+
```

**To get complete instance storage details for an instance type**  
Use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values={{r8id.32xlarge}}" \
    --query 'InstanceTypes[0].InstanceStorageInfo' \
    --output json
```

The example output shows that this instance type has two 3800 GB NVMe SSD volumes, for a total of 7600 GB of instance storage.

```
{
    "TotalSizeInGB": 7600,
    "Disks": [
        {
            "SizeInGB": 3800,
            "Count": 2,
            "Type": "ssd"
        }
    ],
    "NvmeSupport": "required",
    "EncryptionSupport": "required"
}
```

------
#### [ PowerShell ]

**To retrieve instance store volume information**  
Use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) cmdlet. The following example displays the total size of the instance storage for each instance type in the R8i instance families with instance store volumes.

```
(Get-EC2InstanceType -Filter `
    @{Name="instance-type"; Values="r8i*"},
    @{Name="instance-storage-supported"; Values="true"}) |
    Sort-Object {$_.InstanceStorageInfo.TotalSizeInGB} |
    Format-Table InstanceType,
        @{Name="Disks.SizeInGB";Expression={$_.InstanceStorageInfo.Disks[0].SizeInGB}},
        @{Name="Disks.Count";Expression={$_.InstanceStorageInfo.Disks[0].Count}},
        @{Name="TotalSizeInGB";Expression={$_.InstanceStorageInfo.TotalSizeInGB}}
```

The following is example output.

```
InstanceType    Disks.SizeInGB Disks.Count TotalSizeInGB
------------    -------------- ----------- -------------
r8id.large                 118           1           118
r8id.xlarge                237           1           237
r8id.2xlarge               474           1           474
r8id.4xlarge               950           1           950
r8id.8xlarge              1900           1          1900
r8id.12xlarge             2850           1          2850
r8id.16xlarge             3800           1          3800
r8id.24xlarge             2850           2          5700
r8id.32xlarge             3800           2          7600
r8id.48xlarge             3800           3         11400
r8id.metal-48xl           3800           3         11400
r8id.96xlarge             3800           6         22800
r8id.metal-96xl           3800           6         22800
```

**To get complete instance storage details for an instance type**  
Use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) cmdlet.

```
(Get-EC2InstanceType `
    -Filter @{Name="instance-type"; Values="{{r8id.32xlarge}}"}).InstanceStorageInfo |
    Format-List *,
        @{Name="Disks.Count";Expression={$_.Disks[0].Count}},
        @{Name="Disks.SizeInGB";Expression={$_.Disks[0].SizeInGB}},
        @{Name="Disks.Type";Expression={$_.Disks[0].Type.Value}}
```

The example output shows that this instance type has two 3800 GB NVMe SSD volumes, for a total of 7600 GB of instance storage.

```
Disks             : {Amazon.EC2.Model.DiskInfo}
EncryptionSupport : required
NvmeSupport       : required
TotalSizeInGB     : 7600
Disks.Count       : 2
Disks.SizeInGB    : 3800
Disks.Type        : ssd
```

------