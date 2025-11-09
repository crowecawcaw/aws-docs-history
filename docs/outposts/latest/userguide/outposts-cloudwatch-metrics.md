# CloudWatch metrics for Outposts racks

AWS Outposts publishes data points to Amazon CloudWatch for your Outposts. CloudWatch enables you to
retrieve statistics about those data points as an ordered set of time series data, known as
_metrics_. Think of a metric as a variable to monitor, and the data
points as the values of that variable over time. For example, you can monitor the instance
capacity available to your Outpost over a specified time period. Each data point has an
associated timestamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you
can create a CloudWatch alarm to monitor the `ConnectedStatus` metric. If the average
metric is less than `1`, CloudWatch can initiate an action, such as sending a
notification to an email address. You can then investigate potential on-premises or uplink
networking issues that might be impacting the operations of your Outpost. Common issues
include recent on-premises network configuration changes to firewall and NAT rules, or
internet connection issues. For `ConnectedStatus` issues, we recommend verifying
connectivity to the AWS Region from within your on-premises network, and contacting AWS
Support if the problem persists.

For more information about creating a CloudWatch alarm, see [Using Amazon CloudWatch
Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_. For more information about CloudWatch,
see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Contents

- [Metrics](#outposts-metrics "#outposts-metrics")
- [Metric dimensions](#outposts-metric-dimensions "#outposts-metric-dimensions")
- [View CloudWatch metrics for your Outposts rack](#view-metric-data "#view-metric-data")

## Metrics

The `AWS/Outposts` namespace includes the following categories of metrics.

###### Contents

- [Instance metrics](#metrics-instances "#metrics-instances")
- [Amazon EBS metrics](#metrics-ebs "#metrics-ebs")
- [Virtual interface metrics](#metrics-vif "#metrics-vif")
- [Outposts metrics](#metrics-outposts "#metrics-outposts")

### Instance metrics

The following metrics are available for Amazon EC2 instances.

| Metric                               | Dimension                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `InstanceFamilyCapacityAvailability` | `InstanceFamily` and<br>`OutpostId`             | The percentage of instance capacity available. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br>**Unit**: Percent<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `InstanceFamilyCapacityUtilization`  | `Account`, `InstanceFamily`, and<br>`OutpostId` | The percentage of instance capacity in use. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br>**Unit**: Percent<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `InstanceTypeCapacityAvailability`   | `InstanceType` and `OutpostId`                  | The percentage of instance capacity available. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br>**Unit**: Percent<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `InstanceTypeCapacityUtilization`    | `Account`,<br>`InstanceType`, and `OutpostId`   | The percentage of instance capacity in use. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br>**Unit**: Percent<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `UsedInstanceType_Count`             | `Account`,<br>`InstanceType`, and `OutpostId`   | The number of instance types that are currently in use, including any instance<br>types used by managed services such as Amazon Relational Database Service (Amazon RDS) or Application Load Balancer. This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br>**Unit**: Count<br>**Maximum resolution**: 5 minutes                                                                                                                                                                                                                                                                                                                                                                                                       |
| `AvailableInstanceType_Count`        | `InstanceType` and `OutpostId`                  | The number of available instance types. This metric includes the<br>`AvailableReservedInstances` count.<br>To determine the number of instances that you can reserve, subtract the<br>`AvailableReservedInstances` count from the<br>`AvailableInstanceType_Count` count.<br>``<br>Number of instances that you can reserve = `AvailableInstanceType_Count`<br>• `AvailableReservedInstances`<br>``<br>This metric does not include capacity for any Dedicated Hosts configured on the Outpost.<br>**Unit**: Count<br>**Maximum resolution**: 5 minutes                                                                                                                                                                                                       |
| `AvailableReservedInstances`         | `InstanceType` and<br>`OutpostId`               | The number of instances that are available for launch into the compute capacity<br>reserved using [Capacity<br>Reservations](../../../AWSEC2/latest/UserGuide/capacity-reservations-outposts.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-outposts.md").<br>This metric does not include Amazon EC2 Reserved Instances.<br>This metric does not include the number of instances that you can reserve. To<br>determine how many instances you can reserve, subtract the<br>`AvailableReservedInstances` count from the<br>`AvailableInstanceType_Count` count.<br>``<br>Number of instances that you can reserve = `AvailableInstanceType_Count`<br>• `AvailableReservedInstances`<br>``<br>**Unit**: Count<br>**Maximum resolution**: 5 minutes |
| `UsedReservedInstances`              | `InstanceType` and<br>`OutpostId`               | The number of instances that are running in the compute capacity reserved using<br>[Capacity<br>Reservations](../../../AWSEC2/latest/UserGuide/capacity-reservations-outposts.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-outposts.md"). This metric does not include Amazon EC2 Reserved Instances.<br>**Unit**: Count<br>**Maximum resolution**: 5 minutes                                                                                                                                                                                                                                                                                                                                                                                   |
| `TotalReservedInstances`             | `InstanceType` and<br>`OutpostId`               | The total number of instances, running and available for launch, provided by the<br>compute capacity reserved using [Capacity<br>Reservations](../../../AWSEC2/latest/UserGuide/capacity-reservations-outposts.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-outposts.md"). This metric does not include Amazon EC2 Reserved Instances.<br>**Unit**: Count<br>**Maximum resolution**: 5 minutes                                                                                                                                                                                                                                                                                                                                                  |

### Amazon EBS metrics

The following metrics are available for the EBS volume type capacity.

| Metric                                | Dimension                       | Description                                                                                                                                                                                                                  |
| ------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EBSVolumeTypeCapacityUtilization`    | `VolumeType` and<br>`OutpostId` | The percentage of EBS volume type capacity in use.<br>**Unit**: Percent<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                      |
| `EBSVolumeTypeCapacityAvailability`   | `VolumeType` and<br>`OutpostId` | The percentage of EBS volume type capacity available.<br>**Unit**: Percent<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                   |
| `EBSVolumeTypeCapacityUtilizationGB`  | `VolumeType` and<br>`OutpostId` | The number of gigabytes in use for the EBS volume type.<br>**Unit**: Gigabyte<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles).                |
| `EBSVolumeTypeCapacityAvailabilityGB` | `VolumeType` and<br>`OutpostId` | The number of gigabytes of available capacity for the EBS volume type.<br>**Unit**: Gigabyte<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Average` and `pNN.NN` (percentiles). |

### Virtual interface metrics

The following metrics are available for the virtual interface (VIF).

| Metric                | Dimension                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VifBgpSessionState`  | **Dimensions for local gateway VIFs**:<br>`OutpostsID`, `Virtual InterfaceGroupID`,<br>`VirtualInterfaceID`.<br>**Dimensions for service link VIFs**:<br>`OutpostsID`, `VirtualInterfaceID`.                        | The Border Gateway Protocol (BGP) session state between the AWS Outposts of virtual<br>interface (VIF) and on-premise devices.<br>**Unit**: Values 1 through 6 where:<br>• `1` – Idle. This is the initial state<br>where the Outposts rack is waiting for a start event.<br>• `2` – Connect. The Outposts rack is waiting for<br>the TCP connection to be completed.<br>• `3` – Active. The Outposts rack is trying to<br>initiate a TCP connection.<br>• `4` – OpenSent. The router has sent an<br>OPEN message and is waiting for one in return.<br>• `5` – OpenConfirm. The router has<br>received an OPEN message and is waiting for a KEEPALIVE message.<br>• `6` – Established. The BGP connection is<br>fully established and the Outposts rack and on-premise devices can exchange routing<br>information.<br>**Maximum resolution**: 5 minute<br>**Statistics**: The most useful statistic is<br>`Maximum`. |
| `VifConnectionStatus` | **Dimensions for local gateway VIFs**:<br>`OutpostsID`, `Virtual InterfaceGroupID`,<br>`VirtualInterfaceID`.<br>**Dimensions for service link VIFs**:<br>`OutpostsID`, `VirtualInterfaceID`.                        | Shows whether the virtual interfaces (VIFs) are ready to forward traffic.<br>**Unit**: 1 or 0 where:<br>• `1` – Indicates that the Outpost VIF is<br>successfully connected to on-premise devices, configured, and ready to forward traffic.<br>• `0` – Indicates that the Outpost VIF is not ready<br>to forward traffic.<br>**Maximum resolution**: 5 minute<br>**Statistics**: The most useful statistic is<br>`Maximum`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `IfTrafficIn`         | **Dimensions for local gateway VIFs (lgw-vif)**:<br>`OutpostsId`, `VirtualInterfaceGroupId`, and<br>`VirtualInterfaceId`<br>**Dimensions for service link VIFs (sl-vif)**:<br>`OutpostsId` and `VirtualInterfaceId` | The bitrate of data that the Outposts Virtual Interfaces (VIFs) receive from the<br>connected local network devices.<br>**Unit**: Bits per second<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Max` and `Min`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `IfTrafficOut`        | **Dimensions for local gateway VIFs (lgw-vif)**:<br>`OutpostsId`, `VirtualInterfaceGroupId`, and<br>`VirtualInterfaceId`<br>**Dimensions for service link VIFs (sl-vif)**:<br>`OutpostsId` and `VirtualInterfaceId` | The bitrate of data that the Outposts Virtual Interfaces (VIFs) transfer to the<br>connected local network devices.<br>**Unit**: Bits per second<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Max` and `Min`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Outposts metrics

The following metrics are available for your Outposts.

| Metric               | Dimension                         | Description                                                                                                                                                                                                                                        |
| -------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConnectedStatus`    | `OutpostId`                       | The status of an Outpost's service link connection. If the average statistic is<br>less than `1`, the connection is impaired.<br>**Unit**: Count<br>**Maximum resolution**: 1 minute<br>**Statistics**: The most useful statistic is<br>`Average`. |
| `CapacityExceptions` | `InstanceType` and<br>`OutpostId` | The number of insufficient capacity errors for instance launches.<br>**Unit**: Count<br>**Maximum resolution**: 5 minutes<br>**Statistics**: The most useful statistics are<br>`Maximum` and `Minimum`.                                            |

## Metric dimensions

To filter the metrics for your Outpost, use the following dimensions.

| Dimension                 | Description                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `Account`                 | The account or service using the capacity.                                              |
| `InstanceFamily`          | The instance family.                                                                    |
| `InstanceType`            | The instance type.                                                                      |
| `OutpostId`               | The ID of the Outpost.                                                                  |
| `VolumeType`              | The EBS volume type.                                                                    |
| `VirtualInterfaceId`      | The ID of the local gateway or service link Virtual Interface (VIF).                    |
| `VirtualInterfaceGroupId` | The ID of the virtual interface group for the local gateway Virtual Interface<br>(VIF). |

## View CloudWatch metrics for your Outposts rack

You can view the CloudWatch metrics for your Outposts rack using the CloudWatch
console.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the **Outposts** namespace.
4. (Optional) To view a metric across all dimensions, enter its name in the search
   field.

###### To view metrics using the AWS CLI

Use the following [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command to list the available metrics.

```
aws cloudwatch list-metrics --namespace AWS/Outposts
```

###### To get the statistics for a metric using the AWS CLI

Use the following [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") command to get statistics for the specified metric and
dimension. CloudWatch treats each unique combination of dimensions as a separate metric.
You can't retrieve statistics using combinations of dimensions that were not specially
published. You must specify the same dimensions that were used when the metrics were
created.

```
aws cloudwatch get-metric-statistics \
--namespace AWS/Outposts --metric-name InstanceTypeCapacityUtilization \
--statistics Average --period 3600 \
--dimensions Name=OutpostId,Value=op-01234567890abcdef Name=InstanceType,Value=c5.xlarge \
--start-time 2019-12-01T00:00:00Z --end-time 2019-12-08T00:00:00Z
```
