

# Security Incident Response events detail reference
<a name="events-detail-reference-full"></a>

All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others. For definitions of these general fields, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*. 

In addition, each event has a `detail` field that contains data specific to that particular event. The reference below defines the detail fields for the various Security Incident Response events.

When using EventBridge to select and manage Security Incident Response events, it's useful to keep the following in mind:
+ The `source` field for all events from Security Incident Response is set to `"aws.security-ir"`.
+ The `detail-type` field specifies the event type.

  For example, `"Case Updated"`.
+ The `detail` field contains the data that is specific to that particular event. 

For information on constructing event patterns that enable rules to match Security Incident Response events, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.

For more information on events and how EventBridge processes them, see [EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) in the *Amazon EventBridge User Guide*.

**Common Fields:** All AWS Security Incident Response events include these standard Amazon EventBridge fields
+ *version:* EventBridge event format version
+ *id:* Unique identifier for the event
+ *detail-type:* Human-readable description of the event type
+ *source:* Always "aws.security-ir" for Security Incident Response events
+ *account:* AWS account ID where the event occurred
+ *time:* ISO 8601 timestamp when the event occurred
+ *region:* AWS Region where the resource exists
+ *resources:* Array containing the ARN of the affected resource

**Detail Fields:** The `detail` object contains Security Incident Response-specific information
+ *caseId:* Unique identifier for the case (case events only)
+ *membershipId:* Unique identifier for the membership (membership events only)
+ *updatedBy:* Who performed the update (case and comment update events only)
+ *createdBy:* Who created the entity (case and comment creation events only)

**Actor Values:** The `updatedBy` and `createdBy` fields can contain
+ *AWS Responder:* Action performed by an AWS security responder
+ *`security-ir.amazonaws.com`:* Action performed automatically by the service
+ *Account ID:* Action performed by the customer (e.g., "111122223333")

**Resource ARN values:** AWS Security Incident Response resources use these ARN formats
+ *Cases: *`arn:aws:security-ir:{region}:{account-id}:case/{case-id}`
+ *Memberships: *`arn:aws:security-ir:{region}:{account-id}:membership/{membership-id}`