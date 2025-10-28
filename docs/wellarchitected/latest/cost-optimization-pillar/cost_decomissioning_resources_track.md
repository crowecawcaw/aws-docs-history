# COST04-BP01 Track resources over their lifetime

Define and implement a method to track resources and their
associations with systems over their lifetime. You can use tagging
to identify the workload or function of the resource.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Decommission workload resources that are no longer required. A common example is resources
used for testing: after testing has been completed, the resources can be removed. Tracking
resources with tags (and running reports on those tags) can help you identify assets for
decommission, as they will not be in use or the license on them will expire. Using tags is an effective way to track resources, by labeling the resource with
its function, or a known date when it can be decommissioned. Reporting can then be run on
these tags. Example values for feature tagging are `feature-X testing` to identify the purpose
of the resource in terms of the workload lifecycle. Another example is using `LifeSpan` or `TTL` for the resources,
such as to-be-deleted tag key name and value to define the time period or specific time for decommissioning.

**Implementation steps**

- **Implement a tagging scheme:** Implement a tagging
  scheme that identifies the workload the resource belongs to, verifying that all resources
  within the workload are tagged accordingly. Tagging helps you categorize resources by purpose,
  team, environment, or other criteria relevant to your business. For more detail on tagging
  uses cases, strategies, and techniques, see [AWS Tagging Best Practices](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").
- **Implement workload throughput or output monitoring:** Implement workload throughput monitoring or alarming, initiating on either
  input requests or output completions. Configure it to provide notifications when workload
  requests or outputs drop to zero, indicating the workload resources are no longer used.
  Incorporate a time factor if the workload periodically drops to zero under normal
  conditions. For more detail on unused or underutilized resources, see
  [AWS Trusted Advisor Cost Optimization checks](../../../awssupport/latest/user/cost-optimization-checks.md "../../../awssupport/latest/user/cost-optimization-checks.md").
- **Group AWS resources:** Create groups for AWS resources.
  You can use [AWS Resource Groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") to organize and manage your AWS resources that are in the
  same AWS Region. You can add tags to most of your resources to help identify and sort your
  resources within your organization. Use [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") add tags to supported resources in bulk.
  Consider using [AWS Service Catalog](../../../servicecatalog/index.md "../../../servicecatalog/index.md") to create, manage, and distribute portfolios of approved
  products to end users and manage the product lifecycle.

## Resources

**Related documents:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/ "https://aws.amazon.com/premiumsupport/trustedadvisor/")
- [AWS Trusted Advisor Cost Optimization Checks](../../../awssupport/latest/user/cost-optimization-checks.md "../../../awssupport/latest/user/cost-optimization-checks.md")
- [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
- [Publishing
  Custom Metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")

**Related videos:**

- [How to optimize costs using AWS Trusted Advisor](https://youtu.be/zcQPufNFhgg "https://youtu.be/zcQPufNFhgg")

**Related examples:**

- [Organize AWS resources](https://aws.amazon.com/premiumsupport/knowledge-center/resource-groups/ "https://aws.amazon.com/premiumsupport/knowledge-center/resource-groups/")
- [Optimize cost using AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/knowledge-center/trusted-advisor-cost-optimization/ "https://aws.amazon.com/premiumsupport/knowledge-center/trusted-advisor-cost-optimization/")
