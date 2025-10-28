# Including Amazon EventBridge resources in AWS CloudFormation

stacks

AWS CloudFormation enables you to configure and manage your AWS resources across accounts and regions
in a centralized and repeatable manner by treating infrastructure as code. CloudFormation does
this by letting you create _templates_, which define the resources you
want to provision and manage. These resources can include EventBridge artifacts such as event buses
and rules, pipes, schemas, and schedules, among others. Use these resources to include EventBridge
functionality in the technology stacks you provision and manage through CloudFormation.

## Amazon EventBridge resources available in

AWS CloudFormation

EventBridge provides resources for use in CloudFormation templates in the following resource
namespaces:

- [AWS::Events](../../../AWSCloudFormation/latest/UserGuide/AWS_Events.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Events.md")

Template examples include:

    + [Create an API destination for PagerDuty](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.md#aws-resource-events-apidestination--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.md#aws-resource-events-apidestination--examples")
    + [Create an API destinatio for Slack](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.md#aws-resource-events-apidestination--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.md#aws-resource-events-apidestination--examples")
    + [Create a connection with ApiKey authorization
     parameters](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.md#aws-resource-events-connection--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.md#aws-resource-events-connection--examples")
    + [Create a connection with OAuth authorization
     parameters](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.md#aws-resource-events-connection--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.md#aws-resource-events-connection--examples")
    + [Create a global endpoint with event replication](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.md#aws-resource-events-endpoint--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.md#aws-resource-events-endpoint--examples")
    + [Deny policy using multiple principals and actions](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md#aws-resource-events-eventbuspolicy--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md#aws-resource-events-eventbuspolicy--examples")
    + [Grant permission to an organization using a custom event
     bus](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md#aws-resource-events-eventbuspolicy--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md#aws-resource-events-eventbuspolicy--examples")
    + [Create a cross-Region rule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples")
    + [Create a rule that includes a dead-letter queue for a
     target](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples")
    + [Regularly invoke a Lambda function](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples")
    + [Invoke Lambda function in response to an event](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples")
    + [Notify a topic in response to a log nntry](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#aws-resource-events-rule--examples")

- [AWS::EventSchemas](../../../AWSCloudFormation/latest/UserGuide/AWS_EventSchemas.md "../../../AWSCloudFormation/latest/UserGuide/AWS_EventSchemas.md")
- [AWS::Pipes](../../../AWSCloudFormation/latest/UserGuide/AWS_Pipes.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Pipes.md")

Template examples include:

    + [Create a pipe with an event filter](../../../AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.md#aws-resource-pipes-pipe--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.md#aws-resource-pipes-pipe--examples")

- [AWS::Scheduler](../../../AWSCloudFormation/latest/UserGuide/AWS_Scheduler.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Scheduler.md")

## Generating Amazon EventBridge

resource definitions for AWS CloudFormation templates

As an aid to help you jumpstart developing CloudFormation templates, the EventBridge console
enables you to create CloudFormation templates from the existing event buses, rules, and pipes in
your account.

- [Generating an AWS CloudFormation template from an existing EventBridge event bus](eb-generate-event-bus-template.md "eb-generate-event-bus-template.md")
- [Generating an AWS CloudFormation template from an existing EventBridge rule](rule-generate-template.md "rule-generate-template.md")
- [Generating an AWS CloudFormation template from EventBridge Pipes](pipes-generate-template.md "pipes-generate-template.md")

## Bringing the default event bus under AWS CloudFormation management

Because EventBridge provisions the default event bus into your account
automatically, you cannot create it using a CloudFormation template, as you
normally would for any resource you wanted to include in a CloudFormation
stack. To include the default event bus in a CloudFormation stack, you must
first _import_ it into a stack. Once you have imported the
default event bus into a stack, you can then update the event bus properties as
desired.

For more information, see [Updating a default event bus using
AWS CloudFormation in EventBridge](event-bus-update-default-cfn.md "event-bus-update-default-cfn.md")

## Managing AWS CloudFormation stack events using EventBridge

Beyond including EventBridge resources in your CloudFormation stacks, you can use EventBridge to manage
the events generated by CloudFormation stacks themselves. CloudFormation sends events to EventBridge whenever a create, update, delete, or drift-detection operation is performed on a stack. CloudFormation also sends events to EventBridge for status changes to stack sets and stack set instances. You can use EventBridge rules to route events to your defined targets.

For more information, see [Managing
CloudFormation events using EventBridge](../../../AWSCloudFormation/latest/UserGuide/stacks-event-bridge.md "../../../AWSCloudFormation/latest/UserGuide/stacks-event-bridge.md") in the _AWS CloudFormation User
Guide_.
