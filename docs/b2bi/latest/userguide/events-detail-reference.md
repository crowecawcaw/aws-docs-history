# AWS B2B Data Interchange events detail reference

All events from AWS services have a common set of fields containing
metadata about the event, such as the AWS service that is the source of
the event, the time the event was generated, the account and region in which the event
took place, and others. For definitions of these general fields, see [Event structure reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User
Guide_.

In addition, each event has a `detail` field that contains data specific to
that particular event. The reference below defines the detail fields for the various
AWS B2B Data Interchange events.

When using EventBridge to select and manage AWS B2B Data Interchange events, it's useful to
keep the following in mind:

- The `source` field for all events from AWS B2B Data Interchange is set to
  `aws.b2bi`.
- The `detail-type` field specifies the event type.

For example, `Transformation Completed`.

- The `detail` field contains the data that is specific to that
  particular event.
  For information on constructing event patterns that enable rules to match AWS B2B Data Interchange
  events, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
  the _Amazon EventBridge User Guide_.

For more information on events and how EventBridge processes them, see [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User
Guide_.

## Details fields for transformation

events

This section describes the detail fields for the following events:

- Transformation Completed
- Transformation Failed

The `source` and `detail-type` fields are included because they contain specific values for AWS B2B Data Interchange events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
  . . .,
  "detail-type": "string",
  "source": "aws.b2bi",
  . . .,
  "detail": {
    "transformer-job-id" : "string",
    "trading-partner-id" : "string",
    "start-timestamp" : "string"
    "end-timestamp" : "string",
    "x12-transaction-set" : "string",
    "x12-version" : "string",
    "input-file-s3-attributes" : {
       "bucket" : "string",
       "object-key" : "string",
       "object-size-bytes" : "number"
    },
    "output-file-s3-attributes" : {
       "bucket" : "string",
       "object-key" : "string",
       "object-size-bytes" : "number"
    },
    "failure-message" : "string",
    "failure-code" : "string",
    "ack-generation-status" : "string",
    "ack-error-code-detected" : "boolean",
    "input-format" : "string",
    "output-format" : "string",
    "validation-status" : "string",
    "validation-report-s3-location" : {
       "bucket" : "string",
       "object-key" : "string"
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is either `Transformation
 Completed` or `Transformation Failed`.

`source`

Identifies the service that generated the event. For AWS B2B Data Interchange events,
this value is `aws.b2bi`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`transformer-job-id`

The unique, system-generated identifier for a transformer
run

`trading-partner-id`

The unique, system-generated identifier for a trading
partner.

`start-timestamp`

The time stamp for when the transformation request begins
processing.

`end-timestamp`

The time stamp for when the transformation request
finishes processing.

`x12-transaction-set`

A list of supported X12 transaction sets. Transaction sets
are maintained by the X12 Accredited Standards
Committee.

`x12-version`

The version to use for the specified X12 transaction
set.

`input-file-s3-attributes`

This parameter contains the details of the location of the
AWS input storage file.

`bucket`

The container for the object in Amazon S3

`object-key`

The name assigned to the object in
Amazon S3.

`object-size-bytes`

The size, in bytes, of the input file.

`output-file-s3-attributes`

This parameter contains the details of the location of the
AWS output storage file.

`bucket`

The container for the object in Amazon S3

`object-key`

The name assigned to the object in
Amazon S3.

`object-size-bytes`

The size, in bytes, of the output file.

`failure-message`

For failed transformations, the details for why the
transform failed.

`failure-code`

For failed transformations, the reason code for why the
transformations failed.

`ack-generation-status`

This field is only populated when the transformation is
supposed to generate an acknowledgement. The status of
acknowledgement for this transformation. Valid values are
`NOT_ATTEMPTED`, `COMPLETED`, or
`FAILED`.

`ack-error-code-detected`

This field is only populated for transformations that have
a `COMPLETED`
`ack-generation-status`. Specifies whether or not
an error code was detected during the validation step of
acknowledgement generation.

`input-format`

The format for the source, or input, data: either
`JSON` or `XML`. Only populated
for Outbound EDI transformations.

`output-format`

The format for the output file, `X12`. Only
populated for Outbound EDI transformations.

`validation-status`

Value is one of `SUCCEEDED`,
`FAILED`, or `NOT_ATTEMPTED`.

`validation-report-s3-location`

The location in Amazon S3 where the validation report is
stored.

## Details fields for split transformation

events

This section describes the detail fields for the following events:

- Transformation Completed
- Transformation Failed

The `source` and `detail-type` fields are included because they contain specific values for AWS B2B Data Interchange events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
   "version": "0",
   "id": "12345678-abcd-efgh-ijkl-mnopqrstuvwx",
   "detail-type": "Transformation Completed",
   "source": "aws.b2bi",
   "account": "111122223333",
   "time": "2025-07-11T15:30:00Z",
   "region": "US West (Oregon)",
   "resources": [
      "arn:AWS:b2bi:us-west-2:111122223333:transformer/tr-1a2b3c4d5e6f7g8h9",
      "arn:AWS:b2bi:us-west-2111122223333:profile/p-1a2b3c4d5e6f7g8h9",
      "arn:AWS:b2bi:us-west-2:111122223333:capability/ca-1a2b3c4d5e6f7g8h9",
      "arn:AWS:b2bi:us-west-2:111122223333:partnership/ps-1a2b3c4d5e6f7g8h9"
    ],
    "detail": {
       "trading-partner-id": "tp-1a2b3c4d5e6f7g8h9",
       "start-timestamp": "2025-07-11T15:30:00.000Z",
       "end-timestamp": "2025-07-11T15:30:01.000Z",
       "x12-transaction-set": "X12_856",
       "x12-version": "VERSION_4010",
       "input-file-s3-attributes": {
          "bucket": "amzn-s3-demo-source-bucket",
          "object-key": "tp-1a2b3c4d5e6f7g8h9/sample-856-4010.edi",
          "object-size-bytes": 3000
       },
       "output-file-s3-attributes": {
          "bucket": "amzn-s3-demo-destination-bucket",
          "object-key": "tp-1a2b3c4d5e6f7g8h9/sample-856-4010.edi.2025-07-11T15:30:00.000Z.xml",
          "object-size-bytes": 40000
       },
       "split-attributes": {
          "split-number": 1,
          "total-split-count": 1,
          "split-is-valid": false
       },
       "validation-status": "FAILED",
       "validation-report-s3-location": {
          "bucket": "amzn-s3-demo-bucket",
          "object-key": "tp-abc123def456gh789/VALIDATION_REPORT/456_9876_15txn.x12.2025-08-22T21:30:45.123Z.json.validation-errors.txt"
       }
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is either `Transformation
 Completed` or `Transformation Failed`.

`source`

Identifies the service that generated the event. For AWS B2B Data Interchange events,
this value is `aws.b2bi`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`transformer-id`

The unique identifier for the transformer.

`transformer-job-id`

The unique identifier for the transformer job.

`input-file-s3-attributes`

An object containing the S3 details of the input
file.

`output-file-s3-attributes`

An object containing the S3 details of the output file for
this split.

`split-attributes`

An object containing information specific to the
split.

`split-number`

The index of the current split
(1-indexed).

`total-split-count`

The total number of splits.

`split-is-valid`

Whether the current split is valid according
to X12 standard.

`validation-status`

Indicates the validity of the original (pre-split) EDI
file. Possible values:

- `SUCCEEDED`: The original EDI file is
  valid.
- `FAILED`: The original EDI file is
  invalid.
- `NOT_ATTEMPTED`: The validity check
  wasn't performed due to an earlier failure in the
  process.

`validation-report-s3-location`

The location in Amazon S3 where the validation report is
stored. For example:

## Details fields for acknowledgement

events

This section describes the detail fields for the following events:

- Acknowledgement Completed
- Acknowledgement Failed

The `source` and `detail-type` fields are included because they contain specific values for AWS B2B Data Interchange events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
  . . .,
  "detail-type": "string",
  "source": "aws.b2bi",
  . . .,
  "detail": {
    "transformer-job-id" : "string",
    "trading-partner-id" : "string",
    "start-timestamp" : "string"
    "end-timestamp" : "string",
    "input-x12-transaction-set" : "string",
    "input-x12-version" : "string",
    "input-file-s3-attributes" : {
       "bucket" : "string",
       "object-key" : "string",
       "object-size-bytes" : "number"
    },
    "ack-x12-type : "string",
    "ack-x12-version : "string",
    "ack-file-s3-attributes" : {
       "bucket" : "string",
       "object-key" : "string",
       "object-size-bytes" : "number"
    },
    "ack-error-code-detected : "boolean",
    "failure-message" : "string",
    "failure-code" : "string"
  }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is either `Acknowledgement
 Completed` or `Acknowledgement Failed`.

`source`

Identifies the service that generated the event. For AWS B2B Data Interchange events,
this value is `aws.b2bi`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`transformer-job-id`

The unique, system-generated identifier for a transformer
run.

`trading-partner-id`

The unique, system-generated identifier for a trading
partner.

`start-timestamp`

The time stamp for when the acknowledgement request begins
processing.

`end-timestamp`

The time stamp for when the acknowledgement request
finishes processing.

`input-x12-transaction-set`

The X12 transaction set of the input file.

`input-x12-version`

The version to use for the specified X12 transaction
set.

`input-file-s3-attributes`

This parameter contains the details of the location of the
AWS input storage file.

`bucket`

The container for the object in Amazon S3

`object-key`

The name assigned to the object in
Amazon S3.

`object-size-bytes`

The size, in bytes, of the input file.

`ack-x12-type`

X12 type for the acknowledgement.

`ack-x12-version`

X12 version for the acknowledgement.

`ack-file-s3-attributes`

This parameter contains the details of the location of the
AWS acknowledgement storage file. The acknowledgement file
attributes are only included in Acknowledgement Completed
events.

`bucket`

The container for the object in Amazon S3

`object-key`

The name assigned to the object in
Amazon S3.

`object-size-bytes`

The size, in bytes, of the acknowledgement
file.

`ack-error-code-detected`

For Acknowledgement Completed events, is either true or
false, depending on whether an error code was
detected.

`failure-message`

For failed acknowledgements, the details for why the event
failed.

`failure-code`

For failed acknowledgements, the reason code for why the
transformations failed.
