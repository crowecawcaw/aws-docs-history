

# FND01-BP01 Establish management account and organizational structure

 With a multi-account environment, you can meet security, governance, and operational requirements and establish clear boundaries for workload isolation, access control, and cost management. Your organizational structure must accommodate both centralized and decentralized operational models, particularly for enterprises with multiple business units. 

 **Desired outcome:** 
+  You have a secure and scalable AWS organizational structure that matches your organization's security and operational requirements. 
+  For smaller organizations (four to ten accounts), you maintain a flat hierarchy with core foundational [organizational units](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) (OUs). 
+  For medium sized enterprises (100-500 accounts), you establish a federated model that supports autonomous business units and keeps governance and security controls centralized. 
+  For larger enterprises (500-1000\+ accounts), multiple organizations might be required to accommodate full autonomy of different business units. 
+  Your structure supports clear cost allocation, different operational models, and consistent security policies at the appropriate organizational level. Accounts are grouped based on the controls to be implemented. 

 **Common anti-patterns:** 
+  Using a single AWS account for all workloads and environments, leading to poor isolation and security risks. 
+  Mirroring organizational reporting structure in OUs instead of focusing on security and operational needs. 
+  Running production workloads in the management account, exposing the entire organization to the scope of impact of a single workload. 
+  Placing multiple unrelated workloads with different data sensitivity levels into the same account. 
+  Managing users and permissions individually in each account instead of using centralized identity federation. 
+  Creating deep OU hierarchies (more than three or four levels) or designing OUs around temporary organizational structures, which complicates policy inheritance and forces frequent restructuring as the organization evolves. 

 **Benefits of establishing this best practice:** 
+  Separate accounts provide strong security boundaries and limit the scope of impact of security incidents. 
+  Centralized management of common resources and consistent policy application across account groups reduces administrative overhead. 
+  Clear cost allocation and billing separation by business unit or workload. 
+  Clear separation of concerns simplifies the implementation of compliance, auditing, and regulatory requirements for the organization. 
+  OU-based policy inheritance applies security controls and operational standards across hundreds or thousands of accounts without managing policies individually, and still supports exceptions where needed. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A multi-account strategy is the foundation of a secure and well-governed AWS environment because accounts are the strongest isolation boundary AWS provides. Permissions, resource limits, billing, and scope of impact all scale with the account boundary, which makes account structure a primary design decision. With [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), you centralize policy application, consolidated billing, and cross-account controls. 

 The management account's scope of impact is the entire organization, so keep workloads out of it. Security services, logging, and identity management belong in dedicated accounts within a security OU, keeping privileged operations separate from day-to-day engineering activity. This separation reduces the risk that unintended access in a workload account also reaches audit or identity data. Core networking and shared services belong in an infrastructure OU. Their lifecycles are independent of workloads, and their availability affects many teams at once. 

 **For smaller organizations (four to ten accounts):** A single management account alongside core security and infrastructure OUs, plus a workloads OU with production and non-production accounts, provides meaningful isolation without a deep hierarchy. Add OUs later as the organization grows, since restructuring existing ones is more disruptive. 

 **For larger enterprises (500–1000\+ accounts):** A single AWS Organization with use-case-specific OUs under a workloads OU supports independent team operations and keeps security and policy controls centralized. At this scale, automated account provisioning is required, since manual account creation cannot keep up with demand and introduces inconsistency. Federated identity scales better than per-account IAM users, and geographic or regulatory requirements often introduce Region-specific controls that factor into the OU design. Multiple AWS Organizations might be warranted when [capabilities cannot be met within a single organization](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/multiple-organizations.html), such as distinct billing separation or specific regulatory requirements. 

 [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) automates much of the initial setup and ongoing governance of an AWS Organizations environment, reducing the engineering effort to establish a landing zone. Compliance requirements, service quota management across accounts, and documentation needs all influence OU design. Incorporate them into the initial structure even when they are not fully implemented at launch. Basic account metadata (ownership, purpose, and compliance status) supports operational management and becomes harder to backfill as the account count grows. The [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/account-structure.html) provides detailed patterns for account structure within the security and infrastructure OUs. 

 [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) are the primary mechanism for enforcing security boundaries across accounts. SCPs cap the maximum permissions in an account, including permissions granted by IAM policies. Even the account root user cannot exceed those limits. Start with broad restrictions at the root OU and add exceptions only in specific OUs where needed. Deny-by-default takes less effort to enforce than restricting a permissive baseline later. Pair SCPs with [centralized root access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) so member accounts have no persistent root credentials. Use an SCP to restrict the root principal to only the [specific tasks that require root](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks), such as removing a misconfigured S3 bucket policy. Apply restrictive SCPs to the log archive and audit accounts to prevent even administrators from deleting or modifying CloudTrail logs. This helps protect the evidence trail that security investigations depend on, so detective controls remain trustworthy when a workload account experiences unintended access. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create a dedicated management account:** Use a shared email distribution list (not an individual mailbox) for the account's root email, and delegate a small team to manage this distribution list with responsibility for foundational cloud infrastructure. Keep the account contact phone number current by using a dedicated SIM with long-term retention, and document who holds it. Enable [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) and configure multi-factor authentication for the root user. Use federation through [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) or another identity provider for accessing the management account. Review and follow [Best practices for the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html) as you implement this step. 

1.  **Design an organizational unit structure:** Align your OU structure with [business needs, data sensitivity, and workload structure](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous_best_practices.html) rather than mirroring reporting lines. Plan for core foundational OUs (security, infrastructure, workloads) before designing workload-specific child OUs. Consider additional OUs that AWS recommends for specific needs as the environment grows: 
+  Sandbox for experimentation Policy Stagin for testing SCP and control changes 
+  Suspended (with an SCP denying all actions) for accounts pending closure or investigation 
+  Exceptions for accounts that cannot accept standard policies 
+  Deployments for CI/CD tooling 
+  Transitional for newly acquired or migrated accounts 
+  Individual Business Users for per-person exploration 

 Apply policies at the OU level rather than account level so inheritance is predictable. Keep depth shallow, three to four levels at most, to avoid policy inheritance issues that are difficult to troubleshoot. 

1.  **Set up AWS Control Tower:** Configure [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) in your management account. With landing zone v4.0, AWS Control Tower offers flexible deployment options. You can deploy a full landing zone with optional service integrations (such as AWS Config, AWS CloudTrail, security roles, and AWS Backup), or use the [Controls Dedicated experience](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/) to adopt managed controls through the Control Catalog without a full landing zone. AWS Control Tower no longer enforces a mandatory Security OU, so you can define and manage your own organizational structure. Optionally, designate log archive and audit accounts and enable the service integrations that match your governance requirements. 

1.  **Establish a security OU:** Create additional security-focused accounts as needed beyond the AWS Control Tower baseline. Configure centralized logging through [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-tutorial.html) and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html), and enable security services such as [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html) and [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). Apply restrictive [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to the security OU that prevent account closure, log deletion, and security service disablement so that detective controls remain trustworthy even if a workload account experiences unintended access. Consider using the [AWS SRA code library](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/code-repo.html) to automate the deployment of these and other security services in your environment. 

1.  **Create an infrastructure OU:** Set up an infrastructure OU for hosting shared services such as networking resources, shared repositories, images, and snapshots. Consider using AWS SRA patterns for detailed design of [network](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) and [shared services](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/shared-services.html) accounts. 

1.  **Set up a workloads OU structure:** Organize workload accounts according to your design. For smaller organizations, create only production and non-production OUs. For enterprises, create business unit-specific child OUs with their own production and non-production distinction. Follow [Best practices for managing organizational units (OUs) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous_best_practices.html) to keep OU depth manageable and policy inheritance predictable. 

1.  **Implement security controls:** [AWS Control Tower controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) span preventive ([service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html), and [declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_policies.html)), detective (AWS Config rules), and proactive (AWS CloudFormation hooks and Guard) categories. All controls, including mandatory ones, require explicit enablement. Start by enabling preventive controls at the root OU, then layer additional controls for specific OUs as needed. If you use the [Controls Dedicated experience](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/), deploy controls directly from the Control Catalog. Test custom SCPs to verify that they do not conflict with AWS Control Tower's managed controls. 

1.  **Automate account provisioning:** Implement automation for account provisioning and baseline configuration using [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) or custom infrastructure as code solutions such as [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html). Standardized provisioning gives every new account the same baseline guardrails, logging, networking, and identity configuration. Adopt a naming and email convention that reflects account usage (for example, Workloads\+fooA-dev@example.com) and assign account-level tags for cost center, environment, and project. Before creating new accounts, check for existing duplicates and plan to reuse rather than close accounts where possible. The [CloseAccount API has quota limits](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-values) that make reuse the more scalable pattern. With [auto-enrollment](https://docs.aws.amazon.com/controltower/latest/userguide/account-auto-enrollment.html), any account you create through your chosen infrastructure as code method, or move into an OU that AWS Control Tower governs, is enrolled automatically and receives the appropriate baselines and controls. 

1.  **Enable service integrations from each service's own console:** When you enable AWS services across your organization (for example, AWS Config, AWS CloudTrail, GuardDuty, Security Hub CSPM, Security Hub CSPM), we recommend doing so from the service's own console or API rather than from the AWS Organizations console, with AWS Account Management as the documented exception. This approach runs the service's full integration flow (including [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html) setup and member account enrollment) as designed. 

1.  **Establish an account lifecycle and decommissioning process:** Pair the account provisioning in Step 8 with a recurring decommissioning process so the organization does not accumulate stale accounts. Use the periodic ownership review described in [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) to identify candidates, then move each candidate to the Suspended OU described in Step 2 for a defined holding period (30 to 90 days is typical) so owners can reclaim the account if it is still needed. After the holding period, automate closure with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) on an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) schedule, and rate-limit calls to the [CloseAccount API](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html) so the pipeline stays within the [AWS Organizations closure quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-values). Continue to prefer renaming and repurposing accounts over closure when the existing structure still fits, as Step 8 recommends. Protect log archive and audit accounts from this pipeline by applying SCPs to the security OU that deny organizations:CloseAccount, so misclassification cannot remove the evidence trail. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 
+  [FND01-BP04 Establish a strategy for experimental and temporary environments](fnd01-bp04.md) 

 **Related documents:** 
+  [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) 
+  [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 
+  [Centrally managing root access for customers using AWS Organizations](https://aws.amazon.com/blogs/aws/centrally-managing-root-access-for-customers-using-aws-organizations/) 
+  [What is AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) 
+  [AWS security audit guidelines](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-audit-guide.html) 
+  [Terminology and concepts for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) 
+  [Best practices for managing organizational units (OUs) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous_best_practices.html) 
+  [Enforcing enterprise-wide preventive controls with AWS Organizations](https://aws.amazon.com/blogs/mt/enforcing-enterprise-wide-preventive-controls-with-aws-organizations/) 
+  [What is an AWS account?](https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html) 
+  [AWS organization and account structure of the AWS SRA](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/account-structure.html) 

 **Related videos:** 
+  [Cloud Governance Best Practices on AWS](https://aws.amazon.com/video/watch/f973d004042/) 
+  [AWS Security Innovations: Insights from AWS CISO Chris Betz](https://aws.amazon.com/video/watch/b4236060453/) 