

# Data model for conversational analytics segment streams to analyze chats in conversational analytics
<a name="chat-real-time-contact-analysis-segment-streams-data-model"></a>

Conversational analytics segment streams for chat contacts are generated in JSON. Event JSON blobs are published to the associated stream for every contact that has real-time conversational analytics enabled. The following types of events can be published for a conversational analytics session for a chat contact:
+ STARTED events—Each conversational analytics session publishes one STARTED event at the beginning of the session.
+ SEGMENTS events—Each conversational analytics session might publish zero or more SEGMENTS events during the session. These events contain a list of segments with analyzed information. For chat contacts, the list of segments might include "`Attachments`," "`Transcript`," "`Categories`," "`Events`," "`Issues`," or "`PostContactSummary`" segments.
+ COMPLETED or FAILED events—Each conversational analytics session publishes one COMPLETED or FAILED event at the end of the session.

## Common properties included in all events for chat contacts
<a name="chat-segment-streams-data-model-common-properties"></a>

Every event includes the following properties:

**Version**  
The version of the event schema. For chat contacts, this is 2.0.0.  
Type: String

**Channel**  
The type of channel for this contact.  
Type: String  
Valid values: `VOICE`, `CHAT`, `TASK`  
For more information about channels, see [Channels and concurrency for routing contacts in Connect Customer](channels-and-concurrency.md).

**AccountId**  
The identifier of the account where this contact takes place.  
Type: String

**InstanceId**  
The identifier of the instance where this contact takes place.  
Type: String 

**ContactId**  
The identifier of the contact being analyzed.  
Type: String

**StreamingEventType**  
The type of event published.  
Type: String   
Valid values: `STARTED`, `SEGMENTS`, `COMPLETED`, `FAILED`

**StreamingSettings**  
The conversational analytics settings for this contact  
Type: [StreamingSettings](#streamingsettingsobject) object 

## StreamingSettings object
<a name="streamingsettingsobject"></a>

**LanguageCode**  
The language code associated to this contact.  
Type: String   
Valid values: the language code for one of the [supported languages for conversational analytics real-time call analytics](supported-languages.md#supported-languages-contact-lens). 

**Output**  
The conversational analytics output type enabled for this contact.  
Type: String  
Valid values: `Raw`, `Redacted`, `RedactedAndRaw` 

**RedactionTypes**  
The type of redaction enabled for this contact.  
Type: Array of Strings  
Valid values: `PII` 

**RedactionTypesMetadata**  
The redaction metadata for each redaction type.  
Type: RedactionType string to [RedactionMetadata](#redactionmetadata) object   
Valid values: `PII` 

## RedactionMetadata object
<a name="redactionmetadata"></a>

Provides information on redaction settings.

**RedactionMaskMode**  
The data redaction replacement setting  
Type: String   
Valid values: `PII`, `EntityType`

## STARTED event
<a name="chat-segment-streams-data-model-started-event"></a>

`STARTED` events include only the common properties:
+ Version
+ Channel
+ AccountId
+ ContactId
+ StreamingEventType: STARTED
+ StreamingSettings

## SEGMENTS event
<a name="chat-segment-streams-data-model-segments-event"></a>

`SEGMENTS` events include the following properties:
+ Version
+ Channel
+ AccountId
+ OutputType
  + The conversational analytics output type of the current segment
  + Type: String
  + Valid values: `Raw`, `Redacted`
+ ContactId
+ StreamingEventType: SEGMENTS
+ StreamingSettings
+ Segments
  + A list of segments with analyzed information.
  + Type: Array of [Segment](#chat-segment) objects

**Segment**  
An analyzed segment for a real-time analysis session.  
Each segment is an object with the following optional properties. Only one of these properties is present, depending on the segment type:  
+  [Attachments](#chat-attachments)
+  [Categories](#chat-category)
+  [Event](#chat-event)
+  [Issues](#chat-issues)
+  [Transcript](#chat-transcript)
+ [PostContactSummary](#chat-postcontactsummary)

**Attachments**  
The analyzed attachments.  
Required: No  
Type: [RealTimeContactAnalysisSegmentAttachments](https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentAttachments.html) object

**Categories**  
The matched category rules.  
Type: [RealTimeContactAnalysisSegmentCategories](https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentCategories.html) object  
Required: No

**Event**  
Segment type describing a contact event.  
Type: [RealTimeContactAnalysisSegmentEvent](https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentEvent.html) object  
Required: No

**Issues**  
Segment type containing a list of detected issues.  
Type: [RealTimeContactAnalysisSegmentIssues](https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentIssues.html) object  
Required: No

**Transcript**  
The analyzed transcript segment.  
Type: [RealTimeContactAnalysisSegmentTranscript](https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentTranscript.html) object  
Required: No

**PostContactSummary**  
Information about the post-contact summary for a real-time contact segment for chat.  
Type: [RealTimeContactAnalysisSegmentPostContactSummary](https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisSegmentPostContactSummary.html) object   
Required: No

## COMPLETED event
<a name="chat-segment-streams-data-model-completed-event"></a>

`COMPLETED` events include only the following common properties:
+ Version
+ Channel
+ AccountId
+ InstanceId
+ ContactId
+ StreamingEventType: COMPLETED
+ StreamingSettings

## FAILED event
<a name="chat-segment-streams-data-model-failed-event"></a>

`FAILED` events include only the following common properties:
+ Version
+ Channel
+ AccountId
+ InstanceId
+ ContactId
+ StreamingEventType: FAILED
+ StreamingSettings