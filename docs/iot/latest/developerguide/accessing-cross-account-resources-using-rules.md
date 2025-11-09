# Accessing cross-account

resources using AWS IoT rules

You can configure AWS IoT rules for cross-account access so that data ingested on MQTT
topics of one account can be routed into the AWS services, such as Amazon SQS and Lambda, of
another account. The following explains how to set up AWS IoT rules for cross-account data
ingestion, from an MQTT topic in one account, to a destination in another account.

Cross-account rules can be configured using [resource-based permissions](../../../IAM/latest/UserGuide/access_controlling.md#TypesPermissions "../../../IAM/latest/UserGuide/access_controlling.md#TypesPermissions") on the destination resource. Therefore, only
destinations that support resource-based permissions can be enabled for the
cross-account access with AWS IoT rules. The supported destinations include Amazon SQS, Amazon SNS,
Amazon S3, and AWS Lambda.

###### Note

For the supported destinations, except for Amazon SQS, you must define the rule in the
same AWS Region as another service's resource so that the rule action can interact
with that resource. For more information about AWS IoT rule actions, see [AWS IoT rule actions](iot-rule-actions.md "iot-rule-actions.md"). For more information about
rule's SQS action, see [SQS](sqs-rule-action.md "sqs-rule-action.md").

## Prerequisites

- Familiarity with [AWS IoT rules](iot-rules.md "iot-rules.md")
- An understanding of [IAM users](../../../IAM/latest/UserGuide/introduction_identity-management.md "../../../IAM/latest/UserGuide/introduction_identity-management.md"), [roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md"), and [resource-based permission](../../../IAM/latest/UserGuide/access_permissions.md#TypesPermissions "../../../IAM/latest/UserGuide/access_permissions.md#TypesPermissions")
- Having [AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") installed

## Cross-account setup for Amazon SQS

Scenario: Account A sends data from an MQTT message to account B's Amazon SQS
queue.

| AWS account      | Account referred to as | Description                                                                                                                                                |
| ---------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1111-1111-1111` | Account A              | Rule action: `sqs:SendMessage`                                                                                                                             |
| `2222-2222-2222` | Account B              | Amazon SQS queue<br>• ARN:<br>`arn:aws:sqs:region:2222-2222-2222:ExampleQueue`<br>• URL:<br>`https://sqs.region.amazonaws.com/2222-2222-2222/ExampleQueue` |

###### Note

Your destination Amazon SQS queue doesn't have to be in the same AWS Region as
your [AWS IoT rule](iot-rules.md "iot-rules.md"). For more information about rule's SQS action, see [SQS](sqs-rule-action.md "sqs-rule-action.md").

###### Do the Account A tasks

###### Note

To run the following commands, your IAM user should have permissions to
`iot:CreateTopicRule` with the rule's Amazon Resource Name
(ARN) as a resource, and permissions to `iam:PassRole` action
with a resource as the role's ARN.

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account A’s IAM user.
2. Create an IAM role that trusts AWS IoT rules engine, and attaches a policy
   that allows access to account B's Amazon SQS queue. See example commands and
   policy documents in [Granting AWS IoT the required access](iot-create-role.md "iot-create-role.md").
3. To create a rule that is attached to a topic, run the [create-topic-rule command](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md").

```
`aws iot create-topic-rule --rule-name `myRule` --topic-rule-payload file://./`my-rule.json``
```

The following is an example payload file with a rule that inserts all
messages sent to the `iot/test` topic into the specified Amazon SQS
queue. The SQL statement filters the messages and the role ARN grants AWS IoT
permissions to add the message to the Amazon SQS queue.

```
{
	"sql": "SELECT * FROM 'iot/test'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"sqs": {
				"queueUrl": "https://sqs.region.amazonaws.com/2222-2222-2222/ExampleQueue",
				"roleArn": "arn:aws:iam::1111-1111-1111:role/my-iot-role",
				"useBase64": false
			}
		}
	]
}
```

For more information about how to define an Amazon SQS action in an AWS IoT rule,
see [AWS IoT rule actions - Amazon SQS](sqs-rule-action.md "sqs-rule-action.md").

###### Do the Account B tasks

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account B’s IAM user.
2. To give permissions for the Amazon SQS queue resource to account A, run the
   [add-permission command](../../../cli/latest/reference/sqs/add-permission.md "../../../cli/latest/reference/sqs/add-permission.md").

```
aws sqs add-permission --queue-url `https://sqs.region.amazonaws.com/2222-2222-2222/ExampleQueue` --label `SendMessagesToMyQueue` --aws-account-ids `1111-1111-1111` --actions SendMessage
```

## Cross-account setup for Amazon SNS

Scenario: Account A sends data from an MQTT message to an Amazon SNS topic of account
B.

| AWS account      | Account referred to as | Description                                                               |
| ---------------- | ---------------------- | ------------------------------------------------------------------------- |
| `1111-1111-1111` | Account A              | Rule action: `sns:Publish`                                                |
| `2222-2222-2222` | Account B              | Amazon SNS topic ARN:<br>`arn:aws:sns:region:2222-2222-2222:ExampleTopic` |

###### Do the Account A tasks

###### Notes

To run the following commands, your IAM user should have permissions to
`iot:CreateTopicRule` with rule ARN as a resource and
permissions to the `iam:PassRole` action with a resource as role
ARN.

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account A’s IAM user.
2. Create an IAM role that trusts AWS IoT rules engine, and attaches a policy
   that allows access to account B's Amazon SNS topic. For example commands and
   policy documents, see [Granting AWS IoT the required access](iot-create-role.md "iot-create-role.md").
3. To create a rule that is attached to a topic, run the [create-topic-rule command](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md").

```
`aws iot create-topic-rule --rule-name `myRule` --topic-rule-payload file://./`my-rule.json``
```

The following is an example payload file with a rule that inserts all
messages sent to the `iot/test` topic into the specified Amazon SNS
topic. The SQL statement filters the messages, and the role ARN grants AWS IoT
permissions to send the message to the Amazon SNS topic.

```
{
	"sql": "SELECT * FROM 'iot/test'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"sns": {
				"targetArn": "arn:aws:sns:region:2222-2222-2222:ExampleTopic",
				"roleArn": "arn:aws:iam::1111-1111-1111:role/my-iot-role"
			}
		}
	]
}
```

For more information about how to define an Amazon SNS action in an AWS IoT rule,
see [AWS IoT rule actions - Amazon SNS](sns-rule-action.md "sns-rule-action.md").

###### Do the Account B tasks

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account B’s IAM user.
2. To give permission on the Amazon SNS topic resource to account A, run the
   [add-permission command](../../../cli/latest/reference/sns/add-permission.md "../../../cli/latest/reference/sns/add-permission.md").

```
aws sns add-permission --topic-arn `arn:aws:sns:region:2222-2222-2222:ExampleTopic` --label `Publish-Permission` --aws-account-id `1111-1111-1111` --action-name Publish
```

## Cross-account setup for Amazon S3

Scenario: Account A sends data from an MQTT message to an Amazon S3 bucket of account
B.

| AWS account      | Account referred to as | Description                                                 |
| ---------------- | ---------------------- | ----------------------------------------------------------- |
| `1111-1111-1111` | Account A              | Rule action: `s3:PutObject`                                 |
| `2222-2222-2222` | Account B              | Amazon S3 bucket ARN:<br>`arn:aws:s3:::amzn-s3-demo-bucket` |

###### Do the Account A tasks

###### Note

To run the following commands, your IAM user should have permissions to
`iot:CreateTopicRule` with the rule ARN as a resource and
permissions to `iam:PassRole` action with a resource as role
ARN.

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account A’s IAM user.
2. Create an IAM role that trusts AWS IoT rules engine and attaches a policy
   that allows access to account B's Amazon S3 bucket. For example commands and
   policy documents, see [Granting AWS IoT the required access](iot-create-role.md "iot-create-role.md").
3. To create a rule that is attached to your target S3 bucket, run the [create-topic-rule command](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md").

```
`aws iot create-topic-rule --rule-name `my-rule` --topic-rule-payload file://./`my-rule.json``
```

The following is an example payload file with a rule that inserts all
messages sent to the `iot/test` topic into the specified Amazon S3
bucket. The SQL statement filters the messages, and the role ARN grants
AWS IoT permissions to add the message to the Amazon S3 bucket.

```
{
	"sql": "SELECT * FROM 'iot/test'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"s3": {
				"bucketName": "amzn-s3-demo-bucket",
				"key": "${topic()}/${timestamp()}",
				"roleArn": "arn:aws:iam::1111-1111-1111:role/my-iot-role"
			}
		}
	]
}
```

For more information about how to define an Amazon S3 action in an AWS IoT rule,
see [AWS IoT rule actions - Amazon S3](s3-rule-action.md "s3-rule-action.md").

###### Do the Account B tasks

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account B’s IAM user.
2. Create a bucket policy that trusts account A's principal.

The following is an example payload file that defines a bucket policy that
trusts the principal of another account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AddCannedAcl",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root"
 ]
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```

For more information, see [bucket policy examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-use-case-1 "../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-use-case-1"). 3. To attach the bucket policy to the specified bucket, run the [put-bucket-policy command](../../../cli/latest/reference/s3api/put-bucket-policy.md "../../../cli/latest/reference/s3api/put-bucket-policy.md").

```
`aws s3api put-bucket-policy --bucket amzn-s3-demo-bucket --policy file://./`amzn-s3-demo-bucket-policy.json``
```

4. To make the cross-account access work, make sure you have the correct
   **Block all public access** settings. For
   more information, see [Security Best Practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").

## Cross-account setup for AWS Lambda

Scenario: Account A invokes an AWS Lambda function of account B, passing in an MQTT
message.

| AWS account      | Account referred to as | Description                                                                           |
| ---------------- | ---------------------- | ------------------------------------------------------------------------------------- |
| `1111-1111-1111` | Account A              | Rule action: `lambda:InvokeFunction`                                                  |
| `2222-2222-2222` | Account B              | Lambda function ARN: `arn:aws:lambda:region:2222-2222-2222:function:example-function` |

###### Do the Account A tasks

###### Notes

To run the following commands, your IAM user should have permissions to
`iot:CreateTopicRule` with rule ARN as a resource, and
permissions to `iam:PassRole` action with resource as role
ARN.

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account A’s IAM user.
2. Run the [create-topic-rule command](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md") to create a rule that defines
   cross-account access to account B's Lambda function.

```
`aws iot create-topic-rule --rule-name `my-rule` --topic-rule-payload file://./`my-rule.json``
```

The following is an example payload file with a rule that inserts all
messages sent to the `iot/test` topic into the specified Lambda
function. The SQL statement filters the messages and the role ARN grants
AWS IoT permission to pass in the data to the Lambda function.

```
{
	"sql": "SELECT * FROM 'iot/test'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"lambda": {
				"functionArn": "arn:aws:lambda:region:2222-2222-2222:function:example-function"
			}
		}
	]
}
```

For more information about how to define an AWS Lambda action in an AWS IoT
rule, read [AWS IoT rule actions - Lambda](lambda-rule-action.md "lambda-rule-action.md").

###### Do the Account B tasks

1. [Configure AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") using account B’s IAM user.
2. Run [Lambda's add-permission command](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md") to give AWS IoT rules permission
   to activate the Lambda function. To run the following command, your
   IAM user should have permission to `lambda:AddPermission`
   action.

```
aws lambda add-permission --function-name `example-function` --region `us-east-1` --principal iot.amazonaws.com --source-arn `arn:aws:iot:region:1111-1111-1111:rule/example-rule` --source-account `1111-1111-1111` --statement-id `"unique_id"` --action "lambda:InvokeFunction"
```

**Options:**

**--principal**

This field gives permission to AWS IoT (represented by
`iot.amazonaws.com`) to call the Lambda function.

**--source-arn**

This field confirms that only
`arn:aws:iot:region:1111-1111-1111:rule/example-rule` in
AWS IoT triggers this Lambda function and no other rule in the same or
different account can activate this Lambda function.

**--source-account**

This field confirms that AWS IoT activates this Lambda function only on
behalf of the `1111-1111-1111` account.

###### Notes

If you see an error message "The rule could not be found" from your
AWS Lambda function’s console under **Configuration**, ignore the error message and proceed to
test the connection.
