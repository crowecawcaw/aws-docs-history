# Step 3: Create a custom AWS AppConfig extension

An extension defines one or more actions that it performs during an AWS AppConfig workflow. For
example, the AWS authored `AWS AppConfig deployment events to Amazon SNS` extension includes an action to send a notification to an
Amazon SNS topic. Each action is invoked either when you interact with AWS AppConfig or when AWS AppConfig is performing a process on your behalf. These are
called _action points_. AWS AppConfig extensions support the following
action points:

**PRE\_\* action points**: Extension actions configured on
`PRE_*` action points are applied after request validation, but before AWS AppConfig
performs the activity that corresponds to the action point name. These action invocations
are processed at the same time as a request. If more than one request is made, action
invocations run sequentially. Also note that `PRE_*` action points receive and
can change the contents of a configuration. `PRE_*` action points can also
respond to an error and prevent an action from happening.

- `PRE_CREATE_HOSTED_CONFIGURATION_VERSION`
- `PRE_START_DEPLOYMENT`
  **ON\_\* action points**: An extension can also run in
  parallel with an AWS AppConfig workflow by using an `ON_*` action point.
  `ON_*` action points are invoked asynchronously. `ON_*` action
  points don't receive the contents of a configuration. If an extension experiences an
  error during an `ON_*` action point, the service ignores the error and continues
  the workflow.

- `ON_DEPLOYMENT_START`
- `ON_DEPLOYMENT_STEP`
- `ON_DEPLOYMENT_BAKING`
- `ON_DEPLOYMENT_COMPLETE`
- `ON_DEPLOYMENT_ROLLED_BACK`
  **AT\_\* action points**: Extension actions configured on
  `AT_*` action points are invoked synchronously and in parallel to an AWS AppConfig
  workflow. If an extension experiences an error during an `AT_*` action point, the
  service stops the workflow and rolls back the deployment.

- `AT_DEPLOYMENT_TICK`
  The `AT_DEPLOYMENT_TICK` action point supports third-party monitoring
  integration. `AT_DEPLOYMENT_TICK` is invoked during configuration deployment
  processing orchestration. If you use a third-party monitoring solution (for example,
  Datadog or New Relic), you can create an AWS AppConfig extension that checks for alarms at the
  `AT_DEPLOYMENT_TICK` action point and, as a safety guardrail, rolls back the
  deployment if it triggered an alarm.

If you use a third-party monitoring solution like Datadog or New Relic, you can create an
AWS AppConfig extension that checks for alarms at the `AT_DEPLOYMENT_TICK` action point
and, as a safety guardrail, rolls back the deployment if it triggered an alarm. For more information, see the following Datadog and New Relic integration examples on GitHub:

- [Datadog](https://github.com/aws-samples/aws-appconfig-tick-extn-for-datadog "https://github.com/aws-samples/aws-appconfig-tick-extn-for-datadog")
- [New Relic](https://github.com/aws-samples/sample-aws-appconfig-tick-extn-for-newrelic "https://github.com/aws-samples/sample-aws-appconfig-tick-extn-for-newrelic")
  For more
  information about AWS AppConfig extensions, see the following topics:

- [Extending AWS AppConfig workflows using extensions](working-with-appconfig-extensions.md "working-with-appconfig-extensions.md")
- [Walkthrough: Creating custom AWS AppConfig extensions](working-with-appconfig-extensions-creating-custom.md "working-with-appconfig-extensions-creating-custom.md")

###### Sample extension

The following sample extension defines one action that calls the
`PRE_CREATE_HOSTED_CONFIGURATION_VERSION` action point. In the
`Uri` field, the action specifies the Amazon Resource Name (ARN) of the
`MyS3ConfigurationBackUpExtension` Lambda function created earlier in this
walkthrough. The action also specifies the AWS Identity and Access Management (IAM) assume role ARN created
earlier in this walkthrough.

**Sample AWS AppConfig extension**

```
{
    "Name": "MySampleExtension",
    "Description": "A sample extension that backs up configurations to an S3 bucket.",
    "Actions": {
        "PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [
            {
                "Name": "PreCreateHostedConfigVersionActionForS3Backup",
                "Uri": "arn:aws:lambda:`aws-region`:111122223333:function:MyS3ConfigurationBackUpExtension",
                "RoleArn": "arn:aws:iam::111122223333:role/ExtensionsTestRole"
            }
        ]
    },
    "Parameters" : {
        "S3_BUCKET": {
            "Required": false
        }
    }
}
```

###### Note

To view request syntax and field descriptions when creating an extension, see the
[CreateExtension](../../2019-10-09/APIReference/API_CreateExtension.md "../../2019-10-09/APIReference/API_CreateExtension.md")
topic in the _AWS AppConfig API Reference_.

###### To create an extension (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/ "https://console.aws.amazon.com/systems-manager/appconfig/").
2. In the navigation pane, choose **AWS AppConfig**.
3. On the **Extensions** tab, choose **Create
   extension**.
4. For **Extension name**, enter a unique name. For the purposes of
   this walkthrough, enter `MyS3ConfigurationBackUpExtension`.
   Optionally, enter a description.
5. In the **Actions** section, choose **Add new
   action**.
6. For **Action name**, enter a unique name. For the purposes of this
   walkthrough, enter `PreCreateHostedConfigVersionActionForS3Backup`.
   This name describes the action point used by the action and the extension
   purpose.
7. In the **Action point** list, choose
   **PRE_CREATE_HOSTED_CONFIGURATION_VERSION**.
8. For **Uri**, choose **Lambda function** and then
   choose the function in the **Lambda function** list. If you don't see
   your function, verify that you are in the same AWS Region where you created the
   function.
9. For **IAM Role**, choose the role you created earlier in this
   walkthrough.
10. In the **Extension parameters (optional)** section, choose
    **Add new parameter**.
11. For **Parameter name**, enter a name. For the purposes of this
    walkthrough, enter `S3_BUCKET`.
12. Repeat steps 5–11 to create a second action for the
    `PRE_START_DEPLOYMENT` action point.
13. Choose **Create extension**.
