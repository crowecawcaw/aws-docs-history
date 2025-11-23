# Create and configure CloudWatch Application Insights monitoring using

CloudFormation templates

You can add Application Insights monitoring, including key metrics and telemetry, to your
application, database, and web server, directly from AWS CloudFormation templates.

This section provides sample CloudFormation templates in both JSON and YAML formats to help you
create and configure Application Insights monitoring.

To view the Application Insights resource and property reference in the _CloudFormation User
Guide_, see [ApplicationInsights resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_ApplicationInsights.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ApplicationInsights.md").

###### Sample templates

- [Create an Application Insights
  application for the entire CloudFormation stack](#appinsights-cloudformation-apply-to-stack "#appinsights-cloudformation-apply-to-stack")
- [Create an Application Insights
  application with detailed settings](#appinsights-cloudformation-apply-detailed "#appinsights-cloudformation-apply-detailed")
- [Create an Application Insights application
  with CUSTOM mode component configuration](#appinsights-cloudformation-custom "#appinsights-cloudformation-custom")
- [Create an Application Insights
  application with DEFAULT mode component configuration](#appinsights-cloudformation-default "#appinsights-cloudformation-default")
- [Create an
  Application Insights application with DEFAULT_WITH_OVERWRITE mode component
  configuration](#appinsights-cloudformation-default-with-overwrite "#appinsights-cloudformation-default-with-overwrite")

## Create an Application Insights

application for the entire CloudFormation stack

To apply the following template, you must create AWS resources and one or more
resource groups from which to create Application Insights applications to monitor those
resources. For more information, see [Getting started with AWS
Resource Groups](../../../ARG/latest/userguide/gettingstarted.md "../../../ARG/latest/userguide/gettingstarted.md").

The first two parts of the following template specify a resource and a resource
group. The last part of the template creates an Application Insights application for the
resource group, but does not configure the application or apply monitoring. For more
information, see the [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md") command details in the _Amazon CloudWatch Application Insights API
Reference_.

**Template in JSON format**

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "`Test Resource Group stack`",
    "Resources": {
        "EC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId" : "ami-`abcd1234efgh5678i`",
                "SecurityGroupIds" : ["sg-`abcd1234`"]
            }
        },
        ...
        "ResourceGroup": {
            "Type": "AWS::ResourceGroups::Group",
            "Properties": {
                "Name": "`my_resource_group`"
            }
        },
        "AppInsightsApp": {
            "Type": "AWS::ApplicationInsights::Application",
            "Properties": {
                "ResourceGroupName": "`my_resource_group`"
            },
            "DependsOn" : "ResourceGroup"
        }
    }
}
```

**Template in YAML format**

```
---
AWSTemplateFormatVersion: '2010-09-09'
Description: `Test Resource Group stack`
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-`abcd1234efgh5678i`
      SecurityGroupIds:
      - sg-`abcd1234`
  ...
  ResourceGroup:
    Type: AWS::ResourceGroups::Group
    Properties:
      Name: `my_resource_group`
  AppInsightsApp:
    Type: AWS::ApplicationInsights::Application
    Properties:
      ResourceGroupName: `my_resource_group`
    DependsOn: ResourceGroup
```

The following template section applies the default monitoring configuration to the
Application Insights application. For more information, see the [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md") command details in the _Amazon CloudWatch Application Insights API
Reference_.

When `AutoConfigurationEnabled` is set to `true`, all
components of the application are configured with the recommended monitoring
settings for the `DEFAULT` application tier. For more information about
these settings and tiers, see [DescribeComponentConfigurationRecommendation](../../../cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.md "../../../cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.md") and [UpdateComponentConfiguration](../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md") in the _Amazon CloudWatch Application Insights API
Reference_.

**Template in JSON format**

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "`Test Application Insights Application stack`",
    "Resources": {
        "AppInsightsApp": {
            "Type": "AWS::ApplicationInsights::Application",
            "Properties": {
                "ResourceGroupName": "`my_resource_group`",
                "AutoConfigurationEnabled": true
            }
        }
    }
}
```

**Template in YAML format**

```
---
AWSTemplateFormatVersion: '2010-09-09'
Description: `Test Application Insights Application stack`
Resources:
  AppInsightsApp:
    Type: AWS::ApplicationInsights::Application
    Properties:
      ResourceGroupName: `my_resource_group`
      AutoConfigurationEnabled: true
```

## Create an Application Insights

application with detailed settings

The following template performs these actions:

- Creates an Application Insights application with CloudWatch Events notification and OpsCenter
  enabled. For more information, see the [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md") command details in the _Amazon CloudWatch Application Insights API
  Reference_.
- Tags the application with two tags, one of which has no tag values. For
  more information, see [TagResource](../../../cloudwatch/latest/APIReference/API_TagResource.md "../../../cloudwatch/latest/APIReference/API_TagResource.md") in the _Amazon CloudWatch Application Insights API
  Reference_.
- Creates two custom instance group components. For more information, see
  [CreateComponent](../../../cloudwatch/latest/APIReference/API_CreateComponent.md "../../../cloudwatch/latest/APIReference/API_CreateComponent.md") in the _Amazon CloudWatch Application Insights API
  Reference_.
- Creates two log pattern sets. For more information, see [CreateLogPattern](../../../cloudwatch/latest/APIReference/API_CreateLogPattern.md "../../../cloudwatch/latest/APIReference/API_CreateLogPattern.md") in the _Amazon CloudWatch Application Insights API
  Reference_.
- Sets `AutoConfigurationEnabled` to `true`, which
  configures all components of the application with the recommended monitoring
  settings for the `DEFAULT` tier. For more information, see [DescribeComponentConfigurationRecommendation](../../../cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.md "../../../cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.md") in the
  _Amazon CloudWatch Application Insights API Reference_.

**Template in JSON format**

```
{
    "Type": "AWS::ApplicationInsights::Application",
    "Properties": {
        "ResourceGroupName": "`my_resource_group`",
        "CWEMonitorEnabled": true,
        "OpsCenterEnabled": true,
        "OpsItemSNSTopicArn": "arn:aws:sns:`us-east-1:123456789012:my_topic`",
        "AutoConfigurationEnabled": true,
        "Tags": [
            {
                "Key": "`key1`",
                "Value": "`value1`"
            },
            {
                "Key": "`key2`",
                "Value": ""
            }
        ],
        "CustomComponents": [
            {
                "ComponentName": "`test_component_1`",
                "ResourceList": [
                    "arn:aws:ec2:`us-east-1:123456789012:instance/i-abcd1234efgh5678i`"
                ]
            },
            {
                "ComponentName": "`test_component_2`",
                "ResourceList": [
                    "arn:aws:ec2:`us-east-1:123456789012:instance/i-abcd1234efgh5678i`",
                    "arn:aws:ec2:`us-east-1:123456789012:instance/i-abcd1234efgh5678i`"
                ]
            }
        ],
        "LogPatternSets": [
            {
                "PatternSetName": "pattern_set_1",
                "LogPatterns": [
                    {
                        "PatternName": "deadlock_pattern",
                        "Pattern": ".*\\sDeadlocked\\sSchedulers(([^\\w].*)|($))",
                        "Rank": 1
                    }
                ]
            },
            {
                "PatternSetName": "pattern_set_2",
                "LogPatterns": [
                    {
                        "PatternName": "error_pattern",
                        "Pattern": ".*[\\s\\[]ERROR[\\s\\]].*",
                        "Rank": 1
                    },
                    {
                        "PatternName": "warning_pattern",
                        "Pattern": ".*[\\s\\[]WARN(ING)?[\\s\\]].*",
                        "Rank": 10
                    }
                ]
            }
        ]
    }
}
```

**Template in YAML format**

```
---
Type: AWS::ApplicationInsights::Application
Properties:
  ResourceGroupName: `my_resource_group`
  CWEMonitorEnabled: true
  OpsCenterEnabled: true
  OpsItemSNSTopicArn: arn:aws:sns:`us-east-1:123456789012:my_topic`
  AutoConfigurationEnabled: true
  Tags:
  - Key: `key1`
    Value: `value1`
  - Key: `key2`
    Value: ''
  CustomComponents:
  - ComponentName: `test_component_1`
    ResourceList:
    - arn:aws:ec2:`us-east-1:123456789012:instance/i-abcd1234efgh5678i`
  - ComponentName: test_component_2
    ResourceList:
    - arn:aws:ec2:`us-east-1:123456789012:instance/i-abcd1234efgh5678i`
    - arn:aws:ec2:`us-east-1:123456789012:instance/i-abcd1234efgh5678i`
  LogPatternSets:
  - PatternSetName: pattern_set_1
    LogPatterns:
    - PatternName: deadlock_pattern
      Pattern: ".*\\sDeadlocked\\sSchedulers(([^\\w].*)|($))"
      Rank: 1
  - PatternSetName: pattern_set_2
    LogPatterns:
    - PatternName: error_pattern
      Pattern: ".*[\\s\\[]ERROR[\\s\\]].*"
      Rank: 1
    - PatternName: warning_pattern
      Pattern: ".*[\\s\\[]WARN(ING)?[\\s\\]].*"
      Rank: 10
```

## Create an Application Insights application

with `CUSTOM` mode component configuration

The following template performs these actions:

- Creates an Application Insights application. For more information, see [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md") in the _Amazon CloudWatch Application Insights API
  Reference_.
- Component `my_component` sets
  `ComponentConfigurationMode` to `CUSTOM`, which
  causes this component to be configured with the configuration specified in
  `CustomComponentConfiguration`. For more information, see
  [UpdateComponentConfiguration](../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md") in the _Amazon CloudWatch Application Insights API
  Reference_.

**Template in JSON format**

```
{
    "Type": "AWS::ApplicationInsights::Application",
    "Properties": {
        "ResourceGroupName": "my_resource_group,
        "ComponentMonitoringSettings": [
            {
                "ComponentARN": "my_component",
                "Tier": "SQL_SERVER",
                "ComponentConfigurationMode": "CUSTOM",
                "CustomComponentConfiguration": {
                    "ConfigurationDetails": {
                        "AlarmMetrics": [
                            {
                                "AlarmMetricName": "StatusCheckFailed"
                            },
                            ...
                        ],
                        "Logs": [
                            {
                                "LogGroupName": "my_log_group_1",
                                "LogPath": "C:\\LogFolder_1\\*",
                                "LogType": "DOT_NET_CORE",
                                "Encoding": "utf-8",
                                "PatternSet": "my_pattern_set_1"
                            },
                            ...
                        ],
                        "WindowsEvents": [
                            {
                                "LogGroupName": "my_windows_event_log_group_1",
                                "EventName": "Application",
                                "EventLevels": [
                                    "ERROR",
                                    "WARNING",
                                    ...
                                ],
                                "Encoding": "utf-8",
                                "PatternSet": "my_pattern_set_2"
                            },
                            ...
                        ],
                        "Alarms": [
                            {
                                "AlarmName": "my_alarm_name",
                                "Severity": "HIGH"
                            },
                            ...
                        ]
                    },
                    "SubComponentTypeConfigurations": [
                        {
                            "SubComponentType": "EC2_INSTANCE",
                            "SubComponentConfigurationDetails": {
                                "AlarmMetrics": [
                                    {
                                        "AlarmMetricName": "DiskReadOps"
                                    },
                                    ...
                                ],
                                "Logs": [
                                    {
                                        "LogGroupName": "my_log_group_2",
                                        "LogPath": "C:\\LogFolder_2\\*",
                                        "LogType": "IIS",
                                        "Encoding": "utf-8",
                                        "PatternSet": "my_pattern_set_3"
                                    },
                                    ...
                                ],
                                "processes" : [
                                    {
                                        "processName" : "my_process",
                                        "alarmMetrics" : [
                                    {
                                        "alarmMetricName" : "procstat cpu_usage",
                                        "monitor" : true
                                    }, {
                                        "alarmMetricName" : "procstat memory_rss",
                                        "monitor" : true
                                    }
                                ]
                            }
                        ],
                                "WindowsEvents": [
                                    {
                                        "LogGroupName": "my_windows_event_log_group_2",
                                        "EventName": "Application",
                                        "EventLevels": [
                                            "ERROR",
                                            "WARNING",
                                            ...
                                        ],
                                        "Encoding": "utf-8",
                                        "PatternSet": "my_pattern_set_4"
                                    },
                                    ...
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

**Template in YAML format**

```
---
Type: AWS::ApplicationInsights::Application
Properties:
  ResourceGroupName: my_resource_group
  ComponentMonitoringSettings:
  - ComponentARN: my_component
    Tier: SQL_SERVER
    ComponentConfigurationMode: CUSTOM
    CustomComponentConfiguration:
      ConfigurationDetails:
        AlarmMetrics:
        - AlarmMetricName: StatusCheckFailed
        ...
        Logs:
        - LogGroupName: my_log_group_1
          LogPath: C:\LogFolder_1\*
          LogType: DOT_NET_CORE
          Encoding: utf-8
          PatternSet: my_pattern_set_1
        ...
        WindowsEvents:
        - LogGroupName: my_windows_event_log_group_1
          EventName: Application
          EventLevels:
          - ERROR
          - WARNING
          ...
          Encoding: utf-8
          PatternSet: my_pattern_set_2
        ...
        Alarms:
        - AlarmName: my_alarm_name
          Severity: HIGH
        ...
      SubComponentTypeConfigurations:
      - SubComponentType: EC2_INSTANCE
        SubComponentConfigurationDetails:
          AlarmMetrics:
          - AlarmMetricName: DiskReadOps
          ...
          Logs:
          - LogGroupName: my_log_group_2
            LogPath: C:\LogFolder_2\*
            LogType: IIS
            Encoding: utf-8
            PatternSet: my_pattern_set_3
          ...
          Processes:
          - ProcessName: my_process
            AlarmMetrics:
            - AlarmMetricName: procstat cpu_usage
              ...
            ...
          WindowsEvents:
          - LogGroupName: my_windows_event_log_group_2
            EventName: Application
            EventLevels:
            - ERROR
            - WARNING
            ...
            Encoding: utf-8
            PatternSet: my_pattern_set_4
          ...
```

## Create an Application Insights

application with `DEFAULT` mode component configuration

The following template performs these actions:

- Creates an Application Insights application. For more information, see [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md") in the _Amazon CloudWatch Application Insights API
  Reference_.
- Component `my_component` sets
  `ComponentConfigurationMode` to `DEFAULT` and
  `Tier` to `SQL_SERVER`, which causes this
  component to be configured with the configuration settings that Application Insights
  recommends for the `SQL_Server` tier. For more information, see
  [DescribeComponentConfiguration](../../../cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.md") and [UpdateComponentConfiguration](../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md") in the _Amazon CloudWatch Application Insights API
  Reference_.

**Template in JSON format**

```
{
    "Type": "AWS::ApplicationInsights::Application",
    "Properties": {
        "ResourceGroupName": "`my_resource_group`",
        "ComponentMonitoringSettings": [
            {
                "ComponentARN": "`my_component`",
                "Tier": "SQL_SERVER",
                "ComponentConfigurationMode": "DEFAULT"
            }
        ]
    }
}
```

**Template in YAML format**

```
---
Type: AWS::ApplicationInsights::Application
Properties:
  ResourceGroupName: `my_resource_group`
  ComponentMonitoringSettings:
  - ComponentARN: `my_component`
    Tier: SQL_SERVER
    ComponentConfigurationMode: DEFAULT
```

## Create an

Application Insights application with `DEFAULT_WITH_OVERWRITE` mode component
configuration

The following template performs these actions:

- Creates an Application Insights application. For more information, see [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md") in the _Amazon CloudWatch Application Insights API
  Reference_.
- Component `my_component` sets
  `ComponentConfigurationMode` to
  `DEFAULT_WITH_OVERWRITE` and `tier` to
  `DOT_NET_CORE`, which causes this component to be configured
  with the configuration settings that Application Insights recommends for the
  `DOT_NET_CORE` tier. Overwritten configuration settings are
  specified in the `DefaultOverwriteComponentConfiguration`:

      + At the component level `AlarmMetrics` settings are
       overwritten.
      + At the sub-component level, for the `EC2_Instance` type
       sub-components, `Logs` settings are overwritten.

  For more information, see [UpdateComponentConfiguration](../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md") in the _Amazon CloudWatch Application Insights API
  Reference_.

**Template in JSON format**

```
{
    "Type": "AWS::ApplicationInsights::Application",
    "Properties": {
        "ResourceGroupName": "`my_resource_group`",
        "ComponentMonitoringSettings": [
            {
                "ComponentName": "`my_component`",
                "Tier": "DOT_NET_CORE",
                "ComponentConfigurationMode": "DEFAULT_WITH_OVERWRITE",
                "DefaultOverwriteComponentConfiguration": {
                    "ConfigurationDetails": {
                        "AlarmMetrics": [
                            {
                                "AlarmMetricName": "StatusCheckFailed"
                            }
                        ]
                    },
                    "SubComponentTypeConfigurations": [
                        {
                            "SubComponentType": "EC2_INSTANCE",
                            "SubComponentConfigurationDetails": {
                                "Logs": [
                                    {
                                        "LogGroupName": "`my_log_group`",
                                        "LogPath": "C:\\LogFolder\\*",
                                        "LogType": "IIS",
                                        "Encoding": "utf-8",
                                        "PatternSet": "`my_pattern_set`"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

**Template in YAML format**

```
---
Type: AWS::ApplicationInsights::Application
Properties:
  ResourceGroupName: `my_resource_group`
  ComponentMonitoringSettings:
  - ComponentName: `my_component`
    Tier: DOT_NET_CORE
    ComponentConfigurationMode: DEFAULT_WITH_OVERWRITE
    DefaultOverwriteComponentConfiguration:
      ConfigurationDetails:
        AlarmMetrics:
        - AlarmMetricName: StatusCheckFailed
      SubComponentTypeConfigurations:
      - SubComponentType: EC2_INSTANCE
        SubComponentConfigurationDetails:
          Logs:
          - LogGroupName: `my_log_group`
            LogPath: C:\LogFolder\*
            LogType: IIS
            Encoding: utf-8
            PatternSet: `my_pattern_set`
```
