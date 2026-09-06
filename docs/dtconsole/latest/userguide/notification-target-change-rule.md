

# Add or remove a target for a notification rule
<a name="notification-target-change-rule"></a>

You can edit a notification rule to change the target or targets to which it sends notifications. You can use the Developer Tools console or or the AWS CLI to change a notification rule's targets.<a name="notification-target-change-rule-console"></a>

# To change the targets for a notification rule (console)
<a name="notification-target-change-rule-console"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. In the navigation bar, expand **Settings**, and then choose **Notification rules**.

1. In **Notification rules**, review the list of rules configured for your resources in your AWS account in the AWS Region where you are currently signed in. Use the selector to change the AWS Region.

1. Choose the rule, and then choose **Edit**. 

1. In **Targets**, do one of the following:
   + To add another target, choose **Add Target**, and then choose the Amazon SNS topic or AWS Chatbot (Slack) or AWS Chatbot (Microsoft Teams) client that you want to add from the list. You can also choose **Create SNS topic** to create a topic and add it as a target. A notification rule can have up to 10 targets.
   + To remove a target, next to the target you want to remove, choose **Remove target**.

1. Choose **Submit**.<a name="notification-target-change-rule-add-cli"></a>

# To add a target to a notification rule (AWS CLI)
<a name="notification-target-change-rule-add-cli"></a>

1. At a terminal or command prompt, run the **subscribe** command to add a target. For example, the following command adds an Amazon SNS topic as a target for a notification rule.

   ```
   aws codestar-notifications subscribe --arn arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE --target TargetType=SNS,TargetAddress=arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}}
   ```

1. If successful, the command returns the ARN of the updated notification rule, similar to the following.

   ```
   {
       "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE"
   }
   ```<a name="notification-target-change-rule-remove-cli"></a>

# To remove a target from a notification rule (AWS CLI)
<a name="notification-target-change-rule-remove-cli"></a>

1. At a terminal or command prompt, run the the **unsubscribe** command to remove a target. For example, the following command removes an Amazon SNS topic as a target for a notification rule.

   ```
   aws codestar-notifications unsubscribe --arn arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE --target TargetType=SNS,TargetAddress=arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}}
   ```

1. If successful, the command returns the ARN of the updated notification rule and information about the removed target, similar to the following.

   ```
   {
       "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE"
       "TargetAddress": "arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}}"
   }
   ```

## See also
<a name="notification-target-change-also"></a>
+ [Edit a notification rule](notification-rule-edit.md)
+ [Enable or disable notifications for a notification rule](notification-rule-enable-disable.md)