# Deploying a configuration profile with AWS CloudFormation for Accelerate

If you wish to deploy your `CustomerManagedTags` configuration profile using AWS CloudFormation,
you can use the following CloudFormation templates. Put your desired JSON configuration in
the `AMSResourceTaggerConfigurationVersion.Content` field.

When you deploy the templates in a CloudFormation Stack or Stack Set,
the deployment of the `AMSResourceTaggerDeployment` resource will fail if you have
not followed the required JSON format for the configuration.
See [Syntax and structure](acc-tag-tools-profiles.md#acc-rt-config-doc-format "acc-tag-tools-profiles.md#acc-rt-config-doc-format")
for details on the expected format.

For help on deploying these templates as a CloudFormation stack or stack set, see the relevant AWS CloudFormation documentation below:

- [Creating a stack on the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md")
- [Creating a stack with AWS CLI](../../../AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.md")
- [Creating a stack set](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md")

###### Note

If you deploy a configuration version using one of these templates, and then
subsequently delete the CloudFormation stack/stack set, the template configuration version
will remain as the current deployed version, and no additional deployment will be made. If
you wish to revert back to a default configuration, you will need to either manually deploy
an empty configuration (that is, just `{}`), or update your stack to an empty
configuration, rather than deleting the stack.

**JSON**

```
{
  "Description": "Custom configuration for the AMS Resource Tagger.",
  "Resources": {
    "AMSResourceTaggerConfigurationVersion": {
      "Type": "AWS::AppConfig::HostedConfigurationVersion",
      "Properties": {
        "ApplicationId": {
          "Fn::ImportValue": "AMS-ResourceTagger-Configuration-ApplicationId"
        },
        "ConfigurationProfileId": {
          "Fn::ImportValue": "AMS-ResourceTagger-Configuration-CustomerManagedTags-ProfileID"
        },
        "Content": "{\"Options\": {\"ReadOnly\": false}}",
        "ContentType": "application/json"
      }
    },
    "AMSResourceTaggerDeployment": {
      "Type": "AWS::AppConfig::Deployment",
      "Properties": {
        "ApplicationId": {
          "Fn::ImportValue": "AMS-ResourceTagger-Configuration-ApplicationId"
        },
        "ConfigurationProfileId": {
          "Fn::ImportValue": "AMS-ResourceTagger-Configuration-CustomerManagedTags-ProfileID"
        },
        "ConfigurationVersion": {
          "Ref": "AMSResourceTaggerConfigurationVersion"
        },
        "DeploymentStrategyId": {
          "Fn::ImportValue": "AMS-ResourceTagger-Configuration-Deployment-StrategyID"
        },
        "EnvironmentId": {
          "Fn::ImportValue": "AMS-ResourceTagger-Configuration-EnvironmentId"
        }
      }
    }
  }
}
```

**YAML**

```
Description: Custom configuration for the AMS Resource Tagger.
Resources:
  AMSResourceTaggerConfigurationVersion:
    Type: AWS::AppConfig::HostedConfigurationVersion
    Properties:
      ApplicationId:
        !ImportValue AMS-ResourceTagger-Configuration-ApplicationId
      ConfigurationProfileId:
        !ImportValue AMS-ResourceTagger-Configuration-CustomerManagedTags-ProfileID
      Content: |
        {
          "Options": {
            "ReadOnly": false
          }
        }
      ContentType: application/json
  AMSResourceTaggerDeployment:
    Type: AWS::AppConfig::Deployment
    Properties:
      ApplicationId:
        !ImportValue AMS-ResourceTagger-Configuration-ApplicationId
      ConfigurationProfileId:
        !ImportValue AMS-ResourceTagger-Configuration-CustomerManagedTags-ProfileID
      ConfigurationVersion:
        !Ref AMSResourceTaggerConfigurationVersion
      DeploymentStrategyId:
        !ImportValue AMS-ResourceTagger-Configuration-Deployment-StrategyID
      EnvironmentId:
        !ImportValue AMS-ResourceTagger-Configuration-EnvironmentId
```
