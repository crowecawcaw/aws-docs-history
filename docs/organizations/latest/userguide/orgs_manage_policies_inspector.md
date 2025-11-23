# Amazon Inspector policies

Amazon Inspector policies allow you to centrally enable and manage Amazon Inspector across accounts in your AWS organization. With an Amazon Inspector policy, you specify which organizational entities (root, OUs, or accounts) have Amazon Inspector automatically enabled and linked to the Amazon Inspector delegated administrator account. You can use Amazon Inspector policies to simplify service-wide onboarding and ensure consistent enablement of Amazon Inspector in all existing and newly created accounts.

## Key Features and Benefits

Amazon Inspector policies let you define which scan types should be enabled for your organization or subsets of it, ensuring consistent coverage and reducing manual effort. When implemented, they help you onboard new accounts automatically and maintain your scanning baseline as your organization scales.

## How it works

When you attach an Amazon Inspector policy to an organizational entity, the policy automatically enables Amazon Inspector for all member accounts within that scope. Also, if you have finalized Amazon Inspector setup by registering a delegated administrator for Amazon Inspector, that account will have centralized vulnerability visibility over accounts in the organization that have Amazon Inspector enabled.

Amazon Inspector policies can be applied to the entire organization, to specific organizational units (OUs), or to individual accounts. Accounts that join the organization—or move into an OU with an attached Amazon Inspector policy—automatically inherit the policy and have Amazon Inspector enabled and linked to the Amazon Inspector delegated administrator. Amazon Inspector policies allow you to enable Amazon EC2 scanning, Amazon ECR scanning, or Lambda Standard and code scanning, as well as Code Security. Specific configuration settings and suppression rules can be managed via the delegated administrator account for the organization.

When you attach an Amazon Inspector policy to your organization or organizational unit, AWS Organizations
automatically evaluates the policy and applies it based on the scope you define. The policy enforcement process follows specific conflict resolution rules:

- When regions appear in both enable and disable lists, the disable configuration takes precedence. For example, if a region is listed in both enable and disable configurations, Amazon Inspector will be disabled in that region.
- When `ALL_SUPPORTED` is specified for enablement, Amazon Inspector is enabled in all current and future
  regions unless explicitly disabled. This allows you to maintain comprehensive coverage as AWS
  expands into new regions.
- Child policies can modify parent policy settings using inheritance operators, allowing for granular control at different organizational levels. This hierarchical approach ensures that specific organizational units can customize their security settings while maintaining baseline controls.

### Terminology

This topic uses the following terms when discussing Amazon Inspector policies.

| Term                    | Definition                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| Effective policy        | The final policy that applies to an account after combining all inherited policies.      |
| Policy inheritance      | The process by which accounts inherit policies from parent organizational units.         |
| Delegated administrator | An account designated to manage Amazon Inspector policies on behalf of the organization. |
| Service-linked role     | An IAM role that allows Amazon Inspector to interact with other AWS services.            |

### Use cases for Amazon Inspector policies

Organizations launching large-scale workloads across multiple accounts can use this policy to ensure all accounts immediately enable the correct scan types and avoid gaps. Regulatory or compliance-driven environments can use child policies to override or limit scan-types by OU. Rapid growth environments can automate enablement for newly created accounts so they're always compliant with the baseline.

### Policy inheritance and enforcement

Understanding how policies are inherited and enforced is crucial for effective security management
across your organization. The inheritance model follows the AWS Organizations hierarchy, ensuring
predictable and consistent policy application.

- Policies attached at the root level apply to all accounts
- Accounts inherit policies from their parent organizational units
- Multiple policies can apply to a single account
- More specific policies (closer to the account in the hierarchy) take precedence

### Policy validation

When creating Amazon Inspector policies, the following validations occur:

- Region names must be valid AWS region identifiers
- Regions must be supported by Amazon Inspector
- Policy structure must follow AWS Organizations policy syntax rules
- Both `enable_in_regions` and `disable_in_regions` lists must be present, though they can be empty

### Regional considerations and supported Regions

Amazon Inspector policies apply only in Regions where Amazon Inspector and AWS Organizations trusted access are available. Understanding regional behavior helps you implement effective security controls across your organization's global footprint.

- Policy enforcement occurs in each Region independently
- You can specify which Regions to include or exclude in your policies
- New Regions are automatically included when using the `ALL_SUPPORTED` option
- Policies only apply to Regions where Amazon Inspector is available

### Detachment behavior

If you detach an Amazon Inspector policy, Amazon Inspector remains enabled in previously covered accounts. However, future changes to the organizational structure (such as new accounts joining or existing accounts moving into the OU) will no longer automatically enable Amazon Inspector. Any further enablement must be performed manually or through re-attaching a policy.

## Additional details

### Delegated Administrator

Only one delegated administrator can be registered for Amazon Inspector in an organization. You must configure this in the Amazon Inspector console or via APIs before attaching Amazon Inspector policies.

### Prerequisites

You must enable trusted access for AWS Organizations, have a delegated administrator for Amazon Inspector registered, and have service-linked roles available in all accounts.

### Supported Regions

All Regions where Amazon Inspector is available.
