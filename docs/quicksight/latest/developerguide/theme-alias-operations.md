# Theme alias operations

A _theme alias_ is a reference to a version of a theme. For example,
suppose that you create the theme alias `exampleAlias`
for version 1 of the theme `exampleTheme`. You can use the theme alias
`exampleAlias` to reference version 1 of theme
exampleTheme in a `DescribeTheme` API operation, as in the following
example.

###### Example

```
aws quicksight describe-theme
    --aws-account-id `AWSACCOUNTID`
    --theme-id `exampleThemeID`
    --alias-name `exampleAlias`
```

With theme alias operations, you can perform actions on Quick Sight theme aliases. For more
information, see the following API operations.

###### Topics

- [CreateThemeAlias](create-theme-alias.md "create-theme-alias.md")
- [DeleteThemeAlias](delete-theme-alias.md "delete-theme-alias.md")
- [DescribeThemeAlias](describe-theme-alias.md "describe-theme-alias.md")
- [ListThemeAliases](list-theme-aliases.md "list-theme-aliases.md")
- [UpdateThemeAlias](update-theme-alias.md "update-theme-alias.md")
