

# Rightsizing recommendation preferences
<a name="rightsizing-preferences"></a>

With rightsizing recommendation preferences, you can customize the settings that Compute Optimizer uses to generate your recommendations. These preferences apply to your Amazon EC2, EC2 Auto Scaling group, Amazon EBS volumes, Amazon ECS service, and Aurora and Amazon RDS database recommendations. You can do the following:
+ Adjust both the headroom and threshold of your CPU utilization
+ Adjust the headroom of your memory utilization
+ Configure a specific lookback period option
+ Set instance family preferences at the organization, account, or regional level 

These preferences give you greater transparency into how your recommendations are generated. You can also configure rightsizing recommendations to increase savings or performance sensitivity. For instructions on how to set your rightsizing recommendation preferences in AWS Compute Optimizer, see [Setting your rightsizing recommendation preferences](rightsizing-preferences-process.md).

You can be the account manager or the delegated administrator of an AWS Organization. In that case, you can choose the account or organization that the preferences apply to. If you're an individual AWS account holder (not within an organization), the preferences you set apply only to your recommendations.

**Note**  
The rightsizing preferences for CPU and memory utilization are available only for Amazon EC2 instances.
For Amazon RDS DB instances, Amazon EBS volumes, and Amazon ECS services, you can specify only lookback period preferences.

## Preferred EC2 instances
<a name="rightsizing-preferences-preferred-resources"></a>

With rightsizing recommendation preferences, you can specify the EC2 instances you want in your recommendation output. You can define a custom instance consideration set. This set controls the instance types and families that Compute Optimizer recommends for migration. It ensures that Compute Optimizer recommends only instances aligned with your requirements. It doesn't prevent Compute Optimizer from generating recommendations for any of your workloads.

You can customize your instance type selection based on your organizational guidelines or requirements. For example, if you have purchased Savings Plans and Reserved Instances, you can specify only instances covered by those pricing models. Or, if you want to use only instances equipped with certain processors or non-burstable instances because of your application design, you can specify those instances for your recommendation output.

You can also choose to automatically consider future variations of your chosen instance families. By keeping your preferences on the latest version of your preferred families, you can get the best price-to-performance ratio. For instructions on how to specify your preferred EC2 instances, see [Step 3: Specify preferred EC2 instances](rightsizing-preferences-process.md#rightsizing-preferences-preferred-resources-process) in the next section of this user guide.

**Note**  
We recommend that you avoid limiting instance candidates too much. This can reduce your potential savings and rightsizing opportunities.

## Lookback period and metrics
<a name="rightsizing-preferences-lookback-metrics"></a>

With rightsizing recommendation preferences, you can specify the lookback period and the CPU and memory utilization preferences that Compute Optimizer uses for your custom recommendations. For instructions on how to set your lookback period and metrics utilization, see [Step 4: Specify lookback period and metrics](rightsizing-preferences-process.md#rightsizing-preferences-lookback-metrics-process) in the next section of this user guide.

**Topics**
+ [Lookback period](#rightsizing-preferences-lookback)
+ [CPU and memory utilization](#rightsizing-preferences-metrics)

### Lookback period
<a name="rightsizing-preferences-lookback"></a>

Choose a metric analysis lookback period for your rightsizing recommendation preferences. Compute Optimizer analyzes your utilization preference settings for the number of days that you specify. We recommend that you set a lookback period that captures critical signals from your workload utilization history. This can allow Compute Optimizer to identify rightsizing opportunities with higher savings and lower performance risk.

In Compute Optimizer, you can choose from the following lookback period options: 14 days (default), 32 days, or 93 days. The 14-day and 32-day lookback periods require no additional payments. If you have monthly cycles, the 32-day lookback period can capture monthly workload patterns. The 93-day lookback period requires additional payment. To use the 93-day option, you need to enable the enhanced infrastructure metrics preference. For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md).

**Note**  
For Amazon RDS DB instances, you can specify only lookback period preferences.

### CPU and memory utilization
<a name="rightsizing-preferences-metrics"></a>

With rightsizing recommendation preferences, you can customize your utilization settings: CPU threshold, CPU headroom, and memory headroom. These settings help your instance recommendations meet your workload requirements. Depending on the settings you choose, your recommendations can target more savings, more performance headroom, or a higher tolerance for performance risk.

#### CPU utilization threshold
<a name="rightsizing-preferences-metrics-threshold"></a>

The threshold represents the percentile value that Compute Optimizer uses to process utilization data before it generates recommendations. A percentile is the value below which a given percentage of your data points fall. If you set a CPU threshold preference, Compute Optimizer removes the peak usage data points above this threshold. A lower percentile value removes more peak usage from the data. 

Compute Optimizer offers three options for CPU utilization threshold: P90, P95, and P99.5. By default, Compute Optimizer uses a P99.5 threshold for its rightsizing recommendations. This means that Compute Optimizer ignores only the top 0.5% of the highest utilization data points from your utilization history. The P99.5 threshold might be more suited for highly sensitive production workloads where peak utilization significantly affects application performance. If you set the utilization threshold to P90, Compute Optimizer ignores the top 10% of your highest data points from your utilization history. P90 might be a suitable threshold for workloads less sensitive to peak utilization, such as non-production environments.

#### CPU utilization headroom
<a name="rightsizing-preferences-metrics-headroom"></a>

Utilization headroom adds CPU capacity to the Compute Optimizer recommendation. It accounts for future increases in CPU utilization. It represents the gap between the instance's current usage and its maximum capabilities. 

Compute Optimizer provides three options for CPU utilization headroom: 30%, 20%, and 0%. By default, Compute Optimizer uses a 20% headroom. If you need additional capacity for unexpected future increases, set the headroom to 30%. If your utilization is expected to stay constant, you can reduce the headroom. This generates recommendations with less added CPU capacity and more cost savings.

#### Memory utilization headroom
<a name="rightsizing-preferences-metrics-memory-headroom"></a>

Memory utilization headroom adds memory capacity to the Compute Optimizer recommendation. It accounts for future increases in memory utilization. It represents the gap between the instance's current usage and its maximum capabilities. Compute Optimizer provides three options for memory utilization headroom: 30%, 20%, and 10%. By default, Compute Optimizer uses a 20% headroom. If you need additional capacity for unexpected future increases, set the headroom to 30%. If your usage is expected to stay constant, you can reduce the headroom. This generates recommendations with less added memory capacity and more cost savings. 

**Note**  
To receive EC2 instance recommendations that consider the memory utilization metric, you need to enable memory utilization with the CloudWatch agent. You can also configure Compute Optimizer to ingest EC2 memory utilization metrics from your preferred observability product. For more information, see [Enabling memory utilization with the CloudWatch agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) and [ Configure external metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html#configure-external-metrics-ingestion).

#### Utilization presets
<a name="rightsizing-preferences-metrics-presets"></a>

Compute Optimizer provides four preset options for CPU and memory utilization. The following table lists the CPU threshold, CPU headroom, and memory headroom for each preset.


| Preset | CPU threshold | CPU headroom | Memory headroom | 
| --- | --- | --- | --- | 
| Maximum savings | P90 | 0% | 10% | 
| Balanced | P95 | 30% | 30% | 
| Default | P99.5 | 20% | 20% | 
| Maximum performance | P99.5 | 30% | 30% | 

**Maximum savings** adds no CPU capacity and reserves the lowest memory capacity for future growth. It removes the top 10% of the highest data points from your CPU utilization history. This preset might generate recommendations with higher latency or greater degradation risk.

**Balanced** targets CPU utilization below 70% for more than 95% of the time, and memory utilization below 70%. It suits most workloads and can identify more savings opportunities than the default. If your workloads aren't sensitive to CPU or memory utilization spikes, it is a good alternative to the default.

**Default** generates recommendations for all EC2 instances. It targets CPU utilization below 80% for more than 99.5% of the time, and memory utilization below 80%. This provides a very low risk of performance issues but might limit savings opportunities.

**Maximum performance** provides high performance sensitivity. It adds capacity for future increases in CPU and memory usage.

**Note**  
Compute Optimizer might update these threshold and headroom values to reflect the latest technological updates and maintain recommendation quality. Compute Optimizer might adjust your chosen parameters based on your workload characteristics to ensure suitable instance recommendations for you.

You can use the simulated graphs in the console to see how your CPU and memory utilization interacts with the threshold and headroom settings. The graph plots the utilization of an example workload over the lookback period, and marks the threshold and headroom values that you set on the same axes. As you adjust the headroom and threshold, the graph updates to show how those values change the data that Compute Optimizer uses to generate recommendations.

![CPU and memory usage graph](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-graph.png)


**Important**  
The data shown in the simulated graph is representative and for illustrative purposes only. The graph isn't based on your utilization data.

## Next steps
<a name="rightsizing-preferences-next-steps"></a>

For instructions on how to set your rightsizing recommendation preferences in AWS Compute Optimizer, see [Setting your rightsizing recommendation preferences](rightsizing-preferences-process.md).