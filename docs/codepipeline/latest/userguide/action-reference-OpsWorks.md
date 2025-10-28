# AWS OpsWorks deploy action reference

You use an AWS OpsWorks action to deploy with OpsWorks using your pipeline.

## Action type

- Category: `Deploy`
- Owner: `AWS`
- Provider: `OpsWorks`
- Version: `1`

## Configuration parameters

**App**

Required: Yes

The OpsWorks stack. A stack is a container for your application
infrastructure.

**Stack**

Required: Yes

The OpsWorks app. The app represents the code you want to deploy and
run.

**Layer**

Required: No

The OpsWorks stack. A layer specifies the configuration and resources for a
set of instances.

## Input artifacts

- **Number of artifacts:**
  `1`
- **Description:** This is the input artifact for
  your action.

## Output artifacts

- **Number of artifacts:**
  `0 to 1`
- **Description:** Output artifacts do not apply
  for this action type.

## Service role permissions: AWS OpsWorks action

For AWS OpsWorks support, add the following to your policy statement:

```
{
    "Effect": "Allow",
    "Action": [
        "opsworks:CreateDeployment",
        "opsworks:DescribeApps",
        "opsworks:DescribeCommands",
        "opsworks:DescribeDeployments",
        "opsworks:DescribeInstances",
        "opsworks:DescribeStacks",
        "opsworks:UpdateApp",
        "opsworks:UpdateStack"
    ],
    "Resource": "`resource_ARN`"
},
```

## Example action

configuration

YAML

```
Name: ActionName
ActionTypeId:
  Category: Deploy
  Owner: AWS
  Version: 1
  Provider: OpsWorks
InputArtifacts:
  - Name: myInputArtifact
Configuration:
  Stack: `my-stack`
  App: `my-app`
```

JSON

```
{
    "Name": "ActionName",
    "ActionTypeId": {
        "Category": "Deploy",
        "Owner": "AWS",
        "Version": 1,
        "Provider": "OpsWorks"
    },
    "InputArtifacts": [
        {
            "Name": "myInputArtifact"
        }
    ],
    "Configuration": {
        "Stack": "`my-stack`",
        "App": "`my-app`"
    }
}
```

## See also

The following related resources can help you as you work with this action.

- [AWS OpsWorks User Guide](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md") – For information
  about deploying with AWS OpsWorks, see the
  _AWS OpsWorks User Guide_.
