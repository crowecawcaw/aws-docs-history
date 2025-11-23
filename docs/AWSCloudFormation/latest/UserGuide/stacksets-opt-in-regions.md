# Prepare to perform StackSet operations in

AWS Regions that are disabled by default

AWS Regions introduced after March 20, 2019, such as Asia Pacific (Hong Kong), are
disabled by default. You must enable these Regions for your account(s)
before you can use them. For more information, see [Enable or disable
AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management Reference
Guide_.

To create a StackSet from a StackSet's administrator account (if using self-managed
permissions) or organization's management account (if using service-managed permissions)
in a Region that is disabled by default, you must first enable that
Region for the administrator or management account.

For CloudFormation to successfully create or update a stack instance:

- The target account must reside in a Region that's currently
  enabled for that target account.
- The StackSet's administrator account or organization's management account must have
  the same Region enabled as the target account.

###### Important

Be aware that during StackSet operations, administrator and target accounts exchange
metadata regarding the accounts themselves, in addition to the StackSet and StackSet
instances involved.

In addition, if you disable a Region that contains an account in
which StackSet instances reside, you are responsible for deleting any such instances or
resources, if desired. In addition, be aware that metadata regarding the target
account in the disabled Region will be retained in the administrator
account.
