# UpdateThemePermissions

Use the `UpdateThemePermissions` operation to update the resource
permissions for a template. You can grant or revoke permissions in the same command.
To use this operation, you need the ID of the theme that you want to update. You can
use the `ListThemes` operation to list all themes and their corresponding
theme IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-theme-permissions
    --aws-account-id `555555555555`
    --theme-id `111122223333`
    --grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:ListThemeVersions, quicksight:UpdateThemeAlias, quicksight: DescribeThemeAlias, quicksight:UpdateThemePermissions, quicksight:DeleteThemeAlias, quicksight: DeleteTheme, quicksight:ListThemeAliases, quicksight:DescribeTheme, quicksight: CreateThemeAlias, quicksight:UpdateTheme, quicksight: DescribeThemePermissions
    --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:ListThemeVersions, quicksight:UpdateThemeAlias, quicksight: DescribeThemeAlias, quicksight:UpdateThemePermissions, quicksight:DeleteThemeAlias, quicksight: DeleteTheme, quicksight:ListThemeAliases, quicksight:DescribeTheme, quicksight: CreateThemeAlias, quicksight:UpdateTheme, quicksight: DescribeThemePermissions
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-theme-permissions
    --cli-input-json file//:`updatethemepermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information on the `UpdateThemePermissions` operation, see [UpdateThemePermissions](../APIReference/API_UpdateThemePermissions.md "../APIReference/API_UpdateThemePermissions.md") in the _Quick Sight API Reference_.
