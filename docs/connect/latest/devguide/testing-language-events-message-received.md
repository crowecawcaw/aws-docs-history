

# Message received
<a name="testing-language-events-message-received"></a>

Observes when the system plays a prompt or send any voice response to the simulated customer. This event can match messages using different criteria.

## Parameters
<a name="testing-language-events-message-received-parameters"></a>
+ Identifier - Unique identifier for the event (API need to specify this identifier in order for the UI to render properly)
+ Type - Must always be `MessageReceived`.
+ Actor - Must always be `System`. This indicates the event originate from the testing system.
+ Properties - Empty object. Object containing the following message details:
  + PromptId (Optional): Specific prompt ID or ARN to match
  + Text (Optional): Text content of the message to match
  + SSML (Optional): SSML content to match
  + Media (Optional): External media source details
    + Uri: Location of the media file
    + SourceType: Source from which media is fetched such as S3
    + MediaType: Type of media such as "audio/mpeg"
  + MatchingCriteria - Defines how to match the message:
    + Similarity: Uses semantic matching to find similar messages
    + Inclusion: Checks if the observed message contains the specified text

```
{
    "Identifier": "unique identifier",
    "Type": "MessageReceived",
    "Actor": "System",
    "Properties": {
        "PromptId": "string", // [Optional] A prompt ID or prompt ARN to play to the participant along with gathering input. May not be specified if Text or SSML is also specified. Must be specified either statically or as a single valid JSONPath identifier.
        "Text":  "string", // An optional string that defines text to send to the participant along with gathering input. May not be specified if PromptId or SSML is also specified. May be specified statically or dynamically.
        "SSML": "string", // An optional string that defines SSML to send to the participant along with gathering input. May not be specified if Text or PromptId is also specified May be specified statically or dynamically.
        "Media": { // An optional object that defines an external media source
            "Uri": "string", // Location of the message
            "SourceType": "string",// The source from which the message will be fetched. The only supported type is S3
            "MediaType": "string"// The type of the message to be played. The only supported type is Audio
        },
        "MatchingCriteria": { "Type": "Similarity" } // Alternatively, use "Inclusion".
    }
}
```