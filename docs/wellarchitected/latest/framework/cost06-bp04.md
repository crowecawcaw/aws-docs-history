

# COST06-BP04 Consider using shared resources

 Common functions duplicated across teams multiply cost without adding value. When multiple business units need the same capability, such as monitoring, backups, directory services, or connectivity, a shared resource raises utilization and lowers total cost of ownership. Consolidation only pays off when you allocate the shared cost back to the teams that consume it. 

 **Desired outcome:** 
+  You provide common functions from shared resources rather than duplicating them in each workload or account. 
+  You allocate shared cost back to consuming teams through showback or chargeback. 
+  You reserve dedicated resources for critical workloads and share resources for less critical ones. 
+  You tag shared resources so their cost is attributable rather than sitting unallocated. 

 **Common anti-patterns:** 
+  Running underused resources for support functions that several teams could share. 
+  Deploying a separate solution for the same function in every account or workload. 
+  Sharing resources without allocating their cost, so no team owns the spend. 
+  Sharing critical and non-critical workloads on the same resources without regard to their differing requirements. 

 **Benefits of establishing this best practice:** 
+  Consolidating duplicated functions reduces cost and raises utilization of the resources that remain. 
+  Standardizing on shared solutions simplifies the architecture and reduces operational effort. 
+  Consolidated usage metrics improve visibility into how shared capacity is consumed. 
+  Cost allocation makes teams accountable for the shared capacity they use. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Many workloads need the same supporting capabilities, and building each one independently duplicates cost. Monitoring stacks, backup systems, directory services, and network connectivity rarely need to differ between teams. Provide them from a shared location, whether within an account boundary or a dedicated account, to centralize management and cost. 

 When a shared resource serves many teams and no team owns the bill, spend grows unchecked. *Showback* reports the cost of consumed resources to each team, business unit, or account without moving money. *Chargeback* allocates spend from the shared account to the financial cost categories that a reporting process requires, which assigns accountability. Choose showback when the goal is visibility and chargeback when the goal is financial ownership. 

 Not every workload belongs on shared resources. Classify workloads by criticality. Less critical workloads tolerate the general-purpose configuration that maximizes utilization. Critical workloads often justify dedicated resources, which isolate performance and availability from the noise of other tenants. You can share resources across development, testing, and production while maintaining the boundaries between environments. 

 In shared architectures, measure consumption per tenant, particularly for resources that many tenants use at once. Container workloads are the clearest case, because several tasks share the compute and memory of the same host, and a naive split misattributes cost. Split cost allocation data apportions shared compute and memory to individual tasks, which makes task-level showback and chargeback possible for containerized applications. Networking is similar. Centralize connectivity components to reduce redundant charges, and measure traffic patterns to keep them right-sized over time. 

 To share across account boundaries, grant access securely. In a multi-account design, host a service once and share it with other accounts instead of rebuilding it in each one. Use [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) to share a resource with other accounts in the organization. Shareable resources include [VPC subnets and AWS Transit Gateway attachments](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-vpc). For broader controls on secure sharing within an organization, see [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate existing resources for reuse:** Review workloads that already run similar services and identify common functions a new workload could consume instead of rebuilding. Confirm that business logic and technical requirements allow reuse before committing to a shared service. 

1.  **Classify workloads by criticality:** Separate critical from non-critical workloads, and decide which functions run on shared resources and which justify dedicated ones. Apply general-purpose shared configurations to less critical workloads and reserve dedicated resources for critical ones. 

1.  **Share resources across accounts securely:** Use [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) to share resources with other accounts in your organization rather than duplicating them. Restrict access to the roles and accounts that need it, so sharing does not weaken the security boundary between environments. 

1.  **Tag and allocate shared cost:** Tag shared resources and assign them to [cost categories](https://docs.aws.amazon.com/cost-management/latest/userguide/), then activate the tags for cost allocation. Verify that shared cost is not left untagged, and set the granularity that lets you report cost by resource, workload, team, or organization. 

1.  **Measure shared consumption for showback and chargeback:** For container workloads, enable [split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) to attribute shared compute and memory to individual tasks. Use the resulting reports to drive showback or chargeback and to keep shared components right-sized. On Amazon EKS clusters that use accelerated computing instances, split cost allocation data covers the accelerators as well, including NVIDIA and AMD GPUs, AWS Trainium, and AWS Inferentia. On a shared AI or ML cluster the accelerator is usually most of the bill, so splitting on CPU and memory alone charges the accelerator cost to the wrong teams. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 
+  [COST02-BP02 Allocate costs based on workload metrics and business outcomes](cost02-bp02.md) 
+  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md) 

 **Related documents:** 
+  [What is AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) 
+  [Shareable AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html) 
+  [AWS services that you can use with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html) 
+  [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) 
+  [Centralize access using VPC interface endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/centralize-access-using-vpc-interface-endpoints/) 

 **Related videos:** 
+  [AWS Resource Access Manager - granular access control with managed permissions](https://www.youtube.com/watch?v=X3HskbPqR2s) 

 **Related examples:** 
+  [Chargeback shared services: an AWS Transit Gateway example](https://aws.amazon.com/blogs/aws-cloud-financial-management/gs-chargeback-shared-services-an-aws-transit-gateway-example/) 
+  [Build a chargeback and showback model for Savings Plans using the CUR](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-build-a-chargeback-showback-model-for-savings-plans-using-the-cur/) 
+  [Improve cost visibility of Amazon EKS with AWS split cost allocation data](https://aws.amazon.com/blogs/aws-cloud-financial-management/improve-cost-visibility-of-amazon-eks-with-aws-split-cost-allocation-data/) 
+  [Configure fine-grained access to resources shared using AWS Resource Access Manager](https://aws.amazon.com/blogs/security/configure-fine-grained-access-to-your-resources-shared-using-aws-resource-access-manager/) 

 **Related services:** 
+  [AWS Resource Access Manager](https://aws.amazon.com/ram/) 