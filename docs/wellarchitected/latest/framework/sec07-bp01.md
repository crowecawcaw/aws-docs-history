

# SEC07-BP01 Understand your data classification scheme

 A data classification scheme names the sensitivity levels in your organization, the handling rules for each, and who owns the decision. To apply the right controls, know the classification, location, and legal and compliance obligations of the data your workload processes. 

 **Desired outcome:** 
+  You have documented the types of data in your workload and the sensitivity level of each. 
+  Your scheme records the handling requirements for each level: who can access the data, where it is stored, how it is encrypted, how long it is retained, and how it is destroyed. 
+  Your controls match the sensitivity level of the data they protect, and those controls can be audited. 
+  Your workload owners know where sensitive data resides and which protections apply to it. 

 **Common anti-patterns:** 
+  Teams operate without a formal data classification policy that defines sensitivity levels and their handling requirements. 
+  Workload teams ignore the classification scheme the organization has set and invent their own. 
+  Architecture and operations documentation omits the sensitivity of the data the workload processes. 
+  Teams apply controls that do not match the sensitivity of the data, leaving highly sensitive data underprotected. 
+  Workload teams find gaps in the classification policy but never report them back to the policy owners. 

 **Benefits of establishing this best practice:** 
+  Handling of data becomes unambiguous, because every sensitivity level has defined protections. 
+  Compliance with legal regulations and security certifications becomes more straightforward to demonstrate. 
+  Workload owners gain confidence about where sensitive data is stored and how it is protected. 
+  New team members learn the controls early, because the scheme is documented. 
+  Costs drop where controls are right-sized to the actual sensitivity of the data. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Teams protect data by intuition before they have a policy. In a multi-tenant application, you treat each tenant's data as private and block one tenant from reading other tenant data. You give administrators write access and everyone else read-only access or none. This intuition is correct, but it does not scale because it is not officially documented, varies across teams, and cannot be audited. A classification scheme creates a stated policy that names each sensitivity level and the protections that each level requires. 

 A central function defines the sensitivity levels, and each workload maps its data onto those levels. When a workload team is unaware of the scheme, or the scheme has no level that fits the data, teams improvise and consistency breaks down. Report gaps back to the policy owners so they can refine the scheme. 

 Use multiple sensitivity levels to match control cost to data risk. This helps you avoid scenarios where you underprotect data with legal or contractual obligations with too low of a level. On the other hand, if you classify too high, you can burden ordinary data with expensive controls, slow legitimate access, and train teams to see the policy as an obstacle. 

 To know where sensitive data resides, maintain a *data catalog*. The catalog maps data across the organization to its location, sensitivity level, and the controls that protect it. [Resource tags](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) attach classification to each resource. For example, tag a resource with a Classification key of PHI for protected health information, or a Sensitivity key of High. Tools that read tags can then find and act on sensitive resources. [AWS Config](https://aws.amazon.com/config/) watches tagged resources and alerts when a change, such as weakened encryption, moves them out of compliance. [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in AWS Organizations standardize which tag keys and values are valid. Keep private or sensitive data out of the tag keys and values themselves. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Understand your organization's classification scheme:** Review the sensitivity levels your organization defines and the handling requirements for each. Confirm which levels apply to your workload, and note the legal or compliance obligations that attach to them. 

1.  **Identify the sensitive data your workload processes:** Inventory the data your workload ingests, stores, and produces, and assign each type to a sensitivity level. Record where each type is stored and who owns it. 

1.  **Record classifications in a data catalog:** Capture the results in a data catalog that gives a single view of where data resides across the organization and its level of sensitivity. Keep this record current as the workload changes. 

1.  **Tag resources with their sensitivity level:** Apply resource and data-level tags for sensitivity and other operational metadata that supports monitoring and incident response. Use [AWS Organizations tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) to enforce consistent tag keys and values. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC07-BP02 Apply data protection controls based on data sensitivity](sec07-bp02.md) 
+  [SEC07-BP03 Automate identification and classification](sec07-bp03.md) 
+  [SEC07-BP04 Define scalable data lifecycle management](sec07-bp04.md) 

 **Related documents:** 
+  [Data classification whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/data-classification/data-classification.pdf) 
+  [Best practices for tagging AWS resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 

 **Related examples:** 
+  [AWS Organizations tag policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html) 

 **Related tools:** 
+  [AWS Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) 