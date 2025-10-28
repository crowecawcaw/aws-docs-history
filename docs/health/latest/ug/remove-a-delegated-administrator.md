# Removing a delegated administrator from your

organizational view

To remove access for a delegated administrator, call the [DeregisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") API operation.

From your organization's management account, call the following AWS CLI command to remove a
member account as delegated administrator. In the following example command, replace **ACCOUNT_ID** with the member account ID that you want to remove.

```
aws organizations deregister-delegated-administrator --account-id ACCOUNT_ID --service-principal  health.amazonaws.com
```
