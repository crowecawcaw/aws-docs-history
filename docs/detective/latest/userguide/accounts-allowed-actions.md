# Available actions for accounts

Administrator and member accounts have access to the following Detective actions. In the table,
the values have the following meanings:

- **Any** – The account can perform the action for all of
  the accounts under the same Detective administrator account.
- **Self** – The account can only perform the action on
  their own account.
- Dash (–) – The account cannot perform the action.
  In the organization behavior graph, the Detective administrator account determines which
  organization accounts to enable as member accounts. They can configure Detective to enable new
  organization accounts as member accounts automatically, or they can enable organization accounts
  manually.

An administrator account can invite accounts to be member accounts in the behavior graph.
When a member account accepts the invitation and is enabled, Amazon Detective begins to ingest and
extract the member account's data into that behavior graph.

For behavior graphs other than the organization behavior graph, all of the member accounts
are invited accounts.

The following table reflects the default permissions for administrator and member accounts.
You can use custom IAM policies to restrict access further to Detective features and
functions.

| Action                                          | Administrator account (Organization)                                     | Administrator account (Invitation)           | Member (Organization)              | Member (Invitation)                |
| ----------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------- | ---------------------------------- |
| View accounts                                   | Any                                                                      | Any                                          | Self (View administrator accounts) | Self (View administrator accounts) |
| Remove member account                           | Any Invited accounts are removed Organization accounts are disassociated | Any                                          | –                                  | Self                               |
| Add or remove optional data source packages     | Any (Setting applies to all member accounts)                             | Any (Setting applies to all member accounts) | –                                  | –                                  |
| Disable Detective                               | Self                                                                     | Self                                         | –                                  | –                                  |
| View behavior graph data                        | Any                                                                      | Any                                          | –                                  | –                                  |
| Enable or disable optional data source packages | All                                                                      | All                                          | –                                  | –                                  |
