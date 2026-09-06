

# CloudWatch metrics for Outposts servers
<a name="outposts-cloudwatch-metrics"></a>

AWS Outposts publishes data points to Amazon CloudWatch for your Outposts. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time series data, known as *metrics*. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. For example, you can monitor the instance capacity available to your Outpost over a specified time period. Each data point has an associated timestamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor the `ConnectedStatus` metric. If the average metric is less than `1`, CloudWatch can initiate an action, such as sending a notification to an email address. You can then investigate potential on-premises or uplink networking issues that might be impacting the operations of your Outpost. Common issues include recent on-premises network configuration changes to firewall and NAT rules, or internet connection issues. For `ConnectedStatus` issues, we recommend verifying connectivity to the AWS Region from within your on-premises network, and contacting AWS Support if the problem persists.

For more information about creating a CloudWatch alarm, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Metrics](#outposts-metrics)
+ [Metric dimensions](#outposts-metric-dimensions)
+ [View CloudWatch metrics for your Outposts server](#view-metric-data)

## Metrics
<a name="outposts-metrics"></a>

The `AWS/Outposts` namespace includes the following categories of metrics.

**Topics**
+ [Instance metrics](#metrics-instances)
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

## View CloudWatch metrics for your Outposts server
<a name="view-metric-data"></a>

You can view the CloudWatch metrics for your Outposts server using the CloudWatch console.

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