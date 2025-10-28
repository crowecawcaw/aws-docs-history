# DescribeTemplatePermissions

Use the `DescribeTemplatePermission`s operation to describe
read and write permissions for a template. To use this operation, you need the ID of
the template that you want to describe the permissions of. You can use the
`ListTemplates` operation to list all templates and their
corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-template-permissions
    --aws-account-id `AWSACCOUNTID`
    --template-id `222244446666`
```

For more information about the `DescribeTemplatePermissions` operation, see [DescribeTemplatePermissions](../APIReference/API_DescribeTemplatePermissions.md "../APIReference/API_DescribeTemplatePermissions.md") in the _Quick Sight API Reference_.
