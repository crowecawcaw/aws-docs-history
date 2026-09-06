

# DeleteTemplate
<a name="delete-template"></a>

Use the `DeleteTemplate` operation to delete a template. To use this operation, you need the ID of the template that you want to delete. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-template 
    --aws-account-id {{AWSACCOUNTID}} 
    --template-id {{TEMPLATEID}}
```

------

For more information about the `DeleteTemplate` operation, see [DeleteTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTemplate.html) in the *Quick Sight API Reference*.