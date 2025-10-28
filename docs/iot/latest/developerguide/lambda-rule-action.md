# Lambda

A Lambda (`lambda`) action invokes an AWS Lambda function, passing in an
MQTT message. AWS IoT invokes Lambda functions asynchronously.

You can follow a tutorial that shows you how to create and test a rule with a
Lambda action. For more information, see [Tutorial: Formatting a notification by using an AWS Lambda
function](iot-lambda-rule.md "iot-lambda-rule.md").

## Requirements

This rule action has the following requirements:

- For AWS IoT to invoke a Lambda function, you must configure a policy that
  grants the `lambda:InvokeFunction` permission to AWS IoT. You
  can only invoke a Lambda function defined in the same AWS Region where
  your Lambda policy exists. Lambda functions use resource-based policies,
  so you must attach the policy to the Lambda function itself.

Use the following AWS CLI command to attach a policy that grants the
`lambda:InvokeFunction` permission. In this command, replace:

    + `function_name` with the name of the Lambda function.
     You add a new permission to update the function's resource policy.
    + `region` with the AWS Region of the function.
    + `account-id` with the AWS account number where the rule
     is defined.
    + `rule-name` with the name of the AWS IoT rule for which you
     are defining the Lambda action.
    + `unique_id` with a unique statement identifier.

###### Important

If you add a permission for an AWS IoT principal without providing
the `source-arn` or `source-account`, any
AWS account that creates a rule with your Lambda action can
activate rules to invoke your Lambda function from AWS IoT.

For more information, see [AWS Lambda permissions](../../../lambda/latest/dg/intro-permission-model.md "../../../lambda/latest/dg/intro-permission-model.md").

```
aws lambda add-permission \
    --function-name `function_name` \
    --region `region` \
    --principal iot.amazonaws.com \
    --source-arn arn:aws:iot:`region`:`account-id`:rule/`rule_name` \
    --source-account `account-id`
    --statement-id `unique_id`
    --action "lambda:InvokeFunction"
```

- If you use the AWS IoT console to create a rule for the Lambda rule action,
  the Lambda function is triggered automatically. If you use AWS CloudFormation instead
  with the [`AWS::IoT::TopicRule LambdaAction`](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.md"),
  you must add an [`AWS::lambda::Permission`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md")
  resource. The resource then grants you permission to trigger the Lambda function.

The following code shows an example of how to add this resource. In this
example, replace:

    + `function_name` with the name of the Lambda function.
    + `region` with the AWS Region of the function.
    + `account-id` with the AWS account number where the rule
     is defined.
    + `rule-name` with the name of the AWS IoT rule for which you
     are defining the Lambda action.

```
Type: AWS::Lambda::Permission
Properties:
  Action: lambda:InvokeFunction
  FunctionName: !Ref `function_name`
  Principal: "iot.amazonaws.com"
  SourceAccount: `account-id`
  SourceArn: arn:aws:iot:`region`:`account-id`:rule/`rule_name`
```

- If you use an AWS KMS customer managed AWS KMS key to encrypt data at
  rest in Lambda, the service must have permission to use the
  AWS KMS key on the caller's behalf. For more information, see [Encryption at rest](../../../lambda/latest/dg/security-dataprotection.md#security-privacy-atrest "../../../lambda/latest/dg/security-dataprotection.md#security-privacy-atrest") in the _AWS Lambda Developer
  Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`functionArn`

The ARN of the Lambda function to invoke. AWS IoT must have
permission to invoke the function. For more information, see [Requirements](#lambda-rule-action-requirements "#lambda-rule-action-requirements").

If you don't specify a version or alias for your Lambda function,
the most recent version of the function is shut down. You can
specify a version or alias if you want to shut down a specific
version of your Lambda function. To specify a version or alias,
append the version or alias to the ARN of the Lambda function.

```
arn:aws:lambda:us-east-2:123456789012:function:myLambdaFunction:someAlias
```

For more information about versioning and aliases, and see [AWS Lambda function versioning and aliases](../../../lambda/latest/dg/versioning-aliases.md "../../../lambda/latest/dg/versioning-aliases.md").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

## Examples

The following JSON example defines a Lambda action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "lambda": {
                    "functionArn": "arn:aws:lambda:us-east-2:123456789012:function:myLambdaFunction"
                 }
            }
        ]
    }
}

```

The following JSON example defines a Lambda action with substitution templates
in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "lambda": {
                    "functionArn": "arn:aws:lambda:us-east-1:123456789012:function:${topic()}"
                }
            }
        ]
    }
}
```

## See also

- [What is AWS Lambda?](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md") in the
  _AWS Lambda Developer Guide_
- [Tutorial: Formatting a notification by using an AWS Lambda
  function](iot-lambda-rule.md "iot-lambda-rule.md")
