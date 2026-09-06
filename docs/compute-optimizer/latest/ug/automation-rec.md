

# Recommended actions
<a name="automation-rec"></a>

Recommended actions are optimization opportunities that you can implement through Compute Optimizer. They are a subset of Compute Optimizer's recommendations. You can view and apply each recommended action directly or create automation rules to implement them on a recurring schedule when they match your specified criteria.

## Recommended actions summary
<a name="automation-rec-view-summary"></a>

This section of the Recommended actions page summarizes the estimated monthly savings for your selected recommended actions and the total opportunity available based on your filters. You can select and apply up to 10 actions at a time.

## Recommended action types
<a name="automation-rec-view-type"></a>

In the recommended actions table, you will find a list of optimization opportunities. The following recommended action types are supported:
+ Snapshot and delete unattached EBS volumes: This action is recommended for volumes unattached from EC2 instances for 32 or more days. Compute Optimizer creates a snapshot to back up your data before deleting the volume. For more information about this recommendation criteria, see [Idle criteria per resource](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html#idle-criteria).
+ Upgrade EBS volume type: This action is recommended for volumes using previous generation volume types. Upgrading to newer generation volume types, such as gp3 and io2, provides better performance and cost efficiency with improved IOPS and throughput capabilities at lower prices. 

There are several considerations when applying recommended actions:
+ The estimated monthly savings considers the snapshot cost based on the volume's provisioned size. Actual snapshot cost depends on the incremental EBS snapshot size. 
+ When Compute Optimizer implements recommended actions that involve creating EBS snapshots, it automatically applies an AWS-generated tag to each snapshot. The tag key is `aws:compute-optimizer:automation-event-id`, and its value contains the unique identifier of the corresponding automation event. Compute Optimizer applies this tag to EBS snapshots created on or after February 24, 2026.
+ Amazon EBS supports up to four Elastic Volumes modifications per volume within a rolling 24-hour period. Volume modifications applied through Compute Optimizer count toward this limit. After Compute Optimizer completes a volume modification, you can initiate additional modifications as long as the total number of modifications remains within the limit. For more information, see the [Amazon EBS User Guide](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html).
+ Snapshot and delete unattached EBS volumes does not modify resource properties. A later deployment cannot silently reset an optimized property value. If the volume is declared in an infrastructure-as-code (IaC) template (for example, a CloudFormation stack or a Terraform configuration), the IaC tool reports drift after the deletion. Remove the resource definition from your template to reconcile the state.

## Estimated monthly savings
<a name="automation-rec-savings"></a>

**Estimated monthly savings (after discounts)**

This column in the recommended actions table displays the estimated monthly savings from implementing the recommended action. If you have savings estimation mode enabled, the estimated monthly savings include your specific discounts. To receive recommended actions that include your specific discounts, enable the savings estimation mode preference. For more information, see Savings estimation mode.

**Note**  
If you don't enable the savings estimation mode preference, this column displays estimated monthly savings based on On-Demand pricing.

**Estimated monthly savings (On-Demand)**

This column in the recommended actions table displays the estimated monthly savings from implementing the recommended action. The estimated monthly savings calculation is based on On-Demand pricing.