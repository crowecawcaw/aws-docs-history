

# Creating Custom Event Bus resources with CloudFormation
<a name="eb-custom-bus-cloudformation"></a>

You can create a bus, its subscribers, its event sources, and its resource policy from a CloudFormation template. The resource types are in the `AWS::EventsV2` namespace. The `AWS::Events` types belong to Custom Event Bus - Classic and cannot configure a Custom Event Bus.

## The resource types
<a name="eb-custom-bus-cloudformation-types"></a>
+ `AWS::EventsV2::EventBus` is one bus, including its retention period and its encryption key. It requires `Name`.
+ `AWS::EventsV2::Subscriber` is one subscriber on a bus: its filters, its transform, its retry policy, and its single target. It requires `Name`, `EventBusArn`, and `InvokeConfiguration`, which itself requires `TargetArn` and `RoleArn`.
+ `AWS::EventsV2::EventSource` is one managed feed of AWS service events or partner events into a bus. It requires `Name`, `EventBusArn`, and `Configuration`. See [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md).
+ `AWS::EventsV2::ResourcePolicy` is the resource policy of a bus that already exists. It requires `EventBusArn` and `PolicyDocument`. See [Access control for the Custom Event Bus](eb-custom-bus-access.md).

A subscriber's `RoleArn` must name a role in the same account as the subscriber. So a bus shared across accounts is more than one stack: the bus in the owner's account, and the target, the delivery role, and the subscriber in each consuming account.

## Example: a bus, a queue, and a subscriber
<a name="eb-custom-bus-cloudformation-example"></a>

The following template creates a bus that retains events for seven days, an Amazon SQS queue, a dead-letter queue, a delivery role, and a subscriber that delivers orders over 500 to the queue. CloudFormation creates the role and the queues before the subscriber, because the subscriber refers to them with `Fn::GetAtt`. The retention period decides how far back a subscriber can start reading; see [Replaying retained events to a subscriber](eb-custom-bus-replay.md).

```
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  OrdersBus:
    Type: AWS::EventsV2::EventBus
    Properties:
      Name: orders
      Description: Order events for the fulfillment platform
      StorageConfiguration:
        RetentionPeriodInDays: 7

  OrdersQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: large-orders

  OrdersDeadLetterQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: large-orders-dlq

  DeliveryRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: EventBusDeliveryRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: DeliverToQueues
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action: sqs:SendMessage
                Resource:
                  - !GetAtt OrdersQueue.Arn
                  - !GetAtt OrdersDeadLetterQueue.Arn

  LargeOrders:
    Type: AWS::EventsV2::Subscriber
    Properties:
      Name: large-orders
      EventBusArn: !Ref OrdersBus
      FilterConfiguration:
        Filters:
          - Scope: DATA
            Pattern: '{"detail":{"total":[{"numeric":[">",500]}]}}'
      InvokeConfiguration:
        TargetArn: !GetAtt OrdersQueue.Arn
        RoleArn: !GetAtt DeliveryRole.Arn
      RetryPolicy:
        MaxRetryAttempts: 10
        MaxEventAgeInSeconds: 3600
      OnFailureConfiguration:
        Arn: !GetAtt OrdersDeadLetterQueue.Arn

Outputs:
  OrdersBusArn:
    Value: !Ref OrdersBus
    Export:
      Name: orders-bus-arn
```

The delivery role trusts the `events.amazonaws.com` service principal and grants `sqs:SendMessage` on both queues. Without the grant on the dead-letter queue, a failed delivery cannot be recorded and nothing is observable. The identity that deploys the stack also needs `iam:PassRole` on the delivery role.

## Return values
<a name="eb-custom-bus-cloudformation-returns"></a>

`Ref` returns the resource's primary identifier, an ARN. `Fn::GetAtt` returns the read-only properties. The following table lists the values for each resource type.


| Resource type | `Ref` returns | `Fn::GetAtt` attributes | 
| --- | --- | --- | 
| AWS::EventsV2::EventBus | EventBusArn | EventBusArn, State, CreationTime, LastModifiedTime | 
| AWS::EventsV2::Subscriber | SubscriberArn | SubscriberArn, BusName, CreationTime, LastModifiedTime | 
| AWS::EventsV2::EventSource | EventSourceArn | EventSourceArn, State, Revoked, CreationTime, LastModifiedTime | 
| AWS::EventsV2::ResourcePolicy | EventBusArn | RevisionId | 

A subscriber's `State` is a property you set, not an attribute you read. Set it to `STOPPED` to pause delivery and back to `RUNNING` to resume. A bus's `State` is read-only, and its settled value is `ACTIVE`.

## Properties that replace the resource
<a name="eb-custom-bus-cloudformation-replacement"></a>

Six subscriber properties are create-only, so changing any of them in a template replaces the subscriber: `Name`, `EventBusArn`, `InvokeConfiguration.TargetArn`, `Type`, `StartingPosition`, and `PointInTimeConfiguration`. Every other subscriber property, including the filters, the transform, the retry policy, and the dead-letter queue, updates in place.

**Important**  
A subscriber replacement deletes the old subscriber before it creates the new one. No subscriber exists between the two steps. The new subscriber then starts from its own `StartingPosition`, and `LATEST` starts from the newest events, so it never delivers the events published during that window. Changing a target ARN, an ordering type, or a starting position therefore drops events unless you plan for the gap.

To avoid the gap, deploy twice. First add the replacement subscriber under a new logical id and wait for its `State` to reach `RUNNING`. Then remove the old subscriber in a second deployment. Both subscribers deliver during the overlap, so the target receives each matching event twice; use this approach only when duplicates are acceptable.

If you cannot deploy twice, set the new subscriber's `StartingPosition` to `POINT_IN_TIME` and give `PointInTimeConfiguration` a `PointType` of `TIMESTAMP` with a `StartingPoint`, in seconds since the Unix epoch, from before the deployment. The subscriber then reads the events it missed, provided they are still within the bus's retention period.

On a bus, only `Name` is create-only, so the retention period, the description, the encryption key, and the tags all update in place. On an event source, `Name` and `EventBusArn` are create-only, and on a resource policy, `EventBusArn` is.

## Referring to a bus from another stack
<a name="eb-custom-bus-cloudformation-crossstack"></a>

A subscriber needs the full bus ARN, which includes the service-generated identifier after the bus name. Store and pass the ARN, not the name. See [Names, endpoints, and IAM permissions for the Custom Event Bus](eb-custom-bus-names.md).

Within one account and Region, export the ARN from the stack that owns the bus, as the example does, and import it with `EventBusArn: !ImportValue orders-bus-arn`. CloudFormation does not let you change or remove an exported value while another stack imports it. Renaming the bus replaces it and changes its ARN, so a rename fails while an import exists. Remove the importing subscriber first, or export under a new name.

An export cannot be imported from another account or another Region. Pass the bus ARN into the consuming stack as a template parameter instead. The bus owner must also grant the other account permission on the bus, which you do with a resource policy or with AWS Resource Access Manager (AWS RAM). See [Access control for the Custom Event Bus](eb-custom-bus-access.md).