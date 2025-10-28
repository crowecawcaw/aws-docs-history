# Tag your resources to apply AMS backup plans

To assign resources to an AMS backup plan, tag the resource with the plan’s tag key-value pair. You can use AMS Resource Tagger to apply the AMS backup plans to a subset of your resources or for all supported resources in your account. If you want to use an alternate method to apply tags to your resources, such as AWS CloudFormation or Terraform, then turn off Resource Tagger so that it doesn’t compete with your chosen tagging method. For more information, see [Preventing Resource Tagger from modifying resources](acc-rt-using.md#acc-rt-preventing-rt-changes "acc-rt-using.md#acc-rt-preventing-rt-changes").

The following example demonstrates how you can use Resource Tagger to apply the default AMS backup plan on Amazon Elastic Compute Cloud instances in your account. For this backup plan, apply the tag key `ams:rt:backup-orchestrator` and value `true`. To use a different backup plan, change the key to match your desired backup plan's tag key.

To learn about AMS Resource Tagger and understand how to integrate the following referenced profile with the current (already configured) profile in your Accelerate
account, see [Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").

1. Open the AWS AppConfig console at [https://console.aws.amazon.com/systems-manager/appconfig](https://console.aws.amazon.com/systems-manager/appconfig "https://console.aws.amazon.com/systems-manager/appconfig").
2. Choose the **ResourceTagger** application.
3. Choose the **Configuration profiles** tab, then choose **CustomerManagedTags**
4. Choose **Create** to create a new version.
5. Choose **JSON**, and then copy and paste the following JSON object:

```
{
    "AWS::EC2::Instance": {
        "AccelerateBackupPlan": {
            "Enabled": true,
            "Filter": {
                "Fn::AND": [
                    {
                        "Platform": "*"
                    }
                ]
            },
            "Tags": [
                {
                    "Key": "ams:rt:backup-orchestrator",
                    "Value": "true"
                }
            ]
        }
    }
}
```

6. Choose **Create hosted configuration version**.
7. Choose **Start deployment**.
8. Define the following deployment details:

```
Environment: AMSInfrastructure
Hosted configuration version: `Select the version that you have just created.`
Deployment Strategy: AMSNoBakeDeployment
```

9. Choose **Start deployment**. Resource Tagger tags your instances
   `ams:rt:backup-orchestrator: true`, ensuring that your instances are backed
   up in accordance with the default AMS backup plan.
