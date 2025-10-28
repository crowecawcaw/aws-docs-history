# Using AWS CloudFormation to deploy Accelerate configuration changes

If you wish to deploy your `CustomerManagedAlarms`
configuration profile using AWS CloudFormation, you can use the following AWS CloudFormation templates.
Put your desired JSON configuration in the `AMSAlarmManagerConfigurationVersion.Content` field.

When you deploy the templates in a AWS CloudFormation Stack or Stack Set,
the deployment of the `AMSResourceTaggerDeployment` resource will fail if you have not followed the required JSON format for the configuration.
See [Accelerate Configuration profile: monitoring](acc-mem-config-doc-format.md "acc-mem-config-doc-format.md") for details on the expected format.

For help on deploying these templates as a CloudFormation stack or stack set, see the relevant AWS CloudFormation documentation below:

- [Creating a stack on the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md")
- [Creating a stack with AWS CLI](../../../AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.md")
- [Creating a stack set](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md")

###### Note

If you deploy a configuration version using one of these templates, and then subsequently delete the CloudFormation stack/stack set, the template
configuration version will remain as the current deployed version, and no additional deployment will be made. If you wish to revert back to a default configuration,
you will need to either manually deploy an empty configuration (i.e. just {}), or update your stack to an empty configuration, rather than deleting the stack.

**JSON**

```
{
  "Description": "Custom configuration for the AMS Alarm Manager.",
  "Resources": {
    "AMSAlarmManagerConfigurationVersion": {
      "Type": "AWS::AppConfig::HostedConfigurationVersion",
      "Properties": {
        "ApplicationId": {
          "Fn::ImportValue": "AMS-Alarm-Manager-Configuration-ApplicationId"
        },
        "ConfigurationProfileId": {
          "Fn::ImportValue": "AMS-Alarm-Manager-Configuration-CustomerManagedAlarms-ProfileID"
        },
        "Content": "{}",
        "ContentType": "application/json"
      }
    },
    "AMSAlarmManagerDeployment": {
      "Type": "AWS::AppConfig::Deployment",
      "Properties": {
        "ApplicationId": {
          "Fn::ImportValue": "AMS-Alarm-Manager-Configuration-ApplicationId"
        },
        "ConfigurationProfileId": {
          "Fn::ImportValue": "AMS-Alarm-Manager-Configuration-CustomerManagedAlarms-ProfileID"
        },
        "ConfigurationVersion": {
          "Ref": "AMSAlarmManagerConfigurationVersion"
        },
        "DeploymentStrategyId": {
          "Fn::ImportValue": "AMS-Alarm-Manager-Configuration-Deployment-StrategyID"
        },
        "EnvironmentId": {
          "Fn::ImportValue": "AMS-Alarm-Manager-Configuration-EnvironmentId"
        }
      }
    }
  }
}
```

**YAML**

```
Description: Custom configuration for the AMS Alarm Manager.
Resources:
  AMSAlarmManagerConfigurationVersion:
    Type: AWS::AppConfig::HostedConfigurationVersion
    Properties:
      ApplicationId:
        !ImportValue AMS-Alarm-Manager-Configuration-ApplicationId
      ConfigurationProfileId:
        !ImportValue AMS-Alarm-Manager-Configuration-CustomerManagedAlarms-ProfileID
      Content: |
        {

        }
      ContentType: application/json
  AMSAlarmManagerDeployment:
    Type: AWS::AppConfig::Deployment
    Properties:
      ApplicationId:
        !ImportValue AMS-Alarm-Manager-Configuration-ApplicationId
      ConfigurationProfileId:
        !ImportValue AMS-Alarm-Manager-Configuration-CustomerManagedAlarms-ProfileID
      ConfigurationVersion:
        !Ref AMSAlarmManagerConfigurationVersion
      DeploymentStrategyId:
        !ImportValue AMS-Alarm-Manager-Configuration-Deployment-StrategyID
      EnvironmentId:
        !ImportValue AMS-Alarm-Manager-Configuration-EnvironmentId
```
