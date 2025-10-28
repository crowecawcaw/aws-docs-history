# ListThemeAliases

Use the `ListThemeAliases` operation to list all the aliases of a
theme. To use this operation, you need the ID of the theme that is using the aliases
that you want described. You can use the `ListThemes` operation to list all
themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight list-theme-aliases
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
    --max-results `100`
```

For more information about the `ListThemeAliases` operation, see [ListThemeAliases](../APIReference/API_ListThemeAliases.md "../APIReference/API_ListThemeAliases.md") in the _Quick Sight API Reference_.
