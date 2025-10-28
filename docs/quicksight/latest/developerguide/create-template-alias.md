# CreateTemplateAlias

Use the `CreateTemplateAlias` operation to create a template alias for
a template. To use this operation, you need the ID of the template that you want to
create an alias for. You can use the `ListTemplates` operation to list all
templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-template-alias
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --alias-name `ALIAS`
    --template-version-number `VERSION`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-template-alias
    --cli-input-json file://`createtemplatealias`.json
```

For more information about the `CreateTemplateAlias` operation, see [CreateTemplateAlias](../APIReference/API_CreateTemplateAlias.md "../APIReference/API_CreateTemplateAlias.md") in the _Quick Sight API Reference_.
