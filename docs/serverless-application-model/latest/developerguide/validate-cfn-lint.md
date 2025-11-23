# Validate your AWS SAM applications with CloudFormation Linter

AWS CloudFormation Linter (cfn-lint) is an open-source tool that you can use to perform detailed validation on your CloudFormation
templates. Cfn-lint contains rules that are guided by the CloudFormation resource specification. Use cfn-lint to compare your
resources against those rules to receive detailed messages on errors, warnings, or informational suggestions.
Alternatively, create your own custom rules to validate against. To learn more about cfn-lint, see
[cfn-lint](https://github.com/aws-cloudformation/cfn-lint "https://github.com/aws-cloudformation/cfn-lint")
in the _CloudFormation GitHub repository_.

You can use cfn-lint to validate your AWS Serverless Application Model (AWS SAM) templates through the AWS SAM Command Line Interface (AWS SAM CLI)
by running **sam validate** with the **--lint** option.

```
sam validate --lint
```

To customize cfn-lint behavior, such as creating custom rules or specifying validation options, you can define a
configuration file. To learn more, see
[Config File](https://github.com/aws-cloudformation/cfn-lint#config-file "https://github.com/aws-cloudformation/cfn-lint#config-file")
in the _cfn-lint CloudFormation GitHub repository_. When you run **sam validate --lint**,
cfn-lint behavior defined in your configuration file will be applied.

## Examples

### Perform cfn-lint validation on an AWS SAM template

```
sam validate --lint --template myTemplate.yaml
```

## Learn more

To learn more about the **sam validate** command, see
[sam validate](sam-cli-command-reference-sam-validate.md "sam-cli-command-reference-sam-validate.md").
