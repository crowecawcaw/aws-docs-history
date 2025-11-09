# User behavior patterns

| SaaS SUS 3: Do you have a tenant off-boarding plan for inactive tenants? How<br>do you decommission tenant resources that are not being used to limit or prevent<br>waste? |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                            |

Each tenant in the SaaS solution has a footprint that includes infrastructure resources
such as compute, storage, and relevant data. When a tenant decides to off-board (stop using
the SaaS solution), the respective tenant’s footprint should be decommissioned when there is
no expectation that the tenant is likely to be re-activated. The faster unused resources can
be decommissioned (such as by automating the
process), the lower the impact, as decommissioned resources equate to energy saved. Since
this process involves data archiving or deletion, it should be described as part of the service level
agreement (SLA).

- **Best Practice–01:** Keep an updated list of
  infrastructure resources allocated per tenant.
- **Best Practice–02:** Maintain a runbook with a list of
  steps required to off-board a tenant, and periodically test it in non-production
  environment to help ensure it’s current.
- **Best Practice–03:** Use automation tools to run
  decommissioning steps to avoid human errors, and speed up the run time.
  This process should not affect the performance of active tenants.
- **Best Practice–04:** Before decommissioning, the SaaS
  provider should ensure, if required, that a copy of the data is created to meet any
  audit or compliance requirements, and to restore or reactivate the tenant in the future.
- **Best Practice–05:** Start automated decommissioning
  processes as part of a process approval system, such as a ServiceNow-approved workflow.
- **Best Practice–06:** Use auto-scaling to remove capacity
  as demand change.
  **AWS services recommendation:**

- [AWS Systems Manager
  Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") provides visibility into your AWS computing environment.
- [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") provides a detailed view of the configuration of AWS resources in
  your AWS account. This includes how the resources are related to one another and how
  they were configured in the past so that you can see how the configurations and
  relationships change over time.
- [AWS Cost and
  Usage Report](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md") (CUR) with [resource tags](../../../cur/latest/userguide/resource-tags-columns.md "../../../cur/latest/userguide/resource-tags-columns.md")— You can
  use the resource columns in AWS Cost and Usage Reports to find information about the
  specific resources covered by a line item. These columns include user-defined cost
  allocation tags.
- [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") templates describe your desired resources and their dependencies so
  that you can launch and configure them together as a stack. You can use a template to
  create, update, and delete an entire stack as a single unit, as often as you need to,
  instead of managing resources individually.
- [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") provides serverless orchestration for modern applications.
  Orchestration centrally manages a workflow by breaking it into multiple steps, adding
  flow logic, and tracking the inputs and outputs between the steps.
- [Amazon S3
  Inventory](../../../AmazonS3/latest/userguide/storage-inventory.md "../../../AmazonS3/latest/userguide/storage-inventory.md") provides comma-separated values (CSV), Apache optimized row columnar
  (ORC), or Apache Parquet output files that list your objects and their corresponding
  metadata on a daily or weekly basis for an S3 bucket or a shared prefix (that is,
  objects that have names that begin with a common string).
- [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/ "https://aws.amazon.com/s3/storage-classes/") (and the
  Amazon Glacier classes in particular) can be used to store or archive a tenant’s data for
  long-term retention and with reduced energy consumption.
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/ "https://aws.amazon.com/ec2/autoscaling/") and  [Application Auto Scaling](../../../autoscaling/application/userguide/what-is-application-auto-scaling.md "../../../autoscaling/application/userguide/what-is-application-auto-scaling.md") can help you make smart scaling decisions.
- [Quick Suite](https://aws.amazon.com/quicksight/features/ "https://aws.amazon.com/quicksight/features/") provides you with data
  driven analysis and visualization.

| SaaS SUS 4: How do you provide per-tenant footprint visibility (such as<br>resource utilization and carbon emission data) in your SaaS environment? |
| --------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                     |

Reflecting the consumption level per tenant creates awareness, visibility into the SaaS
solutions’ customers sustainability footprint, and improvement process.

- **Best Practice–01:** Instrument your SaaS application to
  collect metrics at a per-tenant level. The goal is to accurately capture all the
  activities and consumption patterns of each tenant in your system.
- **Best Practice–02:** Use application and system monitoring
  tools to identify infrastructure usage patterns on a per-tenant basis. This data must
  contain information that ties it back to the tenant.
- **Best Practice–03:** Provide detailed dashboards and
  visualizations of per-tenant operational data across the different layers of the SaaS
  solution. This data includes total compute required, such as CPU and memory usage, total
  data transfer and network costs, and total data and storage costs. The goal is to create
  a unified view of the per-tenant footprint, which provides useful operational insights
  in to your SaaS environment.
  **AWS services recommendation:**

- AWS SaaS Lens guidance on [Tenant-aware
  Operations](tenant-aware-operations.md "tenant-aware-operations.md")— SaaS providers need to be able to view system activity and health
  through the lens of individual tenants and tenant tiers. This is essential to diagnosing
  and evaluating the trends and patterns of activity and consumption for individual
  tenants.
- AWS SaaS guidance on [Tenant
  Activity and Consumption](tenant-activity-and-consumption.md "tenant-activity-and-consumption.md")—Provide visibility into how tenants are using your
  application and imposing load on your system’s architecture.
- [Amazon Cloudwatch](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") and tools from AWS Partners such as DataDog or New Relic
  can be used to capture and surface per-tenant metrics and consumption data.
- [AWS Systems Manager
  Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") provides visibility into your AWS compute environment.
- [AWS Cost and
  Usage Reports](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md") (AWS CUR) with [resource tags](../../../cur/latest/userguide/resource-tags-columns.md "../../../cur/latest/userguide/resource-tags-columns.md")— You can
  use the resource columns in AWS CUR to find information about the specific resources
  covered by a line item. These columns include user-defined cost allocation tags.
- Tracking SaaS resource and consumption—[This presentation](https://www.slideshare.net/AmazonWebServices/gpstec309saas-monitoring-creating-a-unified-view-of-multitenant-health-featuring-new-relic "https://www.slideshare.net/AmazonWebServices/gpstec309saas-monitoring-creating-a-unified-view-of-multitenant-health-featuring-new-relic") goes through the best practices for capturing and surfacing
  tenant level consumption patterns using an AWS partner solution.
- Use the [AWS Customer Carbon
  Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/ "https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/")to track, measure, review, and forecast the carbon emissions
  generated from your AWS usage.
