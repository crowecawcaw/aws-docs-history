# AWS AppSync targets for rules in Amazon EventBridge

AWS AppSync enables developers to connect their applications and services to data and
events with secure, serverless and high-performing GraphQL and Pub/Sub APIs. With AWS AppSync, you can publish real-time data updates to your applications with GraphQL mutations.
EventBridge supports calling a valid GraphQL mutation operation for matched events.
When you specify an AWS AppSync API mutation as a target, AWS AppSync processes the event via a
mutation operation, which can then trigger subscriptions linked to the mutation.

###### Note

EventBridge supports AWS AppSync public GraphQL APIs. EventBridge does not currently support AWS AppSync Private APIs.

You can use an AWS AppSync GraphQL API target for the following use cases:

- To push, transform, and store event data into your configured data sources.
- To send real-time notifications to connected application clients.

###### Note

AWS AppSync targets only support calling AWS AppSync GraphQL APIs using the [`AWS_IAM` authorization type](../../../appsync/latest/devguide/security-authz.md#aws-iam-authorization "../../../appsync/latest/devguide/security-authz.md#aws-iam-authorization").

For more information on AWS AppSync GraphQL APIs, see the [GraphQL and AWS AppSync
architecture](../../../appsync/latest/devguide/graphql-overview.md "../../../appsync/latest/devguide/graphql-overview.md") in the _AWS AppSync Developer Guide_.

###### To specify an AWS AppSync target for an EventBridge rule using the console

1.  [Create or edit the rule.](eb-create-rule.md "eb-create-rule.md")
2.  Under **Target**, [specify the target](eb-create-rule.md#eb-create-rule-target "eb-create-rule.md#eb-create-rule-target") by choosing **AWS service** and then **AWS AppSync**.
3.  Specify the mutation operation to be parsed and executed, along with the selection set.
    - Choose the AWS AppSync API, and then the GraphQL API mutation to invoke.
    - Under **Configure parameters and selection set**, choose to create a selection set using key-value mapping or an input transformer.

    Key-value mapping
    To use key-value mapping to create your selection set:

        + Specify variables for the API parameters. Each variables can be either a static values or a dynamic JSON path expression to the event payload.
        + Under **Selection set**, choose the variables you want included in the response.

    Input transformer
    To use an input transformer to create your selection set:

        + Specify an input path that defines the variables to use.
        + Specify an input template to define and format the information you want passed to the target.

    For more information, see [Configuring an input transformer when creating a rule in EventBridge](eb-transform-input-rule.md "eb-transform-input-rule.md").

4.  For **Execution role**, choose whether to create a new role or use an existing role.
5.  Complete creating or editing the rule.

## Example: AWS AppSync targets for Amazon EventBridge

In the following example, we'll walk through how to specifying an AWS AppSync target for an EventBridge rule, including defining an input transformation to format events for delivery.

Suppose you have an AWS AppSync GraphQL API, `Ec2EventAPI`, defined by the following schema:

```
type Event {
    id: ID!
    statusCode: String
    instanceId: String
}

type Mutation {
    pushEvent(id: ID!, statusCode: String!, instanceId: String): Event
}

type Query {
    listEvents: [Event]
}

type Subscription {
    subscribeToEvent(id: ID, statusCode: String, instanceId: String): Event
        @aws_subscribe(mutations: ["pushEvent"])
}
```

Applications clients that use this API can subscribe to the `subscribeToEvent` subscription, which is triggered by the `pushEvent` mutation.

You can create an EventBridge rule with a target that sends events to the AppSync API via the `pushEvent` mutation. When the mutation is invoked, any client that is subscribed will receive the event.

To specifying this API as the target for an EventBridge rule, you would do the
following:

1. Set the Amazon Resource Name (ARN) of the rule target to the GraphQL endpoint ARN of the `Ec2EventAPI` API.
2. Specify the mutation GraphQL Operation as a target parameter:

```
mutation CreatePushEvent($id: ID!, $statusCode: String, $instanceId: String) {
  pushEvent(id: $input, statusCode: $statusCode, instanceId: $instanceId) {
    id
    statusCode
    instanceId
  }
}
```

Your mutation selection set must include all the fields you wish to subscribe to in your GraphQL subscription. 3. Configure an input transformer to specify how data from matched events is used in your operation.

Suppose you selected the `“EC2 Instance Launch Successful”` sample event:

```
{
  "version": "0",
  "id": "3e3c153a-8339-4e30-8c35-687ebef853fe",
  "detail-type": "EC2 Instance Launch Successful",
  "source": "aws.autoscaling",
  "account": "123456789012",
  "time": "2015-11-11T21:31:47Z",
  "region": "us-east-1",
  "resources": ["arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:eb56d16b-bbf0-401d-b893-d5978ed4a025:autoScalingGroupName/sampleLuanchSucASG", "arn:aws:ec2:us-east-1:123456789012:instance/i-b188560f"],
  "detail": {
    "StatusCode": "InProgress",
    "AutoScalingGroupName": "sampleLuanchSucASG",
    "ActivityId": "9cabb81f-42de-417d-8aa7-ce16bf026590",
    "Details": {
      "Availability Zone": "us-east-1b",
      "Subnet ID": "subnet-95bfcebe"
    },
    "RequestId": "9cabb81f-42de-417d-8aa7-ce16bf026590",
    "EndTime": "2015-11-11T21:31:47.208Z",
    "EC2InstanceId": "i-b188560f",
    "StartTime": "2015-11-11T21:31:13.671Z",
    "Cause": "At 2015-11-11T21:31:10Z a user request created an AutoScalingGroup changing the desired capacity from 0 to 1.  At 2015-11-11T21:31:11Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 1."
  }
}
```

You can define the following variables for use in your template, using the target input transformer's input path:

```
{
  "id": "$.id",
  "statusCode": "$.detail.StatusCode",
  "EC2InstanceId": "$.detail.EC2InstanceId"
}
```

Compose the input transformer template to define the variables that EventBridge passes to the AWS AppSync mutation operation. The template must evaluate to JSON. Given our input path, you can compose the following template:

```
{
  "id": <id>,
  "statusCode": <statusCode>,
  "instanceId": <EC2InstanceId>
}
```
