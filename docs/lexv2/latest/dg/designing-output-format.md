# Output transcript

format

The output transcript format is nearly the same as the input
transcript format. However it also includes some customer metadata
and a field listing segments that influenced the suggestion of
intents and slot types. You can download the output transcript from
the **Review** page in the console or using the
Amazon Lex V2 API. For more information, see [Input transcript
format](designing-input-format.md "designing-input-format.md").

```
{
    "Participants": [
        {
            "ParticipantId": "string",
            "ParticipantRole": "AGENT | CUSTOMER"
        }
    ],
    "Version": "1.1.0",
    "ContentMetadata": {

        "RedactionTypes": [
            "PII"
        ],
        "Output": "Raw | Redacted"
    },
    "CustomerMetadata": {
        "ContactId": "string",
        "FileName": "string",
        "InputFormat": "Lex"
    },
    "InfluencingSegments": [
        {
            "Id": "string",
            "StartTurnIndex": number,
            "EndTurnIndex": number,
            "Intents": [
                {
                    "Id": "string",
                    "Name": "string",
                    "SampleUtteranceIndex": [
                        {
                            "Index": number,
                            "Content": "String"
                        }
                    ]
                }
            ],
            "SlotTypes": [
                {
                    "Id": "string",
                    "Name": "string",
                    "SlotValueIndex": [
                        {
                            "Index": number,
                            "Content": "String"
                        }
                    ]
                }
            ]
        }
    ],
    "Transcript": [
        {

            "ParticipantId": "string",
            "Id": "string",
            "Content": "string"
        }
    ]
}
```

- **CustomerMetadata** –
  There are two fields added to the
  `CustomerMetadata` field, the name of the
  input file that contains the conversation and the input
  format, which is always "Lex".
- **InfluencingSegments**
  – Identifies the segments of the conversation that
  influenced the suggestion of an intent or slot type. The ID
  of the intent or slot type identifies the specific one
  influenced by the conversation.
