# Security Incident Response events detail reference

All events from AWS services have a common set of fields containing
metadata about the event, such as the AWS service that is the source of
the event, the time the event was generated, the account and region in which the event
took place, and others. For definitions of these general fields, see [Event structure reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User
Guide_.

In addition, each event has a `detail` field that contains data specific to
that particular event. The reference below defines the detail fields for the various
Security Incident Response events.

When using EventBridge to select and manage Security Incident Response events, it's useful to
keep the following in mind:

- The `source` field for all events from Security Incident Response is set to
  `"aws.security-ir"`.
- The `detail-type` field specifies the event type.

For example, `"Case Updated"`.

- The `detail` field contains the data that is specific to that
  particular event.
  For information on constructing event patterns that enable rules to match Security Incident Response
  events, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
  the _Amazon EventBridge User Guide_.

For more information on events and how EventBridge processes them, see [EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User
Guide_.

**Common Fields:** All AWS Security Incident Response events include these standard Amazon EventBridge fields

- _version:_ EventBridge event format version
- _id:_ Unique identifier for the event
- _detail-type:_ Human-readable description of the event type
- _source:_ Always "aws.security-ir" for Security Incident Response events
- _account:_ AWS account ID where the event occurred
- _time:_ ISO 8601 timestamp when the event occurred
- _region:_ AWS Region where the resource exists
- _resources:_ Array containing the ARN of the affected resource
  **Detail Fields:** The `detail` object contains Security Incident Response-specific information

- _caseId:_ Unique identifier for the case (case events only)
- _membershipId:_ Unique identifier for the membership (membership events only)
- _updatedBy:_ Who performed the update (case and comment update events only)
- _createdBy:_ Who created the entity (case and comment creation events only)
  **Actor Values:** The `updatedBy` and `createdBy` fields can contain

- _AWS Responder:_ Action performed by an AWS security responder
- _`security-ir.amazonaws.com`:_ Action performed automatically by the service
- _Account ID:_ Action performed by the customer (e.g., "111122223333")
  **Resource ARN values:** AWS Security Incident Response resources use these ARN formats

- _Cases:_ `arn:aws:security-ir:{region}:{account-id}:case/{case-id}`
- _Memberships:_ `arn:aws:security-ir:{region}:{account-id}:membership/{membership-id}`
