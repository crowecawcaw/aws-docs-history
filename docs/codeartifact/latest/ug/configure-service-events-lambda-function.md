# Use an event to run a Lambda

function

This example shows you how to configure an EventBridge rule that starts an AWS Lambda
function when a package version in a CodeArtifact repository is published, modified, or
deleted.

For more information, see [Tutorial: Schedule
AWS Lambda Functions Using EventBridge](../../../eventbridge/latest/userguide/run-lambda-schedule.md "../../../eventbridge/latest/userguide/run-lambda-schedule.md") in the _Amazon EventBridge User
Guide_.

###### Topics

- [Create the EventBridge rule](#configure-service-events-lambda-create-rule "#configure-service-events-lambda-create-rule")
- [Create the EventBridge rule
  target](#configure-service-events-lambda-create-rule-target "#configure-service-events-lambda-create-rule-target")
- [Configure EventBridge
  permissions](#configure-service-events-lambda-permissions "#configure-service-events-lambda-permissions")

## Create the EventBridge rule

To create a rule that starts a Lambda function, use the `put-rule`
command with the `--name` and `--event-pattern` options. The
following pattern specifies npm packages in the `@types` scope in any
repository in the `my_domain` domain.

```
aws events put-rule --name "`MyCodeArtifactRepoRule`" --event-pattern \
  '{"source":["aws.codeartifact"],"detail-type":["CodeArtifact Package Version State Change"],
  "detail":{"domainName":["`my_domain`"],"domainOwner":["`111122223333`"],"packageNamespace":["types"],"packageFormat":["`npm`"]}}'
```

## Create the EventBridge rule

target

The following command adds a target to the rule that runs the Lambda function when
an event matches the rule. For the `arn` parameter, specify the Amazon
Resource Name (ARN) of the Lambda function.

```
aws events put-targets --rule `MyCodeArtifactRepoRule` --targets \
  Id=1,Arn=arn:aws:lambda:`us-west-2`:`111122223333`:function:`MyLambdaFunction`
```

## Configure EventBridge

permissions

Use the `add-permission` command to grant permissions for the rule to
invoke a Lambda function. For the `--source-arn` parameter, specify the
ARN of the rule that you created earlier in this example.

```
aws lambda add-permission --function-name `MyLambdaFunction` \\
  --statement-id `my-statement-id` --action 'lambda:InvokeFunction' \\
  --principal events.amazonaws.com \\
  --source-arn arn:aws:events:`us-west-2`:`111122223333`:rule/`MyCodeArtifactRepoRule`
```
