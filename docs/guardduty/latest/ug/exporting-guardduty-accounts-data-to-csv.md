# GuardDuty considerations for

exporting member account details in CSV format

As a GuardDuty administrator account, you can export the member account details in a CSV format. These
details include the member account ID, name, type (added by AWS Organizations or through invitation),
and configuration status of GuardDuty and dedicated protection plans.

The **Export CSV** option is displayed on the GuardDuty
**Accounts** page based on how you manage the multiple member accounts.
By using the **Export CSV** option, you can identify which member accounts
have a specific protection plan enabled.

The following list provides the criteria whether or not the **Export
CSV** will be available on your GuardDuty **Accounts**
page:

- You use only AWS Organizations to manage multiple member accounts and the total number of
  member accounts in your GuardDuty organization are up to 5,000.
- You use both AWS Organizations and invitations method, and the total number of member
  accounts in your GuardDuty organization are up to 5,000.

In this scenario, the exported CSV will include whether a member account was added
through AWS Organizations or by using invitation-based method.

- When you use only the invitation-based method to manage multiple member accounts,
  there is no **Export CSV** option.
