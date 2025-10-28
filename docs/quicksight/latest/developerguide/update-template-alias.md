# UpdateTemplateAlias

Use the `UpdateTemplateAlias` operation to update the template alias of
a template. To use this operation, you need the ID of the template that is using the
alias that you want to update. You can use the `ListTemplates` operation to
list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-template-alias
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --alias-name `ALIAS`
    --template-version-number `VERSION`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-template-alias
    --cli-input-json file://`updatetemplatealias`.json
```

The parameter value for `alias-name` can be `$LATEST`.

For more information about the `UpdateTemplateAlias` operation, see [UpdateTemplateAlias](../APIReference/API_UpdateTemplateAlias.md "../APIReference/API_UpdateTemplateAlias.md") in the _Quick Sight API Reference_.
