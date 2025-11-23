# Recommended actions

Recommended actions are optimization opportunities that you can implement through Compute Optimizer. They are a subset of Compute Optimizer's recommendations. You can view and apply each recommended action directly or create automation rules to implement them on a recurring schedule when they match your specified criteria.

## Recommended actions summary

This section of the Recommended actions page summarizes the estimated monthly savings for your selected recommended actions and the total opportunity available based on your filters. You can select and apply up to 10 actions at a time.

## Recommended action types

In the recommended actions table, you will find a list of optimization opportunities. The following recommended action types are supported:

- Snapshot and delete unattached EBS volumes: This action is recommended for volumes unattached from EC2 instances for 32 or more days. Compute Optimizer creates a snapshot to back up your data before deleting the volume. For more information about this recommendation criteria, see [Idle criteria per resource](view-idle-recommendations.md#idle-criteria "view-idle-recommendations.md#idle-criteria").
- Upgrade EBS volume type: This action is recommended for volumes using previous generation volume types. Upgrading to newer generation volume types, such as gp3 and io2, provides better performance and cost efficiency with improved IOPS and throughput capabilities at lower prices.

There are several considerations when applying recommended actions:

- The estimated monthly savings considers the snapshot cost based on the volume's provisioned size. Actual snapshot cost depends on the incremental EBS snapshot size.
- After Compute Optimizer modifies an Amazon EBS volume, you must wait at least six hours and ensure that the volume is in the 'in-use' or 'available' state before you can modify the same volume. For more information, see the [Amazon EBS User Guide](../../../ebs/latest/userguide/ebs-modify-volume.md#elastic-volumes-considerations "../../../ebs/latest/userguide/ebs-modify-volume.md#elastic-volumes-considerations").

## Estimated monthly savings

**Estimated monthly savings (after discounts)**

This column in the recommended actions table displays the estimated monthly savings from implementing the recommended action. If you have savings estimation mode enabled, the estimated monthly savings include your specific discounts. To receive recommended actions that include your specific discounts, enable the savings estimation mode preference. For more information, see Savings estimation mode.

###### Note

If you don't enable the savings estimation mode preference, this column displays estimated monthly savings based on On-Demand pricing.

**Estimated monthly savings (On-Demand)**

This column in the recommended actions table displays the estimated monthly savings from implementing the recommended action. The estimated monthly savings calculation is based on On-Demand pricing.
