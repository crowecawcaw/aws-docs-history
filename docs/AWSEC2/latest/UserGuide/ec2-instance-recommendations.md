# Get EC2 instance recommendations from Compute Optimizer

AWS Compute Optimizer provides Amazon EC2 recommendations to help you improve performance, save
money, or both. You can use these recommendations to decide whether to change to a new instance
type.

To make recommendations, Compute Optimizer analyzes your existing instance specifications and utilization
metrics. The compiled data is then used to recommend which Amazon EC2 instance types are best able to
handle the existing workload. Recommendations are returned along with per-hour instance
pricing. For more information, see [Amazon EC2
instance metrics](../../../compute-optimizer/latest/ug/metrics.md#ec2-metrics-analyzed "../../../compute-optimizer/latest/ug/metrics.md#ec2-metrics-analyzed") in the _AWS Compute Optimizer User Guide_.

###### Contents

- [Requirements](#compute-optimizer-limitations "#compute-optimizer-limitations")
- [Finding classifications](#findings-classifications "#findings-classifications")
- [View recommendations](#viewing-recommendations "#viewing-recommendations")
- [Considerations for evaluating recommendations](#considerations "#considerations")

## Requirements

To get recommendations from Compute Optimizer, you must first opt in to Compute Optimizer. For more information, see
[Getting started with AWS Compute Optimizer](../../../compute-optimizer/latest/ug/getting-started.md "../../../compute-optimizer/latest/ug/getting-started.md") in the
_AWS Compute Optimizer User Guide_.

Compute Optimizer generates recommendations for some instance types, but not all instance types.
If you're using an unsupported instance type, Compute Optimizer will not generate recommendations.
For the list of supported instance types, see [Amazon EC2
instance requirements](../../../compute-optimizer/latest/ug/requirements.md#requirements-ec2-instances "../../../compute-optimizer/latest/ug/requirements.md#requirements-ec2-instances") in the _AWS Compute Optimizer User Guide_.

## Finding classifications

Compute Optimizer classifies its findings for EC2 instances as follows:

- **Under-provisioned** – An EC2 instance is considered
  under-provisioned when at least one specification of your instance, such as CPU, memory,
  or network, does not meet the performance requirements of your workload. Under-provisioned
  EC2 instances might lead to poor application performance.
- **Over-provisioned** – An EC2 instance is considered
  over-provisioned when at least one specification of your instance, such as CPU, memory, or
  network, can be sized down while still meeting the performance requirements of your
  workload, and when no specification is under-provisioned. Over-provisioned EC2 instances
  might lead to unnecessary infrastructure cost.
- **Optimized** – An EC2 instance is considered optimized when
  all specifications of your instance, such as CPU, memory, and network, meet the
  performance requirements of your workload, and the instance is not over-provisioned. An
  optimized EC2 instance runs your workloads with optimal performance and infrastructure
  cost. For optimized instances, Compute Optimizer might sometimes recommend a new generation instance
  type.
- **None** – There are no recommendations for this instance.
  This might occur if you've been opted in to Compute Optimizer for less than 12 hours, or when the
  instance has been running for less than 30 hours, or when the instance type is not
  supported by Compute Optimizer.

## View recommendations

After you opt in to Compute Optimizer, you can view the findings that Compute Optimizer generates for your EC2
instances in the Amazon EC2 console. You can then access the Compute Optimizer console to view the
recommendations. If you recently opted in, findings might not be reflected in the EC2 console
for up to 12 hours.

###### To view recommendations for an instance using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Choose the instance ID to open the instance detail page.
4. On the instance detail page, in the top summary section, locate **AWS Compute Optimizer
   finding**. If there is a finding, we display the finding classification and a
   link to view the details. Otherwise, we display **No recommendations available for
   this instance.**
5. If there is a finding, choose **View detail**. This opens the
   **Recommendations for EC2 instances** page in the Compute Optimizer console. The current
   instance type is labeled **Current**. There are also up to three instance
   type recommendations, labeled **Option 1**, **Option 2**,
   and **Option 3**. This page also shows recent CloudWatch metric data for the
   instance.

###### To view recommendations for all instances in all Regions

You can view recommendations for all of your Amazon EC2 instances in all Regions using
the Compute Optimizer console. For more information, see [Viewing EC2 instances recommendations](../../../compute-optimizer/latest/ug/view-ec2-recommendations.md#ec2-view-recommendations "../../../compute-optimizer/latest/ug/view-ec2-recommendations.md#ec2-view-recommendations") and [Viewing EC2 instance details](../../../compute-optimizer/latest/ug/view-ec2-recommendations.md#ec2-viewing-details "../../../compute-optimizer/latest/ug/view-ec2-recommendations.md#ec2-viewing-details") in the _AWS Compute Optimizer User Guide_.

## Considerations for evaluating recommendations

When you receive a recommendation, you must decide whether to act on it.
Before changing an instance type, consider the following:

- The recommendations don’t forecast your usage. Recommendations are based on your
  historical usage over the most recent 14-day time period. Be sure to choose an instance
  type that is expected to meet your future resource needs.
- Focus on the graphed metrics to determine whether actual usage is lower than instance
  capacity. You can also view metric data (average, peak, percentile) in CloudWatch to further
  evaluate your EC2 instance recommendations. For example, notice how CPU percentage metrics
  change during the day and whether there are peaks that need to be accommodated. For more
  information, see [Viewing
  Available Metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md") in the _Amazon CloudWatch User Guide_.
- Compute Optimizer might supply recommendations for burstable performance instances, which are T3,
  T3a, and T2 instances. If you periodically burst above the baseline, make sure that you
  can continue to do so based on the vCPUs of the new instance type. For more information,
  see [Key concepts for burstable
  performance instances](burstable-credits-baseline-concepts.md "burstable-credits-baseline-concepts.md").
- If you’ve purchased a Reserved Instance, your On-Demand Instance might be billed as a Reserved Instance. Before you change
  your current instance type, first evaluate the impact on Reserved Instance utilization and
  coverage.
- Consider conversions to newer generation instances, where possible.
- When migrating to a different instance family, make sure the current instance type and
  the new instance type are compatible, for example, in terms of virtualization,
  architecture, or network type. For more information, see [Compatibility for changing the instance type](resize-limitations.md "resize-limitations.md").
- Finally, consider the performance risk rating that's provided for each recommendation.
  Performance risk indicates the amount of effort you might need to spend in order to
  validate whether the recommended instance type meets the performance requirements of your
  workload. We also recommend rigorous load and performance testing before and after making
  any changes.
