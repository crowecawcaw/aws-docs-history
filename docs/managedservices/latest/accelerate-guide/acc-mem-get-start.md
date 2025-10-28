# Getting started with Accelerate Alarm Manager

By default, when you onboard with AMS Accelerate, your configuration is deployed to AWS AppConfig, defining an alarm baseline for your resources. The alarm definitions are
applied only to resources with the **ams:rt:\*** tags. We recommend that these tags be applied using the
[Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md"): you set up a basic Resource Tagger configuration in order to let AMS Accelerate know which
resources you want managed.

Use Resource Tagger to apply the tag key **ams:rt:ams-managed** with tag value **true** to any resources you want AMS Accelerate to
monitor.

The following is an example Resource Tagger customization profile that you can use to opt in to monitoring for all of your Amazon EC2 instances. For general information, see
[Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").

```
{
    "AWS::EC2::Instance": {
        "AMSManageAllEC2Instances": {
            "Enabled": true,
            "Filter": {
                "InstanceId": "*"
            },
            "Tags": [
                {
                    "Key": "ams:rt:ams-managed",
                    "Value": "true"
                }
            ]
        }
    }
}
```

For information about how to apply this Resource Tagger configuration, see
[Viewing or making changes to the Resource Tagger configuration](acc-rt-using.md#acc-rt-make-changes "acc-rt-using.md#acc-rt-make-changes").
