# Creating an AWS IoT rule

You can create AWS IoT rules to route data from your connected things to interact with
other AWS services. An AWS IoT rule consists of the following components:

| Components of a rule | Component                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description | Required or Optional |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------------------- |
| Rule name            | The name of the rule. Note that we do not recommend the use of<br>personally identifiable information in your rule names.                                                                                                                                                                                                                                                                                                                                                | Required.   |
| Rule description     | A textual description of the rule. Note that we do not recommend<br>the use of personally identifiable information in your rule<br>descriptions.                                                                                                                                                                                                                                                                                                                         | Optional.   |
| SQL statement        | A simplified SQL syntax to filter messages received on an MQTT<br>topic and push the data elsewhere. For more information, see [AWS IoT SQL reference](iot-sql-reference.md "iot-sql-reference.md").                                                                                                                                                                                                                                                                     | Required.   |
| SQL version          | The version of the SQL rules engine to use when evaluating the<br>rule. Although this property is optional, we strongly recommend that<br>you specify the SQL version. The AWS IoT Core console sets this<br>property to `2016-03-23` by default. If this property is<br>not set, such as in an AWS CLI command or an AWS CloudFormation template,<br>`2015-10-08` is used. For more information, see [SQL versions](iot-rule-sql-version.md "iot-rule-sql-version.md"). | Required.   |
| One or more actions  | The actions AWS IoT performs when enacting the rule. For example, you<br>can insert data into a DynamoDB table, write data to an Amazon S3 bucket,<br>publish to an Amazon SNS topic, or invoke a Lambda function.                                                                                                                                                                                                                                                       | Required.   |
| An error action      | The action AWS IoT performs when it's unable to perform a rule's<br>action.                                                                                                                                                                                                                                                                                                                                                                                              | Optional.   |

Before you create an AWS IoT rule, you must create an IAM role with a policy that
allows access to the required AWS resources. AWS IoT assumes this role when implementing
a rule. For more information, see [Granting an AWS IoT rule the
access it requires](iot-create-role.md "iot-create-role.md") and [Passing role
permissions](pass-role.md "pass-role.md").

When you create a rule, be aware of how much data you're publishing on topics. If you
create rules that include a wildcard topic pattern, they might match a large percentage
of your messages. If this is the case, you might need to increase the capacity of the
AWS resources used by the target actions. We recommend avoiding wildcard topic patterns in republish
rules to prevent duplicate processing and reduce costs.

###### Note

Creating and updating rules are administrator-level actions. Any user who has
permission to create or update rules is able to access data processed by the
rules.

## Create a rule (Console)

###### To create a rule (AWS Management Console)

Use the [AWS Management Console](https://console.aws.amazon.com/iot/home#/home "https://console.aws.amazon.com/iot/home#/home") command
to create a rule:

1. Open the [AWS IoT
   console](https://console.aws.amazon.com/iot/home#/home "https://console.aws.amazon.com/iot/home#/home").
2. On the left navigation, choose **Message routing** from
   **Manage** section. Then choose
   **Rules**.
3. On the **Rules** page, choose **Create
   rule**.
4. On the **Specify rule properties** page, enter a name for
   your rule. **Rule description** and
   **Tags** are optional. Choose
   **Next**.
5. On the **Configure SQL statement** page, choose a SQL
   version and enter a SQL statement. An example SQL statement can be
   `SELECT temperature FROM 'iot/topic' WHERE temperature > 50`.
   For more information, see [SQL
   versions](iot-rule-sql-version.md "iot-rule-sql-version.md") and [AWS IoT SQL
   reference](iot-sql-reference.md "iot-sql-reference.md").
6. On the **Attach rule actions** page, add rule actions to
   route data to other AWS services.
   1. In **Rule actions**, select a rule action from
      the drop down list. For example, you can choose **Kinesis
      Stream**. For more information about rule actions, see
      [AWS IoT
      rule actions](iot-rule-actions.md "iot-rule-actions.md").
   2. Depending on the rule action you choose, enter related
      configuration details. For example, if you choose **Kinesis
      Stream**, you will need to choose or create a data
      stream resource, and optionally enter configuration details such as
      **Partition key**, which is used to group data
      by shard in a steam.
   3. In **IAM role**, choose or create a role to
      grant AWS IoT access to your endpoint. Note that AWS IoT will
      automatically create a policy with a prefix of
      `aws-iot-rule` under your IAM role selected. You
      can choose **View** to view your IAM role and the
      policy from the IAM console. **Error action** is
      optional. You can find more information in [Error
      handling (error action)](rule-error-handling.md "rule-error-handling.md"). For more information about
      creating an IAM role for your rule, see [Grant a
      rule the access it requires](iot-create-role.md "iot-create-role.md"). Choose
      **Next**.

7. On the **Review and create** page, review all the
   configuration and make edits if needed. Choose
   **Create**.

After you create a rule successfully, you will see the rule listed on the
**Rules** page. You can select a rule to open the
**Details** page where you can view a rule, edit a rule,
deactivate a rule, and delete a rule.

## Create a rule (CLI)

###### To create a rule (AWS CLI)

Use the [create-topic-rule](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md") command to create a rule:

```
`aws iot create-topic-rule --rule-name `myrule` --topic-rule-payload file://`myrule`.json`
```

The following is an example payload file with a rule that inserts all messages
sent to the `iot/test` topic into the specified DynamoDB table. The SQL
statement filters the messages and the role ARN grants AWS IoT permission to write to
the DynamoDB table.

```
{
	"sql": "SELECT * FROM 'iot/test'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"dynamoDB": {
				"tableName": "my-dynamodb-table",
				"roleArn": "arn:aws:iam::123456789012:role/my-iot-role",
				"hashKeyField": "topic",
				"hashKeyValue": "${topic(2)}",
				"rangeKeyField": "timestamp",
				"rangeKeyValue": "${timestamp()}"
			}
		}
	]
}
```

The following is an example payload file with a rule that inserts all messages
sent to the `iot/test` topic into the specified S3 bucket. The SQL
statement filters the messages, and the role ARN grants AWS IoT permission to write to
the Amazon S3 bucket.

```
{
	"awsIotSqlVersion": "2016-03-23",
	"sql": "SELECT * FROM 'iot/test'",
	"ruleDisabled": false,
	"actions": [
		{
			"s3": {
				"roleArn": "arn:aws:iam::123456789012:role/aws_iot_s3",
				"bucketName": "amzn-s3-demo-bucket",
				"key": "myS3Key"
			}
		}
	]
}
```

The following is an example payload file with a rule that pushes data to
Amazon OpenSearch Service:

```
{
	"sql": "SELECT *, timestamp() as timestamp FROM 'iot/test'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"OpenSearch": {
				"roleArn": "arn:aws:iam::123456789012:role/aws_iot_es",
				"endpoint": "https://my-endpoint",
				"index": "my-index",
				"type": "my-type",
				"id": "${newuuid()}"
			}
		}
	]
}
```

The following is an example payload file with a rule that invokes a Lambda
function:

```
{
	"sql": "expression",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"lambda": {
				"functionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-lambda-function"
			}
		}
	]
}
```

The following is an example payload file with a rule that publishes to an Amazon SNS
topic:

```
{
	"sql": "expression",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"sns": {
				"targetArn": "arn:aws:sns:us-west-2:123456789012:my-sns-topic",
				"roleArn": "arn:aws:iam::123456789012:role/my-iot-role"
			}
		}
	]
}
```

The following is an example payload file with a rule that republishes on a
different MQTT topic:

```
{
	"sql": "expression",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"republish": {
				"topic": "my-mqtt-topic",
				"roleArn": "arn:aws:iam::123456789012:role/my-iot-role"
			}
		}
	]
}
```

The following is an example payload file with a rule that pushes data to an
Amazon Data Firehose stream:

```
{
	"sql": "SELECT * FROM 'my-topic'",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"firehose": {
				"roleArn": "arn:aws:iam::123456789012:role/my-iot-role",
				"deliveryStreamName": "my-stream-name"
			}
		}
	]
}
```

The following is an example payload file with a rule that uses the Amazon SageMaker AI
`machinelearning_predict` function to republish to a topic if the
data in the MQTT payload is classified as a 1.

```
{
	"sql": "SELECT * FROM 'iot/test' where machinelearning_predict('my-model', 'arn:aws:iam::123456789012:role/my-iot-aml-role', *).predictedLabel=1",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"republish": {
				"roleArn": "arn:aws:iam::123456789012:role/my-iot-role",
				"topic": "my-mqtt-topic"
			}
		}
	]
}
```

The following is an example payload file with a rule that publishes messages to a
Salesforce IoT Cloud input stream.

```
{
	"sql": "expression",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"salesforce": {
				"token": "ABCDEFGHI123456789abcdefghi123456789",
				"url": "https://ingestion-cluster-id.my-env.sfdcnow.com/streams/stream-id/connection-id/my-event"
			}
		}
	]
}
```

The following is an example payload file with a rule that starts an execution of a
Step Functions state machine.

```
{
	"sql": "expression",
	"ruleDisabled": false,
	"awsIotSqlVersion": "2016-03-23",
	"actions": [
		{
			"stepFunctions": {
				"stateMachineName": "myCoolStateMachine",
				"executionNamePrefix": "coolRunning",
				"roleArn": "arn:aws:iam::123456789012:role/my-iot-role"
			}
		}
	]
}
```
