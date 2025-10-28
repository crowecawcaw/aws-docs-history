# UpdateAccountSettings

Use the `UpdateAccountSettings` API operation to update the Amazon Quick Sight settings in your AWS account. Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-account-settings
    --aws-account-id `555555555555`
    --default-namespace `NAMESPACE`
    --notification-email `EMAIL`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-account-settings
    --cli-input-json file://`updateaccountsettings`.json
```

For more information about the `UpdateAccountSettings` API operation, see [UpdateAccountSettings](../APIReference/API_UpdateAccountSettings.md "../APIReference/API_UpdateAccountSettings.md") in the _Amazon Quick Sight API Reference_.
