

# UpdateTemplate
<a name="update-template"></a>

Use the `UpdateTemplate` operation to update a template from an existing Quick Sight analysis or another template.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-template
    --aws-account-id {{555555555555}}
    --template-id {{TEMPLATEID}}
    --source-entity {{SOURCEENTITY}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-template
    --cli-input-json file://{{updatetemplate}}.json
```

------

For more information about the `UpdateTemplate` operation, see [UpdateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplate.html) in the *Quick Sight API Reference*.