# DeleteTemplateAlias

Use the `DeleteTemplateAlias` operation to delete the item that the specified template alias points to. If you provide a specific alias, you delete the version of the template that the alias points to. To use this operation, you need the ID of the template that is using the alias you want to delete. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-template-alias
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --alias-name `ALIAS`
```

For more information about the `DeleteTemplateAlias` operation, see [DeleteTemplateAlias](../APIReference/API_DeleteTemplateAlias.md "../APIReference/API_DeleteTemplateAlias.md") in the _Quick Sight API Reference_.
