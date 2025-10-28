# DescribeThemePermissions

Use the `DescribeThemePermissions` operation to describe the read
and write permissions for a theme. To use this operation, you need the ID of the
theme that you want to describe. You can use the `ListThemes` operation
to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-theme-permissions
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
```

For more information about the `UpdateThemePermissions` operation,
see [UpdateThemePermissions](../APIReference/API_UpdateThemePermissions.md "../APIReference/API_UpdateThemePermissions.md") in the*Quick Sight API Reference*.
