# AWS Shield Network Security Director policies

AWS Shield Network Security Director helps secure your AWS environment by discovering your compute, networking, and network security resources. Network Security Director evaluates each resource's security configuration by analyzing network topology and security configurations against AWS best practices and threat intelligence.

AWS Shield Network Security Director policies allow you to centrally enable and manage Network Security Director
across accounts in your AWS organization. With a Network Security Director policy, you specify which organizational entities (root, OUs, or accounts) have Network Security Director enabled. When accounts join your organization, they automatically inherit the applicable policies based on their location in the organizational hierarchy. This ensures that your resources are analyzed for network security configuration gaps as your organization grows. The policies respect existing organizational structures and provide flexibility in determining which accounts are analyzed.

AWS Shield Network Security Director is currently available in preview.

## How it works

When you attach an AWS Shield Network Security Director policy to an organizational entity, the policy
automatically enables Network Security Director for all member accounts within that scope. Also, if you
have finalized AWS Shield Network Security Director setup by registering a delegated administrator, that
account will have centralized visibility over the network security posture of accounts in the
organization that have AWS Shield Network Security Director enabled.

AWS Shield Network Security Director policies can be applied to the entire organization, to specific
organizational units (OUs), or to individual accounts. Accounts that join the organization—or move into
an OU with an attached policy—automatically inherit the policy and have AWS Shield Network Security Director
enabled and linked to the Network Security Director delegated administrator. Network Security Director
policies allow you to enable a network analysis, view the network topology and network security findings
for your resources, and receive remediation recommendations for resolving configuration gaps. Specific
configuration settings and suppression of individual findings can be managed via the Network
Security Director delegated administrator account for the organization.

When you attach an AWS Shield Network Security Director policy to your organization or organizational
unit, AWS Organizations automatically evaluates the policy and applies it based on the scope you define.
The policy enforcement logic follows specific
conflict resolution rules:

- When regions appear in both enable and disable lists, the disable configuration takes precedence.
  For example, if a region is listed in both enable and disable configurations, AWS Shield Network Security Director will be disabled in that region.
- When `ALL_SUPPORTED` is specified for enablement, AWS Shield Network Security Director is enabled in all
  current and future regions unless explicitly disabled. This allows you to maintain comprehensive coverage as
  AWS expands into new regions.
