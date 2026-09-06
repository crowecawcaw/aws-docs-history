

# AWS service events delivered via AWS CloudTrail
<a name="eb-service-event-cloudtrail"></a>

 AWS CloudTrail is a service that automatically records events such as AWS API calls. You can create EventBridge rules that use the information from CloudTrail. For more information about CloudTrail, see [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

CloudTrail sends the following types of events to the default EventBridge event bus. In each case, the `detail-type` value of the event is the listed event type:
+ `AWS API Call via CloudTrail`

  Events that represent a request to a public AWS service API.

  For more information, see [Understanding CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html) in the *AWS CloudTrail User Guide*.
+ `AWS Console Signin via CloudTrail`

  Attempts to sign in to the AWS Management Console, the AWS Discussion Forums, and the AWS Support Center. 

  For more information, see [AWS Management Console sign-in events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html) in the *AWS CloudTrail User Guide*.
+ `AWS Console Action via CloudTrail`

  Actions that were taken in the console that were not an API calls.

  For more information, see [AWS Management Console sign-in events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html) in the *AWS CloudTrail User Guide*.
+ `AWS Service Event via CloudTrail`

  Events created by AWS services but are not directly triggered by a request to a public AWS service API.

  For more information, see [AWS service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/non-api-aws-service-events.html) in the *AWS CloudTrail User Guide*.
+ `AWS Insight via CloudTrail`

  Insights events are triggered by CloudTrail when customer enables the CloudTrail Insight feature.

  For more information, see [CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-insight-details.html) in the *AWS CloudTrail User Guide*.
+ `AWS Network Activity Event via CloudTrail`

  Network activity events capture API calls made through VPC endpoints from private VPCs. These events require a trail configured with network activity event selectors for the relevant event source.

  For more information, see [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

To record events with one of the CloudTrail `detail-type` values, you must enable a CloudTrail trail with logging. For more information, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.

**Note**  
All CloudTrail events are delivered to the default event bus only. To process CloudTrail events on a custom event bus, create a rule on the default bus that forwards matching events to your custom bus.

The rule state controls which event categories are matched:
+ *Write (mutating) management events* — Matched by rules in the default `ENABLED` state. No special configuration needed beyond an active trail.
+ *Read-only management events* — Matched only by rules with state set to `ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS`. For more information, see [Receiving read-only management events from AWS services](eb-service-event-cloudtrail-management.md).
+ *Data events* — Matched by rules in the default `ENABLED` state. The trail must be configured to capture the specific data event types. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.
+ *Network activity events* — Matched by rules in the default `ENABLED` state. The trail must be configured with network activity event selectors for the relevant event source, and the API call must be made through a VPC endpoint.

Some occurrences in AWS services can be reported to EventBridge both by the service itself and by CloudTrail. For example, an Amazon EC2 API call that starts an instance generates multiple events:
+ `EC2 Instance State-change Notification` events sent directly from Amazon EC2 to EventBridge, as the instance enters the `pending` and then `running` states. For example:

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
+ An `AWS API Call via CloudTrail` event sent from CloudTrail to EventBridge that represents the API call itself. For example:

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

**Note**  
If you use a `Put*Events` API call event as the basis for creating an event pattern, make sure the final event pattern does not exceed 1 MB. The maximum size of any `Put*Events` requests is 1 MB. For more information, see [](eb-putevents.md).

For more information about the services that CloudTrail supports, see [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html) in the *CloudTrail User Guide*.