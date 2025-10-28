# AWS service events delivered via AWS CloudTrail

AWS CloudTrail is a service that automatically records events such as AWS API calls. You can
create EventBridge rules that use the information from CloudTrail. For more information about CloudTrail, see
[What is AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

CloudTrail sends the following types of events to the default EventBridge event bus. In each case, the `detail-type` value of the event is the listed event type:

- `AWS API Call via CloudTrail`

Events that represent a request to a public AWS service API.

For more information, see [Understanding CloudTrail events](../../../awscloudtrail/latest/userguide/cloudtrail-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-events.md")
in the _AWS CloudTrail User Guide_.

- `AWS Console Signin via CloudTrail`

Attempts to sign in to the AWS Management Console, the AWS Discussion Forums,
and the AWS Support Center.

For more information, see [AWS Management Console sign-in events](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.md") in the _AWS CloudTrail
User Guide_.

- `AWS Console Action via CloudTrail`

Actions that were taken in the console that were not an API calls.

For more information, see [AWS Management Console sign-in events](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.md")
in the _AWS CloudTrail User Guide_.

- `AWS Service Event via CloudTrail`

Events created by AWS services but are not directly triggered by a request to a public AWS service API.

For more information, see [AWS service events](../../../awscloudtrail/latest/userguide/non-api-aws-service-events.md "../../../awscloudtrail/latest/userguide/non-api-aws-service-events.md")
in the _AWS CloudTrail User Guide_.

- `AWS Insight via CloudTrail`

Insights events are triggered by CloudTrail when customer enables the CloudTrail Insight
feature.

For more information, see [CloudTrail Insights](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-insight-details.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-insight-details.md")
in the _AWS CloudTrail User Guide_.
To record events with one of the CloudTrail `detail-type` values, you must enable a CloudTrail trail with logging. For more information, see
[Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md")
in the _AWS CloudTrail User Guide_.

Some occurrences in AWS services can be reported to EventBridge both by the service itself and
by CloudTrail. For example, an Amazon EC2 API call that starts an instance generates multiple events:

- `EC2 Instance State-change Notification` events sent directly from Amazon EC2 to EventBridge,
  as the instance enters the `pending` and then `running`
  states. For example:

```
{
    . . .
   "detail-type":"EC2 Instance State-change Notification",
   "source":"aws.ec2",
    . . .
   "detail":{
      "instance-id":"i-abcd1111",
      "state":"pending"
   }
}
```

- An `AWS API Call via CloudTrail` event sent from CloudTrail to EventBridge that represents the API call itself. For example:

```
{
    . . .
   "detail-type":"AWS API Call via CloudTrail",
   "source":"aws.ec2",
    . . .
   ],
  "detail": {
    "eventSource": "ec2.amazonaws.com",
    "eventName": "StartInstances"
    }
}
```

###### Note

If you use a `Put*Events` API call event as the basis for creating an event pattern, make sure the final event pattern does not exceed 256 KB. The maximum size of any
`Put*Events` requests is 256 KB. For more information, see .

For more information about the services that CloudTrail supports, see [CloudTrail supported
services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md") in the _CloudTrail User Guide_.
