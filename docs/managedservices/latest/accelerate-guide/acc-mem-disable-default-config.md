# Disabling the default Accelerate alarm configuration

AMS Accelerate provides the default configuration profile in your account based on the baseline
alarms. However, this default configuration can be disabled by overriding any of the alarm
definitions. You can disable a default configuration rule by overriding the **ConfigurationID** of the rule in your customization configuration
profile and specifying the enabled field with a value of false.

For example, if the following configuration was present in the default configuration profile:

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
                ...
            }
        }
    }
```

You could disable this tagging rule by including the following in your customization configuration profile:

```
{
    "AWS::EC2::Instance": {
        "AMSManagedBlock1": {
            "Enabled": false
        }
    }
}
```

To make these changes, the
[CreateHostedConfigurationVersion](../../../appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md "../../../appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md")
API must be called with the JSON profile document (see [Changing the Accelerate alarm configuration](acc-mem-change-am.md "acc-mem-change-am.md")) and subsequently
must be deployed (see [Deploying Accelerate alarm configuration changes](acc-mem-deploy-change.md "acc-mem-deploy-change.md")). Note that when you create the new configuration
version, you must also include any previously created custom alarms that you want in the JSON profile document.

###### Important

When AMS Accelerate updates the default configuration profile, it's not calibrated against your
configured custom alarms, so review changes to the default alarms when you're overriding them in your customization configuration profile.
