AWS Service Catalog AppRegistry will no longer be open to new customers starting July 30, 2026. If you would like to use the service, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](app-registry-availability-change.md "app-registry-availability-change.md").

# AWS Service Catalog AppRegistry availability change

AWS Service Catalog AppRegistry is transitioning to maintenance mode, and will no longer be open to new customers starting July 30, 2026. AppRegistry is a service that helps customers organize and manage their application resources by creating logical groupings and associating metadata. AppRegistry enables customers to define applications, associate AWS resources to those applications, and apply tags for resource management and cost allocation.

Until further notice, existing AppRegistry customers can continue to use the service normally in established accounts. During this period, AWS will maintain service availability and performance and continue to offer support through AWS Support channels. AWS will not add new features or expand the service into new AWS Regions.

The following are several alternatives to AppRegistry depending on your use case. Tagging, AWS Resource Groups, and AWS Resource Explorer are available at no additional cost. For observability use cases, CloudWatch Application Signals is a paid service that includes a free tier.

## Tagging

If your primary use case is to assign metadata to resources, add tags using customer-defined tag keys (for example, `application`, `project`, or `workload`) in your account. Tagging is the foundation that other AWS management tools build on (services such as AWS Resource Groups, AWS Resource Explorer, AWS Cost Explorer, CloudWatch, Systems Manager, AWS Config, and AWS Security Hub all use tags to organize and filter your resources). By establishing a tagging strategy first, you gain the flexibility to adopt other alternatives over time. For example, after tagging your resources, you can use AWS Resource Groups to create a logical grouping for operations and visibility within your account and search those tagged resources cross-Region and cross-account using AWS Resource Explorer. To learn more, see [Best Practices for Tagging AWS Resources](../../../tag-editor/latest/userguide/best-practices-and-strats.md "../../../tag-editor/latest/userguide/best-practices-and-strats.md").

## AWS Resource Groups

If your primary use case is resource organization and management, use AWS Resource Groups to establish permanent and named groupings based on tags in a single AWS Region. Resource Groups allows you to organize resources by application, environment, or any other tag-based category, making it easier to manage and operate your workloads. To learn more, see [AWS Resource Groups User Guide](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md").

## AWS Resource Explorer

If your primary use case is resource discovery, use AWS Resource Explorer to search and discover a collection of resources by tag, cross-Region and cross-account. Resource Explorer provides a unified view of your AWS resources, enabling you to search and filter by properties including tag, resource type, and AWS Region. To learn more, see [AWS Resource Explorer User Guide](../../../resource-explorer/latest/userguide/welcome.md "../../../resource-explorer/latest/userguide/welcome.md").

## CloudWatch Application Signals Application Map

If your primary use case is application-level observability, use CloudWatch Application Signals for auto-discovery of applications with multi-Region and multi-account support. Application Signals is a paid service that includes a free tier and provides a comprehensive view of your application health, performance, and dependencies. To learn more, see [Application Signals User Guide](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md").

## The `awsApplication` tag

###### Note

The `awsApplication` tag created by AppRegistry is a user tag, persists indefinitely, and can continue to be used for resource grouping, cost allocation, and filtering. Customers can use their existing `awsApplication` tags in combination with the recommended alternatives (AWS Resource Groups, AWS Resource Explorer, Application Signals). There is no requirement to remove or replace this tag as part of the transition.

## Frequently asked questions

**Is AppRegistry being shut down?**

No, AppRegistry is not being shut down. AWS will continue to maintain service availability and offer support through AWS Support channels. AWS will not add new features or expand the service to additional AWS Regions. Starting July 30, 2026, accounts that have not previously used AppRegistry will no longer be able to access the service; existing customers are not affected.

**Will my existing AppRegistry applications continue to work?**

Yes, existing AppRegistry applications will continue to function as they do today. There is no disruption to your current setup, and no action is required on your part.

**What alternatives can customers explore?**

Customers can explore Tagging, AWS Resource Groups, AWS Resource Explorer, and, for observability use cases, CloudWatch Application Signals Application Map. The choice of alternatives depends on your use cases. For instance, you can implement alternative tagging strategies (for example, `project`, `application`, `workload`) and then use AWS Resource Groups for permanent, named tag-based groupings.

**Is there a recommended tagging strategy or key naming convention to replace `awsApplication`?**

There is no single mandated tag key, giving customers the flexibility to select their own custom tag key for their use case. Common conventions include `application`, `project`, or `workload`. The `awsApplication` tag also remains usable for existing customers and does not need to be removed or replaced.

**Are the recommended alternatives available at no additional cost?**

Tagging, AWS Resource Groups, and AWS Resource Explorer are available at no additional cost. CloudWatch Application Signals is a paid service that includes a free tier. For pricing details, refer to the [CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

If you have additional questions, contact us through the [AWS Support Center](https://aws.amazon.com/support "https://aws.amazon.com/support").
