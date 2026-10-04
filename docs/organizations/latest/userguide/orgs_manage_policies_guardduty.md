

# Amazon GuardDuty policies
<a name="orgs_manage_policies_guardduty"></a>

Amazon GuardDuty policies let you centrally enable and manage GuardDuty across accounts in your organization. With a GuardDuty policy, you specify which organizational entities (root, OUs, or accounts) have GuardDuty and its protection plans automatically enabled and managed through the GuardDuty delegated administrator account. You can use GuardDuty policies to simplify service-wide onboarding and ensure consistent protection coverage across all existing and newly created accounts.

## Key features and benefits
<a name="guardduty-policies-features"></a>

GuardDuty policies let you define which protection plans should be enabled for your organization or subsets of it, ensuring consistent coverage and reducing manual effort. When implemented, they help you onboard new accounts automatically and maintain your protection baseline as your organization scales. A single policy governs the GuardDuty foundational detector plus each protection plan.

The following table maps each policy key to the GuardDuty feature it governs.


**GuardDuty policy feature mapping**  

| Policy key | GuardDuty feature | 
| --- | --- | 
| foundational | GuardDuty foundational threat detection | 
| s3\_data\_events | S3 Protection | 
| eks\_audit\_logs | EKS Protection | 
| ebs\_malware\_protection | Malware Protection (EBS volumes) | 
| rds\_login\_events | RDS Protection | 
| lambda\_network\_logs | Lambda Protection | 
| ai\_protection | AI Protection | 
| runtime\_monitoring | Runtime Monitoring (with EKS, ECS Fargate, and EC2 agent management) | 

## How GuardDuty policies work
<a name="guardduty-policies-how-works"></a>

When you attach a GuardDuty policy to an organizational entity, the policy automatically enables the specified GuardDuty protection plans for all member accounts within that scope. GuardDuty policies can be applied to the entire organization (root), to specific organizational units (OUs), or to individual accounts. Accounts that join the organization, or move into an OU with an attached GuardDuty policy, automatically inherit the policy and have GuardDuty enabled and managed through the delegated administrator.

A GuardDuty policy specifies feature enablement per Region using a default with Regional override structure:
+ The `default` block sets the baseline configuration applied in every Region where GuardDuty is available.
+ Optional Region-specific blocks, keyed by Region name, override the default for those Regions. A Region-specific block fully replaces the default for that Region, so it lists every feature you want the policy to manage there.
+ The `default` block is optional. If you omit it, only the Regions you name are managed; every other Region is left unmanaged, meaning the policy neither enables nor disables GuardDuty there.
+ Foundational threat detection must be enabled in any block where any other feature is enabled.

While a GuardDuty organization policy is active, the Regional GuardDuty auto-enablement configurations no longer apply, and the per-account controls on the GuardDuty **Accounts** page are managed by the policy and shown as read-only, marked **Managed by Organization policy**.

## Terminology
<a name="guardduty-policies-terminology"></a>

This topic uses the following terms when discussing GuardDuty policies.


**GuardDuty policy terminology**  

| Term | Definition | 
| --- | --- | 
| Effective policy | The final policy that applies to an account after combining all inherited policies. | 
| Policy inheritance | The process by which accounts inherit policies from parent organizational units. | 
| Management account | The organization's root account. Designates and authorizes the delegated administrator and manages the delegation policy. | 
| Delegated administrator | The account designated to create and manage GuardDuty policies on behalf of the organization. | 
| Delegation policy | The AWS Organizations policy the management account attaches to the delegated administrator to grant it permission to manage GuardDuty policies. | 

## Use cases for GuardDuty policies
<a name="guardduty-policies-use-cases"></a>

GuardDuty policies address common threat-detection management challenges in multi-account environments. The following use cases demonstrate how organizations typically implement these policies.
+ Organizations launching large-scale workloads across multiple accounts can use a GuardDuty policy to ensure all accounts enable the correct protection plans and avoid coverage gaps.
+ Regulatory or compliance-driven environments can use child policies to adjust protection plans per OU.
+ Rapid-growth environments can automate enablement for newly created accounts so they always meet the baseline.

## Policy inheritance and enforcement
<a name="guardduty-policies-inheritance"></a>

Understanding how policies are inherited and enforced is crucial for effective threat-detection management across your organization. The inheritance model follows the AWS Organizations hierarchy.
+ Policies attached at the root level apply to all accounts.
+ Accounts inherit policies from their parent organizational units.
+ Multiple policies can apply to a single account and are merged into an effective policy.
+ More specific policies (closer to the account) take precedence.
+ When the GuardDuty policy type is enabled, it takes precedence over the Regional GuardDuty auto-enablement configuration.

## Policy validation
<a name="guardduty-policies-validation"></a>

When creating GuardDuty policies, the following validations occur:
+ Region names must be valid AWS Region identifiers.
+ Regions must be supported by Amazon GuardDuty.
+ Policy structure must follow AWS Organizations policy syntax rules.
+ Foundational threat detection must be enabled if any other feature is enabled.
+ Policy content and per-organization policy-count limits apply.

## Regional considerations and supported Regions
<a name="guardduty-policies-regions"></a>

Amazon GuardDuty policies apply only in Regions where Amazon GuardDuty and AWS Organizations trusted access are available. Understanding Regional behavior helps you implement effective threat detection across your organization's global footprint.
+ Policy enforcement occurs in each Region independently.
+ When a Regional block is specified in a policy, it completely overrides whatever is defined in the `default` block of the policy.
+ Policies only apply to Regions where Amazon GuardDuty and its respective feature is available.
+ New Regions are automatically included when using the `default` block in a policy.

GuardDuty policies are supported in all Regions where Amazon GuardDuty is available.

## Detachment behavior
<a name="guardduty-policies-detachment"></a>

If you detach an Amazon GuardDuty policy, Amazon GuardDuty remains enabled in previously covered accounts. However, future changes to the organizational structure (such as new accounts joining or existing accounts moving into the OU) no longer automatically enable Amazon GuardDuty. Any further enablement must be performed manually or through re-attaching a policy.

## Delegated administrator
<a name="guardduty-policies-delegated-admin"></a>

GuardDuty policies are managed by the AWS Organizations delegated administrator. The management account designates the delegated administrator and attaches the delegation policy that grants it permission to manage GuardDuty policies. The **Configuration policies** pages in the GuardDuty console are available only to the delegated administrator account.

## Prerequisites
<a name="guardduty-policies-prerequisites"></a>

Before you use GuardDuty policies, complete the following prerequisites:
+ Enable trusted access for the GuardDuty service in AWS Organizations.
+ Assign a delegated administrator (optional) for GuardDuty.
+ Attach the delegation policy for the delegated administrator.
+ Enable the `GUARDDUTY_POLICY` policy type on the organization root. This is done automatically when the delegated administrator creates the first policy in the GuardDuty console.

## Next steps
<a name="guardduty-policies-next-steps"></a>

To get started with GuardDuty policies:

1. Review the prerequisites in Getting started with GuardDuty policies.

1. Plan your policy strategy using the best practices guide.

1. Learn about policy syntax and view example policies.