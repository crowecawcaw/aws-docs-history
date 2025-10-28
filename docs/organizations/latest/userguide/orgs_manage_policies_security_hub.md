# Security Hub policies

AWS Security Hub policies provide security teams with a centralized approach to managing security
configurations across their AWS Organizations. By leveraging these policies, you can establish and
maintain consistent security controls through a central configuration mechanism. This
integration allows you to address security coverage gaps by creating policies that align
with your organization's security requirements and centrally applying them across accounts
and organizational units (OUs).

Security Hub policies are fully integrated with AWS Organizations, allowing management accounts or
delegated administrators to define and enforce security configurations. When accounts join
your organization, they automatically inherit the applicable policies based on their
location in the organizational hierarchy. This ensures that your security standards are
consistently applied as your organization grows. The policies respect existing
organizational structures and provide flexibility in how security configurations are
distributed, while maintaining central control over critical security settings.

## Key features and benefits

Security Hub policies provide a comprehensive set of capabilities that help you manage and
enforce security configurations across your AWS organization. These features
streamline security management while ensuring consistent control over your multi-account
environment.

- Centrally [enable Security Hub](../../../securityhub/latest/userguide/security-hub-adv-getting-started-enable.md#security-hub-adv-getting-started-enable-org-account "../../../securityhub/latest/userguide/security-hub-adv-getting-started-enable.md#security-hub-adv-getting-started-enable-org-account") across accounts and Regions in your
  organization
- Create security policies that define your security configuration across
  accounts and OUs
- Automatically apply security configurations to new accounts when they join
  your organization
- Ensure consistent security settings across your organization
- Prevent member accounts from modifying organization-level security
  configurations

## What are Security Hub policies?

Security Hub policies are AWS Organizations policies that provide centralized control over security
configurations across your organization's accounts. These policies work seamlessly with
AWS Organizations to help you establish and maintain consistent security standards throughout
your multi-account environment.

When you implement Security Hub policies, you gain the ability to define specific security
configurations that automatically propagate across your organization. This ensures that
all accounts, including newly created ones, align with your organization's security
requirements and best practices.

These policies also help you maintain compliance by enforcing consistent security
controls and preventing individual accounts from modifying organization-level security
settings. This centralized approach significantly reduces the administrative overhead of
managing security configurations across large, complex AWS environments.

## How Security Hub policies work

When you attach an Security Hub policy to your organization or organizational unit, AWS Organizations
automatically evaluates the policy and applies it based on the scope you define. The
policy enforcement process follows specific conflict resolution rules:

When regions appear in both enable and disable lists, the disable configuration takes
precedence. For example, if a region is listed in both enable and disable
configurations, Security Hub will be disabled in that region.

When `ALL_SUPPORTED` is specified for enablement, Security Hub is enabled in all
current and future regions unless explicitly disabled. This allows you to maintain
comprehensive security coverage as AWS expands into new regions.

Child policies can modify parent policy settings using inheritance operators, allowing
for granular control at different organizational levels. This hierarchical approach
ensures that specific organizational units can customize their security settings while
maintaining baseline controls.

## Terminology

This topic uses the following terms when discussing Security Hub policies.

| Security Hub policy terminology | Term                                                                                 | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Effective policy                | The final policy that applies to an account after combining all inherited policies.  |
| Policy inheritance              | The process by which accounts inherit policies from parent organizational units.     |
| Delegated administrator         | An account designated to manage Security Hub policies on behalf of the organization. |
| Service-linked role             | An IAM role that allows Security Hub to interact with other AWS services.            | ## Use cases for Security Hub policies Security Hub policies address common security management challenges in multi-account environments. The following use cases demonstrate how organizations typically implement these policies to enhance their security posture. ### Example use case: Regional compliance requirements A multinational corporation needs different Security Hub configurations for different geographical regions. They create a parent policy enabling Security Hub in all regions using `ALL_SUPPORTED`, then use child policies to disable specific regions where different security controls are required. This allows them to maintain compliance with regional regulations while ensuring comprehensive security coverage. ### Example use case: Development team security standards A software development organization implements Security Hub policies that enable monitoring in production regions while keeping development regions unmanaged. They use explicit region lists in their policies rather than `ALL_SUPPORTED` to maintain precise control over security monitoring coverage. This approach allows them to enforce stricter security controls in production environments while maintaining flexibility in development areas. ## Policy inheritance and enforcement Understanding how policies are inherited and enforced is crucial for effective security management across your organization. The inheritance model follows the AWS Organizations hierarchy, ensuring predictable and consistent policy application. <br>• Policies attached at the root level apply to all accounts <br>• Accounts inherit policies from their parent organizational units <br>• Multiple policies can apply to a single account <br>• More specific policies (closer to the account in the hierarchy) take precedence ## Policy validation When creating Security Hub policies, the following validations occur: <br>• Region names must be valid AWS region identifiers <br>• Regions must be supported by Security Hub <br>• Policy structure must follow AWS Organizations policy syntax rules <br>• Both `enable_in_regions` and `disable_in_regions` lists must be present, though they can be empty ## Regional considerations and supported Regions Security Hub policies operate across multiple Regions, requiring careful consideration of your global security requirements. Understanding regional behavior helps you implement effective security controls across your organization's global footprint. <br>• Policy enforcement occurs in each Region independently <br>• You can specify which Regions to include or exclude in your policies <br>• New Regions are automatically included when using the `ALL_SUPPORTED` option <br>• Policies only apply to Regions where Security Hub is available ## Next steps To get started with Security Hub policies: 1. Review the prerequisites in Getting started with Security Hub policies 2. Plan your policy strategy using our best practices guide 3. Learn about policy syntax and view example policies |
