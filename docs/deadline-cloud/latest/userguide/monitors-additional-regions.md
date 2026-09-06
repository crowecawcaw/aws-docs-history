

# Monitors and farms in multiple Regions
<a name="monitors-additional-regions"></a>

The Deadline Cloud monitor displays farms from all AWS Regions where AWS Deadline Cloud (Deadline Cloud) is available. When you open the monitor, you see farms in the same Region as the monitor and farms in other Regions that do not use a customer managed key. In most cases, a single monitor is all you need, even if you have farms in multiple Regions.

## Managing users across Regions
<a name="monitors-add-users-cross-region"></a>

You can add users and groups to farms in any Region from the Deadline Cloud console. The console handles cross-Region AWS IAM Identity Center (IAM Identity Center) membership assignment. Your IAM Identity Center instance doesn't need to be in the same Region as the farm: a membership references the IAM Identity Center user or group by its identifier, so you can assign the same users and groups to farms in any Region. If you assign memberships with the API or the AWS CLI, for example with `AssociateMemberToQueue`, send the request to the Region that contains the farm. For more information about managing farm membership, see [Managing users in Deadline Cloud](managing-users.md).

## When to create additional monitors
<a name="monitors-when-multiple"></a>

Because a single monitor shows farms in all Regions, you typically need only one monitor. You might want additional monitors in the following situations:
+ **Customer managed keys in multiple Regions** – A monitor cannot display farms in other Regions that use a customer managed key. If you have farms with customer managed keys in multiple Regions, you need a monitor in each of those Regions.
+ **Regional availability** – You want all Deadline Cloud resources, including the monitor, IAM Identity Center instance, and farms, to remain within a single Region. This configuration ensures that an outage in one Region does not affect your ability to manage resources in another Region.
+ **Multiple IAM Identity Center instances** – Each monitor connects to one IAM Identity Center instance. If your organization uses separate IAM Identity Center instances for different teams or business units, you need a monitor for each instance.

The following diagram and table compare the two approaches for connecting additional monitors to your IAM Identity Center instance across Regions.

## Comparison of multi-monitor approaches
<a name="monitors-multi-region-comparison"></a>

![Diagram comparing cross-Region IAM Identity Center access and IAM Identity Center multi-Region replication for Deadline Cloud monitors.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitors-additional-regions.png)



**Comparison of multi-monitor approaches**  

| Consideration | Cross-Region IAM Identity Center access | IAM Identity Center multi-Region replication | 
| --- | --- | --- | 
| Setup requirements | No additional IAM Identity Center setup required | Requires configuring IAM Identity Center replication | 
| Identity data location | Remains in the IAM Identity Center Region only | Replicated to each configured Region | 
| Latency | Depends on distance to the IAM Identity Center Region | Lower latency when an IAM Identity Center replica is in the same Region | 
| Regional availability | Depends on IAM Identity Center Region availability | Continues to work if the IAM Identity Center primary Region is unavailable | 

## Cross-Region IAM Identity Center access
<a name="create-monitor-cross-region-access"></a>

With cross-Region IAM Identity Center access, you create an Deadline Cloud monitor in a different Region than your IAM Identity Center instance. Deadline Cloud reads IAM Identity Center identity data from the Region where your IAM Identity Center instance is located.

When you create a monitor using the Deadline Cloud console, the console automatically detects your IAM Identity Center instance and connects the monitor to it, even if the instance is in a different Region. When you create a monitor using an AWS SDK, specify the Region where your IAM Identity Center instance is located.

### Considerations
<a name="cross-region-considerations"></a>
+ Cross-Region IAM Identity Center access requires your IAM Identity Center instance to be in a commercial AWS Region. IAM Identity Center instances in opt-in Regions aren't supported.
+ You can't change the IAM Identity Center Region after you create the monitor.

## IAM Identity Center multi-Region replication
<a name="create-monitor-multi-region-replication"></a>

IAM Identity Center multi-Region replication synchronizes your IAM Identity Center identity store data, including users, groups, and group memberships, to additional AWS Regions. After you enable replication to a Region, you can connect your monitor in that Region to the IAM Identity Center replica.

Multi-Region replication is useful in the following scenarios:
+ You need lower latency for users closer to the replicated Region.
+ You need monitors that continue to work if the IAM Identity Center primary Region is unavailable.

To enable multi-Region replication, see [Using IAM Identity Center across multiple AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html) in the *IAM Identity Center User Guide*. After you enable replication for a Region, you can create Deadline Cloud monitors there by using the console or an AWS SDK.