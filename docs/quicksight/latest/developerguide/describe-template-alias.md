# DescribeTemplateAlias

Use the `DescribeTemplateAlias` operation to describe the template
alias for a template. To use this operation, you need the ID of the template that is
using the alias that you want to describe. You can use the `ListTemplates`
operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-template-alias
    --aws-account-id `AWSACCOUNTID`
    --template-id `222244446666`
    --alias-name `ALIAS`
```

The parameter value for `alias-name` can be `$LATEST`.

For more information about the `DescribeTemplateAlias` operation, see [DescribeTemplateAlias](../APIReference/API_DescribeTemplateAlias.md "../APIReference/API_DescribeTemplateAlias.md") in the _Quick Sight API Reference_.
