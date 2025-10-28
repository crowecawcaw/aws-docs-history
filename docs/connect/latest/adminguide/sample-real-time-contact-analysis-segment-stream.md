# Sample

conversational analytics segment streams to analyze calls using
Contact Lens

This topic provides sample segment streams for STARTED, SEGMENTS, COMPLETED,
and FAILED events that can occur during a voice contact.

## Sample STARTED event

- EventType: STARTED
- Published at the beginning of the conversational analytics
  session.

```
{
    "Version": "1.0.0",
    "Channel": "VOICE",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "LanguageCode": "en-US", // the language code of the contact
    "EventType": "STARTED"
}
```

## Sample SEGMENTS event

- EventType: SEGMENTS
- Published during a conversational analytics session. This event
  contains a list of segments with analyzed information. The list of
  segments may include "`Utterance`,"
  "`Transcript`," "`Categories`" or
  "`PostContactSummary`" segments.

```
{
    "Version": "1.0.0",
    "Channel": "VOICE",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "LanguageCode": "en-US", // the language code of the contact
    "EventType": "SEGMENTS",
    "Segments": [
        {
            "Utterance": {
                "Id": "7b48ca3d-73d3-443a-bf34-a9e8fcc01747",
                "TranscriptId": "121d1581-905f-4169-9804-b841bb4df04a",
                "ParticipantId": "AGENT",
                "ParticipantRole": "AGENT",
                "PartialContent": "Hello, thank you for calling Example Corp. My name is Adam.",
                "BeginOffsetMillis": 19010,
                "EndOffsetMillis": 22980
            }
        },
        {
            "Utterance": {
                "Id": "75acb743-2154-486b-aaeb-c960ae290e88",
                "TranscriptId": "121d1581-905f-4169-9804-b841bb4df04a",
                "ParticipantId": "AGENT",
                "ParticipantRole": "AGENT",
                "PartialContent": "How can I help you?",
                "BeginOffsetMillis": 23000,
                "EndOffsetMillis": 24598
            }
        },
        {
            "Transcript": {
                "Id": "121d1581-905f-4169-9804-b841bb4df04a",
                "ParticipantId": "AGENT",
                "ParticipantRole": "AGENT",
                "Content": "Hello, thank you for calling Example Corp. My name is Adam. How can I help you?",
                "BeginOffsetMillis": 19010,
                "EndOffsetMillis": 24598,
                "Sentiment": "NEUTRAL"
            }
        },
        {
            "Transcript": {
                "Id": "4295e927-43aa-4447-bbfc-8fccc2027530",
                "ParticipantId": "CUSTOMER",
                "ParticipantRole": "CUSTOMER",
                "Content": "I'm having trouble submitting the application, number AX876293 on the portal. I tried but couldn't connect to my POC on the portal. So, I'm calling on this toll free number",
                "BeginOffsetMillis": 19010,
                "EndOffsetMillis": 22690,
                "Sentiment": "NEGATIVE",
                "IssuesDetected": [
                    {
                        "CharacterOffsets": {
                            "BeginOffsetChar": 0,
                            "EndOffsetChar": 81
                        }
                    }
                ]
            }
        },
        {
            "Categories": {
                "MatchedCategories": [
                    "CreditCardRelated",
                    "CardBrokenIssue"
                ],
                "MatchedDetails": {
                    "CreditCardRelated": {
                        "PointsOfInterest": [
                            {
                                "BeginOffsetMillis": 19010,
                                "EndOffsetMillis": 22690
                            }
                        ]
                    },
                    "CardBrokenIssue": {
                        "PointsOfInterest": [
                            {
                                "BeginOffsetMillis": 25000,
                                "EndOffsetMillis": 29690
                            }
                        ]
                    }
                }
            }
        },
        {
            "PostContactSummary": {
                "Content": "Customer contacted Example Corp because of an issue with their application",
                "Status": "COMPLETED"
            }
        }
    ]
}
```

## Sample COMPLETED event

- EventType: COMPLETED
- Published at the end of the conversational analytics session if
  the analysis completed successfully.

```
{
    "Version": "1.0.0",
    "Channel": "VOICE",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "LanguageCode": "en-US", // the language code of the contact
    "EventType": "COMPLETED"
}
```

## Sample FAILED event

- EventType: FAILED
- Published at the end of the conversational analytics session if
  the analysis failed.

```
{
    "Version": "1.0.0",
    "Channel": "VOICE",
    "AccountId": "123456789012", // your AWS account ID
    "InstanceId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  // your Amazon Connect instance ID
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", // the ID of the contact
    "LanguageCode": "en-US", // the language code of the contact
    "EventType": "FAILED"
}
```
