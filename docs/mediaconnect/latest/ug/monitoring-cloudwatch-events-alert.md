# MediaConnect alert

event

MediaConnect publishes an alert event when a resource encounters an error. The event
contains an error code and a message that describes the issue. These alerts are
visible on the MediaConnect console, or by using the `describe-flow` AWS Command Line Interface
(AWS CLI) command. For more information about the `describe-flow` command,
see [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html").

For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of this event.

```
{
 "version": "0",
 "id": "01234567-0123-0123-0123-0123456789ab",
 "detail-type": "MediaConnect Alert",
 "source": "aws.mediaconnect",
 "account": "111122223333",
 "time": "2022-01-06T00:45:47Z",
 "region": "us-east-1",
 "resources": [
 "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow"
 ],
 "detail": {
 "errored": true,
 "error-code": "AccessDeniedException",
 "error-message": "Permission denied accessing encryption key for output Test. Removing output until it is fixed (secret arn:aws:secretsmanager:us-east-1:111122223333:secret:ExampleSecret, role arn:aws:iam::111122223333:role/ExampleKey)"
 }
}

```
