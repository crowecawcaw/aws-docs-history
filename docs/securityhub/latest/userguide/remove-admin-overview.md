# Removing or changing the delegated administrator

Only the organization management account can remove the delegated Security Hub CSPM administrator account.

To change the delegated Security Hub CSPM administrator, you must first remove the current delegated administrator account and then designate a new one.

###### Warning

When you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"), you can't use the Security Hub CSPM console or Security Hub CSPM APIs to change or remove the
delegated administrator account. If the organization management account uses the AWS Organizations console or AWS Organizations APIs to change or remove the delegated Security Hub CSPM administrator,
Security Hub CSPM automatically stops central configuration, and deletes your configuration policies and policy associations. Member accounts
retain the configurations they had before the delegated administrator was changed or removed.

If you use the Security Hub CSPM console to remove the
delegated administrator in one Region, it is automatically removed in all Regions.

The Security Hub CSPM API only removes the delegated Security Hub CSPM administrator account from the Region where
the API call or command is issued. You must repeat the action in other Regions.

If you use the Organizations API to remove the delegated Security Hub CSPM administrator account, it is automatically
removed in all Regions.

## Removing the delegated administrator (Organizations API, AWS CLI)

You can use Organizations to remove the delegated Security Hub CSPM administrator in all Regions.

If you use central configuration to manage accounts, removing the delegated administrator account results in
the deletion of your configuration policies and policy associations. Member accounts
retain the configurations that they had before the delegated administrator was changed or removed. However, these accounts can't be managed by the removed delegated administrator account anymore.
They become self-managed accounts that must be configured separately in each
Region.

Choose your preferred method, and follow the instructions to remove the delegated Security Hub CSPM administrator account with AWS Organizations.

Organizations API, AWS CLI
**To remove the delegated Security Hub CSPM administrator**

From the organization management account, use the [DeregisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") operation of the Organizations API. If you're using the
AWS CLI, run the [deregister-delegated-administrator](../../../cli/latest/reference/organizations/deregister-delegated-administrator.md "../../../cli/latest/reference/organizations/deregister-delegated-administrator.md") command. Provide
the account ID of the delegated administrator, and the
service principal for Security Hub CSPM, which is
`securityhub.amazonaws.com`.

The following example removes the delegated Security Hub CSPM administrator. This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
`$` `aws organizations deregister-delegated-administrator --account-id `123456789012` --service-principal securityhub.amazonaws.com`
```

## Removing the delegated administrator (Security Hub CSPM console)

You can use the Security Hub CSPM console to remove the delegated Security Hub CSPM administrator in all Regions.

When the delegated Security Hub CSPM administrator account is removed, the member accounts are disassociated
from the removed delegated Security Hub CSPM administrator account.

Security Hub CSPM is still enabled in the member accounts. They become standalone accounts
until a new Security Hub CSPM administrator enables them as member accounts.

If the organization management account isn't an enabled account in Security Hub CSPM, then use
the option on the **Welcome to Security Hub CSPM** page.

###### To remove the delegated Security Hub CSPM administrator account from the \*\*Welcome to

Security Hub CSPM\*\* page

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. Choose **Go to Security Hub**.
3. Under **Delegated Administrator**, choose
   **Remove**.

If the organization management account is an enabled account in **Security
Hub**, then use the option on the **General** tab of the
**Settings** page.

###### To remove the delegated Security Hub CSPM administrator account from the **Settings**

page

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the Security Hub CSPM navigation pane, choose **Settings**. Then
   choose **General**.
3. Under **Delegated Administrator**, choose
   **Remove**.

## Removing the delegated administrator (Security Hub CSPM API, AWS CLI)

You can use the Security Hub CSPM API or Security Hub CSPM operations for the AWS CLI to remove the delegated Security Hub CSPM administrator. When you remove the delegated administrator with one of these methods, it is only
removed in the Region where the API call or command was issued. Security Hub CSPM doesn't update
other Regions, and it doesn't remove the delegated administrator account in AWS Organizations.

Choose your preferred method, and follow these steps to remove the delegated Security Hub CSPM administrator account with Security Hub CSPM.

Security Hub CSPM API, AWS CLI
**To remove the delegated Security Hub CSPM administrator**

From the organization management account, use the [DisableOrganizationAdminAccount](../../1.0/APIReference/API_DisableOrganizationAdminAccount.md "../../1.0/APIReference/API_DisableOrganizationAdminAccount.md") operation of the Security Hub CSPM API. If you're using the AWS CLI, run the
[disable-organization-admin-account](../../../cli/latest/reference/securityhub/disable-organization-admin-account.md "../../../cli/latest/reference/securityhub/disable-organization-admin-account.md") command. Provide
the account ID of the delegated Security Hub CSPM administrator.

The following example removes the delegated Security Hub CSPM administrator. This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
`$` `aws securityhub disable-organization-admin-account --admin-account-id `123456789012``
```
