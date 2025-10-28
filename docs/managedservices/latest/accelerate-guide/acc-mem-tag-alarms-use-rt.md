# Accelerate tags using Resource Tagger

The tag-based Alarm Manager manages the lifecycle of per-resource CloudWatch alarms; however, it requires that the
managed resources have specific tags defined by AMS Accelerate.
To use the Resource Tagger to apply the default set of AMS-managed alarms to both Linux and Windows based instances, follow these steps.

1. Browse to the [AppConfig](https://console.aws.amazon.com/systems-manager/appconfig/ "https://console.aws.amazon.com/systems-manager/appconfig/") console within your account.
2. Select the ResourceTagger application.
3. Select the **Configuration profiles** tab, and then select **CustomerManagedTags**.
4. Click **Create** to create a new profile.
5. Select **JSON** and define your configuration. For more examples of filter and platform definition, see
   [Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").

```
{
"AWS::EC2::Instance": {
   "MonitorAllInstances": {
       "Enabled": true,
       "Filter": {
           "Platform": "*"
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

6. Click **Create hosted configuration version**.
7. Click **Start deployment**.
8. Define the following deployment details:

```
Environment: AMSInfrastructure Hosted configuration version: <Select the version that you have just created>
               Deployment Strategy: AMSNoBakeDeployment
```

9. Click **Start deployment**.
   Your instances become tagged with `"ams:rt:ams-managed": "true"` which ensures that additional `"ams:rt:ams-monitoring-policy": "ams-monitored"` and
   `"ams:rt:ams-monitoring-policy-platform": "ams-monitored-linux"` are applied to the instances. These tags then result in the appropriate alarms being created
   for the instance. For more information about this process, see [Monitoring in Accelerate](acc-tag-req-mon.md "acc-tag-req-mon.md").
