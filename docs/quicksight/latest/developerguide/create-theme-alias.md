# CreateThemeAlias

The `CreateThemeAlias` operation creates a theme alias for a theme. To
use this operation, you need the ID of the theme that you want to create an alias for.
You can use the `ListThemes` operation to list all themes and their
corresponding theme IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
    --alias-name `ALIAS`
    --theme-version-number `VERSION`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-theme-alias
    --cli-input-json file://`create-theme-alias`.json
```

For more information about the `CreateThemeAlias` operation, see [CreateThemeAlias](../APIReference/API_CreateThemeAlias.md "../APIReference/API_CreateThemeAlias.md") in the _Quick Sight API Reference_.
