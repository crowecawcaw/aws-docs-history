

# Split line item details
<a name="split-line-item-columns"></a>

Columns under the **splitLineItem** header in AWS Cost and Usage Reports are fields that appear in Cost and Usage Reports if you've opted in to the split cost allocation data feature. For more information, see [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html). The feature is limited to Amazon ECS (including Fargate), AWS Batch, and Amazon EKS only.

[A](#sli-A) \| B \| C \| D \| E \| F \| G \| H \| I \| J \| K \| L \| M \| [N](#sli-N) \| O \| [P](#sli-P) \| Q \| [R](#sli-R) \| [S](#sli-S) \| T \| [U](#sli-U) \| V \| W \| X \| Y \| Z

## A
<a name="splitLineitem-details-A"></a>

### splitLineItem/ActualUsage
<a name="splitLineitem-details-A-ActualUsage"></a>
+ **Description:** The usage for vCPU or memory (based on lineItem/UsageType) you incurred for the specified time period for the Amazon ECS task or Kubernetes pod.
+ **Line items applicable:** Usage
+ **Sample values:** 0.1, 0.5, 1.3
+ **Services:** Amazon ECS, Fargate, Amazon EKS

**Note**  
Fargate costs are calculated based on vCPU and memory reservations and reflected in the lineItem/UsageAmount column. Split cost allocation data computes actual Fargate vCPU and memory usage by observing low latency telemetry data and then aggregating it to the hour, day, and month. Therefore splitLineItem/ActualUsage might not be the same as lineItem/UsageAmount.

## N
<a name="splitLineitem-details-N"></a>

### splitLineItem/NetSplitCost
<a name="splitLineitem-details-N-NetSplitCost"></a>
+ **Description:** The effective cost for Amazon ECS tasks or Kubernetes pods after all discounts have been applied. This column is included in your report only when your account has a discount in the applicable billing period.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

### splitLineItem/NetUnusedCost
<a name="splitLineitem-details-N-NetUnusedCost"></a>
+ **Description:** The effective unused cost for Amazon ECS tasks or Kubernetes pods after all discounts have been applied. This column is included in your report only when your account has a discount in the applicable billing period.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

**Note**  
Unused costs are proportionately applied to the Amazon ECS task or Kubernetes pod based on splitLineItem/SplitUsage.

## P
<a name="splitLineitem-details-P"></a>

### splitLineItem/ParentResourceId
<a name="splitLineitem-details-P-ParentResourceId"></a>
+ **Description:** The resource ID of the parent EC2 instance associated with the Amazon ECS task or Amazon EKS pod (referenced in the lineItem/ResourceId column). The parent resource ID implies that the ECS task or Kubernetes pod workload for the specified time period ran on the parent EC2 instance. This applies only for Amazon ECS tasks or Kubernetes pods with EC2 launch type.
+ **Line items applicable:** Usage
+ **Services:** Amazon ECS, Amazon EKS

**Note**  
splitLineItem/ParentResourceId is available only when resource IDs are included in AWS Cost and Usage Reports.

### splitLineItem/PublicOnDemandSplitCost
<a name="splitLineitem-details-P-PublicOnDemandSplitCost"></a>
+ **Description:** The cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task or Kubernetes pod based on public On-Demand Instance rates (referenced in the pricing/publicOnDemandRate column).
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

### splitLineItem/PublicOnDemandUnusedCost
<a name="splitLineitem-details-P-PublicOnDemandUnusedCost"></a>
+ **Description:** The unused cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task or Kubernetes pod based on public On-Demand Instance rates. Unused costs are costs associated with resources (CPU or memory) on the EC2 instance (referenced in the splitLineItem/ParentResourceIdcolumn) that were not utilized for the specified time period.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

## R
<a name="splitLineitem-details-R"></a>

### splitLineItem/ReservedUsage
<a name="splitLineitem-details-R-ReservedUsage"></a>
+ **Description:** The usage for vCPU or memory (based on lineItem/UsageType) that you configured for the specified time period for the Amazon ECS task or Kubernetes pod.
+ **Line items applicable:** Usage
+ **Sample values:** 1, 2, 4
+ **Services:** Amazon ECS, Fargate, Amazon EKS

## S
<a name="splitLineitem-details-S"></a>

### splitLineItem/SplitCost
<a name="splitLineitem-details-S-SplitCost"></a>
+ **Description:** The cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task or Kubernetes pod. This includes amortized costs if the EC2 instance (referenced in the splitLineItem/parentResourceId column) has upfront or partial upfront charges for reservations or Savings Plans.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

### splitLineItem/SplitUsage
<a name="splitLineitem-details-S-SplitUsage"></a>
+ **Description:** The usage for vCPU or memory (based on lineItem/UsageType) allocated for the specified time period to the Amazon ECS task or Kubernetes pod. This is defined as the maximum usage of splitLineItem/ReservedUsage or splitLineItem/ActualUsage.
+ **Line items applicable:** Usage
+ **Sample values:** 1, 1.3
+ **Services:** Amazon ECS, Fargate, Amazon EKS

### splitLineItem/SplitUsageRatio
<a name="splitLineitem-details-S-SplitUsageRatio"></a>
+ **Description:** The ratio of vCPU or memory (based on lineItem/UsageType) allocated to the Amazon ECS task or Kubernetes pod compared to the overall CPU or memory available on the EC2 instance (referenced in the splitLineItem/ParentResourceId column).
+ **Line items applicable:** Usage
+ **Sample values:** 0.25, 0.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

**Note**  
splitLineItem/SplitUsageRatio is only available for AWS Cost and Usage Reports with a time granularity preference of hourly data.

## U
<a name="splitLineitem-details-U"></a>

### splitLineItem/UnusedCost
<a name="splitLineitem-details-U-UnusedCost"></a>
+ **Description:** The unused cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task or Kubernetes pod. Unused costs are costs associated with resources (CPU or memory) on the EC2 instance (referenced in the splitLineItem/ParentResourceId column) that were not utilized for the specified time period. This includes amortized costs if the EC2 instance (splitLineItem/parentResourceId) has upfront or partial upfront charges for reservations or Savings Plans.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS

**Note**  
Unused costs are proportionately applied to the Amazon ECS task or Kubernetes pod based on splitLineItem/SplitUsage.