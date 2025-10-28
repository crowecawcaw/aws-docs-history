# Managing invited member accounts in Detective

A Detective administrator account can invite accounts to be member accounts in their behavior graph. A behavior graph can contain up to 1,200 member accounts. When a member account accepts the invitation and is enabled, Amazon Detective begins to ingest and extract the member account's data into that behavior graph.

To invite individual accounts, you can manually specify the member accounts to invite to contribute their data to a behavior graph. If you want to add a list of member accounts, you can choose to provide a .csv file containing a list of member accounts to invite to your behavior graph.

For behavior graphs other than the organization behavior graph, all of the member accounts
are invited accounts.The Detective administrator account can also invite accounts that are not organization accounts to the organization behavior graph.

At a high level, the process for inviting accounts to contribute to a behavior graph is as
follows.

1. For each member account to add, the administrator account provides the AWS account
   identifier and the root user email address.
2. Detective validates that the email address is the root user email address for the account. If
   the account information is valid, Detective sends the invitation to the member account.

Detective does not perform this validation or sends email invitations to member accounts
in these Regions:

    * AWS GovCloud (US-East) Region
    * AWS GovCloud (US-West) Region

For other Regions, you can `DisableEmailNotification` using the [CreateMembers](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md") operation of the Detective API. If
`DisableEmailNotification` is set to true, then Detective will not send
invitations to the member accounts. This is a useful setting for accounts that are managed
centrally. 3. The member account accepts or declines the invitation.

Even if the administrator account does not send invitation emails, the member account
still must respond to the invitation. 4. After the member account accepts the invitation, Detective begins to ingest data from the
member account into the behavior graph. 5. As soon as the member account is eligible to be enabled, Detective automatically changes
the member account status to **Enabled**.

For example, the member account status changes to **Enabled** if the administrator account removes other member accounts to make
space for an account.

If more than one account is **Not enabled**, then Detective
enables the accounts in the order in which they were invited. The process to check whether
to enable any **Not enabled** accounts runs every
hour.

The administrator account also can enable accounts manually, instead of waiting for
the automatic process. For example, the administrator account might want to select the
accounts to enable. For information on how to enable a member account, see [Enabling a member account that is Not
enabled](graph-admin-unblock-account.md "graph-admin-unblock-account.md").

Note that Detective began to automatically enable accounts that are **Not enabled** on May 12, 2021. Accounts that were **Not
enabled** before then are not enabled automatically. The administrator account
must enable them manually.
The administrator account can remove invited member accounts from the behavior graph. Detective does not remove any existing data from the behavior graph, which aggregates data across member accounts.

###### Contents

- [Inviting individual accounts to a
  behavior graph](accounts-invited-members-add-individual.md "accounts-invited-members-add-individual.md")
- [Inviting a list of member accounts to a
  behavior graph](accounts-invited-members-add-csv.md "accounts-invited-members-add-csv.md")
- [Enabling a member account that is Not
  enabled](graph-admin-unblock-account.md "graph-admin-unblock-account.md")
- [Removing member accounts from a behavior
  graph](accounts-invited-remove.md "accounts-invited-remove.md")
