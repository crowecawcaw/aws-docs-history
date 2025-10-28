# Input transcript

format

The following is the input file format for generating intents and
slot types for your bot. The input file must contain these fields.
Other fields are ignored.

The input format is compatible with the output format from Contact
Lens for Amazon Connect. If you are using Contact Lens, you don't need to
modify your transcript files. For more information, see [Example Contact Lens output files](../../../connect/latest/adminguide/contact-lens-example-output-files.md "../../../connect/latest/adminguide/contact-lens-example-output-files.md") . If you are using
another contact center application, you must transform your
transcript file to this format.

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
        "ContactId": "string"
    },
    "Transcript": [
        {
            "ParticipantId": "string",
            "Id": "string",
            "Content": "string"
        }
    ]
}
```

The following fields must be present in the input file:

- **Participants**  
  Identifies the participants in the conversation and the role
  that they play.
- **Version**   The
  version of the input file format. Always "1.1.0".
- **ContentMetadata**  
  Indicates whether you removed sensitive information from the
  transcript. Set the `Output` field to "Raw" if
  the transcript contains sensitive information.
- **CustomerMetadata**   A
  unique identifier for the conversation.
- **Transcript**   The
  text of the conversation between parties in the
  conversation. Each turn of the conversation is identified
  with a unique identifier.
