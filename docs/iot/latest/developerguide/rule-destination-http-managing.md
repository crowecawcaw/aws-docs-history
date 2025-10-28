# Managing HTTP topic rule

destinations

You can use the following operations to manage your HTTP topic rule
destinations.

###### In this topic:

- [Creating HTTP topic
  rule destinations](#rule-destination-http-creating "#rule-destination-http-creating")
- [Confirming HTTP topic
  rule destinations](#rule-destination-http-confirming "#rule-destination-http-confirming")
- [Sending a new confirmation
  request](#trigger-confirm "#trigger-confirm")
- [Disabling and deleting
  a topic rule destination](#rule-destination-http-deleting "#rule-destination-http-deleting")

## Creating HTTP topic

rule destinations

You create an HTTP topic rule destination by calling the
`CreateTopicRuleDestination` operation or by using the
AWS IoT console.

After you create a destination, AWS IoT sends a confirmation request to
the confirmation URL. The confirmation request has the following
format:

```
HTTP POST {confirmationUrl}/?confirmationToken={confirmationToken}
Headers:
x-amz-rules-engine-message-type: DestinationConfirmation
x-amz-rules-engine-destination-arn:"arn:aws:iot:us-east-1:123456789012:ruledestination/http/7a280e37-b9c6-47a2-a751-0703693f46e4"
Content-Type: application/json
Body:
{
    "arn":"arn:aws:iot:us-east-1:123456789012:ruledestination/http/7a280e37-b9c6-47a2-a751-0703693f46e4",
    "confirmationToken": "AYADeMXLrPrNY2wqJAKsFNn-…NBJndA",
    "enableUrl": "https://iot.us-east-1.amazonaws.com/confirmdestination/AYADeMXLrPrNY2wqJAKsFNn-…NBJndA",
    "messageType": "DestinationConfirmation"
}
```

The content of the confirmation request includes the following
information:

arn

The Amazon Resource Name (ARN) for the topic rule
destination to confirm.

confirmationToken

The confirmation token sent by AWS IoT Core. The token in the
example is truncated. Your token will be longer. You'll need
this token to confirm your destination with
AWS IoT Core.

enableUrl

The URL to which you browse to confirm a topic rule
destination.

messageType

The type of message.

## Confirming HTTP topic

rule destinations

To complete the endpoint confirmation process, if you're using the
AWS CLI, you must perform the following steps after your confirmation URL
receives the confirmation request.

1. ###### Confirm that the destination is willing to receive
   messages

To confirm that the topic rule destination is willing to
receive IoT messages, either call the `enableUrl`
in the confirmation request, or perform the
`ConfirmTopicRuleDestination` API operation
and pass the `confirmationToken` from the
confirmation request. 2. ###### Set topic rule status to enabled

After you've confirmed that the destination can receive
messages, you must perform the
`UpdateTopicRuleDestination` API operation to
set the status of the topic rule to
`ENABLED`.

If you're using the AWS IoT console, copy the
`confirmationToken` and paste it into the destination's
confirmation dialog in the AWS IoT console. You can then enable the topic
rule.

## Sending a new confirmation

request

To activate a new confirmation message for a destination, call
`UpdateTopicRuleDestination` and set the topic rule
destination's status to `IN_PROGRESS`.

Repeat the confirmation process after you send a new confirmation
request.

## Disabling and deleting

a topic rule destination

To disable a destination, call `UpdateTopicRuleDestination`
and set the topic rule destination's status to `DISABLED`. A
topic rule in the DISABLED state can be enabled again without the need
to send a new confirmation request.

To delete a topic rule destination, call
`DeleteTopicRuleDestination`.
