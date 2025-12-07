# Enable in-flight sensitive data redaction

and message processing

Amazon Connect supports message processing that intercepts and modifies chat messages before
they reach any participant. This capability enables automatic redaction of sensitive
data and custom message processing, helping businesses maintain compliance and security
standards.

The following are processing options, along with features of each option:

- Built-in sensitive data redaction
  - Automatically detects and removes credit card numbers, social security
    numbers, and other PII
  - Supports multiple languages, including English, French, Portuguese,
    German, Italian, and Spanish variants. For a list of the languages
    supported by Contact Lens redaction, see [Languages supported by Amazon Connect features](supported-languages.md "supported-languages.md").
  - Choose to redact selected or all sensitive data entities
  - Replace with generic placeholders ([PII]) or entity-specific
    placeholders ([NAME], [CREDIT\_CARD])

- Custom message processors (via Lambda). For more information, see [What is Lambda?](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") in the AWS
  _Lambda Developer's Guide_.

      + Integrate third-party services for language translation
      + Apply profanity filtering
      + Transform messages using AI/LLM services
      + Implement business-specific message modifications

  To configure message processing, define redaction rules in the **Set recording
  and analytics behavior** block. For more information, see [Enable redaction of sensitive data](enable-analytics.md#enable-redaction "enable-analytics.md#enable-redaction"). You can also specify a Lambda function for custom
  processing.

Your custom processor Lambda will take in an input JSON in the following format:

```
{
  "version": "1.0",
  "instanceId": "string",
  "associatedResourceArn": "string",
  "chatContent": {
    "absoluteTime": "string",
    "content": "string",
    "contentType": "string",
    "id": "string",
    "participantId": "string",
    "displayName": "string",
    "participantRole": "string",
    "initialContactId": "string",
    "contactId": "string"
  }
}
```

And output a JSON in the following format:

```
{
  "status": "string", // "PROCESSED"|"APPROVED"|"FAILED"|"REJECTED"
  "result": {
    "processedChatContent": {
      "content": "string",
      "contentType": "string" // "text/plain"|"text/markdown"|"application/json"
    }
  }
}
```

The processed chat content will replace the original message when published to chat
participants.
