# Retaining Accelerate alarms

When resources monitored by AMS are deleted, any alarms created by Alarm Manager for those resources are automatically deleted by
Alarm Manager. If you need to retain certain alarms for auditing, compliance, or historical purposes, use the Alarm Manager retain-tagging capability.

To retain an alarm even after its monitored resource is deleted, add an `"ams:alarm-manager:retain"` tag to the alarm's custom configuration as
shown in the following example.

```
{
  "AWS::EC2::Instance": {
    "AMSCpuAlarm": {
      "Enabled": true,
      "Tag": {
        "Key": "ams:rt:ams-monitoring-policy",
        "Value": "ams-monitored"
      },
      "AlarmDefinition": {
        "AlarmName": "${EC2::InstanceId}: CPU Too High",
        "AlarmDescription": "AMS Baseline Alarm for EC2 CPUUtilization",
        [...]
        "Tags": [
          {
            "Key": "ams:alarm-manager:retain",
            "Value": "true"
          }
        ]
      }
    }
  }
}
```

An alarm configured with the `"ams:alarm-manager:retain"` tag, is not automatically deleted by Alarm Manager when the monitored resource
is terminated. The retained alarm persists in CloudWatch indefinitely until you manually remove it using CloudWatch.
