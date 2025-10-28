# Stage declaration

The stage level of a pipeline has a basic structure that includes the following
parameters and syntax. For more information, see the [StageDeclaration](../APIReference/API_StageDeclaration.md "../APIReference/API_StageDeclaration.md") object in the _CodePipeline API
Guide_.

The following example shows the stage level of the pipeline structure in both JSON and
YAML. The example shows two stages named `Source` and `Build`. The
example contains two conditions, one for `onSuccess` and one for
`beforeEntry`.

YAML

```
pipeline:
  name: MyPipeline
  roleArn: >-
    arn:aws:iam::`ACCOUNT_ID`:role/service-role/AWSCodePipelineServiceRole-us-west-2-MyPipeline
  artifactStore:
    type: S3
    location: amzn-s3-demo-bucket
  stages:
    - name: Source
      actions:
        - name: Source
          ...
    - name: Build
      actions:
        - name: Build
          ...
      onSuccess:
        conditions:
        - result: ROLLBACK
          rules:
          - name: DeploymentWindowRule
         ...
      beforeEntry:
        conditions:
        - result: FAIL
          rules:
          - name: MyLambdaRule
         ...
  version: 6
metadata:
  pipelineArn: 'arn:aws:codepipeline:us-west-2:`ACCOUNT_ID`:MyPipeline'
  created: '2019-12-12T06:49:02.733000+00:00'
  updated: '2020-09-10T06:34:07.447000+00:00'
```

JSON

```
{
    "pipeline": {
        "name": "MyPipeline",
        "roleArn": "arn:aws:iam::`ACCOUNT_ID`:role/service-role/AWSCodePipelineServiceRole-us-west-2-MyPipeline",
        "artifactStore": {
            "type": "S3",
            "location": "amzn-s3-demo-bucket"
        },
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "Source",
                        ...
                    }
                ]
            },
            {
                "name": "Build",
                "actions": [
                    {
                        "name": "Build",
                        ...
                    }
                ],
                "onSuccess": {
                    "conditions": [
                        {
                            "result": "ROLLBACK",
                            "rules": [
                                {
                                    "name": "DeploymentWindowRule",
                                    ...
                                }
                            ]
                        }
                    ]
                },
                "beforeEntry": {
                    "conditions": [
                        {
                            "result": "FAIL",
                            "rules": [
                                {
                                    "name": "MyLambdaRule",
                                     ...
                                }
                            ]
                        }
                    ]
                }
            }
        ],

            }
        ],
        "version": 6
    },
    "metadata": {
        "pipelineArn": "arn:aws:codepipeline:us-west-2:`ACCOUNT_ID`:MyPipeline",
        "created": "2019-12-12T06:49:02.733000+00:00",
        "updated": "2020-09-10T06:34:07.447000+00:00"
    }
}
```

## `name`

The name of the stage.

## `actions`

The action level of a pipeline has a basic structure that includes the following
parameters and syntax. To view parameters and examples, see [Action declaration](action-requirements.md "action-requirements.md").

## `conditions`

Conditions contain one or more rules that are available in a list of rules in
CodePipeline. If all rules in a condition succeed, then the condition is met. You
can configure conditions so that when the criteria are not met, the specified result
engages.

You can configure the following types of conditions:

- `beforeEntry`
- `onFailure`
- `onSuccess`

For more information and examples, see [Configure conditions for a stage](stage-conditions.md "stage-conditions.md").

## `rules`

Each condition has a rule set which is an ordered set of rules that are evaluated
together. Therefore, if one rule fails in the condition, then the condition fails.
You can override rule conditions at pipeline runtime.

The available rules are provided in the Rule reference. For more information, see
the Rule structure reference at [Rule structure reference](rule-reference.md "rule-reference.md").
