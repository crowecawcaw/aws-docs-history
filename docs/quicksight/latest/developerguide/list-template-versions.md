# ListTemplateVersions

Use the `ListTemplateVersions` operation to list all the versions of the templates in the current Quick Sight account. To use this operation to list the versions of a template, you need that template's ID. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight list-template-versions
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --page-size `10`
    --max-items `100`
```

For more information about the `ListTemplateVersions` operation, see [ListTemplateVersions](../APIReference/API_ListTemplateVersions.md "../APIReference/API_ListTemplateVersions.md") in the _Quick Sight API Reference_.
