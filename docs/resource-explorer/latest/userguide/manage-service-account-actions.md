# Effect of account actions on Resource Explorer

multi-account search

###### Note

It takes up to 24 hours to remove accounts and resources from multi-account search
results.

Account actions have the following effects on AWS Resource Explorer multi-account search.

## Resource Explorer disabled

When you disable Resource Explorer for an account, it is disabled only for that account in
the AWS Region that is selected when you disable it.

You must disable Resource Explorer separately in each Region where it's enabled.

After 24 hours, resources from this account won't appear in search results.

Other Resource Explorer data and settings are not removed.

## Member account is removed from an

organization

When a member account is removed from an organization, the Resource Explorer administrator
account loses permissions to view resources in the member account.

If the removed account is an administrator or delegated administrator account, all
the multi-account views previously created by these accounts will also be
removed.

Resource Explorer continues to run in both accounts.

Resource search results no longer include resources from this account.

## Account is suspended

When an account is suspended in AWS, the account loses permissions to view
resources in Resource Explorer. The administrator account for a suspended account can view the
existing resources.

For an organization account, the member account status can also change to
**Account Suspended**. This happens if the account is suspended
at the same time that the administrator account attempts to enable the account. The
administrator account for an **Account Suspended** account cannot
view resources for that account.

Otherwise, the suspended status doesn't affect the member account status.

After 90 days, the account is either deactivated or reactivated. When the account
is reactivated, its Resource Explorer permissions are restored. If the member account status is
**Account Suspended**, the administrator account must enable
the account manually.

## Account is closed

When an AWS account is closed, Resource Explorer responds to the closure as follows:

- Resource Explorer retains the resources for the account for 90 days from the
  effective date of the account closure. At the end of the 90 day period,
  Resource Explorer permanently deletes all resources for the account.
- To retain resources for more than 90 days, you can use a custom action
  with an EventBridge rule to store the resources in an Amazon S3 bucket. As long as
  Resource Explorer retains the resources, when you reopen the closed account, Resource Explorer
  restores the resources for the account.
- If the account is a Resource Explorer administrator account, it is removed as an
  administrator and all the member accounts are removed. If the account is a
  member account, it is disassociated and removed as a member from the Resource Explorer
  administrator account.
- For more information, see [Closing an
  account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md").

## Account opt-out

If an account opts-out of a Region, you will still see their resources in search
results for up to 24 hours.

After 24 hours, resources from this account won't appear in search results. For
more information, see [Opt-out behaviors](opt-in-region-considerations.md#behaviors "opt-in-region-considerations.md#behaviors").
