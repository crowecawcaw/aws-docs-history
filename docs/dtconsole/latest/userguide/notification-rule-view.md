

# View notification rules
<a name="notification-rule-view"></a>

You can use the Developer Tools console or the AWS CLI to view all of the notification rules for all resources in an AWS Region. You can also view the details of each notification rule. Unlike the process for creating a notification rule, you do not have to go to the resource page for the resource.<a name="notification-rule-view-console"></a>

# To view notification rules (console)
<a name="notification-rule-view-console"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. In the navigation bar, expand **Settings**, and then choose **Notification rules**.

1. In **Notification rules**, review the list of rules configured for your resources in your AWS account in the AWS Region where you are currently signed in. Use the selector to change the AWS Region.

1. To view the details of a notification rule, choose it from the list, and then choose **View details**. You can also simply choose its name in the list.<a name="notification-rule-view-list-cli"></a>

# To view a list of notification rules (AWS CLI)
<a name="notification-rule-view-list-cli"></a>

1. At a terminal or command prompt, run the **list-notification-rules** command to view all notification rules for the specified AWS Region.

   ```
   aws codestar-notifications list-notification-rules --region {{us-east-1}}
   ```

1. If successful, this command returns the ID and ARN for each notification rule in the AWS Region, similar to the following.

   ```
   {
       "NotificationRules": [
           {
               "Id": "dc82df7a-EXAMPLE",
               "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE"
           },
           {
               "Id": "8d1f0983-EXAMPLE",
               "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/8d1f0983-EXAMPLE"
           }
       ]
   }
   ```<a name="notification-rule-view-details-cli"></a>

# To view details of a notification rule (AWS CLI)
<a name="notification-rule-view-details-cli"></a>

1. At a terminal or command prompt, run the **describe-notification-rule** command, specifying the ARN of the notification rule.

   ```
   aws codestar-notifications describe-notification-rule --arn arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE
   ```

1. If successful, the command returns output similar to the following.

   ```
   {
       "LastModifiedTimestamp": 1569199844.857,
       "EventTypes": [
           {
               "ServiceName": "CodeCommit",
               "EventTypeName": "Branches and tags: Created",
               "ResourceType": "Repository",
               "EventTypeId": "codecommit-repository-branches-and-tags-created"
           }
       ],
       "Status": "ENABLED",
       "DetailType": "FULL",
       "Resource": "arn:aws:codecommit:{{us-east-1}}:{{123456789012}}:{{MyDemoRepo}}",
       "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE",
       "Targets": [
           {
               "TargetStatus": "ACTIVE",
               "TargetAddress": "arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}}",
               "TargetType": "SNS"
           }
       ],
       "Name": "{{MyNotificationRule}}",
       "CreatedTimestamp": 1569199844.857,
       "CreatedBy": "arn:aws:iam::123456789012:user/Mary_Major"
   }
   ```<a name="notification-rule-view-tags-cli"></a>

# To view a list of tags for a notification rule (AWS CLI)
<a name="notification-rule-view-tags-cli"></a>

1. At a terminal or command prompt, run the **list-tags-for-resource** command to view all tags for a specified notification rule ARN.

   ```
   aws codestar-notifications list-tags-for-resource --arn arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/fe1efd35-EXAMPLE
   ```

1. If successful, this command returns output similar to the following.

   ```
   {
       "Tags": {
           "Team": "Li_Juan"
       }
   }
   ```