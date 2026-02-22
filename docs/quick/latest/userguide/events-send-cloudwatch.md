# Creating rules to send Amazon Quick Sight events to

Amazon CloudWatch

You can write simple rules to indicate which Amazon Quick Sight events interest you and which
automated actions to take when an event matches a rule. For example, you can configure
Amazon Quick Sight to send events to Amazon CloudWatch whenever a Amazon Quick Sight asset is placed in a folder. For
more information, see the [Amazon EventBridge user
guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Under **Events** in the navigation pane, choose
   **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. The rule name must be unique within
   this Region. For example, enter
   `QuickSightAssetChangeRuleCloudWatch`.
5. Choose **default** Event bus.
6. Choose **Rule with an event pattern**, and then choose
   **Next**.
7. For **Event source**, choose **AWS events or EventBridge
   partner events**.
8. In the **Creation method** section, choose **Custom
   pattern (JSON editor)**.
9. In the **Event pattern** text box, enter the following
   snippet and choose **Next**.

```
{
  "source": ["aws.quicksight"]
}
```

Alternatively, you can create the rule that only subscribes to a subset of
event types in Amazon Quick Sight. For example, the following rule will only triggered when
an asset is added to or removed from a folder with id
`77e307e8-b41b-472a-90e8-fe3f471537be`.

```
{
  "source": ["aws.quicksight"],
  "detail-type": ["QuickSight Folder Membership Updated"],
  "detail": {
    "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be"
  }
}
```

10. For **Targets**, choose **AWS service**
    > **CloudWatch log group.**
11. Choose from an existing log group or create a new one by entering a new log
    group name.
12. Optionally, you can add another target for this rule.
13. In **Configure tags**, choose
    **Next**.
14. Choose **Create rule**.
    For more information, see [Creating Amazon EventBridge rule that
    reacts To events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the Amazon EventBridge user guide.
