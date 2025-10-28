# Using resource-based policies for Amazon EventBridge

When a [rule](eb-rules.md "eb-rules.md") runs in EventBridge, all of the [targets](eb-targets.md "eb-targets.md") associated with the rule are invoked. Rules can
invoke AWS Lambda functions, publish to Amazon SNS topics, or relay the event to Kinesis streams. To
make API calls against the resources you own, EventBridge needs the appropriate permissions. For
Lambda, Amazon SNS, Amazon SQS, and Amazon CloudWatch Logs resources, EventBridge uses resource-based policies. For Kinesis
streams, EventBridge uses [identity-based](eb-use-identity-based.md "eb-use-identity-based.md")
policies.

You use the AWS CLI to add permissions to your targets. For information about how to install
and configure the AWS CLI, see [Getting
Set Up with the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the _AWS Command Line Interface User Guide_.

###### Topics

- [Amazon API Gateway permissions](#eb-api-gateway-permissions "#eb-api-gateway-permissions")
- [CloudWatch Logs permissions](#eb-cloudwatchlogs-permissions "#eb-cloudwatchlogs-permissions")
- [AWS Lambda permissions](#eb-lambda-permissions "#eb-lambda-permissions")
- [Amazon SNS permissions](#eb-sns-permissions "#eb-sns-permissions")
- [Amazon SQS permissions](#eb-sqs-permissions "#eb-sqs-permissions")
- [EventBridge Pipes specifics](#eb-pipes-identity-diff "#eb-pipes-identity-diff")

## Amazon API Gateway permissions

To invoke your Amazon API Gateway endpoint by using a EventBridge rule, add the following permission
to the policy of your API Gateway endpoint.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "execute-api:Invoke",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:events:`us-east-1`:`123456789012`:rule/`rule-name`"
 }
 },
 "Resource": [
 "arn:aws:execute-api:`us-east-1`:`123456789012`:`API-id`/stage/GET/`api`"
 ]
 }
 ]
}`

```

## CloudWatch Logs permissions

When CloudWatch Logs is the target of a rule, EventBridge creates log streams, and CloudWatch Logs stores the
text from the events as log entries. To allow EventBridge to create the log stream and log the
events, CloudWatch Logs must include a resource-based policy that enables EventBridge to write to
CloudWatch Logs.

If you use the AWS Management Console to add CloudWatch Logs as the target of a rule, the resource-based
policy is created automatically. If you use the AWS CLI to add the target, and the policy
doesn't already exist, you must create it.

For more information, see [PutResourcePolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md") in the _CloudWatch Logs API Reference guide_.

## AWS Lambda permissions

To invoke your AWS Lambda function by using a EventBridge rule, add the following permission
to the policy of your Lambda function.

```
{
  "Effect": "Allow",
  "Action": "lambda:InvokeFunction",
  "Resource": "arn:aws:lambda:`region`:`account-id`:function:`function-name`",
  "Principal": {
    "Service": "events.amazonaws.com"
  },
  "Condition": {
    "ArnLike": {
      "AWS:SourceArn": "arn:aws:events:`region`:`account-id`:rule/`rule-name`"
    }
  },
  "Sid": "InvokeLambdaFunction"
}
```

###### To add the above permissions that enable EventBridge to invoke Lambda functions using the AWS CLI

- At a command prompt, enter the following command.

```
aws lambda add-permission --statement-id "InvokeLambdaFunction" \
--action "lambda:InvokeFunction" \
--principal "events.amazonaws.com" \
--function-name "arn:aws:lambda:`region`:`account-id`:function:`function-name`" \
--source-arn "arn:aws:events:`region`:`account-id`:rule/`rule-name`"
```

For more information about setting permissions that enable EventBridge to invoke Lambda
functions, see [AddPermission](../../../lambda/latest/dg/API_AddPermission.md "../../../lambda/latest/dg/API_AddPermission.md")
and [Using Lambda with Scheduled
Events](../../../lambda/latest/dg/with-scheduled-events.md "../../../lambda/latest/dg/with-scheduled-events.md") in the _AWS Lambda Developer Guide_.

## Amazon SNS permissions

To allow EventBridge to publish to an Amazon SNS topic, use the `aws sns
 get-topic-attributes` and the `aws sns set-topic-attributes`
commands.

###### Note

You can't use `Condition` blocks in Amazon SNS topic policies for
EventBridge.

###### To add permissions that enable EventBridge to publish SNS topics

1. To list the attributes of an SNS topic, use the following command.

```
aws sns get-topic-attributes --topic-arn "arn:aws:sns:`region`:`account-id`:`topic-name`"
```

The following example shows the result of a new SNS topic.

```
{
    "Attributes": {
        "SubscriptionsConfirmed": "0",
        "DisplayName": "",
        "SubscriptionsDeleted": "0",
        "EffectiveDeliveryPolicy": "{\"http\":{\"defaultHealthyRetryPolicy\":{\"minDelayTarget\":20,\"maxDelayTarget\":20,\"numRetries\":3,\"numMaxDelayRetries\":0,\"numNoDelayRetries\":0,\"numMinDelayRetries\":0,\"backoffFunction\":\"linear\"},\"disableSubscriptionOverrides\":false}}",
        "Owner": "`account-id`",
        "Policy": "{\"Version\":\"2012-10-17\",		 	 	 \"Id\":\"__default_policy_ID\",\"Statement\":[{\"Sid\":\"__default_statement_ID\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":[\"SNS:GetTopicAttributes\",\"SNS:SetTopicAttributes\",\"SNS:AddPermission\",\"SNS:RemovePermission\",\"SNS:DeleteTopic\",\"SNS:Subscribe\",\"SNS:ListSubscriptionsByTopic\",\"SNS:Publish\"],\"Resource\":\"arn:aws:sns:`region`:`account-id`:`topic-name`\",\"Condition\":{\"StringEquals\":{\"AWS:SourceOwner\":\"`account-id`\"}}}]}",
        "TopicArn": "arn:aws:sns:`region`:`account-id`:`topic-name`",
        "SubscriptionsPending": "0"
    }
}
```

2. Use a [JSON to
   string converter](https://tools.knowledgewalls.com/jsontostring "https://tools.knowledgewalls.com/jsontostring") to convert the following statement to a
   string.

```
{
  "Sid": "PublishEventsToMyTopic",
  "Effect": "Allow",
  "Principal": {
    "Service": "events.amazonaws.com"
  },
  "Action": "sns:Publish",
  "Resource": "arn:aws:sns:`region`:`account-id`:`topic-name`"
}
```

After you convert the statement to a string, it looks like the following
example.

```
{\"Sid\":\"PublishEventsToMyTopic\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"events.amazonaws.com\"},\"Action\":\"sns:Publish\",\"Resource\":\"arn:aws:sns:`region`:`account-id`:`topic-name`\"}
```

3. Add the string you created in the previous step to the
   `"Statement"` collection inside the `"Policy"`
   attribute.
4. Use the `aws sns set-topic-attributes` command to set the new
   policy.

```
aws sns set-topic-attributes --topic-arn "arn:aws:sns:`region`:`account-id`:`topic-name`" \
--attribute-name Policy \
--attribute-value "{\"Version\":\"2012-10-17\",		 	 	 \"Id\":\"__default_policy_ID\",\"Statement\":[{\"Sid\":\"__default_statement_ID\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":[\"SNS:GetTopicAttributes\",\"SNS:SetTopicAttributes\",\"SNS:AddPermission\",\"SNS:RemovePermission\",\"SNS:DeleteTopic\",\"SNS:Subscribe\",\"SNS:ListSubscriptionsByTopic\",\"SNS:Publish\"],\"Resource\":\"arn:aws:sns:`region`:`account-id`:`topic-name`\",\"Condition\":{\"StringEquals\":{\"AWS:SourceOwner\":\"`account-id`\"}}}, {\"Sid\":\"PublishEventsToMyTopic\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"events.amazonaws.com\"},\"Action\":\"sns:Publish\",\"Resource\":\"arn:aws:sns:`region`:`account-id`:`topic-name`\"}]}"
```

For more information, see the [SetTopicAttributes](../../../sns/latest/api/API_SetTopicAttributes.md "../../../sns/latest/api/API_SetTopicAttributes.md") action in the
_Amazon Simple Notification Service API Reference_.

## Amazon SQS permissions

To allow an EventBridge rule to invoke an Amazon SQS queue, use the `aws sqs
 get-queue-attributes` and `aws sqs set-queue-attributes`
commands.

If the policy for the SQS queue is empty, you first need to create a policy and then
you can add the permissions statement to it. A new SQS queue has an empty policy.

If the SQS queue already has a policy, you need to copy the original policy and
combine it with a new statement to add the permissions statement to it.

###### To add permissions that enable EventBridge rules to invoke an SQS queue

1. To list SQS queue attributes. At a command prompt, enter the following
   command.

```
aws sqs get-queue-attributes \
--queue-url https://sqs.`region`.amazonaws.com/`account-id`/`queue-name` \
--attribute-names Policy
```

2. Add the following statement.

```
{
      "Sid": "AWSEvents_custom-eventbus-ack-sqs-rule_dlq_sqs-rule-target",
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:`region`:`account-id`:`queue-name`",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:events:`region`:`account-id`:rule/`bus-name`/`rule-name`"
        }
      }
    }
```

3. Use a [JSON to
   string converter](https://tools.knowledgewalls.com/jsontostring "https://tools.knowledgewalls.com/jsontostring") to convert the preceding statement into a string.
   After you convert the policy to a string, it looks like the following.

```
{\"Sid\": \"EventsToMyQueue\", \"Effect\": \"Allow\", \"Principal\": {\"Service\": \"events.amazonaws.com\"}, \"Action\": \"sqs:SendMessage\", \"Resource\": \"arn:aws:sqs:`region`:`account-id`:`queue-name`\", \"Condition\": {\"ArnEquals\": {\"aws:SourceArn\": \"arn:aws:events:`region`:`account-id`:rule/`rule-name`\"}}
```

4. Create a file called `set-queue-attributes.json` with the
   following content.

```
{
    "Policy": "{\"Version\":\"2012-10-17\",		 	 	 \"Id\":\"arn:aws:sqs:`region`:`account-id`:`queue-name`/SQSDefaultPolicy\",\"Statement\":[{\"Sid\": \"EventsToMyQueue\", \"Effect\": \"Allow\", \"Principal\": {\"Service\": \"events.amazonaws.com\"}, \"Action\": \"sqs:SendMessage\", \"Resource\": \"arn:aws:sqs:`region`:`account-id`:`queue-name`\", \"Condition\": {\"ArnEquals\": {\"aws:SourceArn\": \"arn:aws:events:`region`:`account-id`:rule/`rule-name`\"}}}]}"
}
```

5. Set the policy attribute by using the
   `set-queue-attributes.json` file you just created as the
   input, as shown in the following command.

```
aws sqs set-queue-attributes \
--queue-url https://sqs.`region`.amazonaws.com/`account-id`/`queue-name` \
--attributes file://set-queue-attributes.json
```

For more information, see [Amazon SQS Policy
Examples](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSExamples.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSExamples.md") in the _Amazon Simple Queue Service Developer Guide_.

## EventBridge Pipes specifics

EventBridge Pipes does not support resource-based policies and has no APIs which support resource based policy conditions.

However, if you configure pipe access through an interface VPC endpoint, that VPC
endpoint supports resource policies that enable you to manage access to EventBridge Pipe APIs. For more information, see [Using Amazon EventBridge with Interface VPC endpoints](eb-related-service-vpc.md "eb-related-service-vpc.md")
