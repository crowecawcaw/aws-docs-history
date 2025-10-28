# Sample

conversational analytics streams to analyze chats in
Contact Lens

This topic provides sample segment streams for STARTED, SEGMENTS, COMPLETED,
and FAILED events that occur during a chat contact.

## Sample STARTED event

- EventType: STARTED
- Published at the beginning of the conversational analytics
  session.

```
{
    "Version": "2.0.0",
    "Channel": "CHAT",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "StreamingEventType": "STARTED",
    "StreamingSettings": {
      "LanguageCode": "en-US", // the language code of the contact
      "Output": "RedactedAndRaw",
      "RedactionTypes": [
          "PII"
      ],
      "RedactionTypesMetadata": {
        "PII": {
            "RedactionMaskMode": "PII"
         }
       }
    }
}
```

## Sample SEGMENTS event

- EventType: [SEGMENTS](chat-real-time-contact-analysis-segment-streams-data-model.md#chat-segment-streams-data-model-segments-event "chat-real-time-contact-analysis-segment-streams-data-model.md#chat-segment-streams-data-model-segments-event")
- Published during a conversational analytics session. This event
  contains a list of [RealtimeContactAnalysisSegment](../APIReference/API_RealtimeContactAnalysisSegment.md "../APIReference/API_RealtimeContactAnalysisSegment.md") objects with analyzed
  information. The list of segments may include
  `"Transcript"`, `"Categories"`,
  `"Issue"`, `"Event"`,
  `"Attachment"`, or "PostContactSummary"
  segments.

```
{
    "Version": "2.0.0",
    "Channel": "CHAT",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "OutputType": "Redacted",
    "StreamingEventType": "SEGMENTS",
    "StreamingSettings": {
        "LanguageCode": "en-US", // the language code of the contact
        "Output": "RedactedAndRaw",
        "RedactionTypes": [
            "PII"
        ],
        "RedactionTypesMetadata": {
            "PII": {
                "RedactionMaskMode": "PII"
            }
        }
    },
    "Segments": [{
        "Transcript": {
            "Id": "07a2d668-5c9e-4f69-b2fe-986261b0743a",
            "ParticipantId": "a309ac1e-ca87-44ca-bb5d-197eca8ed77a",
            "ParticipantRole": "AGENT",
            "DisplayName": "[PII]",
            "Content": "Hello, thank you for contacting Example Corp. My name is Ray.",
            "ContentType": "text/markdown",
            "Time": {
                "AbsoluteTime": "2024-03-14T19:39:26.715Z"
            },
            "Sentiment": "NEUTRAL"
        }
    }, {
        "Categories": {
            "MatchedDetails": {
                "Hi": {
                    "PointsOfInterest": [{
                        "TranscriptItems": [{
                            "Id": "5205b050-8aa9-4645-a381-a308801649ab",
                            "CharacterOffsets": {
                                "BeginOffsetChar": 0,
                                "EndOffsetChar": 40
                            }
                        }]
                    }]
                }
            }
        }
    }, {
        "Issues": {
            "IssuesDetected": [{
                "TranscriptItems": [{
                    "Content": "I have an issue with my bank account",
                    "Id": "0e5574a7-2aeb-4eab-8bb5-3a7f66a2284a",
                    "CharacterOffsets": {
                        "BeginOffsetChar": 7,
                        "EndOffsetChar": 43
                    }
                }]
            }]
        }
    }, {
        "Attachments": {
            "Id": "06ddc1eb-2302-4a8e-a73f-37687fe41aa9",
            "ParticipantId": "7810b1de-cca8-4153-b522-2498416255af",
            "ParticipantRole": "CUSTOMER",
            "DisplayName": "Customer",
            "Attachments": [{
                "AttachmentName": "Lily.jpg",
                "ContentType": "image/jpeg",
                "AttachmentId": "343e34da-391a-4541-8b7e-3909d931fcfa",
                "Status": "APPROVED"
            }],
            "Time": {
                "AbsoluteTime": "2024-03-14T19:39:26.715Z"
            }
        }
    }, {
        "Event": {
            "Id": "fbe61c5f-d0d8-4345-912a-4e81f5734d3b",
            "ParticipantId": "7810b1de-cca8-4153-b522-2498416255af",
            "ParticipantRole": "CUSTOMER",
            "DisplayName": "Customer",
            "EventType": "application/vnd.amazonaws.connect.event.participant.left",
            "Time": {
                "AbsoluteTime": "2024-03-14T19:40:00.614Z"
            }
        }
    },
    {
        "PostContactSummary": {
            "Content": "Customer contacted Example Corp because of an issue with their bank account",
            "Status": "COMPLETED"
        }
    }]
}
```

## Sample COMPLETED event

- EventType: COMPLETED
- Published at the end of the conversational analytics session if
  the analysis completed successfully.

```
{
    "Version": "2.0.0",
    "Channel": "CHAT",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "StreamingEventType": "COMPLETED",
    "StreamingEventSettings": {
        "LanguageCode": "en-US", // the language code of the contact
        "Output": "RedactedAndRaw",
        "RedactionTypes": ["PII"],
        "RedactionTypesMetadata": {
            "PII": {
                "RedactionMaskMode": "PII"
            }
        }
    }
}
```

## Sample FAILED event

- EventType: FAILED
- Published at the end of the conversational analytics session if
  the analysis failed.

```
{
    "Version": "2.0.0",
    "Channel": "CHAT",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "StreamingEventType": "FAILED",
    "StreamingEventSettings": {
        "LanguageCode": "en-US",
        "Output": "RedactedAndRaw",
        "RedactionTypes": ["PII"],
        "RedactionTypesMetadata": {
            "PII": {
                "RedactionMaskMode": "PII"
            }
        }
    }
}
```
