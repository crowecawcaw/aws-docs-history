# Data

model for conversational analytics segment streams to analyze voice contacts
in Contact Lens

Real-time contact analysis segment streams are generated in JSON. Event JSON blobs are published to
the associated stream for every contact that has real-time conversational
analytics enabled. The following types of events can be published for a
conversational analytics session for a voice contact:

- STARTED events—Each conversational analytics session publishes
  one STARTED event at the beginning of the session.
- SEGMENTS events—Each conversational analytics session may
  publish zero or more SEGMENTS events during the session. These events
  contain a list of segments with analyzed information. For voice
  contacts, the list of segments may include "`Utterance`",
  "`Transcript`", "`Categories`", or
  "`PostContactSummary`" segments.
- COMPLETED or FAILED events—Each conversational analytics
  session publishes one COMPLETED or FAILED event at the end of the
  session.

## Common

properties included in all events for voice contacts

Every event includes the following properties:

**Version**

The version of the event schema.

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

**ContactId**

The identifier of the contact being analyzed.

Type: String

**InstanceId**

The identifier of the instance where this contact takes
place.

Type: String

**LanguageCode**

The language code associated to this contact.

Type: String

Valid values: the language code for one of the [supported
languages for Contact Lens real-time call
analytics](supported-languages.md#supported-languages-contact-lens "supported-languages.md#supported-languages-contact-lens").

**EventType**

The type of event published.

Type: String

Valid values: `STARTED`, `SEGMENTS`,
`COMPLETED`, `FAILED`

## STARTED

event

`STARTED` events include only the common properties:

- Version
- Channel
- AccountId
- ContactId
- LanguageCode
- EventType: STARTED

## SEGMENTS

event

`SEGMENTS` events include the following properties:

- Version
- Channel
- AccountId
- ContactId
- LanguageCode
- EventType: SEGMENTS
- Segments: In addition to the common properties,
  `SEGMENTS` events include a list of segments with
  analyzed information.

Type: Array of [Segment](#segment "#segment")
objects

- PostContactSummary: Information about the post-contact summary for
  a voice contact segment.

Type: [PostContactSummary](../APIReference/API_connect-contact-lens_PostContactSummary.md "../APIReference/API_connect-contact-lens_PostContactSummary.md") objects

Required: No

**Segment**

An analyzed segment for a real-time analysis session.

Each segment is an object with the following optional
properties. Only one of these properties is present, depending
on the segment type:

- Utterance
- Transcript
- Categories
- PostContactSummary

**Utterance**

The analyzed utterance.

Required: No

- **Id**

The identifier of the utterance.

Type: String

- **TranscriptId**

The identifier of the transcript associated to this
utterance.

Type: String

- **ParticipantId**

The identifier of the participant.

Type: String

- **ParticipantRole**

The role of participant. For example, is it a
customer, agent, or system.

Type: String

- **PartialContent**

The content of the utterance.

Type: String

- **BeginOffsetMillis**

The beginning offset in the contact for this
transcript.

Type: Integer

- **EndOffsetMillis**

The end offset in the contact for this
transcript.

Type: Integer

**Transcript**

The analyzed transcript.

Type: [Transcript](../../../contact-lens/latest/APIReference/API_Transcript.md "../../../contact-lens/latest/APIReference/API_Transcript.md") object

Required: No

**Categories**

The matched category rules.

Type: [Categories](../../../contact-lens/latest/APIReference/API_Categories.md "../../../contact-lens/latest/APIReference/API_Categories.md") object

Required: No

**PostContactSummary**

Information about the post-contact summary for a voice contact
segment.

Type: [PostContactSummary](../APIReference/API_connect-contact-lens_PostContactSummary.md "../APIReference/API_connect-contact-lens_PostContactSummary.md") object

Required: No

## COMPLETED

event

`COMPLETED` events include only the following common
properties:

- Version
- Channel
- AccountId
- ContactId
- LanguageCode
- EventType: COMPLETED

## FAILED

event

`FAILED` events include only the following common
properties:

- Version
- Channel
- AccountId
- ContactId
- LanguageCode
- EventType: FAILED
