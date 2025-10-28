# Understanding management policy

inheritance

###### Important

The information in this section does **_not_** apply to authorization policies: service control
policies (SCPs) and resource control policies (RCPs). For more information about how
SCPs and RCPs work in an AWS Organizations hierarchy, see [SCP evaluation](orgs_manage_policies_scps_evaluation.md "orgs_manage_policies_scps_evaluation.md") and [RCP evaluation](orgs_manage_policies_rcps_evaluation.md "orgs_manage_policies_rcps_evaluation.md").

You can attach management policies to organization entities (organization root,
organizational unit (OU), or account) in your organization:

- When you attach a management policy to the organization root, all OUs and accounts
  in the organization inherit that policy.
- When you attach a management policy to a specific OU, accounts that are directly
  under that OU or any child OU inherit the policy.
- When you attach a management policy to a specific account, it affects only that
  account.
  Because you can attach management policies to multiple levels in the organization,
  accounts can inherit multiple policies.

This following topics explain how parent policies and child policies are processed into
the effective policy for an account.

###### Topics

- [Terminology](inheritance-terminology.md "inheritance-terminology.md")
- [Management policy types](syntax-inheritance.md "syntax-inheritance.md")
- [Inheritance operators](policy-operators.md "policy-operators.md")
- [Inheritance examples](inheritance-examples.md "inheritance-examples.md")
