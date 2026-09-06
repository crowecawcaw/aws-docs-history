

# CloudWatch metrics for Outposts racks
<a name="outposts-cloudwatch-metrics"></a>

AWS Outposts publishes data points to Amazon CloudWatch for your Outposts. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time series data, known as *metrics*. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. For example, you can monitor the instance capacity available to your Outpost over a specified time period. Each data point has an associated timestamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor the `ConnectedStatus` metric. If the average metric is less than `1`, CloudWatch can initiate an action, such as sending a notification to an email address. You can then investigate potential on-premises or uplink networking issues that might be impacting the operations of your Outpost. Common issues include recent on-premises network configuration changes to firewall and NAT rules, or internet connection issues. For `ConnectedStatus` issues, we recommend verifying connectivity to the AWS Region from within your on-premises network, and contacting AWS Support if the problem persists.

For more information about creating a CloudWatch alarm, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Metrics](#outposts-metrics)
+ [Metric dimensions](#outposts-metric-dimensions)
+ [View CloudWatch metrics for your Outposts rack](#view-metric-data)

## Metrics
<a name="outposts-metrics"></a>

The `AWS/Outposts` namespace includes the following categories of metrics.

**Topics**
+ [Instance metrics](#metrics-instances)
+ [Amazon EBS metrics](#metrics-ebs)
+ [Virtual interface metrics](#metrics-vif)
+ [LAG metrics](#metrics-lag)
+ [Outposts metrics](#metrics-outposts)

### Instance metrics
<a name="metrics-instances"></a>

The following metrics are available for Amazon EC2 instances.


| Metric | Dimension | Description | 
| --- | --- | --- | 
| `InstanceFamilyCapacityAvailability` | `InstanceFamily` and `OutpostId` | The percentage of instance capacity available. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br />**Unit**: Percent<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `InstanceFamilyCapacityUtilization` | `Account`, `InstanceFamily`, and `OutpostId` | The percentage of instance capacity in use. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br />**Unit**: Percent<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `InstanceTypeCapacityAvailability` | `InstanceType` and `OutpostId` | The percentage of instance capacity available. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br />**Unit**: Percent<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `InstanceTypeCapacityUtilization` | `Account`, `InstanceType`, and `OutpostId` | The percentage of instance capacity in use. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br />**Unit**: Percent<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `UsedInstanceType_Count` | `Account`, `InstanceType`, and `OutpostId` | The number of instance types that are currently in use, including any instance types used by managed services such as Amazon Relational Database Service (Amazon RDS) or Application Load Balancer. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br />**Unit**: Count<br />**Maximum resolution**: 5 minutes | 
| `AvailableInstanceType_Count` | `InstanceType` and `OutpostId` | The number of available instance types. This metric includes the `AvailableReservedInstances` count.<br />To determine the number of instances that you can reserve, subtract the `AvailableReservedInstances` count from the `AvailableInstanceType_Count` count.<pre>Number of instances that you can reserve = AvailableInstanceType_Count - AvailableReservedInstances</pre><br /> This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br />**Unit**: Count<br />**Maximum resolution**: 5 minutes | 
| `AvailableReservedInstances` | `InstanceType` and `OutpostId` | The number of instances that are available for launch into the compute capacity reserved using [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-outposts.html).<br />This metric does not include Amazon EC2 Reserved Instances.<br />This metric does not include the number of instances that you can reserve. To determine how many instances you can reserve, subtract the `AvailableReservedInstances` count from the `AvailableInstanceType_Count` count.<pre>Number of instances that you can reserve = AvailableInstanceType_Count - AvailableReservedInstances</pre><br />**Unit**: Count<br />**Maximum resolution**: 5 minutes | 
| `UsedReservedInstances` | `InstanceType` and `OutpostId` | The number of instances that are running in the compute capacity reserved using [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-outposts.html). This metric does not include Amazon EC2 Reserved Instances.<br />**Unit**: Count<br />**Maximum resolution**: 5 minutes | 
| `TotalReservedInstances` | `InstanceType` and `OutpostId` | The total number of instances, running and available for launch, provided by the compute capacity reserved using [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-outposts.html). This metric does not include Amazon EC2 Reserved Instances.<br />**Unit**: Count<br />**Maximum resolution**: 5 minutes | 

### Amazon EBS metrics
<a name="metrics-ebs"></a>

The following metrics are available for the EBS volume type capacity.


| Metric | Dimension | Description | 
| --- | --- | --- | 
| `EBSVolumeTypeCapacityUtilization` | `VolumeType` and `OutpostId` | The percentage of EBS volume type capacity in use.<br />**Unit**: Percent<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `EBSVolumeTypeCapacityAvailability` | `VolumeType` and `OutpostId` | The percentage of EBS volume type capacity available.<br />**Unit**: Percent<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `EBSVolumeTypeCapacityUtilizationGB` | `VolumeType` and `OutpostId` | The number of gigabytes in use for the EBS volume type.<br />**Unit**: Gigabyte<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 
| `EBSVolumeTypeCapacityAvailabilityGB` | `VolumeType` and `OutpostId` | The number of gigabytes of available capacity for the EBS volume type.<br />**Unit**: Gigabyte<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Average` and `pNN.NN` (percentiles). | 

### Virtual interface metrics
<a name="metrics-vif"></a>

The following metrics are available for the virtual interface (VIF).


| Metric | Dimension | Description | 
| --- | --- | --- | 
| `VifBgpSessionState` | **Dimensions for local gateway VIFs**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, `VirtualInterfaceId`.<br />**Dimensions for service link VIFs**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, `VirtualInterfaceId`. `VirtualInterfaceGroupId` always displays as "-" for service link VIFs; included for CloudWatch widget alignment. | The Border Gateway Protocol (BGP) session state between the AWS Outposts of virtual interface (VIF) and on-premise devices.<br />**Unit**: Values 1 through 6 where:+  `1` – Idle. This is the initial state where the Outposts rack is waiting for a start event. <br />+  `2` – Connect. The Outposts rack is waiting for the TCP connection to be completed. <br />+  `3` – Active. The Outposts rack is trying to initiate a TCP connection. <br />+  `4` – OpenSent. The router has sent an OPEN message and is waiting for one in return. <br />+  `5` – OpenConfirm. The router has received an OPEN message and is waiting for a KEEPALIVE message. <br />+  `6` – Established. The BGP connection is fully established and the Outposts rack and on-premise devices can exchange routing information. <br />**Maximum resolution**: 5 minute<br />**Statistics**: The most useful statistic is `Maximum`. | 
| `VifConnectionStatus` | **Dimensions for local gateway VIFs**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, `VirtualInterfaceId`.<br />**Dimensions for service link VIFs**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, `VirtualInterfaceId`. `VirtualInterfaceGroupId` always displays as "-" for service link VIFs; included for CloudWatch widget alignment. | Shows whether the virtual interfaces (VIFs) are ready to forward traffic.<br />**Unit**: 1 or 0 where:+  `1` – Indicates that the Outpost VIF is successfully connected to on-premise devices, configured, and ready to forward traffic. <br />+  `0` – Indicates that the Outpost VIF is not ready to forward traffic. <br />**Maximum resolution**: 5 minute<br />**Statistics**: The most useful statistic is `Maximum`. | 
| `IfTrafficIn` | **Dimensions for local gateway VIFs (lgw-vif)**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, and `VirtualInterfaceId`<br />**Dimensions for service link VIFs (sl-vif)**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, and `VirtualInterfaceId`. `VirtualInterfaceGroupId` always displays as "-" for service link VIFs; included for CloudWatch widget alignment. | The bitrate of data that the Outposts Virtual Interfaces (VIFs) receive from the connected local network devices.<br />**Unit**: Bits per second<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Max` and `Min`. | 
| `IfTrafficOut` | **Dimensions for local gateway VIFs (lgw-vif)**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, and `VirtualInterfaceId`<br />**Dimensions for service link VIFs (sl-vif)**: `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, and `VirtualInterfaceId`. `VirtualInterfaceGroupId` always displays as "-" for service link VIFs; included for CloudWatch widget alignment. | The bitrate of data that the Outposts Virtual Interfaces (VIFs) transfer to the connected local network devices.<br />**Unit**: Bits per second<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Max` and `Min`. | 

The `LagId` dimension has been added to the `VifBgpSessionState`, `VifConnectionStatus`, `IfTrafficIn`, and `IfTrafficOut` metrics. This enables you to associate VIF-level metrics with their corresponding LAG, making it easier to identify whether a connectivity issue originates at the VIF configuration level or the physical LAG level. A new CloudWatch widget displays all metrics (existing VIF metrics and new LAG metrics) using the updated dimension name `OutpostId`. The previous widget continues to display with the legacy dimension name `OutpostsId` for backward compatibility.

### LAG metrics
<a name="metrics-lag"></a>

AWS Outposts publishes Link Aggregation Group (LAG) status metrics to Amazon CloudWatch. These metrics provide visibility into the operational status of LAG connections between Outpost network devices and your on-premises network devices. Use these metrics together with VIF metrics to correlate physical LAG health with virtual interface and BGP session state for end-to-end connectivity troubleshooting.


| Metric | Dimensions | Description | 
| --- | --- | --- | 
| `LagStatus` | `OutpostId`, `LagId`, `VirtualInterfaceGroupId`, `VirtualInterfaceId` | The operational status of the LAG connection between an Outpost network device and your on-premises network device.<br />**Unit**: Values where:+  `1` – LAG is operational (up) <br />+  `0` – LAG is not operational (down) <br />**Reporting Criteria**: There is data to report.<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistic is `Maximum`. | 

The following dimensions are used for the `LagStatus` metric.


| Dimension | Description | 
| --- | --- | 
| OutpostId | The ID of the Outpost (e.g., op-1234567890abcdef0) | 
| LagId | The ID of the Link Aggregation Group (e.g., op-lag-02343ndswe3190d1) | 
| VirtualInterfaceGroupId | The ID of the Virtual Interface Group. Always displays as "-" for LAG metrics; included for CloudWatch widget alignment with VIF metrics. | 
| VirtualInterfaceId | The ID of the Virtual Interface. Always displays as "-" for LAG metrics; included for CloudWatch widget alignment with VIF metrics. | 

**Important**  
If the entire Outpost loses connectivity, the underlying telemetry service cannot collect data from network devices. No metric data points are published during this period, and the CloudWatch graph will show a gap for the affected time range.

### Outposts metrics
<a name="metrics-outposts"></a>

The following metrics are available for your Outposts.


| Metric | Dimension | Description | 
| --- | --- | --- | 
| `ConnectedStatus` | `OutpostId` | The status of an Outpost's service link connection. If the average statistic is less than `1`, the connection is impaired.<br />**Unit**: Count<br />**Maximum resolution**: 1 minute<br />**Statistics**: The most useful statistic is `Average`. | 
| `CapacityExceptions` | `InstanceType` and `OutpostId` | The number of insufficient capacity errors for instance launches.<br />**Unit**: Count<br />**Maximum resolution**: 5 minutes<br />**Statistics**: The most useful statistics are `Maximum` and `Minimum`. | 

## Metric dimensions
<a name="outposts-metric-dimensions"></a>

To filter the metrics for your Outpost, use the following dimensions.


| Dimension | Description | 
| --- | --- | 
| Account | The account or service using the capacity. | 
| InstanceFamily | The instance family. | 
| InstanceType | The instance type. | 
| OutpostId | The ID of the Outpost. | 
| VolumeType | The EBS volume type. | 
| LagId | The ID of the Link Aggregation Group associated with this VIF. | 
| VirtualInterfaceId | The ID of the local gateway or service link Virtual Interface (VIF). | 
| VirtualInterfaceGroupId | The ID of the virtual interface group for the local gateway Virtual Interface (VIF). | 

## View CloudWatch metrics for your Outposts rack
<a name="view-metric-data"></a>

You can view the CloudWatch metrics for your Outposts rack using the CloudWatch console.

**To view metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Select the **Outposts** namespace.

1. (Optional) To view a metric across all dimensions, enter its name in the search field.

**To view metrics using the AWS CLI**  
Use the following [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) command to list the available metrics.

```
aws cloudwatch list-metrics --namespace AWS/Outposts
```

**To get the statistics for a metric using the AWS CLI**  
Use the following [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) command to get statistics for the specified metric and dimension. CloudWatch treats each unique combination of dimensions as a separate metric. You can't retrieve statistics using combinations of dimensions that were not specially published. You must specify the same dimensions that were used when the metrics were created.

```
aws cloudwatch get-metric-statistics \
--namespace AWS/Outposts --metric-name InstanceTypeCapacityUtilization \
--statistics Average --period 3600 \
--dimensions Name=OutpostId,Value=op-01234567890abcdef Name=InstanceType,Value=c5.xlarge \
--start-time 2019-12-01T00:00:00Z --end-time 2019-12-08T00:00:00Z
```