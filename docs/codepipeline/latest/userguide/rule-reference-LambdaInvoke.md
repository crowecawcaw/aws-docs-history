# LambdaInvoke

When you create a condition, you can add the `LambdaInvoke` rule. This section
provides a reference for the rule parameters. For more information about rules and
conditions, see [How do stage conditions work?](concepts-how-it-works-conditions.md "concepts-how-it-works-conditions.md").

You must have already created a function in Lambda as a separate resource.

###### Topics

- [Rule type](#rule-reference-CloudWatchAlarm-type "#rule-reference-CloudWatchAlarm-type")
- [Configuration parameters](#rule-reference-LambdaInvoke-config "#rule-reference-LambdaInvoke-config")
- [Example rule configuration](#rule-reference-LambdaInvoke-example "#rule-reference-LambdaInvoke-example")
- [See also](#rule-reference-LambdaInvoke-links "#rule-reference-LambdaInvoke-links")

## Rule type

- Category: `Rule`
- Owner: `AWS`
- Provider: `LambdaInvoke`
- Version: `1`

## Configuration parameters

**FunctionName**

Required: Yes

The name of the Lambda function.

**UserParameters**

Required: No

These are parameters that are provided as input for the function in
key-value pair format.

## Example rule configuration

YAML

```
- name: MyLambdaRule
  ruleTypeId:
    category: Rule
    owner: AWS
    provider: LambdaInvoke
    version: '1'
  configuration:
    FunctionName: my-function
  inputArtifacts:
  - name: SourceArtifact
  region: us-east-1
```

JSON

```
[
    {
        "name": "MyLambdaRule",
        "ruleTypeId": {
            "category": "Rule",
            "owner": "AWS",
            "provider": "LambdaInvoke",
            "version": "1"
        },
        "configuration": {
            "FunctionName": "my-function"
        },
        "inputArtifacts": [
            {
                "name": "SourceArtifact"
            }
        ],
        "region": "us-east-1"
    }
]
```

## See also

The following related resources can help you as you work with this rule.

- [Creating On Failure conditions](stage-conditions.md#stage-conditions-onfailure "stage-conditions.md#stage-conditions-onfailure") – This section provides
  steps for creating an On Failure condition with an alarm rule.
