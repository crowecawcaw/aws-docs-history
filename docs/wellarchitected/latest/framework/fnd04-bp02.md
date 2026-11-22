

# FND04-BP02 Establish an organization view of cloud inventory and dependencies

 A clear view of your cloud resources is essential for running a secure and cost-efficient cloud environment. A full operational inventory captures all cloud assets, including infrastructure, applications, licenses, and their dependencies, along with details such as location, ownership, and configuration. The inventory stays accurate when automated processes continuously discover and track resources. 

 **Desired outcome:** 
+  You have a central, organization-wide view of all cloud resources across your entire AWS organization, including infrastructure, applications, licenses, and configurations. 
+  Automated discovery continuously finds and tracks resources across accounts and Regions, keeping your inventory current without manual work. 
+  All resources follow standard tagging and naming through enforced policies, providing consistent metadata for organization and management. 
+  You have real-time visibility into resource use, costs, and operational health across all AWS accounts through shared dashboards and reporting. 
+  Resource relationships and dependencies are mapped and visualized, so you can understand complex architectures and the impact of changes. 

 **Common anti-patterns:** 
+  Managing inventory from scattered sources of truth or relying on manual processes to track resources across teams. 
+  Allowing untagged or inconsistently tagged resources without enforced governance policies. 
+  Relying on manual inventory updates and ignoring native automated discovery tools. 
+  Overlooking dependency tracking and failing to understand how resources relate to each other. 
+  Failing to track resources consistently across multiple accounts and Regions. 

 **Benefits of establishing this best practice:** 
+  A full view of resources across the organization supports better decisions and more effective resource management. 
+  Resource owners, dependencies, and configurations are quick to find, which shortens troubleshooting and planning time. 
+  Underused resources surface, waste is cut, and expenses are tracked accurately across teams. 
+  Automated discovery and tracking keep the inventory accurate without manual effort. 
+  Documented resource dependencies lower the risk of unintended impact from changes and speed up troubleshooting. 
+  Known relationships between resources support architectural decisions, migration planning, and capacity planning. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 An operational inventory is the foundation of daily cloud management. Without a clear view of which resources exist and how they relate to each other, your organization faces higher costs from forgotten or underused assets, slower incident response, and friction when planning changes. 

 An operational inventory captures what resources exist, where they run, who owns them, how they are configured, and how they depend on each other. This detail helps you answer questions during incidents ("Which resources does this service use?"), optimize spend ("Which resources can we safely shut down?"), and plan capacity ("How close are we to a service quota?"). A complete inventory covers infrastructure resources (Amazon EC2 instances, VPCs, Amazon S3 buckets), managed cloud services (Amazon RDS, Amazon ECS, AWS Lambda), applications and their components, licenses and software assets, and security groups and IAM roles, along with details such as location, ownership, configuration, tags, and dependencies. 

 AWS provides services that run continual discovery. [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) sets the organizational boundary and account structure that defines your inventory scope. [AWS Config](https://aws.amazon.com/config/) continuously tracks resource configurations across your organization. With [AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html), you can search for resources across Regions using tags and resource types. [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) collects detailed metadata from compute resources. [Workload Discovery on AWS](https://docs.aws.amazon.com/solutions/workload-discovery-on-aws/) builds visualizations of your workloads and maps dependencies across your environment. 

 A successful inventory depends on organizational alignment on governance, especially resource tagging standards. Set tagging standards early and enforce them through preventive controls to keep the inventory organized and useful. Map resource dependencies to assess the impact of changes, follow dependency chains during troubleshooting, and plan migrations with a full view of what moves together. 

 *Shadow IT* (the use of cloud services by teams outside formal governance processes) is a common risk to inventory accuracy. Set up processes to find and bring shadow IT resources into your central inventory. Work with IT, finance, and business units to understand why teams picked alternative solutions. Then bring those resources under governance without disrupting the value they provide. Integration with existing ITSM and CMDB systems keeps cloud and on-premises inventory consistent. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Engage with cross-functional stakeholders:** Bring together a team with representatives from IT, finance, security, and business units to gain their support in maintaining the cloud inventory. Define roles and responsibilities for inventory upkeep and align on governance policies. 

1.  **Conduct a resource discovery:** Identify all cloud services and resources in use across the organization, including infrastructure services, application services, and managed software services. Use [AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html) to search for resources using metadata across AWS Regions. Capture key details such as ownership, cost, and use patterns. 

1.  **Map resource relationships and dependencies:** Build a view of how resources depend on each other so you can understand architectures, size the scope of impact of changes, and plan migrations. Use [Workload Discovery on AWS](https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/solution-overview.html) to generate architecture diagrams automatically and visualize dependencies across accounts and Regions. Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) relationship data to follow dependency chains during troubleshooting and change planning. 

1.  **Implement cloud resource tagging:** Make sure that your tags capture relevant metadata: business unit, cost center, environment, and purpose. Use [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) to organize AWS resources into logical groups based on criteria such as tags. Use [tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) to enforce tagging standards across accounts. 

1.  **Implement a centralized cloud inventory system:** Set up a central system to hold the inventory. [Deploy Guidance for Resource Inventory Management on AWS](https://docs.aws.amazon.com/solutions/resource-inventory-management-on-aws/) and align it with your organization's governance needs. For multi-cloud environments, make sure that the inventory system can collect and correlate data from different cloud providers. 

1.  **Implement continuous discovery:** Set up automated processes to continuously discover, inventory, and monitor cloud resources. Configure [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) across all accounts and Regions with [aggregators](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) to centralize configuration data. Use [AWS Auto Inventory](https://github.com/aws-samples/aws-auto-inventory) to scan resources across multiple Regions and services. Consider [automated discovery in AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/automated-discovery.html) and [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) for managed node metadata. 

1.  **Establish operational dashboards and reporting:** Build dashboards, reports, and analytics using [AWS Quick](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) or similar tools. Use [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) to track service quotas. Consider the [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US) to bring inventory, cost, and usage metrics into shared views. 

1.  **Integrate with existing ITSM and CMDB systems:** Connect your cloud inventory to existing IT service management and CMDB systems to keep a single view. Use ITSM and CMDB vendor integrations built on the AWS Config, Service Catalog, AWS Systems Manager, and AWS Security Hub CSPM APIs. Qualified partners are listed in the [AWS Partner Solution Finder](https://partners.amazonaws.com/search/partners). You can also build direct integrations with the [AWS SDKs](https://builder.aws.com/build/tools) so that CMDB records stay current as cloud resources change. 

1.  **Provide training and ongoing support:** Train users and teams on cloud inventory processes and tools, and set up regular review cycles to check inventory completeness and tagging compliance. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND03-BP01 Define observability standards and policies](fnd03-bp01.md) 
+  [FND04-BP01 Implement standardized attribution policies](fnd04-bp01.md) 
+  [FND04-BP05 Establish service quota management](fnd04-bp05.md) 
+  [FND05-BP05 Maintain an auditable cloud inventory record](fnd05-bp05.md) 

 **Related documents:** 
+  [Establishing Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html) 
+  [Guidance for Tagging on AWS](https://docs.aws.amazon.com/solutions/tagging-on-aws/) 
+  [Visualizing Resources with Workload Discovery on AWS](https://docs.aws.amazon.com/solutions/workload-discovery-on-aws/) 
+  [Guidance for Resource Inventory Management on AWS](https://docs.aws.amazon.com/solutions/resource-inventory-management-on-aws/) 
+  [AWS launches enhanced AWS Resource Explorer features for new resource insights](https://aws.amazon.com/blogs/mt/aws-launches-enhanced-aws-resource-explorer-features-for-new-resource-insights/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Centralize your operations (COP320)](https://www.youtube.com/watch?v=9-RBjmhDdaM) 
+  [AWS re:Invent 2023 - Centralize hybrid & multicloud management with AWS (COP324)](https://www.youtube.com/watch?v=D90CbElOQ5g) 
+  [AWS re:Invent 2023 - How to manage applications at scale and innovate faster with AWS (COP328)](https://www.youtube.com/watch?v=E7h62PdfNGc) 