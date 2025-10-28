# UpdateTemplatePermissions

Use the `UpdateTemplatePermissions` operation updates the
resource permissions for a template. You can grant or revoke permissions in the same
command. To use this operation, you need the ID of the template that you want to
update the permissions of. You can use the `ListTemplates` operation to
list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-template-permissions
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --grant-permissions Principal=arn:aws:quicksight:``us-east-1``:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=DescribeTemplate
    --revoke-permissions Principal=arn:aws:quicksight:``us-east-1``:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=DescribeTemplate
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-template-permissions
    --cli-input-json file://`updatetemplatepermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information on the `UpdateTemplatePermissions` operation, see [UpdateTemplatePermissions](../APIReference/API_UpdateTemplatePermissions.md "../APIReference/API_UpdateTemplatePermissions.md") in the _Quick Sight API Reference_.
