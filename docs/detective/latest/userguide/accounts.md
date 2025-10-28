# Managing accounts in Detective

When an account enables Detective,
it becomes the administrator account for the behavior graph, and it chooses the member accounts
for the behavior graph. An administrator account can invite accounts to join a behavior graph. When the account
accepts the invitation, Detective enables the account as a member account. Member accounts that are
added by invitation can remove themselves from the behavior graph.

When an account is enabled as a member account, Detective begins to ingest and extract the member
account's data into that behavior graph.

Each behavior graph contains data from one or more accounts. A behavior graph can have up to 1,200 member accounts.

If you are integrated with AWS Organizations, then the organization management account designates the
Detective administrator account for the organization. That Detective administrator account then becomes
the administrator account for the organization behavior graph. The Detective administrator account can
enable any organization account as a member account in the organization behavior graph.
Organization accounts cannot remove themselves from the organization behavior graph.

Detective charges each account for the data that it contributes to each behavior graph. For
information on tracking the volume of data for each account in a behavior graph, see [Forecasting and monitoring Amazon Detective costs](tracking-usage-logging.md "tracking-usage-logging.md").

###### Contents

- [Account restrictions and recommendations
  in Detective](accounts-restrictions-recommendations.md "accounts-restrictions-recommendations.md")
- [Using Organizations to manage behavior graph accounts](accounts-orgs-transition.md "accounts-orgs-transition.md")
- [Designating the Detective administrator for an
  organization](accounts-designate-admin.md "accounts-designate-admin.md")
- [Available actions for accounts](accounts-allowed-actions.md "accounts-allowed-actions.md")
- [Viewing the list of accounts](accounts-view-list.md "accounts-view-list.md")
- [Managing organization accounts as Detective member accounts](accounts-orgs-members.md "accounts-orgs-members.md")
- [Managing invited member accounts in Detective](accounts-invited-members.md "accounts-invited-members.md")
- [For member accounts: Managing behavior graph
  invitations and memberships](member-account-graph-management.md "member-account-graph-management.md")
- [Effect of account actions on behavior graphs](accounts-effects.md "accounts-effects.md")
- [Using Detective Python scripts to manage accounts](detective-github-scripts.md "detective-github-scripts.md")
