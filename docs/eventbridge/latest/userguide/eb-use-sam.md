# Using AWS Serverless Application Model templates to deploy Amazon EventBridge resources

You can build and test [rules](eb-rules.md "eb-rules.md") manually in the EventBridge console,
which can help in the development process as you refine [event
patterns](eb-event-patterns.md "eb-event-patterns.md"). However, once you are ready to deploy your application, it’s easier to use a
framework like [AWS SAM](../../../serverless-application-model/latest/developerguide/what-is-sam.md "../../../serverless-application-model/latest/developerguide/what-is-sam.md") to launch all your
serverless resources consistently.

We'll use this [example
application](https://github.com/aws-samples/amazon-eventbridge-producer-consumer-example "https://github.com/aws-samples/amazon-eventbridge-producer-consumer-example") to look into the ways you can use AWS SAM templates to build EventBridge resources.
The template.yaml file in this example is a AWS SAM template that defines four [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") functions and shows two different ways to
integrate the Lambda functions with EventBridge.

For a walkthrough of this example application, see [Tutorial: Create a sample Amazon EventBridge application](eb-tutorial-get-started.md "eb-tutorial-get-started.md").

There are two approaches to using EventBridge and AWS SAM templates. For simple integrations where
one Lambda function is invoked by one rule, the the **Combined template**
approach is recommended. If you have complex routing logic, or you are connecting to resources
outside of your AWS SAM template, the **Separated template** approach is the
better choice.

###### Approaches:

- [Combined template](#eb-combined-template "#eb-combined-template")
- [Separated template](#eb-separated-template "#eb-separated-template")

## Combined template

The first approach uses the `Events` property to configure the EventBridge rule. The following example code defines an [event](eb-events.md "eb-events.md") that
invokes your Lambda function.

###### Note

This example automatically creates the rule on the default [event bus](eb-event-bus.md "eb-event-bus.md"), which exists in every AWS account. To associate the rule with a
custom event bus, you can add the `EventBusName` to the template.

```
atmConsumerCase3Fn:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: atmConsumer/
    Handler: handler.case3Handler
    Runtime: nodejs12.x
    Events:
      Trigger:
        Type: CloudWatchEvent
        Properties:
          Pattern:
            source:
              - custom.myATMapp
            detail-type:
              - transaction
            detail:
              result:
                - "anything-but": "approved"
```

This YAML code is equivalent to an event pattern in the EventBridge console. In YAML, you only
need to define the event pattern, and AWS SAM automatically creates an IAM role with the
required permissions.

## Separated template

In the second approach to defining an EventBridge configuration in AWS SAM, the resources are
separated more clearly in the template.

1. First, you define the Lambda function:

```
atmConsumerCase1Fn:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: atmConsumer/
    Handler: handler.case1Handler
    Runtime: nodejs12.x
```

2. Next, define the rule using an `AWS::Events::Rule` resource. The properties
   define the event pattern and can also specify [targets](eb-targets.md "eb-targets.md"). You can explicitly define multiple targets.

```
EventRuleCase1:
  Type: AWS::Events::Rule
  Properties:
    Description: "Approved transactions"
    EventPattern:
      source:
        - "custom.myATMapp"
      detail-type:
        - transaction
      detail:
        result:
          - "approved"
    State: "ENABLED"
    Targets:
      -
        Arn:
          Fn::GetAtt:
            - "atmConsumerCase1Fn"
            - "Arn"
        Id: "atmConsumerTarget1"
```

3. Finally, define an `AWS::Lambda::Permission` resource that grants
   permission to EventBridge to invoke the target.

```
PermissionForEventsToInvokeLambda:
  Type: AWS::Lambda::Permission
  Properties:
    FunctionName:
      Ref: "atmConsumerCase1Fn"
    Action: "lambda:InvokeFunction"
    Principal: "events.amazonaws.com"
    SourceArn:
      Fn::GetAtt:
        - "EventRuleCase1"
        - "Arn"
```
