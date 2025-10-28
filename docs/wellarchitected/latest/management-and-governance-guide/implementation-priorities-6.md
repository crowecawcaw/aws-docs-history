# Implementation priorities

The M&G Guide recommends that you implement your Cloud
Financial Management capabilities with transparency in mind. This
includes enabling your builder teams to see the financial impact
of their cloud usage for the resources they provision, as well as
to define specific controls related to the financial governance of
your resources.

## Enable Cloud Financial Management

Configure detailed information sources including
[Billing
and Cost Management](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md") tools to create the reporting your
organization needs. Regularly review (minimally on a monthly
basis) the cost and usage by different dimensions to understand
cost drivers. Establish organizational metrics, such as a
[unit
metric](https://aws.amazon.com/blogs/aws-cloud-financial-management/what-is-a-unit-metric/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/what-is-a-unit-metric/") to identify cost attribution categories as you
scale. If required, ensure that your cost reporting includes all
costs (labor, licensing, infrastructure, and more) to create the
total cost of application management (TCAM).

## Tag, track, and monitor resource costs across their lifecycle

A consistent and
[well-designed
tagging strategy](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md") is required to manage and track costs
across your AWS environments. Once resources in your environments
are tagged, you must activate both
[AWS-generated
tags](../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md "../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md") and
[user-defined
tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") separately to use them in your cost reporting and
analysis tools. Enforce
[tag
options](../../../servicecatalog/latest/adminguide/tagoptions.md "../../../servicecatalog/latest/adminguide/tagoptions.md") using distribution and preconfigured infrastructure
as code templates for governance. Use
[tag
policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") to enforce and maintain consistent tags across
your organization and resources.

Track resources over their lifetime and design your workloads to
gracefully handle resource termination as you automatically
identify and decommission non-critical or low utilization
resources. Analyze the design, architecture, and all components of
each workload or application for cost effectiveness, including
license costs. Use
[Managed
entitlements](https://aws.amazon.com/blogs/awsmarketplace/how-aws-marketplace-features-help-you-govern-and-manage-software-purchases-for-your-organization/ "https://aws.amazon.com/blogs/awsmarketplace/how-aws-marketplace-features-help-you-govern-and-manage-software-purchases-for-your-organization/") to track and help ensure that you have
compliance with your established agreements while avoiding
unexpected true-up bills for exceeding license limits. Determine
if the component and resources will be running for extended
periods (for commitment discounts), or dynamic and transiently
running (for Spot or On-Demand Instances). Implement the
appropriate
[pricing
models](../../../marketplace/latest/userguide/pricing.md "../../../marketplace/latest/userguide/pricing.md") for all components of your applications sourced from
AWS Marketplace.

## Establish mechanisms for cost governance

Create policies and mechanisms that define how resources are managed by your
organization. The policies should cover cost aspects of resources and workloads, including
creation, modification, and decommissioning over the resource lifetime. Create an
obsolescence plan and defined retention period with lifecycle policies for resources as they
are provisioned. Implement account structure, groups, and roles to help allocate costs and
control who can create, modify, or decommission instances and resources in each group.
Identify any new controls that could support a more efficient cost spend. Update your
distribution of infrastructure as code templates in [Service Catalog](https://aws.amazon.com/servicecatalog/features/ "https://aws.amazon.com/servicecatalog/features/") so that cost is transparent and only approved
instance sizes are available in a self-service manner across your multi-account framework.
Enforce tagging of resources as they are provisioned to ensure effective cost governance.

## Continually optimize for cost efficiency

Review historic spend patterns to detect cost spikes (one-time or
recurring) or continual cost increases, assuming 14–30 days of
historical spend. Implement mechanisms to periodically identify
and
[right-size
instances based on current workload metrics](../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md "../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md") and
characteristics. This can be evaluated using AWS Cost Explorer,
AWS Trusted Advisor, and AWS Compute Optimizer, along with AWS
Partner tools, such as VMware CloudHealth, Apptio Cloudability,
and CloudCheckr. Cost efficiencies can also be achieved with
Compute Savings Plans, Reserved Instances, Spot Instances for
ephemeral workloads, and Amazon CloudFront Security Savings
Bundle. Continually reviewing cost metrics can help to identify
over purchased or underutilized savings mechanisms. For example,
you can optimize your storage costs with S3 Intelligent-Tiering,
Amazon Glacier, or implementing lifecycle policies and purge
processes. Centralize redundant or shared infrastructure to
optimize costs. Manage demand and supply resources dynamically by
implementing scheduled or automatic scaling, buffering, or
throttling. Review new EC2 instance types as they are released to
take advantage of a better price-performance ratio.
