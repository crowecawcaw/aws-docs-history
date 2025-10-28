# Removing the Detective administrator

account

The organization management account can remove the current Detective administrator account in a
Region. When you remove the Detective administrator account, Detective only removes it from the current
Region. It does not change the delegated administrator account in Organizations.

When the organization management account removes the Detective administrator account in a
Region, Detective deletes the organization behavior graph. Detective is disabled for the removed Detective
administrator account.

To remove the current delegated administrator account for Detective, you use the Organizations API. When
you remove the delegated administrator account for Detective in Organizations, Detective deletes all of the
organization behavior graphs where the delegated administrator account is the Detective
administrator account. Organization behavior graphs that have the organization management
account as the Detective administrator account are not affected.

Console
From the Detective console, you can remove the Detective administrator account.

When you remove the Detective administrator account, Detective is disabled for the account, and the
organization behavior graph is deleted. The Detective administrator account is only removed in the
current Region.

###### Important

Removing a Detective administrator account does not affect the delegated administrator account
in Organizations.

###### To remove the Detective administrator account (**Enable Detective**

page)

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. Choose **Get started**.
3. Under **Delegated Administrator**, choose **Disable
   Amazon Detective**.
4. On the confirmation dialog box, enter `disable`, then choose
   **Disable Amazon Detective**.

###### To remove a Detective administrator account (**General** page)

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, under **Settings**, choose
   **General**.
3. Under **Delegated Administrator**, choose **Disable
   Amazon Detective**.
4. On the confirmation dialog box, enter `disable`, then choose
   **Disable Amazon Detective**.

Detective API, AWS CLI
To remove the Detective administrator account, you can use an API call or the AWS CLI. You must
use the organization management account credentials.

When you remove the Detective administrator account, Detective is disabled for the account, and the
organization behavior graph is deleted.

###### Important

Removing a Detective administrator account does not affect the delegated administrator account
in Organizations.

###### To remove the Detective administrator account (Detective API, AWS CLI)

- **Detective API:** Use the [`DisableOrganizationAdminAccount`](../APIReference/API_DisableOrganizationAdminAccount.md "../APIReference/API_DisableOrganizationAdminAccount.md") operation.

When you use the Detective API to remove the Detective administrator account, it is only removed
in the Region where the API call or command was issued.

- **AWS CLI:** At the command line, run the [`disable-organization-admin-account`](../../../cli/latest/reference/detective/disable-organization-admin-account.md "../../../cli/latest/reference/detective/disable-organization-admin-account.md") command.

```
aws detective disable-organization-admin-account
```

## Removing the delegated administrator account

Removing the Detective administrator account does not automatically remove the delegated
administrator account in Organizations. To remove the delegated administrator account for Detective, you can
use the Organizations API.

When you remove the delegated administrator account, this deletes all organization behavior
graphs where the delegated administrator account is the Detective administrator account. It also
disables Detective for the account in those Regions.

###### To remove the delegated administrator account (Organizations API, AWS CLI)

- **Organizations API:** Use the [`DeregisterDelegatedAdministrator`](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") operation. You must provide the
  account identifier of the Detective administrator account, and the service principal for Detective,
  which is `detective.amazonaws.com`.
- **AWS CLI:** At the command line, run the [`deregister-delegated-administrator`](../../../cli/latest/reference/organizations/deregister-delegated-administrator.md "../../../cli/latest/reference/organizations/deregister-delegated-administrator.md") command.

```
aws organizations deregister-delegated-administrator --account-id `<Detective administrator account ID>` --service-principal `<Detective service principal>`
```

**Example**

```
aws organizations deregister-delegated-administrator --account-id 777788889999 --service-principal detective.amazonaws.com
```
