# Inheritance terminology

This topic uses the following terms when discussing management policy
inheritance.

**Policy inheritance**

The interaction of policies at differing levels of an organization, moving
from the top-level root of the organization, down through the organizational
unit (OU) hierarchy to individual accounts.

You can attach policies to the organization root, OUs, individual
accounts, and to any combination of these organization entities. Policy
inheritance refers to management policies that are attached to the
organization root or to an OU. All accounts that are members of the
organization root or OU where a management policy is attached
_inherit_ that policy.

For example, when management policies are attached to the organization
root, all accounts in the organization inherit that policy. That's because
all accounts in an organization are always under the organization root. When
you attach a policy to a specific OU, accounts that are directly under that
OU or any child OU inherit that policy. Because you can attach policies to
multiple levels in the organization, accounts might inherit multiple policy
documents for a single policy type.

**Parent policies**

Policies that are attached higher in the organizational tree than policies
that are attached to entities lower in the tree.

For example, if you attach management policy A to the organization root,
it's just a policy. If you also attach policy B to an OU under that root,
policy A is the parent policy of Policy B. Policy B is the child policy of
Policy A. Policy A and policy B merge to create the effective tag policy for
accounts in the OU.

**Child policies**

Policies that are attached at a lower level in the organization tree than
the parent policy.

**Effective policies**

The final, single policy document that specifies the rules that apply to
an account. The effective policy is the aggregation of any policies the
account inherits, plus any policy that is directly attached to the account.
For more information, see [Viewing effective management
policies](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

**Inheritance operators**

Operators that control how inherited policies merge into a single
effective policy. These operators are considered an advanced feature.
Experienced policy authors can use them to limit what changes a child policy
can make and how settings in policies merge. For more information, see [Inheritance operators](policy-operators.md "policy-operators.md").
