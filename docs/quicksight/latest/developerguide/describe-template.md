# DescribeTemplate

Use the `DescribeTemplate` operation to describe a template's
metadata. To use this operation, you need the ID of the template that you want to
describe. You can use the `ListTemplates` operation to list all templates and
their corresponding template IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-template
    --aws-account-id `AWSACCOUNTID`
    --template-id `TEMPLATEID`
    --version-number `VERSION`
    --alias-name `ALIAS`
```

The parameter value for `alias-name` can be `$LATEST`.

For more information about the `DescribeTemplate` operation, see [DescribeTemplate](../APIReference/API_DescribeTemplate.md "../APIReference/API_DescribeTemplate.md") in the _Quick Sight API Reference_.
