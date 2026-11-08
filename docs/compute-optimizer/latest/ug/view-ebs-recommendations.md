

# Viewing Amazon EBS volume recommendations
<a name="view-ebs-recommendations"></a>

AWS Compute Optimizer generates volume type, volume size, IOPS, and throughput recommendations for Amazon Elastic Block Store (Amazon EBS) volumes. Recommendations for your EBS volumes are displayed in the following pages of the AWS Compute Optimizer console:
+ The **EBS volumes recommendations** page lists each of your current volumes, their [finding classifications](#ebs-recommendations-findings), their current volume type, and their current hourly price.

  The top recommendation from Compute Optimizer is listed next to each volume. It includes the following:
  + Recommended volume type
  + Recommended volume size
  + Recommended IOPS
  + Monthly price of the recommendation
  + Price difference between your current volume and the recommendation

  Use this page to compare each volume with its top recommendation. Then decide whether to upsize or downsize the volume.
+ The **EBS volume details** page, which you can access from the EBS volume recommendations page, lists up to three recommendations for a volume. It shows the specifications for each recommendation, their [performance risk](#ebs-performance-risk), and their monthly prices. The details page also displays utilization metric graphs for the current volume.

Compute Optimizer refreshes the recommendations daily. It looks at the specs and use of the current volume over the last 14 days. For more information, see [Metrics analyzed by AWS Compute Optimizer](metrics.md).

Compute Optimizer generates recommendations only for EBS volumes that meet a set of requirements. Recommendations might take up to 24 hours to appear. Enough metric data must also build up first. For more information, see [Resource requirements](requirements.md).

**Topics**
+ [Finding classifications](#ebs-recommendations-findings)
+ [Estimated monthly savings and savings opportunity](#ebs-savings-calculation)
+ [Performance risk](#ebs-performance-risk)
+ [Utilization graphs](#ebs-utilization-graphs)
+ [Accessing EBS volumes recommendations and details](ebs-view-recommendations.md)

## Finding classifications
<a name="ebs-recommendations-findings"></a>

The **Finding** column on the **EBS volumes recommendations** page provides a summary of how each of your volumes performed during the analyzed period.

The following findings classifications apply to EBS volumes.


| Classification | Description | 
| --- | --- | 
| Not optimized | An EBS volume is considered not optimized when Compute Optimizer has identified a volume type, volume size, or IOPS specification that can provide better performance or cost for your workload. | 
| Optimized | An EBS volume is considered optimized when Compute Optimizer determines that the volume is correctly provisioned to run your workload, based on the chosen volume type, volume size, and IOPS specification. For optimized resources, Compute Optimizer might sometimes recommend a new generation volume type. | 

## Estimated monthly savings and savings opportunity
<a name="ebs-savings-calculation"></a>

Estimated monthly savings (after discounts)  
This column lists the approximate monthly savings if you move your EBS volumes to the recommended specs. It includes your specific discounts. To get these discounts in your recommendations, you must activate the savings estimation mode preference. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).  
If you don't activate the savings estimation mode preference, this column displays the default On-Demand pricing discount information.

Estimated monthly savings (On-Demand)  
This column lists the approximate monthly savings if you move your EBS volumes to the recommended specs. It uses On-Demand prices.

Savings opportunity (%)  
This column lists the price difference, as a percent, between the current volume and the recommended volume. If savings estimation mode is on, Compute Optimizer uses your specific discounts. If it's off, Compute Optimizer uses only On-Demand prices. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the *AWS Cost Management User Guide*.

### Estimated monthly savings calculation
<a name="ebs-estimated-monthly-savings-calculation"></a>

For each recommendation, Compute Optimizer calculates the cost to run a new EBS volume with the recommended specs. It bases the monthly savings on two things: how many hours the current volume runs, and the rate difference between the current and recommended specs.

The Compute Optimizer dashboard shows the total monthly savings for all EBS volumes in the account that have a finding of *Not optimized*.

## Performance risk
<a name="ebs-performance-risk"></a>

The performance risk columns on the **EBS volume details** page the **EBS volume recommendations** page define the likelihood of the current and recommended EBS volume not meeting your workload requirements. Compute Optimizer calculates an individual performance risk score for each specification of the EBS volume, including volume type, volume size, baseline IOPS, burst IOPS, baseline throughput, and burst throughput. The performance risk of the current and recommended EBS volume is calculated as the maximum performance risk score across the analyzed resource specifications.

The values range from very low, low, medium, high, and very high. A performance risk of very low means that the EBS volume is predicted to always provide enough capability. The higher the performance risk means that you should validate whether the volume meets the performance requirements of your workload before migrating your resource. Decide whether to optimize for performance improvement, for cost reduction, or for a combination of these two. For more information, see [Requesting modifications to your EBS Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Note**  
If Compute Optimizer doesn’t display a risk value for your current Amazon EBS volume, this means that the volume is predicted to provide enough performance capability and is considered to have a very low performance risk.

## Utilization graphs
<a name="ebs-utilization-graphs"></a>

The **EBS volume details** page displays utilization metric graphs for your current volume. The graphs display data for the analysis period. Compute Optimizer uses the maximum utilization point within each five-minute time interval to generate EBS volume recommendations.

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks. You can also change the statistic of the graphs between average and maximum.

The following utilization graphs are displayed on the details page:


| Graph name | Description | 
| --- | --- | 
| Read operations (per second) | The completed read operations per second for the current EBS volume.<br />For Xen instances, data is reported only when there is read activity on the volume. | 
| Write operations (per second) | The completed write operations per second to the current EBS volume.<br />For Xen instances, data is reported only when there is write activity on the volume. | 
| Read bandwidth (KiB/second) | The read kibibytes (KiB) per second from the current EBS volume. | 
| Write bandwidth (KiB/second) | The written kibibytes (KiB) per second to the current EBS volume. | 
| Burst balance (percent) | The percentage of I/O credits remaining in the burst bucket for the current EBS volume.<br />This metric is displayed only for General Purpose SSD (`gp2`) volumes in the Compute Optimizer console. | 
| IOPS exceeded check | Reports whether an application consistently attempted to drive IOPS that exceeds the volume's provisioned IOPS performance within the last minute. This metric can be either 0 (provisioned IOPS not exceeded) or 1 (provisioned IOPS exceeded). | 
| Throughput exceeded check | Reports whether an application consistently attempted to drive throughput that exceeds the volume's provisioned throughput performance within the last minute. This metric can be either 0 (provisioned throughput not exceeded) or 1 (provisioned throughput exceeded). | 

The **IOPS exceeded check** and **Throughput exceeded check** metrics work for all volume types except magnetic (standard). The volume must be attached to a Nitro instance. These metrics don't work with Multi-Attach volumes. They aren't published for volumes attached to Amazon ECS and Fargate tasks.