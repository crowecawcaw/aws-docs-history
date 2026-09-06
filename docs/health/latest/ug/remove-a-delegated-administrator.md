

# Removing a delegated administrator from your organizational view
<a name="remove-a-delegated-administrator"></a>

To remove access for a delegated administrator, call the [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html) API operation.

From your organization's management account, call the following AWS CLI command to remove a member account as delegated administrator. In the following example command, replace **ACCOUNT\_ID** with the member account ID that you want to remove.

```
aws organizations deregister-delegated-administrator --account-id ACCOUNT_ID --service-principal  health.amazonaws.com 
```