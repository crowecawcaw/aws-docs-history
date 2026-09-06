

# Create a notification rule
<a name="notification-rule-create"></a>

You can use the Developer Tools console or the AWS CLI to create notification rules. You can create an Amazon SNS topic to use as a target for a notification rule as part of creating the rule. If you want to use an AWS Chatbot client as a target, you must create that client before you can create the rule. For more information, see [Configure an AWS Chatbot client for a Slack channel](notifications-chatbot.md#notifications-chatbot-configure-client).<a name="notification-rule-create-console"></a>

# To create a notification rule (console)
<a name="notification-rule-create-console"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. Use the navigation bar to navigate to the resource. 
   + For CodeBuild, choose **Build**, choose **Build projects**, and choose a build project.
   + For CodeCommit, choose **Source**, choose **Repositories**, and choose a repository.
   + For CodeDeploy, choose **Applications**, and choose an application.
   + For CodePipeline, choose **Pipeline**, choose **Pipelines**, and choose a pipeline.

1. On the resource page, choose **Notify**, and then choose **Create notification rule**. You can also go to the **Settings** page for the resource, go to **Notifications** or **Notification rules**, and then choose **Create notification rule**.

1. In **Notification name**, enter a name for the rule.

1. In **Detail type**, choose **Basic** if you want only the information provided to Amazon EventBridge included in the notification. Choose **Full** if you want to include information provided to Amazon EventBridge and information that might be supplied by the resource service or the notification manager.

   For more information, see [Understanding notification contents and security](security.md#security-notifications).

1.  In **Events that trigger notifications**, select the events for which you want to send notifications. For event types for a resource, see the following:
   + CodeBuild: [Events for notification rules on build projects](concepts.md#events-ref-buildproject)
   + CodeCommit: [Events for notification rules on repositories](concepts.md#events-ref-repositories)
   + CodeDeploy: [Events for notification rules on deployment applications](concepts.md#events-ref-deployapplication)
   + CodePipeline: [Events for notification rules on pipelines](concepts.md#events-ref-pipeline)

1. In **Targets**, do one of the following:
   + If you have already configured a resource to use with notifications, in **Choose target type**, choose either **AWS Chatbot (Slack)**,  **AWS Chatbot (Microsoft Teams)**, or **SNS topic**. In **Choose target**, choose the name of the client (for a Slack or Microsoft Teams client configured in AWS Chatbot) or the Amazon Resource Name (ARN) of the Amazon SNS topic (for Amazon SNS topics already configured with the policy required for notifications).
   + If you have not configured a resource to use with notifications, choose **Create target**, and then choose **SNS topic**. Provide a name for the topic after **codestar-notifications-**, and then choose **Create**.
**Note**  
If you create the Amazon SNS topic as part of creating the notification rule, the policy that allows the notifications feature to publish events to the topic is applied for you. Using a topic created for notification rules helps ensure that you subscribe only those users that you want to receive notifications about this resource.
You cannot create an AWS Chatbot client as part of creating a notification rule. If you choose AWS Chatbot (Slack) or AWS Chatbot (Microsoft Teams), you will see a button directing you to configure a client in AWS Chatbot. Choosing that option opens the AWS Chatbot console. For more information, see [Configure an AWS Chatbot client for a Slack channel](notifications-chatbot.md#notifications-chatbot-configure-client).
If you want to use an existing Amazon SNS topic as a target, you must add the required policy for AWS CodeStar Notifications in addition to any other policies that might exist for that topic. For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md) and [Understanding notification contents and security](security.md#security-notifications). 


1. Choose **Submit**, and then review the notification rule.
**Note**  
Users must subscribe and confirm subscriptions to the Amazon SNS topic you specified as the target of the rule before they will receive notifications. For more information, see [To subscribe users to an Amazon SNS topic used for notifications](subscribe-users-sns.md#set-up-sns-subscribe).<a name="notification-rule-create-cli"></a>

# To create a notification rule (AWS CLI)
<a name="notification-rule-create-cli"></a>

1. At a terminal or command prompt, run the **create-notification rule** command to generate the JSON skeleton.

   ```
   aws codestar-notifications create-notification-rule --generate-cli-skeleton > {{rule.json}}
   ```

   You can name the file anything you want. In this example, the file is named {{rule.json}}.

1. Open the JSON file in a plaintext editor and edit it to include the resource, event types, and Amazon SNS target that you want for the rule. 

   The following example shows a notification rule named **MyNotificationRule** for a repository named {{MyDemoRepo}} in an AWS account with the ID {{123456789012}}. Notifications with the full detail type are sent to an Amazon SNS topic named {{MyNotificationTopic}} when branches and tags are created.

   ```
   {
       "Name": "{{MyNotificationRule}}",
       "EventTypeIds": [
           "codecommit-repository-branches-and-tags-created"
       ],
       "Resource": "arn:aws:codecommit:{{us-east-1}}:{{123456789012}}:{{MyDemoRepo}}",
       "Targets": [
           {
               "TargetType": "SNS",
               "TargetAddress": "arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}}"
           }
       ],
       "Status": "ENABLED",
       "DetailType": "FULL"
   }
   ```

   Save the file.

1. Using the file you just edited, at the terminal or command line, run the **create-notification-rule** command again to create the notification rule.

   ```
   aws codestar-notifications create-notification-rule --cli-input-json  file://{{rule}}.json
   ```

1. If successful, the command returns the ARN of the notification rule, similar to the following.

   ```
   {
       "Arn": "arn:aws:codestar-notifications:{{us-east-1}}:{{123456789012}}:notificationrule/dc82df7a-EXAMPLE"
   }
   ```<a name="notification-rule-list-event-types"></a>

# To list event types for notification rules (AWS CLI)
<a name="notification-rule-list-event-types"></a>

1. At a terminal or command prompt, run the **list-event-types** command. You can use the `--filters` option to limit the response to a specific resource type or other attribute. For example, the following returns a list of event types for CodeDeploy applications.

   ```
   aws codestar-notifications list-event-types --filters Name=SERVICE_NAME,Value=CodeDeploy
   ```

1. This command produces output similar to the following.

   ```
   {
       "EventTypes": [
           {
               "EventTypeId": "codedeploy-application-deployment-succeeded",
               "ServiceName": "CodeDeploy",
               "EventTypeName": "Deployment: Succeeded",
               "ResourceType": "Application"
           },
           {
               "EventTypeId": "codedeploy-application-deployment-failed",
               "ServiceName": "CodeDeploy",
               "EventTypeName": "Deployment: Failed",
               "ResourceType": "Application"
           },
           {
               "EventTypeId": "codedeploy-application-deployment-started",
               "ServiceName": "CodeDeploy",
               "EventTypeName": "Deployment: Started",
               "ResourceType": "Application"
           }
       ]
   }
   ```<a name="notification-rule-add-tag"></a>

# To add a tag to a notification rule (AWS CLI)
<a name="notification-rule-add-tag"></a>

1. At a terminal or command prompt, run the **tag-resource** command. For example, use the following command to add a tag key-value pair that has the name {{Team}} and the value {{Li\_Juan}}.

   ```
   aws codestar-notifications tag-resource --arn arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/fe1efd35-EXAMPLE --tags Team=Li_Juan
   ```

1. This command produces output similar to the following.

   ```
   {
       "Tags": {
           "Team": "Li_Juan"
       }
   }
   ```