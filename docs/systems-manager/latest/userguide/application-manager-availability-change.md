

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# AWS Systems Manager Application Manager availability change
<a name="application-manager-availability-change"></a>

AWS Systems Manager Application Manager is no longer open to new customers. SSM Application Manager is a console capability that enables DevOps teams to define or auto-discover applications, associate AWS resources to those applications, apply tags for resource management and monitor applications' health.

Until further notice, existing SSM Application Manager customers can continue to use the service normally in established accounts. During this period, AWS will maintain service availability and performance and continue to offer support through AWS Support channels. AWS will not add new features or expand the service into new Regions.

We have identified several alternatives to SSM Application Manager depending on your use case. AWS Console for SAP Applications, Tagging, AWS Resource Groups, and AWS Resource Explorer are available at no additional cost. For observability use cases, Amazon CloudWatch Application Signals is a paid service that includes a free tier.

## Alternatives to Application Manager
<a name="application-manager-availability-change-alternatives"></a>

**AWS Console for SAP Applications**  
If your primary use case is to manage SAP HANA-based applications on AWS, use AWS Console for SAP Applications. This centralized experience provides an application-centric view to register and manage SAP HANA-based applications running on AWS. The console offers a unified dashboard to view your registered SAP applications, understand your landing zone setup, and gain visibility into resources consumed by your SAP workloads. From the application details page, you can view application topology, associated resources, and perform operations including application-aware start/stop and automated validation. To learn more, see the [AWS Console for SAP Applications announcement](https://aws.amazon.com/blogs/awsforsap/announcing-aws-console-for-sap-applications-a-unified-experience-to-register-and-manage-your-sap-applications-on-aws/).

**Tagging**  
If your primary use case is to assign metadata to resources, add tags using customer-defined tag keys (e.g., application, project, or workload) to your account. Tagging is the foundation that not only AWS Systems Manager builds on, but also many other AWS management tools (services such as Resource Groups, Resource Explorer, Cost Explorer, CloudWatch, Config, and Security Hub all use tags to organize and filter your resources). By establishing a tagging strategy first, you gain the flexibility to adopt other alternatives over time. For example, after tagging your resources, you can use AWS Resource Groups to create a logical grouping for operations and visibility within your account and search those tagged resources cross-Region and cross-account using AWS Resource Explorer. To learn more, see [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html).

**AWS Resource Groups**  
If your primary use case is resource organization and management, use AWS Resource Groups to establish permanent and named groupings based on tags in a single Region. Resource Groups allow you to organize resources by application, environment, or any other tag-based category, making it easier to manage and operate your workloads. To learn more, see the [AWS Resource Groups User Guide](https://docs.aws.amazon.com/ARG/latest/userguide/).

**AWS Resource Explorer**  
If your primary use case is resource discovery, use AWS Resource Explorer to search and discover a collection of resources by tag, cross-Region and cross-account. Resource Explorer provides a unified view of your AWS resources, enabling you to search and filter by properties including tag, resource type, and Region. To learn more, see the [AWS Resource Explorer User Guide](https://docs.aws.amazon.com/resource-explorer/latest/userguide/).

**Amazon CloudWatch Application Signals Application Map**  
If your primary use case is application-level observability, use Amazon CloudWatch Application Signals for auto-discovery of applications with multi-Region and multi-account support. Application Signals is a paid service that includes a free tier and provides a comprehensive view of your application's health, performance, and dependencies. To learn more, see the [Application Signals User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html).

**Note**  
The `awsApplication` tags and AppManager resource groups created through SSM Application Manager persist indefinitely and can continue to be used for resource grouping, cost allocation, and filtering. Customers can use their existing AppManager resource groups and `awsApplication` tags in combination with the recommended alternatives (Resource Groups, Resource Explorer, Application Signals). There is no requirement to remove or replace this tag as part of the transition to maintenance mode.

## Frequently asked questions
<a name="application-manager-availability-change-faq"></a>

**Is AWS Systems Manager Application Manager shut down?**  
No, AWS Systems Manager Application Manager is entering maintenance mode. AWS will continue to maintain service availability and offer support through AWS Support channels. AWS will not add new features or expand the service to additional Regions. Starting July 30, 2026, accounts that have not previously used AWS Systems Manager Application Manager will no longer be able to access the service; existing customers are not affected.

**Will my existing AWS Systems Manager Application Manager applications continue to work?**  
Yes, existing AWS Systems Manager Application Manager applications will continue to function as they do today. There is no disruption to your current setup, and no action is required on your part. No APIs are impacted by this change. Application Manager only uses existing SSM APIs.

**What alternatives can customers explore?**  
Customers can explore different alternatives depending on their use cases: AWS Console for SAP Applications, Tagging, AWS Resource Groups, AWS Resource Explorer, and, for observability use cases, Amazon CloudWatch Application Signals Application Map.

**Is there a recommended tagging strategy or key naming convention to replace AppManager and awsApplication?**  
There is no single mandated tag key, giving customers the flexibility to select their own custom tag key for their use case. Common conventions include applications, projects, or workloads. The AppManager resource groups and `awsApplication` tags also remain usable for existing customers and do not need to be removed or replaced. In concert with this move of Application Manager to maintenance mode, `awsApplication` is also moving to maintenance mode.

If you have additional questions, contact us through the [AWS Support Center](https://console.aws.amazon.com/support).