# CloudWatchAlarm

When you create a condition, you can add the `CloudWatchAlarm` rule. This
section provides a reference for the rule parameters. For more information about rules and
conditions, see [How do stage conditions work?](concepts-how-it-works-conditions.md "concepts-how-it-works-conditions.md").

You must have already created an alarm in Amazon CloudWatch as a separate resource.

###### Topics

- [Rule type](#rule-reference-CloudWatchAlarm-type "#rule-reference-CloudWatchAlarm-type")
- [Configuration parameters](#rule-reference-CloudWatchAlarm-config "#rule-reference-CloudWatchAlarm-config")
- [Example rule
  configuration](#rule-reference-CloudWatchAlarm-example "#rule-reference-CloudWatchAlarm-example")
- [See also](#rule-reference-CloudWatchAlarm-links "#rule-reference-CloudWatchAlarm-links")

## Rule type

- Category: `Rule`
- Owner: `AWS`
- Provider: `CloudWatchAlarm`
- Version: `1`

## Configuration parameters

**AlarmName**

Required: Yes

The name of the CloudWatch alarm. This is a separate resource created in
CloudWatch.

**AlarmStates**

Required: No

The desired CloudWatch alarm states for the rule to monitor. Valid values
are ALARM, OK, and INSUFFICIENT_DATA.

**WaitTime**

Required: No

The wait time in minutes to allow for a state change before running the
rule result. For example, configure 20 minutes to wait for an alarm state to
change to OK before applying the rule result.

## Example rule

configuration

YAML

```
rules:
    - name: MyMonitorRule
      ruleTypeId:
        category: Rule
        owner: AWS
        provider: CloudWatchAlarm
        version: '1'
      configuration:
        AlarmName: CWAlarm
        WaitTime: '1'
      inputArtifacts: []
      region: us-east-1
```

JSON

```

                            "rules": [
                                {
                                    "name": "MyMonitorRule",
                                    "ruleTypeId": {
                                        "category": "Rule",
                                        "owner": "AWS",
                                        "provider": "CloudWatchAlarm",
                                        "version": "1"
                                    },
                                    "configuration": {
                                        "AlarmName": "CWAlarm",
                                        "WaitTime": "1"
                                    },
                                    "inputArtifacts": [],
                                    "region": "us-east-1"
                                }
                            ]
                        }
```

## See also

The following related resources can help you as you work with this rule.

- [Creating On Failure conditions](stage-conditions.md#stage-conditions-onfailure "stage-conditions.md#stage-conditions-onfailure") – This section provides
  steps for creating an On Failure condition with an alarm rule.
