# Instance store volume limits for EC2 instances

The number, size, and type of instance store volumes are determined by the instance type.
Some instance types, such as M6, C6, and R6, do not support instance
store volumes, while other instance types, such as M5d, C6gd, and R6gd, do support instance
store volumes. You can’t attach more instance store volumes to an instance than is supported
by its instance type. For the instance types that do support instance store volumes, the number and
size of the instance store volumes vary by instance size. For example, `m5d.large`
supports 1 x 75 GB instance store volume, while `m5d.24xlarge` supports 4 x 900
GB instance store volumes.

For instance types with **NVMe instance store volumes**, all
of the supported instance store volumes are automatically attached to the instance at
launch. For instance types with **non-NVMe instance store volumes**,
such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must manually specify the
block device mappings for the instance store volumes that you want to attach at launch. Then,
after the instance has launched, you must [format and mount the attached instance store volumes](making-instance-stores-available-on-your-instances.md "making-instance-stores-available-on-your-instances.md") before you can use them. You
can't attach an instance store volume after you launch the instance.

Some instance types use NVMe or SATA-based solid state drives (SSD), while others use
SATA-based hard disk drives (HDD). SSDs deliver high random I/O performance with very low
latency, but you don't need the data to persist when the instance terminates or you can
take advantage of fault-tolerant architectures. For more information, see
[SSD instance store volumes for EC2 instances](ssd-instance-store.md "ssd-instance-store.md").

The data on NVMe instance store volumes and some HDD instance store volumes is encrypted
at rest. For more information, see [Data protection in Amazon EC2](data-protection.md "data-protection.md").

## Available instance store volumes

The _Amazon EC2 Instance Types Guide_ provides the quantity, size, type, and performance
optimizations of instance store volumes available on each supported instance type. For more information,
see the following:

- [Instance store specifications – General purpose](../../../ec2/latest/instancetypes/gp.md#gp_instance-store "../../../ec2/latest/instancetypes/gp.md#gp_instance-store")
- [Instance store specifications – Compute optimized](../../../ec2/latest/instancetypes/co.md#co_instance-store "../../../ec2/latest/instancetypes/co.md#co_instance-store")
- [Instance store specifications – Memory optimized](../../../ec2/latest/instancetypes/mo.md#mo_instance-store "../../../ec2/latest/instancetypes/mo.md#mo_instance-store")
- [Instance store specifications – Storage optimized](../../../ec2/latest/instancetypes/so.md#so_instance-store "../../../ec2/latest/instancetypes/so.md#so_instance-store")
- [Instance store specifications – Accelerated computing](../../../ec2/latest/instancetypes/ac.md#ac_instance-store "../../../ec2/latest/instancetypes/ac.md#ac_instance-store")
- [Instance store specifications – High-performance computing](../../../ec2/latest/instancetypes/hpc.md#hpc_instance-store "../../../ec2/latest/instancetypes/hpc.md#hpc_instance-store")
- [Instance store specifications – Previous generation](../../../ec2/latest/instancetypes/pg.md#pg_instance-store "../../../ec2/latest/instancetypes/pg.md#pg_instance-store")

Console

###### To retrieve instance store volume information

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instance Types**.
3. Add the filter **Local instance storage = true**. The
   **Storage** column indicates the total size of the instance
   storage for the instance type.
4. (Optional) Click the **Preferences** icon and then turn on
   **Storage disk count**. This column indicates the number of
   instance store volumes.
5. (Optional) Add filters to further scope to specific instance types of interest.

AWS CLI

###### To retrieve instance store volume information

Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md")
command. The following example displays the total size of the instance storage for each
instance type in the R6i instance families with instance store volumes.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=r6i*" "Name=instance-storage-supported,Values=true" \
    --query "InstanceTypes[].[InstanceType, InstanceStorageInfo.TotalSizeInGB]" \
    --output table
```

The following is example output.

```
----------------------------
|  DescribeInstanceTypes   |
+----------------+---------+
|  r6id.16xlarge  |  3800  |
|  r6idn.16xlarge |  3800  |
|  r6idn.8xlarge  |  1900  |
|  r6id.2xlarge   |  474   |
|  r6idn.xlarge   |  237   |
|  r6id.12xlarge  |  2850  |
|  r6idn.2xlarge  |  474   |
|  r6id.xlarge    |  237   |
|  r6idn.24xlarge |  5700  |
|  r6id.4xlarge   |  950   |
|  r6id.32xlarge  |  7600  |
|  r6id.24xlarge  |  5700  |
|  r6idn.large    |  118   |
|  r6idn.4xlarge  |  950   |
|  r6id.large     |  118   |
|  r6id.8xlarge   |  1900  |
|  r6idn.32xlarge |  7600  |
|  r6idn.metal    |  7600  |
|  r6id.metal     |  7600  |
|  r6idn.12xlarge |  2850  |
+----------------+--------+
```

###### To get complete instance storage details for an instance type

Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md")
command.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=`r6id.16xlarge`" \
    --query "InstanceTypes[].InstanceStorageInfo"
```

The example output shows that this instance type has two 1900 GB NVMe SSD volumes, for a
total of 3800 GB of instance storage.

```
[
    {
        "TotalSizeInGB": 3800,
        "Disks": [
            {
                "SizeInGB": 1900,
                "Count": 2,
                "Type": "ssd"
            }
        ],
        "NvmeSupport": "required",
        "EncryptionSupport": "required"
    }
]
```

PowerShell

###### To retrieve instance store volume information

Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md")
cmdlet. The following example displays the total size of the instance storage for each
instance type in the R6i instance families with instance store volumes.

```
(Get-EC2InstanceType -Filter @{Name="instance-type"; Values="r6i*"},@{Name="instance-storage-supported"; Values="true"}) | Format-Table @{Name="InstanceType";Expression={$_.InstanceType}}, @{Name="TotalSize";Expression={$_.InstanceStorageInfo.TotalSizeInGB}}
```

The following is example output.

```
InstanceType   TotalSize
------------   ---------
r6idn.16xlarge      3800
r6id.16xlarge       3800
r6id.xlarge          237
r6idn.8xlarge       1900
r6idn.2xlarge        474
r6id.12xlarge       2850
r6idn.xlarge         237
r6id.2xlarge         474
r6id.4xlarge         950
r6idn.24xlarge      5700
r6id.32xlarge       7600
r6id.24xlarge       5700
r6idn.large          118
r6id.large           118
r6idn.4xlarge        950
r6id.8xlarge        1900
r6id.metal          7600
r6idn.32xlarge      7600
r6idn.metal         7600
r6idn.12xlarge      2850
```

###### To get complete instance storage details for an instance type

Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md")
cmdlet. The output is converted to JSON format.

```
(Get-EC2InstanceType -Filter @{Name="instance-type"; Values="`r6id.16xlarge`"}).InstanceStorageInfo | ConvertTo-Json
```

The example output shows that this instance type has two 1900 GB NVMe SSD volumes, for a
total of 3800 GB of instance storage.

```
{
  "Disks": [
    {
      "Count": 2,
      "SizeInGB": 1900,
      "Type": "ssd"
    }
  ],
  "EncryptionSupport": {
    "Value": "required"
  },
  "NvmeSupport": {
    "Value": "required"
  },
  "TotalSizeInGB": 3800
}
```
