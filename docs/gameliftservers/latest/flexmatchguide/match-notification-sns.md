# Tutorial: Set up an Amazon SNS topic

You can have Amazon GameLift Servers publish all events that a FlexMatch matchmaker generates to an Amazon SNS
topic.

###### To create an SNS topic for Amazon GameLift Servers event notifications

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns "https://console.aws.amazon.com/sns").
2. In the navigation pane, choose **Topics**.
3. On the **Topics** page, choose **Create
   topic**.
4. Create a topic in the console. For more information, see [To create a topic
   using the AWS Management Console](../../../sns/latest/dg/sns-create-topic.md#create-topic-aws-console "../../../sns/latest/dg/sns-create-topic.md#create-topic-aws-console") in the _Amazon Simple Notification Service Developer Guide_.
5. On the **Details** page for your topic, choose
   **Edit**.
6. (Optional) On the **Edit** page for your topic, expand
   **Access policy**, then add the bold syntax from the following
   AWS Identity and Access Management (IAM) policy statement to the end of your existing policy. (The entire policy
   is shown here for clarity.) Be sure to use the Amazon Resource Name (ARN) details for your
   own SNS topic and Amazon GameLift Servers matchmaking configuration.

JSON

```
`{
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
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`your_topic_name`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`111122223333`"
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
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`your_topic_name`",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:gamelift:`us-east-1`:`111122223333`:matchmakingconfiguration/`your_configuration_name`"
 }
 }
 }
 ]
}`

```

7. Choose **Save changes**.
