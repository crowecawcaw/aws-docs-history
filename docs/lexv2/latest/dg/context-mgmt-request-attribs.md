# Setting request

attributes for your Lex V2 bot

_Request attributes_ contain request-specific
information and apply only to the current request. A client
application sends this information to . Use request attributes
to pass information that doesn't need to persist for the entire
session. You can create your own request attributes or you can use
predefined attributes. To send request attributes, use the
`x-amz-lex-request-attributes` header in a
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md") or the
`requestAttributes` field in a
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md") request. Because request
attributes don't persist across requests like session attributes do,
they are not returned in `RecognizeUtterance` or
`RecognizeText` responses.

###### Note

To send information that persists across requests, use session
attributes.

## Setting user-defined request

attributes for each Lex V2 bot request

A _user-defined request attribute_ is data
that you send to your bot in each request. You send the
information in the `amz-lex-request-attributes`
header of a `RecognizeUtterance` request or in the
`requestAttributes` field of a
`RecognizeText` request.

To send request attributes to , you create a
string-to-string map of the attributes. The following shows how
to map request attributes:

```
{
   "attributeName": "attributeValue",
   "attributeName": "attributeValue"
}
```

For the `PostText` operation, you insert the map
into the body of the request using the
`requestAttributes` field, as follows:

```
"requestAttributes": {
   "attributeName": "attributeValue",
   "attributeName": "attributeValue"
}
```

For the `PostContent` operation, you base64 encode
the map, and then send it as the
`x-amz-lex-request-attributes` header.

If you are sending binary or structured data in a request
attribute, you must first transform the data to a simple string.
For more information, see [Setting complex
attributes in your Lex V2 bot](context-mgmt-complex-attributes.md "context-mgmt-complex-attributes.md").

Amazon Lex V2 provides predefined request attributes for managing the way that it processes information sent to your bot.
The attributes do not persist for the entire session, so you must send the predefined attributes in each request.
All predefined attributes are in the `x-amz-lex:` namespace.

In addition to the following predefined attributes, Amazon Lex provides predefined attributes for messaging platforms.
For a list of those attributes, see Deploying an Amazon Lex Bot on a Messaging Platform.

## Setting the Response Type

If you have two client applications that have different capabilities, you may need to limit the format of messages in a
response. For example, you might want to restrict messages sent to a Web client to plain text, but enable a mobile client
to use both plain text and Speech Synthesis Markup Language (SSML). To set the format of messages returned by the `PostContent`
and `PostText` operations, use the x-amz-lex:accept-content-types" request attribute.

You can set the attribute to any combination of the following message types:

- `PlainText` — The message contains plain UTF-8 text.
- `SSML` — The message contains text formatted for voice output.
- `CustomPayload` — The message contains a custom format that you have created
  for your client. You can define the payload to meet the needs of your application.

Amazon Lex V2 returns only messages with the specified type in the Message field of the response. You can set more than one value by
separating values with a comma. If you are using message groups, every message group must contain at least one message of the
specified type. Otherwise, you get a `NoUsableMessageException` error. For more information, see Message Groups.

## Setting predefined request

attributes in your Lex V2 bot

Amazon Lex V2 provides predefined request attributes for managing the way that it processes
information sent to your bot. The attributes do not persist for the entire session, so you must
send the predefined attributes in each request. All predefined attributes are in the `x-amz-lex:` namespace.

## Disabling intent switches in your Lex V2 bot

To control whether users can switch between intents during intent confirmation or slot elicitation,
use the `x-amz-lex:intent-switch` request attribute. When set to `DISABLE`, this attribute prevents users
from triggering a different intent while they are in the middle of completing the current intent flow.

For example, if a user is in the process of booking a flight and is being prompted for flight details, then utterances
such as “check weather” or “book hotel” - which might normally trigger other intents - will be ignored, ensuring the
conversation remains focused on the current booking process.
