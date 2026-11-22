

# FND01-BP02 Establish ownership for billing, security, and operations

 Every resource in your workload needs a named owner so that changes, troubleshooting, and cost decisions have a clear point of contact. Assign owners for workloads, accounts, infrastructure, shared services, and applications. Record that ownership in a central register or as metadata on the resource. 

 **Desired outcome:** 
+  Your resources have identified owners by using metadata or a central register. 
+  Your AWS accounts have a single owner where possible. 
+  You have configured alternate contacts for billing, security, and operations in all accounts. 
+  Your ownership model defines risk ownership, change ownership, and support responsibility. 

 **Common anti-patterns:** 
+  Leaving alternate contacts for AWS accounts unpopulated, causing critical notifications to be missed. 
+  Setting the security alternate contact to a team or individual with no security knowledge, runbooks, or permissions to act on the notifications they receive, so security findings reach a recipient who cannot respond. 
+  Deploying resources without tags that identify the teams that own them. 
+  Routing incidents to an ITSM queue without an email mapping, delaying response. 
+  Assigning two teams overlapping ownership of a critical piece of infrastructure, creating unclear accountability during incidents. 
+  Maintaining ownership information in a document that is rarely reviewed or updated, leading to stale assignments. 
+  Relying only on periodic cleanup instead of tying resource ownership reassignment to the HR joiner, mover, and leaver process, so resources owned by employees who move or leave linger without a current owner until the next review. 

 **Benefits of establishing this best practice:** 
+  Assigned ownership makes change approvals direct and reduces coordination overhead. 
+  The correct owners can be engaged quickly when troubleshooting issues, which minimizes downtime. 
+  Clear ownership tracking supports accurate cost allocation and chargeback to the responsible cost centers. 
+  Compliance and audit processes take less effort when ownership information is consistent and readily available. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Clear resource ownership is a foundational element of cloud governance because it determines accountable parties during changes, incidents, and cost attribution. Without defined ownership, organizations experience delayed incident response, unclear change approval processes, and difficulty tracking cloud spending back to responsible teams. 

 Ownership models typically span multiple dimensions that rarely align to the same team: 
+  **Risk ownership:** The team accountable for business consequences 
+  **Change ownership:** The team authorized to modify the resource 
+  **Support responsibility:** responders to pages and incidents 
+  **Financial accountability:** The cost center that pays for the resource 

 A single resource can have four different owners across these dimensions, and clarity about each dimension reduces coordination cost during high-stakes events. 

 In AWS, ownership is recorded through multiple mechanisms. [AWS Organizations](https://aws.amazon.com/organizations/) manages alternate contacts for billing, security, and operations across all accounts, so AWS notifications reach the right teams as people change roles. Account-level tags in AWS Organizations apply to all metered usage in the account, which makes them useful for cost allocation. Tags record resource-level ownership. Enforce them with [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) so the data flows into cost allocation, access control, and operational workflows. For services and resources outside AWS, a central register keeps ownership information accessible during incidents and audits. 

 These alternate contacts receive AWS security notifications, billing questions, and operational communications. They're account-level metadata, separate from your IAM users or federated identities. When these contacts point to people who have left the organization, critical notifications such as an AWS abuse report about unintended access can go unanswered. Alternate contacts route billing notifications to finance and security notifications to the security team, so nothing is cross-posted to a single inbox. 

**Important**  
 Use distribution lists and shared phone numbers for alternate contacts rather than individual email addresses. People change roles and leave organizations, and a missed AWS security or billing notification can lead to unintended access or service disruption. 

 Use a consistent set of ownership tags (typically Owner, CostCenter, BusinessUnit, and Environment). These tags feed cost allocation, access control, automation, and incident response. Tags only work when they're enforced. Without enforcement, teams skip tags under deadline pressure or introduce variations of the same tag (Owner, owner, ownerEmail, OwnedBy) that break queries and reports. [Tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) define required tag keys and allowed values, and AWS Config rules detect non-compliant resources. Service control policies can block resource creation when required tags are missing. Introduce SCP-based enforcement carefully to avoid blocking legitimate operations. 

 Define the ownership model before you deploy resources. If you retrofit the model onto a large environment, you have to backfill metadata across thousands of existing resources. An informal handoff during a team reorganization leaves behind stale tags, outdated alternate contacts, and unrevised documentation, making ownership unclear. For non-AWS systems that interact with your cloud environment, maintain a current central register as the source of truth during incident response. Integrate it with runbooks and operational processes so the information stays in regular use. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define ownership categories for your organization:** Determine what ownership means for the resource use cases in your environment. Ownership can imply who owns the risk for the resource, who owns changes to the resource, who supports the resource when troubleshooting, or who is financially or administratively accountable. Document these categories and the specific tag keys that will capture them (such as Owner, CostCenter, BusinessUnit, Environment). Establish the process for transferring ownership when teams reorganize, and integrate it with your HR joiner, mover, and leaver workflow so that when an employee changes role or leaves, the resources they own are reassigned to a new owner or decommissioned as part of offboarding rather than left to be discovered later. 

1.  **Configure alternate contacts using AWS Organizations:** Use [AWS Organizations to manage alternate contacts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_contacts.html) for your accounts centrally. Use company-owned email distribution lists and shared phone numbers for billing, operations, and security contacts in each active AWS account. This approach provides redundancy when individuals change roles or leave the company. Point the security alternate contact at a team that has the knowledge, runbooks, and permissions to act on security notifications, ideally one with 24/7 coverage such as a security operations center (SOC), so findings reach responders who can investigate and remediate without delay. Point the billing alternate contact on each payer (management) account at the team that owns invoice payment, typically procurement or finance, so payment issues are seen and resolved before they escalate to account suspension. If an account is not managed by AWS Organizations, configure the account's alternate contacts directly to point to a group rather than an individual. Document which distribution list owns each contact type and establish a process for periodic validation that the distribution lists remain monitored. 

1.  **Apply account-level tags in AWS Organizations:** Tag your AWS accounts with ownership metadata such as owner, cost center, business unit, or environment directly in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html). Account-level tags apply to all metered usage within the account, which makes them useful for cost allocation even for resources that do not support resource-level tags. Activate account tags as [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/account-tags-cost-allocation.html) in the Billing and Cost Management console so they appear in your Cost and Usage Reports alongside resource-level tags. Newly activated tags can take up to 24 hours to appear in reports, so activate them early. Use account-level tags as a fallback when resource-level tagging is incomplete. 

1.  **Implement ownership tags for AWS resources:** Use tags to identify owners and their contact information for individual AWS resources within each account. Use [AWS Config](https://aws.amazon.com/config/) rules such as [required-tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) to enforce that resources have the required ownership tags, and pair them with [automated remediation](https://aws.amazon.com/blogs/mt/implementing-automated-and-centralized-tagging-controls-with-aws-config-and-aws-organizations/) for non-compliant resources. Shift enforcement left by validating tags in CI/CD pipelines with tools like [AWS CloudFormation Guard](https://aws.amazon.com/blogs/devops/introducing-a-managed-hook-for-guard/) before resources are created. For in-depth guidance on building a tagging strategy, see [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). 

1.  **Integrate ownership data with operational workflows:** Configure monitoring and alerting systems to include ownership tags in notification payloads so that alerts route directly to the responsible team. Use [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) to send cost alerts to the owners identified through cost allocation tags. Integrate ownership data from tags or your central register into your ITSM system so incidents route automatically to the correct support teams, and expose the same data in dashboards that responders use during incidents. 

1.  **Document ownership for non-AWS resources:** For other resources, services, and infrastructure that integrate with your cloud environment, create documentation that identifies ownership. Store this documentation in a system accessible to all team members, ideally integrated with your incident response runbooks so ownership information is available exactly when it is needed. Maintain the documentation as part of your operational processes, with a regular review cadence (quarterly is typical) to keep it current. Establish clear responsibility for who maintains the register and how updates are propagated. 

1.  **Review accounts on a regular cadence and act on stale ownership:** Schedule a periodic review (quarterly aligns with the cadence in Step 6) that scans every AWS account for signals of stale or missing ownership: absent Owner, CostCenter, or BusinessUnit tags, alternate contacts that bounce or no longer point to monitored distribution lists, no recent [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) activity, and zero or near-zero spend. Enumerate accounts through the [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) APIs, source spend signals from [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), and source activity signals from CloudTrail. Automate the review with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) on an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) schedule that flags candidates, notifies the responsible team, and (after a defined holding period) queues approved closures. For each candidate, reassign ownership, repurpose the account, or queue it for closure. Account closure is bounded by [CloseAccount API quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-values), so the automation must rate-limit closures within those quotas and prefer account reuse when the existing structure still fits. See [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) for OU placement (such as the Suspended OU with a deny-all SCP) used as the staging area during the closure path. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 

 **Related documents:** 
+  [Update the alternate contacts for an account in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_contacts.html) 
+  [Tagging AWS Organizations resources](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html) 
+  [Using account tags for cost allocation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/account-tags-cost-allocation.html) 
+  [Tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) 
+  [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 
+  [Implementing automated and centralized tagging controls with AWS Config and AWS Organizations](https://aws.amazon.com/blogs/mt/implementing-automated-and-centralized-tagging-controls-with-aws-config-and-aws-organizations/) 
+  [A practical guide to getting started with policy as code](https://aws.amazon.com/blogs/infrastructure-and-automation/a-practical-guide-to-getting-started-with-policy-as-code/) 
+  [Introducing a managed hook for Guard](https://aws.amazon.com/blogs/devops/introducing-a-managed-hook-for-guard/) 

 **Related examples:** 
+  [AWS Config Rules - Amazon EC2 with required tags and valid values](https://github.com/awslabs/aws-config-rules/blob/master/python/ec2_require_tags_with_valid_values.py) 

 **Related workshops:** 
+  [Tagging Workshop](https://catalog.workshops.aws/tagging/) 

 **Related services:** 
+  [AWS Config Rules - required-tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 