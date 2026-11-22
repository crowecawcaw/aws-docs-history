

# FND05-BP09 Establish security tooling for investigating incidents

 In a multi-account cloud environment, dedicate an account to operating security services, monitoring accounts, and automating security alerting and response. Security teams then have unified visibility and can investigate incidents consistently across the organization. 

 **Desired outcome:** 
+  You have established faster incident response capabilities through the ability to detect, investigate, and respond to security incidents more quickly across the entire organization. 
+  You have improved your ability to assess and manage risks across the organization through centralized visibility and control. 
+  You have improved threat detection through better capability to identify activity that spans multiple accounts or services and is harder to spot from a single account. 
+  Your security tooling account is a centralized hub for managing security services and monitoring across each account in your organization. 

 **Common anti-patterns:** 
+  Excessive decentralization of security management where individual teams independently implement security tools without coordination, leading to inconsistent standards and visibility gaps. 
+  Ignoring account boundaries and attempting to manage all security aspects from the central account without respecting the autonomy and specific needs of individual accounts or business units. 
+  Relying heavily on manual processes for security operations instead of using automation. 
+  Keeping incident response processes isolated within the security team without integration with other teams. 
+  Centralizing all security data without considering residency requirements, potentially violating compliance regulations. 
+  Implementing too many security tools without proper integration, leading to alert fatigue and inefficient operations. 

 **Benefits of establishing this best practice:** 
+  Unified visibility across the accounts and services in your organization supports faster incident detection and response. 
+  Security teams can detect and investigate activity that spans multiple accounts or services through correlated analysis. 
+  Reduced duplication of security tool deployments and consistent security standards simplify operations across the organization. 
+  Automated security alerting and response capabilities reduce manual overhead and improve response times and consistency. 
+  Centralized visibility into security posture and centralized compliance reporting support better risk management decisions. 
+  Delegated administration models let security teams manage tools and investigate incidents without requiring direct access to workload accounts. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Effective security investigation requires that tooling and data are already in place before an incident occurs. Organizations that attempt to deploy security services reactively, after an incident is detected, face delays that permit threats to persist and expand. A dedicated Security Tooling account, separate from workload accounts, centralizes security services with their own access controls, independent of the workloads they protect. 

 Use [AWS Organizations](https://aws.amazon.com/organizations/) and organizational units (OUs) to manage multiple accounts and apply consistent security policies. Create dedicated Security Tooling and Log Archive accounts within a security OU, and keep the two accounts separate. The Security Tooling account hosts active security services that detect threats, analyze configurations, and orchestrate responses in near real time. The Log Archive account stores immutable copies of logs for compliance, forensics, and long-term retention. This separation prevents operational security tooling from interfering with audit trail integrity and prevents investigators from inadvertently modifying logs during an incident. Configure the Security Tooling account as the delegated administrator for these services. [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) evaluates your environment against security standards and consolidates findings. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) correlates those findings with signals from Amazon Inspector, Amazon Macie, and Amazon GuardDuty to generate exposure findings. AWS [recommends enabling both Security Hub CSPM and Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html). Use [Amazon GuardDuty](https://aws.amazon.com/guardduty/) for threat detection, [Amazon Detective](https://aws.amazon.com/detective/) for security investigations, and [AWS Config](https://aws.amazon.com/config/) for resource inventory and configuration tracking. The [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) provides guidance on structuring this account and its associated services. 

**Important**  
 Do not host production workloads in the Security Tooling account. Use it only to run security services and coordinate security operations. Mixing workloads with tooling introduces conflicts of interest and complicates response when the account itself is the subject of an investigation. 

 Configure [IAM roles and policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) for cross-account access so the security team can reach resources across accounts under least privilege. Route events through [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to automate responses to security incidents across the organization. See [Sending and receiving events between AWS accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html). For compliance and audit, combine [AWS Config Aggregators](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) with [AWS Config Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) and [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) for a centralized view of compliance status across all accounts. 

 **Smaller organizations** with a handful of accounts can start with a focused stack of CloudTrail, GuardDuty, and AWS Security Hub CSPM, and add services as maturity and requirements grow. Enable AWS Security Hub CSPM alongside Security Hub CSPM once multiple detection sources are in place, so that CSPM findings are correlated with Inspector, Macie, and GuardDuty into exposure findings. **Larger organizations** with formal compliance obligations typically need the full suite: Macie for sensitive-data discovery, Detective for investigation graphs, both Security Hub CSPM and Security Hub CSPM for exposure-based risk prioritization, AWS Security Incident Response for automated triage and escalation, and AWS Config Conformance Packs for framework-aligned compliance reporting. Regardless of scale, establish the architectural foundation early. Set up the security OU, the dedicated accounts, and the delegated administration model so that additional services can be enabled later without re-architecting. Regularly review and update your security configurations, conduct security assessments, and maintain comprehensive documentation of your security architecture and processes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up AWS Organizations and organizational structure:** Set up [AWS Organizations](https://aws.amazon.com/organizations/) and create a [well-structured organizational setup](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html). Create a dedicated security OU for hosting security tooling and log archive accounts. In recent [AWS Control Tower](https://aws.amazon.com/controltower/) deployments, the Security OU is no longer automatically created or managed, so you can define and manage your own organizational structure. 

1.  **Create a Security Tooling account:** Create a Security Tooling account in the security OU. Use the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) to set up this account and deploy associated security services. 

1.  **Enable audit logging and configuration tracking:** [Set up an organization-wide AWS CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) and deliver its logs to a dedicated S3 bucket in the Log Archive account to preserve audit trail integrity. Turn on [AWS Config](https://aws.amazon.com/config/) across the organization and [set up multi-account, multi-Region data aggregation](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) with the aggregator in the Security Tooling account so investigators have a consolidated view of resource configurations. See [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html). 

1.  **Enable threat detection with Amazon GuardDuty:** [Turn on Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html) in the Security Tooling account and designate it as the GuardDuty administrator. See [Managing multiple accounts in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html). 

1.  **Enable security investigation capabilities with Amazon Detective:** Turn on [Amazon Detective](https://aws.amazon.com/detective/) in the Security Tooling account and configure it as the Detective administrator. See [Managing Amazon Detective in a multi-account environment](https://docs.aws.amazon.com/detective/latest/userguide/). Detective correlates data from GuardDuty, CloudTrail, and VPC Flow Logs to support investigation. 

1.  **Enable centralized security posture management:** [Enable AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html) in the Security Tooling account and configure it as the [Security Hub CSPM administrator](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html) to run security-standards checks and consolidate findings from across your organization. AWS [recommends enabling both Security Hub CSPM and Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html), so enable [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) in the same account. Security Hub CSPM findings are routed to Security Hub CSPM automatically, where they're correlated with findings from Amazon Inspector, Amazon Macie, and Amazon GuardDuty to generate exposure findings that identify the most critical risks. 

1.  **Enable sensitive data discovery with Amazon Macie:** [Turn on Amazon Macie in the Security Tooling account](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html) and set it as the Macie administrator. See [Managing multiple accounts in Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html). Use Macie to discover and classify sensitive data in Amazon S3 so security teams know which workloads hold personally identifiable or regulated information. 

1.  **Enable access analysis with AWS IAM Access Analyzer:** Turn on [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) for the organization through the [delegated administrator functionality in AWS Organizations](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-delegated-administrator.html). Access Analyzer surfaces IAM policies and resource shares that grant access outside your trust boundary. 

1.  **Enable network protection management:** Turn on [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) in the Security Tooling account and configure it as the Firewall Manager administrator. See [Setting up AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/enable-integration.html). 

1.  **Configure centralized operational management:** Configure [AWS Systems Manager](https://aws.amazon.com/systems-manager/) in the Security Tooling account for centralized operational management. See [Setting up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/). 

1.  **Enable AWS Security Incident Response:** Turn on [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) to help prepare for, respond to, and recover from security events. This service automates triage of security findings from services like [Amazon GuardDuty](https://aws.amazon.com/guardduty/), escalates critical security events, and provides access to AWS Security Incident Response engineers. See [Getting started with AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/getting-started.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) 
+  [FND04-BP02 Establish an organization view of cloud inventory and dependencies](fnd04-bp02.md) 
+  [FND04-BP03 Establish standard repositories of shared resources and patterns](fnd04-bp03.md) 
+  [FND05-BP11 Establish encryption and key management standards](fnd05-bp11.md) 

 **Related documents:** 
+  [Security OU - Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) 
+  [Managing GuardDuty accounts with AWS Organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html) 
+  [What are Security Hub CSPM and Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) 
+  [Integrating AWS Security Hub CSPM with AWS Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html) 
+  [Amazon Detective and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-detective.html) 
+  [Managing multiple Macie accounts with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html) 
+  [What is AWS Security Incident Response?](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) 