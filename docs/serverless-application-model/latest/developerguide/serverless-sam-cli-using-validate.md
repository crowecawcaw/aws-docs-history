# Validate AWS SAM template files

Validate your templates with `sam validate`. Currently, this command
validates that the template provided is valid JSON / YAML. As with most AWS SAM CLI
commands, it looks for a `template.[yaml|yml]` file in your current working
directory by default. You can specify a different template file/location with the
`-t` or `--template` option.

Example:

```
`$` `sam validate`
`<path-to-template>`/template.yaml is a valid SAM Template
```

###### Note

The `sam validate` command requires AWS credentials to be configured.
For more information, see [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md").
