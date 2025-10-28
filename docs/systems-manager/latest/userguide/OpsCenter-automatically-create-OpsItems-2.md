# Configure EventBridge rules to

create OpsItems

When Amazon EventBridge receives an event, it creates a new OpsItem based on default rules. You
can create a rule or edit an existing rule to set OpsCenter as the target of an EventBridge
event. For information about how to create an event rule, see [Creating a rule for an
AWS service](../../../eventbridge/latest/userguide/create-eventbridge-rule.md "../../../eventbridge/latest/userguide/create-eventbridge-rule.md") in the _Amazon EventBridge User Guide_.

###### To configure an EventBridge rule to create OpsItems in OpsCenter

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. On the **Rules** page, for **Event
   bus**, choose **default**.
4. For **Rules**, choose a rule by selecting the check box
   next to its name.
5. Select the name of the rule to open its details page. In **Rule
   details**, verify that **Status** is set to
   **Enabled**.

###### Note

If required, you can update the status using **Edit**
in the upper-right corner of the page. 6. Choose the **Targets** tab. 7. On the **Targets** tab, choose
**Edit**. 8. For **Target types**, select
**AWS service**. 9. For **Select a target**, choose **Systems Manager
OpsItem**. 10. For many target types, EventBridge needs permission to send events to the target.
In these cases, EventBridge can create the AWS Identity and Access Management (IAM) role needed for your
rule to run:

    * To create an IAM role automatically, choose **Create a
     new role for this specific resource**.
    * To use an IAM role that you created to give EventBridge permission to
     create OpsItems in OpsCenter, choose **Use existing
     role**.

11. In **Additional settings**, for **Configure
    target input**, choose **Input
    Transformer**.

You can use the **Input transformer** option to specify a
deduplication string and other important information for OpsItems, such as
title and severity. 12. Choose **Configure input transformer**. 13. In **Target input transformer**, for **Input
path**, specify the values to parse from the triggering event.
For example, to parse the start time, end time, and other details from the
event that triggers the rule, use the following JSON.

```
{
    "end-time": "$.detail.EndTime",
    "failure-cause": "$.detail.cause",
    "resources": "$.resources[0]",
    "source": "$.detail.source",
    "start-time": "$.detail.StartTime"
}
```

14. For **Template**, specify the information to send to the
    target. For example, use the following JSON to pass information to
    OpsCenter. The information is used to create an OpsItem.

###### Note

If the input template is in the JSON format, then the object value in
the template can't include quotes. For example, the values for
resources, failure-cause, source, start time, and end time can't be in
quotes.

```
{
    "title": "EBS snapshot copy failed",
    "description": "CloudWatch Event Rule SSMOpsItems-EBS-snapshot-copy-failed was triggered. Your EBS snapshot copy has failed. See below for more details.",
    "category": "Availability",
    "severity": "2",
    "source": "EC2",
    "operationalData": {
        "/aws/dedup": {
            "type": "SearchableString",
            "value": "{\"dedupString\":\"SSMOpsItems-EBS-snapshot-copy-failed\"}"
        },
        "/aws/automations": {
            "value": "[ { \"automationType\": \"AWS:SSM:Automation\", \"automationId\": \"AWS-CopySnapshot\" } ]"
        },
        "failure-cause": {
            "value": <failure-cause>
        },
        "source": {
            "value": <source>
        },
        "start-time": {
            "value": <start-time>
        },
        "end-time": {
            "value": <end-time>
        },
         },
        "resources": {
            "value": <resources>
        }
    }
}
```

For more information about these fields, see [Transforming target
input](../../../eventbridge/latest/userguide/transform-input.md "../../../eventbridge/latest/userguide/transform-input.md") in the _Amazon EventBridge User Guide_. 15. Choose **Confirm**. 16. Choose **Next**. 17. Choose **Next**. 18. Choose **Update rule**.
After an OpsItem is created from an event, you can view the event details by opening
the OpsItem and scrolling down to the **Private operational data**
section. For information about how to configure the options in an OpsItem, see [Manage OpsItems](OpsCenter-working-with-OpsItems.md "OpsCenter-working-with-OpsItems.md").
