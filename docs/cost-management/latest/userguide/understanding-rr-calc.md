# Understanding rightsizing recommendations

calculations

This section provides an overview of the savings calculations that are used in your
rightsizing recommendations algorithms.

## Consolidated billing family

To identify all instances for all accounts in the consolidated billing family,
rightsizing recommendations look at the usage for the last 14 days for each account.
If the instance was stopped or terminated, we remove it from consideration. For all
remaining instances, we call CloudWatch to get maximum CPU utilization data, memory
utilization (if enabled), network in/out, local disk input/ output (I/O), and
performance of attached EBS volumes for the last 14 days. This is to produce
conservative recommendations, not to recommend instance modifications that could be
detrimental to application performance or that could unexpectedly impact your
performance.

## Determining if an instance is idle,

underutilized, or neither

We look at the maximum CPU utilization of the instance for the last 14 days to
make one of the following assessments:

- **Idle** – If the maximum CPU utilization is at or
  below 1%. A termination recommendation is generated, and savings are
  calculated. For more information, see [Savings calculation](#savings-calc "#savings-calc").
- **Underutilized** – If the maximum CPU utilization
  is above 1% and cost savings are available in modifying the instance
  type, a modification recommendation is generated.

If the instance isn't idle or underutilized, we don't generate any
recommendations.

## Generating modification recommendations

Recommendations use a machine learning engine to identify the optimal Amazon EC2
instance types for a particular workload. Instance types include those that are a
part of AWS Auto Scaling groups.

The recommendations engine analyzes the configuration and resource usage of a
workload to identify dozens of defining characteristics. For example, it can
determine whether a workload is CPU-intensive or whether it exhibits a daily
pattern. The recommendations engine analyzes these characteristics and identifies
the hardware resources that the workload requires.

Finally, it concludes how the workload would perform on various Amazon EC2 instances to
make recommendations for the optimal AWS compute resources that the specific
workload.

## Savings calculation

We first examine the instance running in the last 14 days to identify whether it
was partially or fully covered by an RI or Savings Plans, or running On-Demand. Another
factor is whether the RI is size-flexible. The cost to run the instance is
calculated based on the On-Demand hours and the rate of the instance type.

For each recommendation, we calculate the cost to operate a new instance. We
assume that a size-flexible RI covers the new instance in the same way as the
previous instance if the new instance is within the same instance family. Estimated
savings are calculated based on the number of On-Demand running hours and the
difference in On-Demand rates. If the RI isn't size-flexible, or if the new instance
is in a different instance family, the estimated savings calculation is based on
whether the new instance had been running during the last 14 days as
On-Demand.

Cost Explorer only provides recommendations with an estimated savings greater
than or equal to $0. These recommendations are a subset of Compute Optimizer results. For more
performance-based recommendations that might result in a cost increase, see [Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/").

You can choose to view saving with or without consideration for RI or Savings Plans
discounts. Recommendations consider both discounts by default. Considering RI or
Savings Plans discounts might result in some recommendations showing a savings value of $0.
To change this option, see [Using your rightsizing recommendations](rr-use.md "rr-use.md").

###### Note

Rightsizing recommendations doesn't capture second-order effects of
rightsizing, such as the resulting RI hour’s availability and how they will
apply to other instances. Potential savings based on reallocation of the RI
hours aren't included in the calculation.
