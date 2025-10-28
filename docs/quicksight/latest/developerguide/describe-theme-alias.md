# DescribeThemeAlias

Use the `DescribeThemeAlias` operation to describe the alias for a
theme. To use this operation, you need the ID of the theme that is using the alias that
you want to describe. You can use the `ListThemes` operation to list all
themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-theme-alias
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
    --alias-name `ALIAS`
```

For more information about the `DescribeThemeAlias` operation, see [DescribeThemeAlias](../APIReference/API_DescribeThemeAlias.md "../APIReference/API_DescribeThemeAlias.md") in the _Quick Sight API Reference_.
