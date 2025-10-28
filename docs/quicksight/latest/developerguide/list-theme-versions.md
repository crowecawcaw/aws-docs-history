# ListThemeVersions

Use the `ListThemeVersions` operation to list all the versions of the themes in the current AWS account. To use this operation to list the versions of a theme, you need that theme's ID. You can use the `ListThemes` operation to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight list-theme-version
    --aws-account-id `AWSACCOUNTID`
    --theme-id `THEMEID`
    --page-size `10`
    --max-items `100`
```

To list all themes and their theme IDs, call the `ListThemes`
operation.

For more information about the `ListThemeVersions` operation, see [ListThemeVersions](../APIReference/API_ListThemeVersions.md "../APIReference/API_ListThemeVersions.md") in the _Quick Sight API Reference_.
