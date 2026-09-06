

# UpdateAccountSettings
<a name="update-account-settings"></a>

Use the `UpdateAccountSettings` API operation to update the Amazon Quick Sight settings in your AWS account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-account-settings 
    --aws-account-id {{555555555555}} 
    --default-namespace {{NAMESPACE}} 
    --notification-email {{EMAIL}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-account-settings
    --cli-input-json file://{{updateaccountsettings}}.json
```

------

For more information about the `UpdateAccountSettings` API operation, see [UpdateAccountSettings](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountSettings.html) in the *Amazon Quick Sight API Reference*.