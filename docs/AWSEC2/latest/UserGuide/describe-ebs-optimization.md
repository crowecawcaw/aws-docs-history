# Find EBS-optimized EC2 instance types

You can view the instances types that support EBS optimization in each Region.

Console

###### To find instance types that are EBS-optimized by default

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instance Types**.
3. Add the filter **EBS optimization support = default**.
4. (Optional) Click the **Preferences** icon and then turn on
   the relevant columns, such as **EBS Maximum IOPS** and
   **EBS Baseline IOPS**.
5. (Optional) Add filters to further scope to specific instance types of interest.

AWS CLI

###### To find instance types that are EBS-optimized by default

Use the following [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command.

```
aws ec2 describe-instance-types \
    --filters Name=ebs-info.ebs-optimized-support,Values=default  \
    --query 'InstanceTypes[].{InstanceType:InstanceType, \
        "MaxBandwidth(Mb/s)":EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps,\
        MaxIOPS:EbsInfo.EbsOptimizedInfo.MaximumIops,\
        "MaxThroughput(MB/s)":EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps}' \
    --output=table
```

###### To find instance types that optionally support EBS optimization

Use the following [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command.

```
aws ec2 describe-instance-types \
    --filters Name=ebs-info.ebs-optimized-support,Values=supported \
    --query 'InstanceTypes[].{InstanceType:InstanceType, \
        "MaxBandwidth(Mb/s)":EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps, \
        MaxIOPS:EbsInfo.EbsOptimizedInfo.MaximumIops, \
        "MaxThroughput(MB/s)":EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps}' \
    --output=table
```

The following is example output for `eu-west-1`.

````
--------------------------------------------------------------------------
|                         DescribeInstanceTypes                          | +--------------+----------------------+----------+-----------------------+
| InstanceType | MaxBandwidth(Mb/s)   | MaxIOPS  |  MaxThroughput(MB/s)  | +--------------+----------------------+----------+-----------------------+
|  i2.2xlarge  |  1000                |  8000    |  125.0                |
|  m2.4xlarge  |  1000                |  8000    |  125.0                |
|  m2.2xlarge  |  500                 |  4000    |  62.5                 |
|  c1.xlarge   |  1000                |  8000    |  125.0                |
|  i2.xlarge   |  500                 |  4000    |  62.5                 |
|  m3.xlarge   |  500                 |  4000    |  62.5                 |
|  m1.xlarge   |  1000                |  8000    |  125.0                |
|  r3.4xlarge  |  2000                |  16000   |  250.0                |
|  r3.2xlarge  |  1000                |  8000    |  125.0                |
|  c3.xlarge   |  500                 |  4000    |  62.5                 |
|  m3.2xlarge  |  1000                |  8000    |  125.0                |
|  r3.xlarge   |  500                 |  4000    |  62.5                 |
|  i2.4xlarge  |  2000                |  16000   |  250.0                |
|  c3.4xlarge  |  2000                |  16000   |  250.0                |
|  c3.2xlarge  |  1000                |  8000    |  125.0                |
|  m1.large    |  500                 |  4000    |  62.5                 | +--------------+----------------------+----------+-----------------------+ ``` PowerShell ###### To find instance types that are EBS-optimized by default Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") cmdlet. ``` Get-EC2InstanceType ` -Filter @{Name="ebs-info.ebs-optimized-support"; Values="default"} | ` Select InstanceType, ` @{Name="MaxBandwidth(Mb/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps)}}, ` @{Name="MaxIOPS"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumIops)}}, ` @{Name="MaxThroughput (MB/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps)}} ``` ###### To find instance types that optionally support EBS optimization Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") cmdlet. ``` Get-EC2InstanceType ` -Filter @{Name="ebs-info.ebs-optimized-support"; Values="supported"} | ` Select InstanceType, ` @{Name="MaxBandwidth(Mb/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps)}}, ` @{Name="MaxIOPS"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumIops)}}, ` @{Name="MaxThroughput (MB/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps)}} ``` The following is example output for `eu-west-1`. ``` InstanceType MaxBandwidth(Mb/s) MaxIOPS MaxThroughput (MB/s) ------------ ------------------ ------- -------------------- m2.4xlarge                 1000    8000              125.000 i2.2xlarge                 1000    8000              125.000 c1.xlarge                  1000    8000              125.000 m2.2xlarge                  500    4000               62.500 r3.2xlarge                 1000    8000              125.000 m3.xlarge                   500    4000               62.500 r3.4xlarge                 2000   16000              250.000 m1.xlarge                  1000    8000              125.000 i2.xlarge                   500    4000               62.500 c3.xlarge                   500    4000               62.500 c3.4xlarge                 2000   16000              250.000 c3.2xlarge                 1000    8000              125.000 i2.4xlarge                 2000   16000              250.000 r3.xlarge                   500    4000               62.500 m3.2xlarge                 1000    8000              125.000 m1.large                    500    4000               62.500 ```
````
