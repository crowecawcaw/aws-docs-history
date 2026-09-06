

# UpdateThemeAlias
<a name="update-theme-alias"></a>

Use the `UpdateThemeAlias` operation to update an alias of a theme. To use this operation, you need the ID of the theme that is using the alias that you want to update. You can use the `ListThemes` operation to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-theme-alias 
    --aws-account-id {{AWSACCOUNTID}} 
    --theme-id {{THEMEID}} 
    --alias-name {{ALIAS}} 
    --theme-version-number {{VERSION}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-theme-alias 
    --cli-input-json file://{{updatethemealias}}.json
```

------

For more information about the `UpdateThemeAlias` operation, see [UpdateThemeAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemeAlias) in the *Quick Sight API Reference*.