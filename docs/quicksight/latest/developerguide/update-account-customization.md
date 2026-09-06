

# UpdateAccountCustomization
<a name="update-account-customization"></a>

Use the `UpdateAccountCustomization` API operation to update Amazon Quick Sight customizations in the current AWS Region. Currently, the only customization that you can use is a theme.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-account-customization 
    --aws-account-id {{555555555555}} 
    --namespace {{NAMESPACE}} 
    --account-customization {{DEFAULTTHEME}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-account-customization
    --cli-input-json file://{{updateaccountcustomization}}.json
```

------

For more information about the `UpdateAccountCustomization` API operation, see [UpdateAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountCustomization.html) in the *Amazon Quick Sight API Reference*.