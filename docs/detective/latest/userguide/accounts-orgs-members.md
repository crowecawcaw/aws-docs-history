# Managing organization accounts as Detective member accounts

In the organization behavior graph, the Detective administrator account determines which
organization accounts to enable as member accounts. By default, new organization accounts are not enabled as member accounts. Their status is
**Not a member**. The Detective administrator account can configure Detective to automatically enable new organization
accounts as member accounts in the organization behavior graph.

The Detective administrator can configure Detective to enable new organization accounts as member accounts
automatically. When you choose to enable organization accounts automatically, then Detective begins to enable
new accounts as member accounts as they are added to the organization. Detective does not enable
existing organization accounts that are not yet enabled.

The Detective can enable organization accounts as member accounts manually, if you do not want to automatically enable new organization accounts. They can also manually enable disassociated organization accounts. The Detective administrator cannot enable an organization account as a member account if the organization behavior graph already has the maximum 1,200 enabled accounts. In this case, the organization account status remains **Not a member**.

The Detective administrator also can disassociate organization accounts from the
organization behavior graph. To stop ingesting data from an organization account in the organization behavior graph, you
can disassociate the account. Existing data for that account remains in the behavior
graph.

###### Contents

- [Enabling new organization accounts as Detective member
  accounts](accounts-orgs-members-autoenable.md "accounts-orgs-members-autoenable.md")
- [Enabling organization accounts as Detective member
  accounts](accounts-orgs-members-enable.md "accounts-orgs-members-enable.md")
- [Disassociating organization accounts as
  Detective member accounts](accounts-orgs-members-disassociate.md "accounts-orgs-members-disassociate.md")
