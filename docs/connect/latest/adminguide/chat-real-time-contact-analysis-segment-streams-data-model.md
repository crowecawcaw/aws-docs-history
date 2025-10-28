# Data model for conversational analytics segment streams to analyze chats in

Contact Lens

Conversational analytics segment streams for chat contacts are generated in
JSON. Event JSON blobs are published to the associated stream for every contact
that has real-time conversational analytics enabled. The following types of
events can be published for a conversational analytics session for a chat
contact:

- STARTED events—Each conversational analytics session publishes
  one STARTED event at the beginning of the session.
- SEGMENTS events—Each conversational analytics session may
  publish zero or more SEGMENTS events during the session. These events
  contain a list of segments with analyzed information. For chat contacts,
  the list of segments may include "`Attachments`,"
  "`Transcript`," "`Categories`,"
  "`Events`," "`Issues`," or
  "`PostContactSummary`" segments.
- COMPLETED or FAILED events—Each conversational analytics
  session publishes one COMPLETED or FAILED event at the end of the
  session.

## Common

properties included in all events for chat contacts

Every event includes the following properties:

**Version**

The version of the event schema. For chat contacts, this is
2.0.0.

Type: String

**Channel**

The type of channel for this contact.

Type: String

Valid values: `VOICE`, `CHAT`,
`TASK`

For more information about channels, see [Channels and concurrency for routing contacts
in Amazon Connect](channels-and-concurrency.md "channels-and-concurrency.md").

**AccountId**

The identifier of the account where this contact takes
place.

Type: String

**InstanceId**

The identifier of the instance where this contact takes
place.

Type: String

**ContactId**

The identifier of the contact being analyzed.

Type: String

**StreamingEventType**

The type of event published.

Type: String

Valid values: `STARTED`, `SEGMENTS`,
`COMPLETED`, `FAILED`

**StreamingSettings**

The Contact Lens settings for this contact

Type: [StreamingSettings](#streamingsettingsobject "#streamingsettingsobject") object

## StreamingSettings object

**LanguageCode**

The language code associated to this contact.

Type: String

Valid values: the language code for one of the [supported
languages for Contact Lens real-time call
analytics](supported-languages.md#supported-languages-contact-lens "supported-languages.md#supported-languages-contact-lens").

**Output**

The Contact Lens output type enabled for this
contact.

Type: String

Valid values: `Raw`, `Redacted`,
`RedactedAndRaw`

**RedactionTypes**

The type of redaction enabled for this contact.

Type: Array of Strings

Valid values: `PII`

**RedactionTypesMetadata**

The redaction metadata for each redaction type.

Type: RedactionType string to [RedactionMetadata](#redactionmetadata "#redactionmetadata") object

Valid values: `PII`

## RedactionMetadata object

Provides information on redaction settings.

**RedactionMaskMode**

The data redaction replacement setting

Type: String

Valid values: `PII`, `EntityType`

## STARTED

event

`STARTED` events include only the common properties:

- Version
- Channel
- AccountId
- ContactId
- StreamingEventType: STARTED
- StreamingSettings

## SEGMENTS

event

`SEGMENTS` events include the following properties:

- Version
- Channel
- AccountId
- OutputType
  - The Contact Lens output type of the current
    segment
  - Type: String
  - Valid values: `Raw`,
    `Redacted`

- ContactId
- StreamingEventType: SEGMENTS
- StreamingSettings
- Segments
  - A list of segments with analyzed information.
  - Type: Array of [Segment](#chat-segment "#chat-segment")
    objects

**Segment**

An analyzed segment for a real-time analysis session.

Each segment is an object with the following optional
properties. Only one of these properties is present, depending
on the segment type:

- [Attachments](#chat-attachments "#chat-attachments")
- [Categories](#chat-category "#chat-category")
- [Event](#chat-event "#chat-event")
- [Issues](#chat-issues "#chat-issues")
- [Transcript](#chat-transcript "#chat-transcript")
- [PostContactSummary](#chat-postcontactsummary "#chat-postcontactsummary")

**Attachments**

The analyzed attachments.

Required: No

Type: [RealTimeContactAnalysisSegmentAttachments](../APIReference/API_RealTimeContactAnalysisSegmentAttachments.md "../APIReference/API_RealTimeContactAnalysisSegmentAttachments.md")
object

**Categories**

The matched category rules.

Type: [RealTimeContactAnalysisSegmentCategories](../APIReference/API_RealTimeContactAnalysisSegmentCategories.md "../APIReference/API_RealTimeContactAnalysisSegmentCategories.md")
object

Required: No

**Event**

Segment type describing a contact event.

Type: [RealTimeContactAnalysisSegmentEvent](../APIReference/API_RealTimeContactAnalysisSegmentEvent.md "../APIReference/API_RealTimeContactAnalysisSegmentEvent.md") object

Required: No

**Issues**

Segment type containing a list of detected issues.

Type: [RealTimeContactAnalysisSegmentIssues](../APIReference/API_RealTimeContactAnalysisSegmentIssues.md "../APIReference/API_RealTimeContactAnalysisSegmentIssues.md") object

Required: No

**Transcript**

The analyzed transcript segment.

Type: [RealTimeContactAnalysisSegmentTranscript](../APIReference/API_RealTimeContactAnalysisSegmentTranscript.md "../APIReference/API_RealTimeContactAnalysisSegmentTranscript.md")
object

Required: No

**PostContactSummary**

Information about the post-contact summary for a real-time
contact segment for chat.

Type: [RealTimeContactAnalysisSegmentPostContactSummary](../APIReference/API_RealTimeContactAnalysisSegmentPostContactSummary.md "../APIReference/API_RealTimeContactAnalysisSegmentPostContactSummary.md")
object

Required: No

## COMPLETED

event

`COMPLETED` events include only the following common
properties:

- Version
- Channel
- AccountId
- InstanceId
- ContactId
- StreamingEventType: COMPLETED
- StreamingSettings

## FAILED

event

`FAILED` events include only the following common
properties:

- Version
- Channel
- AccountId
- InstanceId
- ContactId
- StreamingEventType: FAILED
- StreamingSettings
