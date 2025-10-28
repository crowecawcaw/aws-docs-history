# Template alias operations

A _template alias_ is a reference to a version of a template. For
example, suppose that you create the template alias `exampleAlias` for version 1
of the template `exampleTemp`. You can use the template alias
`exampleAlias` to reference version 1 of template `exampleTemp` in
a `DescribeTemplate` API operation, as in the following example.

```
aws quicksight describe-template
    --aws-account-id `AWSACCOUNTID`
    --template-id `exampleTempID`
    --alias-name `exampleAlias`
```

With template alias API operations, you can perform actions on Quick Sight template aliases.
For more information, see the following API operations.

###### Topics

- [CreateTemplateAlias](create-template-alias.md "create-template-alias.md")
- [DeleteTemplateAlias](delete-template-alais.md "delete-template-alais.md")
- [DescribeTemplateAlias](describe-template-alias.md "describe-template-alias.md")
- [ListTemplateAliases](list-template-aliases.md "list-template-aliases.md")
- [UpdateTemplateAlias](update-template-alias.md "update-template-alias.md")
