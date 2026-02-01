# DSREL04-BP02 Design adaptive capacity management within

sovereign boundaries

Implement adaptive capacity management strategies that balance
operational resilience with data sovereignty requirements in highly
regulated environments. This approach enables organizations to
automatically scale resources within approved jurisdictional
boundaries while maintaining strict compliance with data residency
regulations.

**Desired outcome:** Workloads scale
automatically to meet demand while maintaining adherence to data
sovereignty requirements. Resources adjust dynamically within
approved geographic boundaries without manual intervention,
optimizing both performance and cost. Automated policies confine
data and compute resources to designated jurisdictions during
scaling events. Each capacity change is logged with compliance
metadata, providing complete audit trails for regulatory review.

**Common anti-patterns:**

- Implementing disaster recovery or auto scaling mechanisms that
  inadvertently move data or compute resources across sovereign
  boundaries without proper governance.
- Over-provisioning resources to handle peak loads rather than
  implementing dynamic scaling within approved regions, leading to
  unnecessary costs.
- Failing to implement comprehensive resource tagging and
  automated compliance checks for sovereignty tracking and policy
  enforcement.
- Making scaling decisions without considering data residency
  requirements or validating AWS service compliance with local
  regulations.
- Relying on manual capacity management instead of automated,
  policy-driven scaling processes that respect compliance
  boundaries.
- Neglecting real-time monitoring and alerting systems for
  tracking sovereignty compliance during scaling events.

**Benefits of establishing this best
practice:**

- Maintains continuous regulatory adherence through automated
  enforcement of data residency and sovereignty requirements
  during scaling operations.
- Optimizes costs by dynamically right-sizing resources based on
  actual demand while maintaining compliance within sovereign
  boundaries.
- Enhances operational resilience through automated scaling and
  distributed capacity across multiple availability zones within
  approved regions.
- Improves incident response through automated scaling mechanisms
  that respect compliance boundaries without manual intervention.
- Provides comprehensive audit readiness through detailed logging
  and monitoring of capacity decisions and their compliance
  impact.
- Reduces compliance risk by systematically blocking unauthorized
  data or resource movement outside approved jurisdictions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing effective capacity management in regulated
environments requires a balanced approach that combines automated
scaling capabilities with strict data sovereignty controls.
Organizations must establish a comprehensive framework that uses
AWS services while enforcing policy-driven governance, so that
capacity adjustments maintain adherence to regulatory requirements
and data residency obligations.

Success depends on creating a robust architecture that integrates
resource tagging, service control policies, and automated scaling
mechanisms with continuous compliance monitoring, enabling
organizations to dynamically adjust capacity while maintaining
strict control over data location and resource boundaries.

This approach not only optimizes operational efficiency but also
demonstrates due diligence in maintaining regulatory adherence,
particularly crucial for organizations operating in highly
regulated industries where data sovereignty violations can result
in significant penalties and loss of trust.

Key implementation elements:

- Identify geographic restrictions for data.
- Select AWS services and Regions certified for sovereignty.
- Implement auto scaling with guardrails for resource limits.
- Track data location and resource configurations.

### Implementation steps

1. Implement a resource tagging strategy to identify data
   classification and sovereignty requirements. Use
   [AWS Resource Groups](../../../ARG/latest/userguide/welcome.md "../../../ARG/latest/userguide/welcome.md") to organize resources by compliance
   scope. Enforce tagging using
   [AWS Organizations Tag Policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") and
   [Service
   Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"). Use
   [AWS CloudFormation Guard rules](../../../cfn-guard/latest/ug/writing-rules.md "../../../cfn-guard/latest/ug/writing-rules.md") to block incorrectly
   tagged resources from being deployed.
2. Create capacity management policies, configure
   [AWS Service Quotas](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") for default limits and quota
   monitoring, and set up resource scheduling for effective
   resource management.
3. Configure
   [AWS Auto Scaling](../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md "../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md") and
   [Application
   Auto Scaling](../../../autoscaling/application/userguide/what-is-application-auto-scaling.md "../../../autoscaling/application/userguide/what-is-application-auto-scaling.md") with scaling policies, resource limits,
   and target tracking. Set up scaling notifications to track
   scale-out and scale-in events.
4. Deploy
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") for custom metrics, dashboards, and
   alarms. Implement
   [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") for logging, and
   [AWS Config
   rules](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") for continuous compliance assessment.
5. Configure
   [AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") for Region-specific keys, key policies, and key
   rotation. Set up data movement controls for data sovereignty
   [by
   constructing data perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/ "https://aws.amazon.com/identity/data-perimeters-on-aws/").

## Resources

**Related best practices:**

- [REL07-BP01
  Use automation when obtaining or scaling resources](../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md "../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md")
- [SUS02-BP01
  Scale workload infrastructure dynamically](../sustainability-pillar/sus_sus_user_a2.md "../sustainability-pillar/sus_sus_user_a2.md")
- [PERF02-BP05
  Scale your compute resources dynamically](../performance-efficiency-pillar/perf_compute_hardware_scale_compute_resources_dynamically.md "../performance-efficiency-pillar/perf_compute_hardware_scale_compute_resources_dynamically.md")

**Related documents:**

- [Data Residency with Hybrid Cloud Services Lens](../data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.md "../data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.md")
- [Performance and capacity management](../../../whitepapers/latest/aws-caf-operations-perspective/performance-and-capacity-management.md "../../../whitepapers/latest/aws-caf-operations-perspective/performance-and-capacity-management.md")
- [Management and Governance Cloud Environment Guide](../management-and-governance-guide/aws-service-management-tools.md "../management-and-governance-guide/aws-service-management-tools.md")

**Related examples:**

- [Capacity
  management](../../../whitepapers/latest/aws-outposts-high-availability-design/capacity-management.md "../../../whitepapers/latest/aws-outposts-high-availability-design/capacity-management.md")
- [Implementing
  and enforcing tagging](../../../whitepapers/latest/tagging-best-practices/implementing-and-enforcing-tagging.md "../../../whitepapers/latest/tagging-best-practices/implementing-and-enforcing-tagging.md")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Application Auto Scaling](https://aws.amazon.com/application-auto-scaling/ "https://aws.amazon.com/application-auto-scaling/")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/")
- [AWS Service Quotas](https://aws.amazon.com/service-quotas/ "https://aws.amazon.com/service-quotas/")
- [AWS Organizations Tag Policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md")
- [Service
  Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md")
