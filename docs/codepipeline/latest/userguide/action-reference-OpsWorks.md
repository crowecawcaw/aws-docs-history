

# AWS OpsWorks deploy action reference
<a name="action-reference-OpsWorks"></a>

You use an AWS OpsWorks action to deploy with OpsWorks using your pipeline.

## Action type
<a name="action-reference-StepFunctions-type"></a>
+ Category: `Deploy`
+ Owner: `AWS`
+ Provider: `OpsWorks`
+ Version: `1`

## Configuration parameters
<a name="action-reference-OpsWorks-config"></a>

**App**  
Required: Yes  
The OpsWorks app. The app represents the code you want to deploy and run.

**Stack**  
Required: Yes  
The OpsWorks stack. A stack is a container for your application infrastructure.

**Layer**  
Required: No  
The OpsWorks layer. A layer specifies the configuration and resources for a set of instances.

## Input artifacts
<a name="action-reference-OpsWorks-input"></a>
+ **Number of artifacts:** `1`
+ **Description:** This is the input artifact for your action.

## Output artifacts
<a name="action-reference-OpsWorks-output"></a>
+ **Number of artifacts:** `0 to 1` 
+ **Description:** Output artifacts do not apply for this action type.

## Service role permissions: AWS OpsWorks action
<a name="edit-role-opsworks"></a>

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
    "Resource": "{{resource_ARN}}"
},
```

## Example action configuration
<a name="action-reference-OpsWorks-example"></a>

------
#### [ YAML ]

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
  Stack: {{my-stack}}
  App: {{my-app}}
```

------
#### [ JSON ]

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
        "Stack": "{{my-stack}}",
        "App": "{{my-app}}"
    }
}
```

------

## See also
<a name="action-reference-OpsWorks-links"></a>

The following related resources can help you as you work with this action.
+ [AWS OpsWorks User Guide](https://docs.aws.amazon.com/step-functions/latest/dg/) – For information about deploying with AWS OpsWorks, see the *AWS OpsWorks User Guide*.