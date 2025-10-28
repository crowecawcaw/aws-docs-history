# DeleteThemeAlias

Use the `DeleteThemeAlias` operation to delete the version of the theme
that the specified theme alias points to. If you provide a specific alias, you delete
the version of the theme that the alias points to. To use this operation, you need the
ID of the theme that is using the alias that you want to delete. You can use the
`ListThemes` operation to list all themes and their corresponding theme
IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-theme-alias
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
    --alias-name `ALIAS`
```

For more information about the `DeleteThemeAlias` operation, see [DeleteThemeAlias](../APIReference/API_DeleteThemeAlias.md "../APIReference/API_DeleteThemeAlias.md") in the _Quick Sight API Reference_.
