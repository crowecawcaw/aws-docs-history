

# UpdateContactRecordingAndAnalyticsBehavior
<a name="contact-actions-updatecontactrecordingandanalyticsbehavior"></a>

Sets contact recording behavior, including analysis behavior and which participants of the contact to record.

## Parameter object
<a name="updatecontactrecordingandanalyticsbehavior-parameter"></a>

```
{
    // Only ONE of the following channel behavior objects can be defined per configuration
    
    "ChatBehavior": { // Configuration for chat channel interactions
        "ChatAnalyticsBehavior": {
            "Enabled": either "True" or "False". Must be set statically.
            "AnalyticsLanguage": Must be one of languages supported by Contact Lens analysis. Can be set dynamically. Use the format xx-XX, for example, en-US for US English.
            "ConversationalAnalyticsRedactionConfiguration": { 
                "Enabled": either "True" or "False". Must be set statically. Determines whether to redact sensitive data in Contact Lens output.
                "RedactionResults": either "RedactedAndOriginal" or "RedactedOnly". Can be set dynamically. Determines whether to provide both versions or only redacted output.
                "RedactionMaskMode": either "EntityType" or "PII". Must be set statically.
                "RedactionEntities": [ ] a list of entity types to redact from the analytics output. Must be set statically.
            },
            "InFlightChatRedactionConfiguration": { // In-flight redaction for chat messages as they are sent. Only available for chat channel.
                "Enabled": either "True" or "False". Must be set statically. Determines whether to redact sensitive data in real-time chat messages.
                "RedactionMaskMode": either "EntityType" or "PII". Must be set statically.
                "RedactionEntities": [ ] a list of entity types to redact from chat messages in-flight. Must be set statically.
                "DeliverUnprocessedMessages": either "True" or "False". Must be set statically. Determines whether to deliver messages that fail redaction.
            },
            "AnalyticsModes": ["ContactLens"]. Can only be set to ContactLens for chat channel.
            "SentimentConfiguration": { // Optional parameter to enable sentiment analysis
                "Enabled": either "True" or "False". Must be set statically.
            },
            "SummaryConfiguration": { // Optional parameter to enable post-contact summary
                "SummaryModes": ["PostContact", "AutomatedInteraction"]. Can be set to "PostContact" or "AutomatedInteraction", or both for chat channel.
            }
        }
    },
    
    "VoiceBehavior": { // Configuration for voice channel interactions
        "VoiceRecordingBehavior": {
            "RecordedParticipants": [ ] a list of participants to record, chosen from "Agent" and "Customer". An empty list disables recording. Must be set statically.
            "IVRRecordingBehavior": Can be either "Enabled" or "Disabled". Must be set statically.
        },
        "VoiceAnalyticsBehavior": { // An object that holds voice analytics settings. Can only be set if RecordedParticipants contains both Agent and Customer.
            "Enabled": either "True" or "False". Must be set statically.
            "AnalyticsLanguage": Must be one of languages supported by Contact Lens analysis. Must be set statically. Use the format xx-XX, for example, en-US for US English.
            "ConversationalAnalyticsRedactionConfiguration": { // Redaction settings for analytics output (transcripts, audio files)
                "Enabled": either "True" or "False". Must be set statically. Determines whether to redact sensitive data in Contact Lens output.
                "RedactionResults": either "RedactedAndOriginal" or "RedactedOnly". Can be set dynamically. Determines whether to provide both versions or only redacted output.
                "RedactionMaskMode": either "EntityType" or "PII". Must be set statically.
                "RedactionEntities": [ ] a list of entity types to redact from the analytics output. Must be set statically.
            },
            "AnalyticsModes": ["RealTime", "AutomatedInteraction"]. Can be set to one of "RealTime" or "PostContact" and also can include "AutomatedInteraction" for voice channel.
            "SentimentConfiguration": { // Optional parameter to enable sentiment analysis
                "Enabled": either "True" or "False". Must be set statically.
            },
            "SummaryConfiguration": { // Optional parameter to enable post-contact summary
                "SummaryModes": ["PostContact", "AutomatedInteraction"]. Can be set to "PostContact" or "AutomatedInteraction", or both for voice channel. Must be set statically.
            }
        }
    },
    
    "ScreenRecordingBehavior": { // Optional configuration for agent screen recording. Can be defined independently or alongside any channel behavior.
        "ScreenRecordedParticipants": [ ] a list of participants for which to record their screen, can only include "Agent". An empty list disables screen recording. Must be set statically.
    }
}
```

**Notes**
+ `AnalyticsRedactionMaskMode`: Optional, String. Allowed values:
  + `PII`: All PII data is replaced with `[PII]`. For example, Jane Doe is replaced with `[PII]`
  + `EntityType`: Each PII entity is replaced with its type. For example, Jane Doe is replaced with `[NAME]`.
  + If no value is provided, the default `PII` is used.
+ `AnalyticsRedactionEntities`: Optional, Array of strings.
  + Valid values include: "BANK\_ACCOUNT\_NUMBER", "BANK\_ROUTING", "CREDIT\_DEBIT\_NUMBER", "CREDIT\_DEBIT\_CVV", "CREDIT\_DEBIT\_EXPIRY", "INTERNATIONAL\_BANK\_ACCOUNT\_NUMBER", "PIN", "SWIFT\_CODE", "CA\_HEALTH\_NUMBER", "UK\_NATIONAL\_HEALTH\_SERVICE\_NUMBER", "CA\_SOCIAL\_INSURANCE\_NUMBER", "SSN", "UK\_NATIONAL\_INSURANCE\_NUMBER", "PASSPORT\_NUMBER", "DRIVER\_ID", "IN\_AADHAAR", "NAME", "AGE", "EMAIL", "PHONE", "ADDRESS", "US\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER", "UK\_UNIQUE\_TAXPAYER\_REFERENCE\_NUMBER", "IN\_PERMANENT\_ACCOUNT\_NUMBER", "IN\_NREGA", "AWS\_ACCESS\_KEY", "AWS\_SECRET\_KEY", "IP\_ADDRESS", "MAC\_ADDRESS", "PASSWORD", "URL", "USERNAME", "LICENSE\_PLATE", "VEHICLE\_IDENTIFICATION\_NUMBER", "IN\_VOTER\_NUMBER", "DATE\_TIME", "AGENT\_DISPLAY\_NAME", "CUSTOMER\_DISPLAY\_NAME", "ATTACHMENT\_NAME".
  + An empty array is not allowed.
  + If `AnalyticsRedactionEntities` is not present, the default "redact all PII data" is used.
  + The following redaction entities are not supported for chat in-flight redaction:
    + IN\_PERMANENT\_ACCOUNT\_NUMBER
    + IN\_NREGA
    + IN\_VOTER\_NUMBER
    + IN\_AADHAAR
    + DATE\_TIME
    + CUSTOMER\_DISPLAY\_NAME
    + AGENT\_DISPLAY\_NAME
    + ATTACHMENT\_NAME

For more information on sensitive data redaction, see [Enable redaction of sensitive data](https://docs.aws.amazon.com/connect/latest/adminguide/enable-analytics.html#enable-redaction) in the *Connect Customer Administrator's Guide*.

For more information on in-flight chat redaction, see [Enable in-flight sensitive data redaction and message processing](https://docs.aws.amazon.com/connect/latest/adminguide/redaction-message-processing.html).

For a list of languages supported by Contact Lens post-call analysis, see [Contact Lens supported languages](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html). For the 4-character language code to use, see [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) in the *Amazon Transcribe Developer Guide*.

## Results and conditions
<a name="updatecontactrecordingandanalyticsbehavior-results"></a>

None.

## Errors
<a name="updatecontactrecordingandanalyticsbehavior-errors"></a>
+ **NoMatchingError** - if no other Error matches. Must always be defined.
+ **ChannelMismatch** - if the media channel that initiated the contact is not the same as the one defined in the action. For screen recording, any channel other than voice, chat or tasks would result in this branch being taken. Must always be defined.
+ **InFlightRedactionConfigurationFailed** - if starting/stopping in-flight chat redaction fails. Must be defined if chat behavior is defined in action.

## Corresponding block in the UI
<a name="updatecontactrecordingandanalyticsbehavior-ui"></a>

[Set recording, analytics and processing behavior](https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-analytics-processing-behavior.html)