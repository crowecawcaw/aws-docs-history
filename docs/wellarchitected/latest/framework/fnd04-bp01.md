

# FND04-BP01 Implement standardized attribution policies

 A standard tagging and attribution strategy is the foundation for cost allocation, governance, security, and operational visibility in the cloud. Define your tagging schema centrally, apply it consistently across accounts and Regions, and automate enforcement where possible. Align the schema with your business goals, cost tracking needs, and governance rules. 

 **Desired outcome:** 
+  Your organization has a clear view of its cloud environment and can find resources by owner, cost center, environment, and compliance scope. 
+  You have efficient operations, with clear processes for resource tracking, reporting, auditing, and troubleshooting. 
+  Your environment has stronger governance and security through consistent tagging and automated enforcement. 
+  You can quickly see which resources hold sensitive data, need specific security controls, or fall under particular compliance requirements. 

 **Common anti-patterns:** 
+  Applying tags without a common approach, leading to inconsistency and confusion across the organization. 
+  Using an overly complex tagging schema, which drives non-compliance and pushback from resource owners. 
+  Relying only on manual tagging and skipping automated enforcement, which leaves tags missing or wrong. 
+  Failing to review and update tagging policies as the organization's needs change, leaving tags stale and irrelevant. 
+  Skipping tag governance by not setting clear ownership and processes for tag management. 
+  Ignoring tag limits, which causes important tags to be dropped or overwritten on some resources. 

 **Benefits of establishing this best practice:** 
+  Accurate cost allocation across teams, projects, and applications. 
+  You can find resources by business context, which speeds up tracking, reporting, and troubleshooting. 
+  Quick identification of resources that hold sensitive data or need specific controls. 
+  Attribute-based access control (ABAC) using tags adjusts permissions automatically as resources change. 
+  Automated tag enforcement keeps tags consistent without manual work. 
+  Well-tagged resources support auditing, lifecycle management, and policy enforcement across the environment. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 As organizations grow, the number of resources makes manual tracking impossible. Without a tagging strategy, you cannot determine who owns a resource, what it costs, whether it holds sensitive data, or which compliance rules apply to it, which creates risk across your organization. 

 Many organizations find tagging disparities only after resources are running in production, which forces you to make expensive fixes. A mature strategy moves enforcement earlier in the development lifecycle. Check tags as teams write and deploy infrastructure, before resources reach production. [Tag policies with infrastructure as code (IaC) validation](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html) check that AWS CloudFormation, Terraform, and Pulumi deployments include required tags. Resource creation fails if required tags are missing. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/) block creation of untagged resources but cannot fix existing ones. [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) monitor for drift and flag non-compliant resources that predate the policies. Implemented together, preventive and detective controls form defense in depth. When you deploy through AWS CloudFormation, tags on the stack pass through to supported resources. AWS Resource Groups include resources automatically based on their tags. 

 Tags add particular value when they tie into operational and security workflows and become the main way to select resources, control access, and automate. [Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) uses tags to define permissions that apply automatically based on resource attributes. With ABAC, you do not update IAM policies each time you create a new resource. Owners tag accurately when tag values control their access. Start with a small set of required tags that serve common needs: cost allocation, ownership, environment, and compliance scope. A typical starting set includes CostCenter or BusinessUnit for financial allocation, Owner or Team for the responsible group, Environment for values such as production or development, Application or Project to group resources by business application, DataClassification for resources under specific security or regulatory rules, and ManagedBy to mark whether the resource is managed manually, through IaC, or by automation. Use [tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) to define these requirements centrally and [enforce their format and allowed values](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-enforcement.html). Teams can add optional tags for their own needs beyond the required set. 

 After you define your cost allocation tags, [activate them in AWS Billing and Cost Management and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) so they appear in cost reports, AWS Cost Explorer, and [AWS Cost and Usage Reports (CUR)](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html). This makes your tags into a financial visibility tool that improves the detail of your cost analysis. 

 For new environments, enforce tagging from the start. For existing environments with many resources, phase in enforcement. Start with detective controls to give visibility without blocking work. Use the data to prioritize fixes, then add preventive controls for new resources as you correct tags on existing ones. 

**Important**  
 Tag limits depend on resource type. Most AWS resources support up to 50 tags. Design your schema to fit within these limits, and prefer multi-purpose tags over single-use tags. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up AWS Organizations:** If not already in place, set up [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) to manage multiple accounts centrally. This is the foundation for central tag policy management and enforcement. 

1.  **Define tag policies:** [Define tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) to set standard tags and their allowed values across your organization. Tag policies attach to the organization root, OUs, or individual accounts rather than to resources directly, so you can apply a baseline at the root, layer stricter rules at specific OUs, and grant narrow exceptions at the account level. Review all relevant [tagging use cases](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-use-cases.html) and work with stakeholders across the organization. Start with a small set of required tags (typically 5–8) that serve common needs. 

1.  **Implement shift-left enforcement through IaC validation:** Turn on [tag policies with IaC validation](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html) to check AWS CloudFormation, Terraform, and Pulumi deployments for required tags before resources are created. This catches tagging gaps during infrastructure authoring and stops them before they reach production. 

1.  **Implement enforcement through SCPs:** Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/) to enforce tagging rules, such as blocking the creation of untagged resources. Attach policies to organizational units at the right level of your hierarchy. 

1.  **Deploy compliance monitoring with AWS Config:** Deploy [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) across all accounts to monitor tagging compliance. Use [required-tags rules](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) and [automatic remediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) to fix tag issues across accounts. 

1.  **Organize resources using resource groups:** Use [resource groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) built from tags to manage related resources together across accounts. Resource groups support bulk operations on sets of resources that share common tags. 

1.  **Activate cost allocation tags:** [Set up AWS Cost Explorer and activate cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the management account. Activated tags show up in cost reports, AWS Cost Explorer, and [AWS Cost and Usage Reports (CUR)](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) for detailed cost analysis. 

1.  **Implement attribute-based access control (ABAC):** Use [ABAC](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) with tags in IAM policies where it fits your access model. ABAC cuts the need to update policies every time new resources are created and encourages accurate tagging. 

1.  **Manage tags at scale:** Use [AWS Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) to edit tags in bulk across many resources and accounts through the console. For automation and scale, use the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html) to script tag operations across thousands of resources or integrate tagging into existing workflows. 

1.  **Establish a review and governance process:** Set a regular schedule to review your tagging strategy and compliance. Use AWS Config aggregators to see compliance across accounts, collect feedback from teams on tagging pain points, and update tag policies as needs change. Document tag ownership and define a process for requesting new tags or changing tag definitions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 
+  [FND04-BP06 Establish centralized backup standards and mechanisms](fnd04-bp06.md) 

 **Related documents:** 
+  [Tagging use cases](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-use-cases.html) 
+  [Implementing automated and centralized tagging controls](https://aws.amazon.com/blogs/mt/implementing-automated-and-centralized-tagging-controls-with-aws-config-and-aws-organizations/) 
+  [Tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) 
+  [AWS Resource Groups Tagging API Reference](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html) 
+  [Understanding AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/) 
+  [Establishing Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html) 
+  [Guidance for Tagging on AWS](https://docs.aws.amazon.com/solutions/tagging-on-aws/) 
+  [Visualizing Resources with Workload Discovery on AWS](https://aws.amazon.com/blogs/mt/visualizing-resources-with-workload-discovery-on-aws/) 
+  [Conformance Packs in AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) 
+  [Enforcing organization-wide Amazon S3 bucket-tagging policies](https://aws.amazon.com/blogs/storage/enforcing-organization-wide-amazon-s3-bucket-tagging-policies/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - What's new with AWS governance and compliance (COP340)](https://www.youtube.com/watch?v=O_r3-thv0pA) 
+  [AWS re:Invent 2023 - How to customize AWS compliance and auditing services (COP209)](https://www.youtube.com/watch?v=VA2yajo1_4k) 