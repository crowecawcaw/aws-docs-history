

# Tutorial: Set up an Amazon SNS topic
<a name="match-notification-sns"></a>

You can have Amazon GameLift Servers publish all events that a FlexMatch matchmaker generates to an Amazon SNS topic.

**To create an SNS topic for Amazon GameLift Servers event notifications**

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns).

1. In the navigation pane, choose **Topics**.

1. On the **Topics** page, choose **Create topic**.

1. Create a topic in the console. For more information, see [To create a topic using the AWS Management Console](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html#create-topic-aws-console) in the *Amazon Simple Notification Service Developer Guide*.

1. On the **Details** page for your topic, choose **Edit**.

1. (Optional) On the **Edit** page for your topic, expand **Access policy**, then add the bold syntax from the following AWS Identity and Access Management (IAM) policy statement to the end of your existing policy. (The entire policy is shown here for clarity.) Be sure to use the Amazon Resource Name (ARN) details for your own SNS topic and Amazon GameLift Servers matchmaking configuration.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Id": "__default_policy_ID",
     "Statement": [
       {
         "Sid": "__default_statement_ID",
         "Effect": "Allow",
         "Principal": {
           "AWS": "*"
         },
         "Action": [
           "SNS:GetTopicAttributes",
           "SNS:SetTopicAttributes",
           "SNS:AddPermission",
           "SNS:RemovePermission",
           "SNS:DeleteTopic",
           "SNS:Subscribe",
           "SNS:ListSubscriptionsByTopic",
           "SNS:Publish"
         ],
         "Resource": "arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{your_topic_name}}",
         "Condition": {
           "StringEquals": {
           "AWS:SourceAccount": "{{111122223333}}"
           }
         }
       },
       {
         "Sid": "__console_pub_0",
         "Effect": "Allow",
         "Principal": {
           "Service": "gamelift.amazonaws.com"
         },
         "Action": "SNS:Publish",
         "Resource": "arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{your_topic_name}}",
         "Condition": {
           "ArnLike": {
           "aws:SourceArn": "arn:aws:gamelift:{{us-east-1}}:{{111122223333}}:matchmakingconfiguration/{{your_configuration_name}}"
           }
         }
       }
     ]
   }
   ```

------

1. Choose **Save changes**.