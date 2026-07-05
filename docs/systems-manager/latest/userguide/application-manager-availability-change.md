# AWS Systems Manager Application Manager availability change

AWS Systems Manager (SSM) Application Manager is transitioning to maintenance mode and, from July 30, 2026,
will no longer be open to new customers. SSM Application Manager is a console capability that enables
DevOps teams to define or auto-discover applications, associate AWS resources to those
applications, apply tags for resource management and monitor applications' health.

Until further notice, existing SSM Application Manager customers can continue to use the service
normally in established accounts. During this period, AWS will maintain service
availability and performance and continue to offer support through AWS Support channels.
AWS will not add new features or expand the service into new Regions.

We have identified several alternatives to SSM Application Manager depending on your use case. AWS
Console for SAP Applications, Tagging, AWS Resource Groups, and AWS Resource Explorer
are available at no additional cost. For observability use cases, Amazon CloudWatch
Application Signals is a paid service that includes a free tier.

## Alternatives to Application Manager

**AWS Console for SAP Applications**

If your primary use case is to manage and operate your SAP HANA-based
applications on AWS, use AWS Console for SAP Applications, a new
centralized management experience that provides SAP customers with an
application-centric view to register and manage their SAP HANA-based
applications running on AWS. The console offers a unified dashboard to view
your registered SAP applications, understand your landing zone setup, and
gain visibility into the resources consumed by your SAP workloads. From the
application details page, customers can view application topology, associated
resources, and perform management operations including application-aware
start/stop, automated validation of SAP workload configurations, and
scheduled operations. To learn more, see the [AWS Console for SAP Applications announcement](https://aws.amazon.com/blogs/awsforsap/announcing-aws-console-for-sap-applications-a-unified-experience-to-register-and-manage-your-sap-applications-on-aws/ "https://aws.amazon.com/blogs/awsforsap/announcing-aws-console-for-sap-applications-a-unified-experience-to-register-and-manage-your-sap-applications-on-aws/").

**Tagging**

If your primary use case is to assign metadata to resources, add tags using
customer-defined tag keys (e.g., application, project, or workload) to your
account. Tagging is the foundation that not only AWS Systems Manager builds on, but
also many other AWS management tools (services such as Resource Groups,
Resource Explorer, Cost Explorer, CloudWatch, Config, and Security Hub all
use tags to organize and filter your resources). By establishing a tagging
strategy first, you gain the flexibility to adopt other alternatives over
time. For example, after tagging your resources, you can use AWS Resource
Groups to create a logical grouping for operations and visibility within your
account and search those tagged resources cross-Region and cross-account
using AWS Resource Explorer. To learn more, see [Best Practices for Tagging AWS Resources](../../../tag-editor/latest/userguide/best-practices-and-strats.md "../../../tag-editor/latest/userguide/best-practices-and-strats.md").

**AWS Resource Groups**

If your primary use case is resource organization and management, use AWS
Resource Groups to establish permanent and named groupings based on tags in a
single Region. Resource Groups allow you to organize resources by
application, environment, or any other tag-based category, making it easier
to manage and operate your workloads. To learn more, see the [AWS Resource Groups
User Guide](../../../ARG/latest/userguide.md "../../../ARG/latest/userguide.md").

**AWS Resource Explorer**

If your primary use case is resource discovery, use AWS Resource Explorer
to search and discover a collection of resources by tag, cross-Region and
cross-account. Resource Explorer provides a unified view of your AWS
resources, enabling you to search and filter by properties including tag,
resource type, and Region. To learn more, see the [AWS Resource Explorer User
Guide](../../../resource-explorer/latest/userguide.md "../../../resource-explorer/latest/userguide.md").

**Amazon CloudWatch Application Signals Application
Map**

If your primary use case is application-level observability, use Amazon
CloudWatch Application Signals for auto-discovery of applications with
multi-Region and multi-account support. Application Signals is a paid service
that includes a free tier and provides a comprehensive view of your
application's health, performance, and dependencies. To learn more, see the
[Application Signals User Guide](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.md").

###### Note

The `awsApplication` tags and AppManager resource groups created via
SSM Application Manager persist indefinitely and can continue to be used for resource grouping,
cost allocation, and filtering. Customers can use their existing AppManager resource
groups and `awsApplication` tags in combination with the recommended
alternatives (Resource Groups, Resource Explorer, Application Signals). There is no
requirement to remove or replace this tag as part of the transition to maintenance
mode.

## Frequently asked questions

**Is AWS Systems Manager Application Manager shut
down?**

No, AWS Systems Manager Application Manager is entering maintenance mode. AWS will
continue to maintain service availability and offer support through AWS
Support channels. AWS will not add new features or expand the service to
additional Regions. Starting July 30, 2026, accounts that have not previously
used AWS Systems Manager Application Manager will no longer be able to access the service;
existing customers are not affected.

**Will my existing AWS Systems Manager Application Manager applications
continue to work?**

Yes, existing AWS Systems Manager Application Manager applications will continue to
function as they do today. There is no disruption to your current setup, and
no action is required on your part. No APIs are impacted by this change.
Application Manager only uses existing SSM APIs.

**What alternatives can customers
explore?**

Customers can explore different alternatives depending on their use cases:
AWS Console for SAP Applications, Tagging, AWS Resource Groups, AWS
Resource Explorer, and, for observability use cases, Amazon CloudWatch
Application Signals Application Map.

**Is there a recommended tagging strategy or key naming
convention to replace AppManager and awsApplication?**

There is no single mandated tag key, giving customers the flexibility to
select their own custom tag key for their use case. Common conventions
include applications, projects, or workloads. The AppManager resource groups
and `awsApplication` tags also remain usable for existing
customers and do not need to be removed or replaced. In concert with this
move of Application Manager to maintenance mode, `awsApplication` is also
moving to maintenance mode.

If you have additional questions, please contact us via the [AWS Support
Center](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").
