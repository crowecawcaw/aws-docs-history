

# AWS service event metadata
<a name="events-structure"></a>

The following fields appear in all events delivered to an event bus, and comprise the event's *metadata*:

```
{
  "version": "0",
  "id": "{{UUID}}",
  "detail-type": "{{event name}}",
  "source": "{{event source}}",
  "account": "{{ARN}}",
  "time": "{{timestamp}}",
  "region": "{{region}}",
  "replay-name": "{{replay name}}",
  "resources": [
    "{{ARN}}"
  ],
  "detail": {
    {{JSON object}}
  }
}
```

**version**  <a name="event-metadata-ref-version"></a>
By default, this is set to 0 (zero) in all events.

**id**  <a name="event-metadata-ref-id"></a>
A unique identifier in UUID format that's generated for every event. You can use `id` to trace events as they move through rules to targets.

**detail-type**  <a name="event-metadata-ref-detail-type"></a>
Identifies, in combination with the **source** field, the fields and values that appear in the **detail** field.  
Events that are delivered by CloudTrail have one of the following values for `detail-type`. For more information, see [AWS service events delivered via CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.  
+ `AWS API Call via CloudTrail`
+ `AWS Console Signin via CloudTrail`
+ `AWS Console Action via CloudTrail`
+ `AWS Service Event via CloudTrail`
+ `AWS Insight via CloudTrail`

**source**  <a name="event-metadata-ref-source"></a>
Identifies the service that generated the event. All events that come from AWS services begin with "aws." Customer-generated events can have any value here, as long as it doesn't begin with "aws." We recommend the use of Java package-name style reverse domain-name strings.

**account**  <a name="event-metadata-ref-account"></a>
The 12-digit number identifying an AWS account.

**time**  <a name="event-metadata-ref-time"></a>
The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service can report the start time, so this value might be before the time the event is received.

**region**  <a name="event-metadata-ref-region"></a>
Identifies the AWS Region where the event originated.

**replay-name**  <a name="event-metadata-ref-replay"></a>
A string representing the name of the replay. This field is present only for archived events that are resent to a target as part of a replay.  
For more information, see [Archiving and replaying events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-archive.html) in the *EventBridge User Guide*.

**resources**  <a name="event-metadata-ref-resources"></a>
A JSON array that contains ARNs that identify resources that are involved in the event. The service generating the event determines whether to include these ARNs. For example, Amazon EC2 instance state-changes include Amazon EC2 instance ARNs, Auto Scaling events include ARNs for both instances and Auto Scaling groups, but API calls with AWS CloudTrail do not include resource ARNs.

**detail**  <a name="event-metadata-ref-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field. It can be `"{}"`.   
AWS API call events have detail objects with approximately 50 fields nested several levels deep.  
[PutEvents](https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutEvents.html) accepts data in JSON format. For the JSON number (integer) data type, the constraints are: a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807.

**Example: Amazon EC2 instance state-change notification**  
The following event in Amazon EventBridge indicates an Amazon EC2 instance being terminated.  

```
{
  "version": "0",
  "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
  "detail-type": "EC2 Instance State-change Notification",
  "source": "aws.ec2",
  "account": "111122223333",
  "time": "2017-12-22T18:43:48Z",
  "region": "us-west-1",
  "resources": [
    "arn:aws:ec2:us-west-1:123456789012:instance/i-1234567890abcdef0"
  ],
  "detail": {
    "instance-id": " i-1234567890abcdef0",
    "state": "terminated"
  }
}
```

## Minimum information needed for a valid custom event
<a name="eb-custom-event"></a>

When you create custom events they must include the following fields:
+ `detail`
+ `detail-type`
+ `source`

```
{
  "detail-type": "{{event name}}",
  "source": "{{event source}}",
  "detail": {
  }
}
```