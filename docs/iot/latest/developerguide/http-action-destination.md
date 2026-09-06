

# HTTP action destinations
<a name="http-action-destination"></a>

An HTTP action destination is a web service to which the rules engine can route data from a topic rule. An AWS IoT Core resource describes the web service for AWS IoT. Destination resources can be shared by different rules.

Before AWS IoT Core can send data to another web service, it must confirm that it can access the service's endpoint.

## Overview
<a name="http-action-destination-overview"></a>

An HTTP action destination refers to a web service that supports a confirmation URL and one or more data collection URLs. The destination resource contains the confirmation URL of your web service. When you configure an HTTP action, you specify the actual URL of the endpoint that should receive the data along with the web service's confirmation URL. After your destination is confirmed, the topic rule sends the result of the SQL statement to the HTTPS endpoint (and not to the confirmation URL).

An HTTP action destination can be in one of the following states:

ENABLED  
The destination has been confirmed and can be used by a rule action. A destination must be in the `ENABLED` state for it to be used in a rule. You can only enable a destination that's in DISABLED status.

DISABLED  
The destination has been confirmed but it can't be used by a rule action. This is useful if you want to temporarily prevent traffic to your endpoint without having to go through the confirmation process again. You can only disable a destination that's in ENABLED status.

IN\_PROGRESS  
Confirmation of the destination is in progress.

ERROR  
Destination confirmation timed out.

After an HTTP action destination has been confirmed and enabled, it can be used with any rule in your account.

## Managing HTTP action destinations
<a name="http-action-destination-managing"></a>

You can use the following operations to manage your HTTP action destinations.

### Creating HTTP action destinations
<a name="http-action-destination-creating"></a>

You create an HTTP action destination by calling the `CreateTopicRuleDestination` operation or by using the AWS IoT console.

After you create a destination, AWS IoT sends a confirmation request to the confirmation URL. The confirmation request has the following format:

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

The content of the confirmation request includes the following information:

arn  
The Amazon Resource Name (ARN) for the HTTP action destination to confirm.

confirmationToken  
The confirmation token sent by AWS IoT Core. The token in the example is truncated. Your token will be longer. You'll need this token to confirm your destination with AWS IoT Core.

enableUrl  
The URL to which you browse to confirm a topic rule destination.

messageType  
The type of message.

### Confirming HTTP action destinations
<a name="http-action-destination-confirming"></a>

To complete the endpoint confirmation process, if you're using the AWS CLI, you must perform the following steps after your confirmation URL receives the confirmation request.

1. 

**Confirm that the destination is ready to receive messages**  
To confirm that the HTTP action destination is ready to receive IoT messages, either call the `enableUrl` in the confirmation request, or perform the `ConfirmTopicRuleDestination` API operation and pass the `confirmationToken` from the confirmation request.

1. 

**Set topic rule status to enabled**  
After you've confirmed that the destination can receive messages, you must perform the `UpdateTopicRuleDestination` API operation to set the status of the topic rule to `ENABLED`.

If you're using the AWS IoT console, copy the `confirmationToken` and paste it into the destination's confirmation dialog in the AWS IoT console. You can then enable the topic rule.

### Sending a new confirmation request
<a name="trigger-confirm"></a>

To activate a new confirmation message for a destination, call `UpdateTopicRuleDestination` and set the topic rule destination's status to `IN_PROGRESS`. 

Repeat the confirmation process after you send a new confirmation request.

### Disabling and deleting an HTTP action destination
<a name="http-action-destination-deleting"></a>

To disable a destination, call `UpdateTopicRuleDestination` and set the topic rule destination's status to `DISABLED`. A topic rule in the DISABLED state can be enabled again without the need to send a new confirmation request.

To delete an HTTP action destination, call `DeleteTopicRuleDestination`.

## Certificate Authority Support
<a name="http-action-destination-certificates"></a>

**Note**  
Self-signed certificates are not supported. 

 HTTPS Endpoints in an HTTP action destination support certificates issued by both [AWS Private Certificate Authority ](https://www.amazontrust.com/repository/) and [Lets Encrypt](https://letsencrypt.org/certificates/). 