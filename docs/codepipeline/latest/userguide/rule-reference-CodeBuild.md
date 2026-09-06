

# CodeBuild rule
<a name="rule-reference-CodeBuild"></a>

When you create a condition, you can add the CodeBuild rule. This section provides a reference for the rule parameters. For more information about rules and conditions, see [How do stage conditions work?](concepts-how-it-works-conditions.md).

You can use the CodeBuild rule to create a condition where the succesful run of your build project meets the rule criteria, such as the build run being successful for a beforeEntry condition.

**Note**  
For beforeEntry conditions that are configured with the **Skip** result, only the following rules are available: `LambdaInvoke` and `VariableCheck`.

**Topics**
+ [Service role policy permissions](#rule-reference-Commands-policy)
+ [Rule type](#rule-reference-Commands-type)
+ [Configuration parameters](#rule-reference-Commands-config)
+ [Example rule configuration](#rule-reference-Commands-example)
+ [See also](#rule-reference-Commands-links)

## Service role policy permissions
<a name="rule-reference-Commands-policy"></a>

For permissions for this rule, add the following to your CodePipeline service role policy statement. Scope down permissions to the resource level.

```
{
    "Effect": "Allow",
    "Action": [
        "codebuild:BatchGetBuilds",
        "codebuild:StartBuild"
    ],
    "Resource": "{{resource_ARN}}"
},
```

## Rule type
<a name="rule-reference-Commands-type"></a>
+ Category: `Rule`
+ Owner: `AWS`
+ Provider: `CodeBuild`
+ Version: `1`

## Configuration parameters
<a name="rule-reference-Commands-config"></a>

**ProjectName**  
Required: Yes  
`ProjectName` is the name of the build project in CodeBuild.

**PrimarySource**  
Required: Conditional  
The value of the `PrimarySource` parameter must be the name of one of the input artifacts to the action. CodeBuild looks for the buildspec file and runs the buildspec commands in the directory that contains the unzipped version of this artifact.  
This parameter is required if multiple input artifacts are specified for a CodeBuild action. When there is only one source artifact for the action, the `PrimarySource` artifact defaults to that artifact.

**BatchEnabled**  
Required: No  
The Boolean value of the `BatchEnabled` parameter allows the action to run multiple builds in the same build execution.  
When this option is enabled, the `CombineArtifacts` option is available.  
For pipeline examples with batch builds enabled, see [CodePipeline integration with CodeBuild and batch builds](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-pipeline-batch.html).

**CombineArtifacts**  
Required: No  
The Boolean value of the `CombineArtifacts` parameter combines all build artifacts from a batch build into a single artifact file for the build action.  
To use this option, the `BatchEnabled` parameter must be enabled.

**EnvironmentVariables**  
Required: No  
The value of this parameter is used to set environment variables for the CodeBuild action in your pipeline. The value for the `EnvironmentVariables` parameter takes the form of a JSON array of environment variable objects. See the example parameter in [Action declaration (CodeBuild example)](action-reference-CodeBuild.md#action-reference-CodeBuild-example).  
Each object has three parts, all of which are strings:  
+ `name`: The name or key of the environment variable. 
+ `value`: The value of the environment variable. When using the `PARAMETER_STORE` or `SECRETS_MANAGER` type, this value must be the name of a parameter you have already stored in AWS Systems Manager Parameter Store or a secret you have already stored in AWS Secrets Manager, respectively.
**Note**  
We strongly discourage the use of environment variables to store sensitive values, especially AWS credentials. When you use the CodeBuild console or AWS CLI, environment variables are displayed in plain text. For sensitive values, we recommend that you use the `SECRETS_MANAGER` type instead. 
+ `type`: (Optional) The type of environment variable. Valid values are `PARAMETER_STORE`, `SECRETS_MANAGER`, or `PLAINTEXT`. When not specified, this defaults to `PLAINTEXT`.
When you enter the `name`, `value`, and `type` for your environment variables configuration, especially if the environment variable contains CodePipeline output variable syntax, do not exceed the 1000-character limit for the configuration’s value field. A validation error is returned when this limit is exceeded.
For more information, see [ EnvironmentVariable](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html) in the AWS CodeBuild API Reference. For an example CodeBuild action with an environment variable that resolves to the GitHub branch name, see [Example: Use a BranchName variable with CodeBuild environment variables](actions-variables.md#actions-variables-examples-env-branchname).

## Example rule configuration
<a name="rule-reference-Commands-example"></a>

------
#### [ YAML ]

```
name: codebuild-rule
ruleTypeId:
  category: Rule
  owner: AWS
  provider: CodeBuild
  version: '1'
configuration:
  ProjectName: my-buildproject
  EnvironmentVariables: '[{"name":"VAR1","value":"variable","type":"PLAINTEXT"}]'
inputArtifacts:
- name: SourceArtifact
region: us-east-1
```

------
#### [ JSON ]

```
{
    "name": "codebuild-rule",
    "ruleTypeId": {
        "category": "Rule",
        "owner": "AWS",
        "provider": "CodeBuild",
        "version": "1"
    },
    "configuration": {
        "ProjectName": "my-buildproject"
    },
    "inputArtifacts": [
        {
            "name": "SourceArtifact",
            "EnvironmentVariables": "[{\"name\":\"VAR1\",\"value\":\"variable\",\"type\":\"PLAINTEXT\"}]"
        }
    ],
    "region": "us-east-1"
}
```

------

## See also
<a name="rule-reference-Commands-links"></a>

The following related resources can help you as you work with this rule.
+ For more information about rules and conditions, see [Condition](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_Condition.html), [RuleTypeId](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RuleTypeId.html), and [RuleExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RuleExecution.html) in the *CodePipeline API Guide*.