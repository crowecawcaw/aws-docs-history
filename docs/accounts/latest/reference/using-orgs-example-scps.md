# Restrict access using AWS Organizations service control

policies

This topic presents examples that show how you can use service control policies (SCPs) in
AWS Organizations to restrict what the users and roles in the accounts in your organization can do.
For more information about service control policies, see the following topics in the
_AWS Organizations User Guide_:

- [Creating
  SCPs](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md")
- [Attaching SCPs to OUs
  and accounts](../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md")
- [Strategies for
  SCPs](../../../organizations/latest/userguide/orgs_manage_policies_scps_strategies.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_strategies.md")
- [SCP policy
  syntax](../../../organizations/latest/userguide/orgs_manage_policies_scps_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_syntax.md")

###### Example 1: Prevent accounts from modifying their own alternate contacts

The following example denies the `PutAlternateContact` and
`DeleteAlternateContact` API operations from being called by any member
account in [standalone account
mode](manage-acct-api-modes-of-operation.md "manage-acct-api-modes-of-operation.md"). This prevents any principal in the affected accounts from changing
their own alternate contacts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Deny",
 "Action": [
 "account:PutAlternateContact",
 "account:DeleteAlternateContact"
 ],
 "Resource": [ "arn:aws:account::*:account" ]
 }
 ]
}`

```

###### Example 2: Prevent any member account from modifying alternate contacts for any other member account in the organization

The following example generalizes the `Resource` element to "\*", which
means that it applies to both [standalone mode requests and organizations mode requests](manage-acct-api-modes-of-operation.md "manage-acct-api-modes-of-operation.md"). This means that
even the delegated admin account for Account Management, if the SCP applies to it, is blocked from
changing any alternate contact for any account in the organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Deny",
 "Action": [
 "account:PutAlternateContact",
 "account:DeleteAlternateContact"
 ],
 "Resource": [ "*" ]
 }
 ]
}`

```

###### Example 3: Prevent a member account in an OU from modifying its own alternate contacts

The following example SCP includes a condition that compares the account's
organization path to a list of two OUs. This results in blocking a principal in any
account in the specified OUs from modifying their own alternate contacts.
