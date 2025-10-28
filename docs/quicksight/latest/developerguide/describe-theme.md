# DescribeTheme

Use the `DescribeTheme` operation to describe a theme. To use this
operation, you need the ID of the theme that you want to describe. You can use the
`ListThemes` operation to list all themes and their corresponding theme
IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-theme
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
    --version-number `1`
    --alias-name `ALIAS`
```

The parameter value for `alias-name` can be `$LATEST`.

For more information about the `DescribeTheme` operation, see [DescribeTheme](../APIReference/API_DescribeTheme.md "../APIReference/API_DescribeTheme.md") in the _Quick Sight API Reference_.
