

# Delete a notification rule
<a name="notification-rule-delete"></a>

There can be only 10 notification rules configured for a resource, so consider deleting rules you no longer need. You can use the Developer Tools console or the AWS CLI to delete a notification rule.

**Note**  
You cannot undo the deletion of a notification rule, but you can recreate it. Deleting a notification rule does not delete the target.<a name="notification-rule-delete-console"></a>

# To delete a notification rule (console)
<a name="notification-rule-delete-console"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. In the navigation bar, expand **Settings**, and then choose **Notification rules**.

1. In **Notification rules**, review the rules configured for resources in your AWS account in the AWS Region where you are currently signed in. Use the selector to change the AWS Region.

1. Choose the notification rule, and then choose **Delete**.

1. Type **delete**, and then choose **Delete**.<a name="notification-rule-delete-cli"></a>

# To delete a notification rule (AWS CLI)
<a name="notification-rule-delete-cli"></a>

1. At a terminal or command prompt, run the **delete-notification-rule** command, specifying the ARN of the notification rule.

   ```
   aws codestar-notifications delete-notification-rule --arn arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE
   ```

1. If successful, the command returns the ARN of the deleted notification rule, similar to the following.

   ```
   {
       "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE"
   }
   ```