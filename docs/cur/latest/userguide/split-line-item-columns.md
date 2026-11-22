

# Split line item details

Columns under the **splitLineItem** header in AWS Cost and Usage Reports are fields that appear in Cost and Usage Reports if you've opted in to the split cost allocation data feature. For more information, see [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html). Split cost allocation data supports Amazon ECS (including Fargate), AWS Batch, Amazon EKS, AWS PCS, Amazon S3, and networking flexible cost allocation. For networking, it allocates supported NAT gateway, Amazon EC2 instance, and VPC peering connection charges.

[A](#sli-A) \| B \| C \| D \| E \| F \| G \| H \| I \| J \| K \| L \| M \| [N](#sli-N) \| O \| [P](#sli-P) \| Q \| [R](#sli-R) \| [S](#sli-S) \| T \| [U](#sli-U) \| V \| W \| X \| Y \| Z

## A
<a name="splitLineitem-details-A"></a>

### splitLineItem/ActualUsage
<a name="splitLineitem-details-A-ActualUsage"></a>
+ **Description:** The usage for vCPU or memory (based on lineItem/UsageType) you incurred for the specified time period for the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job. For networking, the data attributed to the resource that generated it for the line item's time period. The value uses the usage type's unit, such as GB. On the unattributed line item, this is the usage that couldn't be traced to a resource.
+ **Line items applicable:** Usage
+ **Sample values:** 0.1, 0.5, 1.3
+ **Services:** Amazon ECS, Fargate, Amazon EKS, Amazon VPC, AWS PCS

**Note**  
Fargate costs are calculated based on vCPU and memory reservations and reflected in the lineItem/UsageAmount column. Split cost allocation data computes actual Fargate vCPU and memory usage by observing low latency telemetry data and then aggregating it to the hour, day, and month. Therefore splitLineItem/ActualUsage might not be the same as lineItem/UsageAmount.  
For AWS PCS, costs are based on requested resources only, so splitLineItem/ActualUsage is empty.

## N
<a name="splitLineitem-details-N"></a>

### splitLineItem/NetSplitCost
<a name="splitLineitem-details-N-NetSplitCost"></a>
+ **Description:** The effective cost for Amazon ECS tasks, Kubernetes pods, or AWS PCS Slurm jobs after all discounts have been applied. This column is included in your report only when your account has a discount in the applicable billing period. For networking, the share of the networking resource's charge after discounts that is assigned to the resource that generated usage, or to unattributed usage. For Amazon S3, this is the cost allocated to the prefix after discounts.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, Amazon VPC, AWS PCS, Amazon S3

### splitLineItem/NetUnusedCost
<a name="splitLineitem-details-N-NetUnusedCost"></a>
+ **Description:** The effective unused cost for Amazon ECS tasks, Kubernetes pods, or AWS PCS Slurm jobs after all discounts have been applied. This column is included in your report only when your account has a discount in the applicable billing period.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, AWS PCS

**Note**  
Unused costs are proportionately applied to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job based on splitLineItem/SplitUsage.

## P
<a name="splitLineitem-details-P"></a>

### splitLineItem/ParentResourceId
<a name="splitLineitem-details-P-ParentResourceId"></a>
+ **Description:** The resource ID of the parent resource whose cost is split. For Amazon ECS tasks and Amazon EKS pods with the EC2 launch type, and for all AWS PCS Slurm jobs, this is the EC2 instance that the task, pod, or job ran on. For networking, the resource whose charge is split: the NAT gateway ARN for a NAT gateway's data processing and data transfer charges, or the Amazon EC2 instance ID for an instance's data transfer charges. For Amazon S3, this is the name of the bucket whose charge is allocated.
+ **Line items applicable:** Usage
+ **Services:** Amazon ECS, Amazon EKS, Amazon VPC, AWS PCS, Amazon S3

**Note**  
splitLineItem/ParentResourceId is available only when resource IDs are included in AWS Cost and Usage Reports.

### splitLineItem/PublicOnDemandSplitCost
<a name="splitLineitem-details-P-PublicOnDemandSplitCost"></a>
+ **Description:** The cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job based on public On-Demand Instance rates (referenced in the pricing/publicOnDemandRate column).

  For networking, the share of the networking resource's charge at public On-Demand rates that is assigned to the resource that generated usage, or to unattributed usage.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, Amazon VPC, AWS PCS

### splitLineItem/PublicOnDemandUnusedCost
<a name="splitLineitem-details-P-PublicOnDemandUnusedCost"></a>
+ **Description:** The unused cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job based on public On-Demand Instance rates. Unused costs are costs associated with resources (CPU or memory) on the EC2 instance (referenced in the splitLineItem/ParentResourceIdcolumn) that were not utilized for the specified time period.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, AWS PCS

## R
<a name="splitLineitem-details-R"></a>

### splitLineItem/ReservedUsage
<a name="splitLineitem-details-R-ReservedUsage"></a>
+ **Description:** The usage for vCPU or memory (based on lineItem/UsageType) that you configured for the specified time period for the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job.
+ **Line items applicable:** Usage
+ **Sample values:** 1, 2, 4
+ **Services:** Amazon ECS, Fargate, Amazon EKS, AWS PCS

## S
<a name="splitLineitem-details-S"></a>

### splitLineItem/SplitCost
<a name="splitLineitem-details-S-SplitCost"></a>
+ **Description:** The cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job. This includes amortized costs if the EC2 instance (referenced in the splitLineItem/parentResourceId column) has upfront or partial upfront charges for reservations or Savings Plans. For networking, the share of the networking resource's unblended charge assigned to the resource that generated usage, or to unattributed usage. For Amazon S3, this is the unblended cost allocated to the prefix.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, Amazon VPC, AWS PCS, Amazon S3

### splitLineItem/SplitUsage
<a name="splitLineitem-details-S-SplitUsage"></a>
+ **Description:** The usage for vCPU or memory (based on lineItem/UsageType) allocated for the specified time period to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job. This is defined as the maximum usage of splitLineItem/ReservedUsage or splitLineItem/ActualUsage. For networking, the data attributed to the resource that generated it for the line item's time period. The value uses the usage type's unit, such as GB. Networking has no reserved usage, so the usage charged is the usage that occurred. For Amazon S3, this is the storage in GB-Mo or the number of requests allocated to the prefix.
+ **Line items applicable:** Usage
+ **Sample values:** 1, 1.3
+ **Services:** Amazon ECS, Fargate, Amazon EKS, Amazon VPC, AWS PCS, Amazon S3

### splitLineItem/SplitUsageRatio
<a name="splitLineitem-details-S-SplitUsageRatio"></a>
+ **Description:** The ratio of vCPU or memory (based on lineItem/UsageType) allocated to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job compared to the overall CPU or memory available on the EC2 instance (referenced in the splitLineItem/ParentResourceId column).
+ **Line items applicable:** Usage
+ **Sample values:** 0.25, 0.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, AWS PCS

**Note**  
splitLineItem/SplitUsageRatio is only available for AWS Cost and Usage Reports with a time granularity preference of hourly data.

## U
<a name="splitLineitem-details-U"></a>

### splitLineItem/UnusedCost
<a name="splitLineitem-details-U-UnusedCost"></a>
+ **Description:** The unused cost for vCPU or memory (based on lineItem/UsageType) allocated for the time period to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job. Unused costs are costs associated with resources (CPU or memory) on the EC2 instance (referenced in the splitLineItem/ParentResourceId column) that were not utilized for the specified time period. This includes amortized costs if the EC2 instance (splitLineItem/parentResourceId) has upfront or partial upfront charges for reservations or Savings Plans. For Amazon S3 line items, this column is empty. Usage that matches no prefix is reported on the unattributed line item.
+ **Line items applicable:** Usage
+ **Sample values:** 1.35, 1.75
+ **Services:** Amazon ECS, Fargate, Amazon EKS, AWS PCS

**Note**  
Unused costs are proportionately applied to the Amazon ECS task, Kubernetes pod, or AWS PCS Slurm job based on splitLineItem/SplitUsage.