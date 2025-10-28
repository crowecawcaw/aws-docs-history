# ListTemplateAliases

Use the `ListTemplateAliases` operation to list all the aliases of a
template. To use this operation, you need the ID of the template that is using the
aliases that you want to list. You can use the `ListTemplates` operation to
list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight list-template-aliases
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --page-size `10`
    --max-items `100`
```

For more information about the `ListTemplateAliases` operation, see [ListTemplateAliases](../APIReference/API_ListTemplateAliases.md "../APIReference/API_ListTemplateAliases.md") in the _Quick Sight API Reference_.
