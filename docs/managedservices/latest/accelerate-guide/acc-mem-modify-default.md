# Modifying the Accelerate alarm default configuration

While you can't modify the default configuration profile, you can provide overrides to
the defaults by specifying a configuration block in your customization profile with the
same **ConfigurationID** as the default configuration block. If you do this, your whole
configuration block overwrites the default configuration block for which tagging configuration to apply.

For example, consider the following default configuration profile:

```
{
    "AWS::EC2::Instance": {
        "AMSManagedBlock1": {
            "Enabled": true,
            "Tag": {
                "Key": "ams:rt:ams-monitoring-policy",
                "Value": "ams-monitored"
            },
            "AlarmDefinition": {
                "AlarmName": "${EC2::InstanceId}: AMS Default Alarm",
                "Namespace": "AWS/EC2",
                "MetricName": "CPUUtilization",
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "${EC2::InstanceId}"
                    }
                ],
                "Threshold": 5,
                ...
            }
        }
    }
}
```

In order to change the threshold of this alarm to 10, **you must provide the entire alarm definition**, not only the parts
you want to change. For example, you might provide the following customization profile:

```
{
    "AWS::EC2::Instance": {
        "AMSManagedBlock1": {
            "Enabled": true,
            "Tag": {
                "Key": "ams:rt:ams-monitoring-policy",
                "Value": "ams-monitored"
            },
            "AlarmDefinition": {
                "AlarmName": "${EC2::InstanceId}: AMS Default Alarm",
                "Namespace": "AWS/EC2",
                "MetricName": "CPUUtilization",
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "${EC2::InstanceId}"
                    }
                ],
                "Threshold": 10,
                ...
            }
        }
    }
}
```

###### Important

Remember to deploy your configuration changes after you have made them. In SSM
AppConfig, you must deploy a new version of the configuration after creating it.
